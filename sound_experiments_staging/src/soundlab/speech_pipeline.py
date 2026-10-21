"""
Speech Intelligence & Vocal Separation Pipeline:
- Batch ASR transcription using faster-whisper (GPU CTranslate2)
- UVR5 Vocal Separation using audio-separator (MDX-Net / BS-Roformer)
- Automated Speech Similarity Matching (identifying identical performances across different background music)
- Quality Ranking & Master/Variant Designation
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from soundlab.catalog import CatalogDB
from soundlab.config import config
from soundlab.speech_dedup import SpeechDedupEngine, compute_transcript_similarity


class SpeechPipeline:
    """End-to-end pipeline for speech transcription, UVR5 separation, and quality grading."""

    def __init__(self, catalog: Optional[CatalogDB] = None):
        self.catalog = catalog or CatalogDB()
        self.dedup_engine = SpeechDedupEngine(self.catalog)

    def process_all_transcripts(self) -> Dict[str, Any]:
        """Transcribe all active raw recordings that do not yet have transcripts."""
        with self.catalog.get_connection() as conn:
            rows = conn.execute(
                "SELECT r.id as raw_id, r.file_path, r.file_size_bytes, r.duration_sec, s.id as source_id, s.title, s.metadata_json "
                "FROM raw_files r "
                "JOIN sources s ON s.id = r.source_id "
                "WHERE r.status = 'active';"
            ).fetchall()

        processed_count = 0
        duplicate_speeches = []

        for row in rows:
            meta = json.loads(row["metadata_json"] or "{}")
            if "transcript" in meta and meta["transcript"]:
                continue

            audio_file = Path(row["file_path"])
            if not audio_file.exists():
                continue

            print(f"[Transcribing] #{row['raw_id']}: {row['title']}...")
            try:
                transcript, segments = self.dedup_engine.transcribe_file(audio_file)
                meta["transcript"] = transcript
                meta["segments_count"] = len(segments)

                # Quality evaluation
                q_score = self.dedup_engine.evaluate_audio_quality(
                    audio_file, row["file_size_bytes"], row["duration_sec"] or 1.0
                )
                meta["quality_score"] = q_score

                # Update source metadata in catalog
                with self.catalog.get_connection() as conn:
                    conn.execute(
                        "UPDATE sources SET metadata_json = ? WHERE id = ?;",
                        (json.dumps(meta), row["source_id"]),
                    )

                # Check if this speech matches an existing speech in the dataset
                match_id = self.dedup_engine.link_speech_duplicates(row["raw_id"], transcript, q_score)
                if match_id:
                    duplicate_speeches.append({
                        "raw_id": row["raw_id"],
                        "matched_source_id": match_id,
                        "title": row["title"],
                    })

                processed_count += 1
            except Exception as e:
                print(f"[Transcribe Error] Failed on #{row['raw_id']}: {e}")

        return {
            "processed_count": processed_count,
            "duplicate_speeches_found": len(duplicate_speeches),
            "details": duplicate_speeches,
        }

    def separate_vocals_uvr5(self, audio_path: Path, output_dir: Optional[Path] = None) -> Optional[Path]:
        """
        Extract clean vocal stem using UVR5 architecture (MDX-Net / BS-Roformer).
        Saves clean isolated vocals to derived storage on D:.
        """
        from audio_separator.separator import Separator

        out_path = output_dir or (config.derived_dir / "vocals")
        out_path.mkdir(parents=True, exist_ok=True)

        separator = Separator(
            output_dir=str(out_path),
            output_format="WAV",
        )
        # Load high-precision vocal extraction model
        separator.load_model(model_filename="UVR-MDX-NET-Inst_HQ_3.onnx")
        output_files = separator.separate(str(audio_path))

        vocal_file = None
        for f in output_files:
            if "Vocals" in f or "vocals" in f.lower():
                vocal_file = out_path / f
                break

        return vocal_file
