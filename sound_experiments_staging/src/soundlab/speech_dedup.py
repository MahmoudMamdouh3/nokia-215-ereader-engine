"""
Speech-Level Deduplication & Vocal Quality Evaluator:
- Transcribes audio using faster-whisper (GPU-accelerated)
- Identifies identical speeches/interviews even when disguised by different background music
- Evaluates audio fidelity to designate the Master recording and link redundant edits
- Never deletes raw files
"""

from __future__ import annotations

import difflib
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from soundlab.catalog import CatalogDB
from soundlab.config import config


def normalize_text(text: str) -> str:
    """Normalize transcript text by stripping punctuation and lowercasing."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return " ".join(text.split())


def analyze_speech_overlap(text1: str, text2: str) -> Dict[str, Any]:
    """
    Quantify exact spoken overlap between two recordings.
    Calculates asymmetric containment to prevent treating a 2-minute quote
    inside a 2-hour video as a complete duplicate.
    """
    w1 = [w.lower() for w in re.sub(r"[^\w\s]", "", text1).split()]
    w2 = [w.lower() for w in re.sub(r"[^\w\s]", "", text2).split()]

    if not w1 or not w2:
        return {
            "classification": "DISTINCT",
            "overlap_words": 0,
            "words_1": len(w1),
            "words_2": len(w2),
            "containment_1_pct": 0.0,
            "containment_2_pct": 0.0,
            "seq_ratio_pct": 0.0,
        }

    matcher = difflib.SequenceMatcher(None, w1, w2)
    blocks = matcher.get_matching_blocks()
    # Only count contiguous matching phrases of 4 or more words
    overlap_words = sum(b.size for b in blocks if b.size >= 4)

    c1 = overlap_words / float(len(w1)) if w1 else 0.0
    c2 = overlap_words / float(len(w2)) if w2 else 0.0
    seq_ratio = matcher.ratio()

    # Exact duplicate: both recordings are >= 85% identical speech
    if c1 >= 0.85 and c2 >= 0.85:
        classification = "EXACT_DUPLICATE"
    # Excerpt: one is predominantly contained (>= 75%) inside a much longer talk (< 50%)
    elif (c1 >= 0.75 and c2 < 0.50) or (c2 >= 0.75 and c1 < 0.50):
        classification = "EXCERPT"
    # Partial overlap: significant shared quote (>= 20 words or >= 30% each)
    elif overlap_words >= 20 or (c1 >= 0.30 and c2 >= 0.30):
        classification = "PARTIAL_OVERLAP"
    else:
        classification = "DISTINCT"

    return {
        "classification": classification,
        "overlap_words": overlap_words,
        "words_1": len(w1),
        "words_2": len(w2),
        "containment_1_pct": round(c1 * 100, 1),
        "containment_2_pct": round(c2 * 100, 1),
        "seq_ratio_pct": round(seq_ratio * 100, 1),
    }


def compute_transcript_similarity(text1: str, text2: str) -> float:
    """Compute overall sequence similarity ratio between two transcripts."""
    analysis = analyze_speech_overlap(text1, text2)
    return analysis["seq_ratio_pct"] / 100.0


class SpeechDedupEngine:
    """Detects duplicate speeches across videos with different background music."""

    def __init__(self, catalog: Optional[CatalogDB] = None, whisper_model_size: str = "base.en"):
        self.catalog = catalog or CatalogDB()
        self.model_size = whisper_model_size
        self._model = None

    def _get_whisper(self):
        """Lazy load faster-whisper model on GPU with automatic CUDA DLL resolution."""
        if self._model is None:
            import os
            import sys
            torch_lib = Path(sys.prefix) / "Lib" / "site-packages" / "torch" / "lib"
            if torch_lib.exists():
                try:
                    os.add_dll_directory(str(torch_lib))
                except Exception:
                    pass
                os.environ["PATH"] = str(torch_lib) + os.pathsep + os.environ.get("PATH", "")

            from faster_whisper import WhisperModel
            try:
                self._model = WhisperModel(self.model_size, device="cuda", compute_type="float16")
            except Exception as e:
                print(f"[Whisper Warning] CUDA load failed ({e}), using CPU int8 fallback")
                self._model = WhisperModel(self.model_size, device="cpu", compute_type="int8")
        return self._model

    def transcribe_file(self, audio_path: Path) -> Tuple[str, List[Dict[str, Any]]]:
        """Transcribe an audio recording into text and timestamps."""
        model = self._get_whisper()
        segments, info = model.transcribe(str(audio_path), beam_size=3, vad_filter=True)
        
        full_text = []
        segments_data = []
        for s in segments:
            full_text.append(s.text.strip())
            segments_data.append({
                "start": s.start,
                "end": s.end,
                "text": s.text.strip(),
            })

        return " ".join(full_text), segments_data

    def evaluate_audio_quality(self, audio_path: Path, file_size: int, duration: float) -> float:
        """
        Compute an audio quality score:
        - Bitrate estimate
        - Codec type
        - Duration stability
        Higher score = Cleaner, higher-fidelity recording.
        """
        if duration <= 0:
            return 0.0
        bitrate_kbps = (file_size * 8) / (duration * 1000.0)
        
        score = min(bitrate_kbps / 128.0, 2.0) * 50.0  # Up to 100
        ext = audio_path.suffix.lower()
        if ext in [".flac", ".wav"]:
            score += 25.0  # Lossless bonus
        elif ext in [".opus", ".m4a"]:
            score += 15.0  # Modern high-efficiency container
            
        return score

    def link_speech_duplicates(self, source_id: int, transcript: str, quality_score: float) -> Optional[Dict[str, Any]]:
        """
        Compare against existing transcripts in the catalog (excluding itself).
        Quantifies overlap percentage and classification (EXACT_DUPLICATE, EXCERPT, PARTIAL_OVERLAP).
        If an exact duplicate speech is found, designates the higher audio quality as Master.
        """
        with self.catalog.get_connection() as conn:
            # Check existing transcripts, excluding this current recording
            rows = conn.execute(
                "SELECT id, metadata_json FROM sources WHERE metadata_json LIKE '%transcript%' AND id != ?;",
                (source_id,),
            ).fetchall()

            for r in rows:
                meta = json.loads(r["metadata_json"] or "{}")
                existing_transcript = meta.get("transcript", "")
                if not existing_transcript:
                    continue

                analysis = analyze_speech_overlap(transcript, existing_transcript)
                cls = analysis["classification"]

                if cls != "DISTINCT":
                    other_q = float(meta.get("quality_score", 50.0))
                    match_info = {
                        "matched_source_id": r["id"],
                        "classification": cls,
                        "overlap_words": analysis["overlap_words"],
                        "this_containment_pct": analysis["containment_1_pct"],
                        "other_containment_pct": analysis["containment_2_pct"],
                        "this_quality": quality_score,
                        "other_quality": other_q,
                        "preferred_master": source_id if quality_score >= other_q else r["id"],
                    }

                    if cls == "EXACT_DUPLICATE":
                        print(f"[Speech Match: EXACT] Source #{source_id} matches #{r['id']} ({analysis['containment_1_pct']}% identical words, Master: #{match_info['preferred_master']})")
                    elif cls == "EXCERPT":
                        print(f"[Speech Match: EXCERPT] Source #{source_id} is an excerpt/clip of #{r['id']} ({analysis['overlap_words']} words overlap)")
                    elif cls == "PARTIAL_OVERLAP":
                        print(f"[Speech Match: PARTIAL] Source #{source_id} shares quotes with #{r['id']} ({analysis['overlap_words']} words overlap)")

                    return match_info

        return None
