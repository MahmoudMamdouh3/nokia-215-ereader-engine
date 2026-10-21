import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from soundlab.ingestion import IngestionEngine

urls = [
    "https://www.youtube.com/watch?v=cwq4kdl3X3g", # Part 2
    "https://www.youtube.com/watch?v=_nRxn1U1yXo", # Part 3
    "https://www.youtube.com/watch?v=ge6L5GOc5Ew", # Part 4
    "https://www.youtube.com/watch?v=nIvVKQ8cQg4", # Part 5
    "https://www.youtube.com/watch?v=IvAHqRJucXM", # Part 6
    "https://www.youtube.com/watch?v=ZVZgPxVsvgE", # Part 7
    "https://www.youtube.com/watch?v=ZBYm0Cl3TPQ", # Part 8
    "https://www.youtube.com/watch?v=tLIQsRFraa4", # Part 9
]

print(f"Starting parallel ingestion for {len(urls)} parts of Kobe Doin' Work (Spike Lee close-mic commentary)...")

def ingest_url(u):
    engine = IngestionEngine()
    try:
        res = engine.download_url(u)
        return (u, res)
    except Exception as e:
        return (u, f"Error: {e}")

with ThreadPoolExecutor(max_workers=3) as pool:
    futures = [pool.submit(ingest_url, u) for u in urls]
    for fut in as_completed(futures):
        u, res = fut.result()
        print(f"Finished {u} -> {res}")

print("Batch complete!")
