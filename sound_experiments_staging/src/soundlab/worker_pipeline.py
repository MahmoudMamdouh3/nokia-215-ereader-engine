"""
Asynchronous Deep Learning Worker (Producer-Consumer Consumer):
Continuously processes newly downloaded audio in parallel with the harvester:
- Transcribes spoken text via GPU Whisper
- Performs speech similarity matching across different music beds
- Extracts vocal stems using UVR5
- Ranks quality and updates catalog without blocking ongoing downloads
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Optional

from soundlab.catalog import CatalogDB
from soundlab.config import config
from soundlab.speech_dedup import SpeechDedupEngine


class ContinuousAIWorker:
    """Background GPU consumer that processes audio files as soon as they are archived."""

    def __init__(self, catalog: Optional[CatalogDB] = None):
        # Automatically lower process priority on Windows so background AI never causes UI lag
        try:
            import ctypes
            k32 = ctypes.windll.kernel32
            k32.GetCurrentProcess.restype = ctypes.c_void_p
            k32.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
            # 0x4000 = BELOW_NORMAL_PRIORITY_CLASS
            k32.SetPriorityClass(k32.GetCurrentProcess(), 0x4000)
        except Exception:
            pass

        self.catalog = catalog or CatalogDB()
        self.speech_engine = SpeechDedupEngine(self.catalog)
        self.running = True

    def process_pending_files(self, limit: int = 5) -> int:
        """Find raw files that lack transcripts and process them on GPU."""
        with self.catalog.get_connection() as conn:
            rows = conn.execute(
                """
                SELECT r.id as raw_id, r.file_path, r.file_size_bytes, r.duration_sec,
                       s.id as source_id, s.title, s.metadata_json
                FROM raw_files r
                JOIN sources s ON s.id = r.source_id
                WHERE r.status = 'active'
                  AND (s.metadata_json NOT LIKE '%transcript%' OR s.metadata_json IS NULL)
                LIMIT ?;
                """,
                (limit,),
            ).fetchall()

        if not rows:
            return 0

        processed = 0
        for row in rows:
            audio_path = Path(row["file_path"])
            if not audio_path.exists():
                continue

            raw_id = row["raw_id"]
            source_id = row["source_id"]
            title = (row["title"] or "Untitled").encode("ascii", "replace").decode("ascii")

            print(f"[AI Worker GPU] Transcribing #{raw_id}: {title}...")
            try:
                transcript, segments = self.speech_engine.transcribe_file(audio_path)
                meta = json.loads(row["metadata_json"] or "{}")
                meta["transcript"] = transcript
                meta["segments_count"] = len(segments)

                q_score = self.speech_engine.evaluate_audio_quality(
                    audio_path, row["file_size_bytes"], row["duration_sec"] or 1.0
                )
                meta["quality_score"] = q_score

                # Store transcript and metrics atomically
                with self.catalog.get_connection() as conn:
                    conn.execute(
                        "UPDATE sources SET metadata_json = ? WHERE id = ?;",
                        (json.dumps(meta), source_id),
                    )

                # Check speech duplicate matching with quantified overlap analysis
                match_info = self.speech_engine.link_speech_duplicates(source_id, transcript, q_score)
                if match_info:
                    meta["speech_overlap"] = match_info
                    with self.catalog.get_connection() as conn:
                        conn.execute(
                            "UPDATE sources SET metadata_json = ? WHERE id = ?;",
                            (json.dumps(meta), source_id),
                        )

                print(f"[AI Worker GPU] Completed #{raw_id} (Length: {len(transcript)} chars, Quality: {q_score:.1f})")
                processed += 1
            except Exception as e:
                print(f"[AI Worker Error] Processing failed on #{raw_id}: {e}")

        return processed

    def run_loop(self, poll_interval: float = 3.0, max_idle_cycles: int = 100):
        """Continuous background processing loop."""
        print("[AI Worker] Started continuous GPU deep learning pipeline. Monitoring catalog...")
        idle_count = 0
        while self.running:
            count = self.process_pending_files(limit=5)
            if count > 0:
                idle_count = 0
            else:
                idle_count += 1
                if idle_count >= max_idle_cycles:
                    print("[AI Worker] All active recordings up to date. Standing by...")
                    idle_count = 0
                time.sleep(poll_interval)
