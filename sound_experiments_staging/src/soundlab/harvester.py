"""
Automated Batch Harvester for Sound Experiments:
Discovers and ingests recordings at scale across multiple search vectors.
"""

from __future__ import annotations

import subprocess
import time
from pathlib import Path
from typing import List, Optional

from soundlab.catalog import CatalogDB
from soundlab.config import config
from soundlab.ingestion import IngestionEngine, KOBE_DISCOVERY_QUERIES


def discover_query_urls(query: str, max_results: int = 25) -> List[str]:
    """Search YouTube via yt-dlp and extract candidate video URLs."""
    cmd = [
        "yt-dlp",
        f"ytsearch{max_results}:{query}",
        "--flat-playlist",
        "--print", "%(webpage_url)s",
        "--no-playlist",
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=120)
        urls = [line.strip() for line in res.stdout.splitlines() if line.strip().startswith("http")]
        return urls
    except Exception as e:
        print(f"[Search Error] Query '{query}' failed: {e}")
        return []


class AutoHarvester:
    """Manages continuous or batch discovery and downloading of Kobe Bryant audio."""

    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self.catalog = CatalogDB()
        self.engine = IngestionEngine(self.catalog)

    def harvest_query(self, query: str, max_results: int = 20, max_workers: Optional[int] = None) -> int:
        """Discover and download audio for a specific search query using parallel worker threads."""
        workers = max_workers or self.max_workers
        print(f"\n[Harvester] Searching for: '{query}' (limit: {max_results})...")
        urls = discover_query_urls(query, max_results=max_results)
        print(f"[Harvester] Found {len(urls)} candidate URLs. Launching {workers} parallel worker threads...")

        success_count = 0
        from concurrent.futures import ThreadPoolExecutor, as_completed

        def worker_task(url: str) -> bool:
            # Each worker thread instantiates its own engine and connection
            thread_engine = IngestionEngine()
            try:
                res = thread_engine.download_url(url)
                return res is not None
            except Exception as e:
                print(f"[Harvester Error] Failed to process {url}: {e}")
                return False

        with ThreadPoolExecutor(max_workers=workers) as executor:
            future_to_url = {executor.submit(worker_task, url): url for url in urls}
            for future in as_completed(future_to_url):
                if future.result():
                    success_count += 1

        print(f"[Harvester] Finished '{query}': Ingested {success_count} clean recordings in parallel.")
        return success_count

    def harvest_all_seed_queries(self, max_per_query: int = 15, max_workers: Optional[int] = None) -> int:
        """Run discovery and parallel ingestion across all Kobe Bryant seed queries."""
        total_ingested = 0
        for q in KOBE_DISCOVERY_QUERIES:
            total_ingested += self.harvest_query(q, max_results=max_per_query, max_workers=max_workers)
        return total_ingested

