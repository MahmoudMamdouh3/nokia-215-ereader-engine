import sys
import os
import sqlite3
import numpy as np
from pathlib import Path
from soundlab.config import config
from soundlab.catalog import CatalogDB
from soundlab.speaker_filter import KobeVoiceprintFilter
from soundlab.speech_dedup import SpeechDedupEngine
from resemblyzer import preprocess_wav

def diarize_recordings_grouped(raw_ids):
    catalog = CatalogDB()
    speaker_filter = KobeVoiceprintFilter(catalog)
    speech_engine = SpeechDedupEngine(catalog)
    
    with catalog.get_connection() as conn:
        for rid in raw_ids:
            row = conn.execute("""
                SELECT r.id, s.title, r.file_path, r.duration_sec 
                FROM raw_files r 
                JOIN sources s ON r.source_id = s.id 
                WHERE r.id = ? AND r.status = 'active'
            """, (rid,)).fetchone()
            
            if not row:
                continue
                
            fpath = Path(row["file_path"])
            if not fpath.exists():
                continue
                
            print(f"\n[Diarizing Grouped] #{rid}: {row['title']} ({row['duration_sec']:.1f}s)...")
            
            # 1. Transcribe with Whisper
            _, segments = speech_engine.transcribe_file(fpath)
            if not segments:
                continue
                
            # 2. Group adjacent segments into conversational utterances
            utterances = []
            current_utt = {
                "start": segments[0]["start"],
                "end": segments[0]["end"],
                "text": segments[0]["text"],
            }
            
            for seg in segments[1:]:
                # If gap is small (< 1.5s) and current utterance length < 12s, merge
                if seg["start"] - current_utt["end"] < 1.5 and (seg["end"] - current_utt["start"]) < 15.0:
                    current_utt["end"] = seg["end"]
                    current_utt["text"] += " " + seg["text"]
                else:
                    utterances.append(current_utt)
                    current_utt = {
                        "start": seg["start"],
                        "end": seg["end"],
                        "text": seg["text"],
                    }
            utterances.append(current_utt)
            
            print(f"  Grouped into {len(utterances)} conversational utterances (from {len(segments)} fragments)")
            
            # 3. Audio biometric verification per utterance
            wav = preprocess_wav(str(fpath))
            kobe_count = 0
            total_kobe_sec = 0.0
            
            # Clear old segments for this file to avoid duplicate keys in testing
            conn.execute("DELETE FROM kobe_segments WHERE raw_file_id = ?", (rid,))
            
            for utt in utterances:
                start_sec = utt["start"]
                end_sec = utt["end"]
                dur = end_sec - start_sec
                if dur < 1.5:
                    continue
                    
                start_idx = int(start_sec * 16000)
                end_idx = int(end_sec * 16000)
                slice_wav = wav[start_idx:end_idx]
                if len(slice_wav) < 16000 * 1.5:
                    continue
                    
                sim = speaker_filter.compute_similarity(slice_wav)
                
                # Biometric threshold: Kobe Bryant voice is >= 0.81 for multi-second utterances
                if sim >= 0.81:
                    kobe_count += 1
                    total_kobe_sec += dur
                    clean_text = " ".join(utt["text"].split())
                    conn.execute("""
                        INSERT INTO kobe_segments 
                        (raw_file_id, start_sec, end_sec, duration_sec, speaker_score, transcription)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (rid, round(start_sec, 3), round(end_sec, 3), round(dur, 3), round(sim, 4), clean_text))
                    print(f"    [Kobe Segment] {start_sec:.1f}s - {end_sec:.1f}s ({dur:.1f}s | Score: {sim:.4f}): \"{clean_text[:60]}...\"")
            
            conn.commit()
            print(f"  -> Total Pure Kobe Isolated: {kobe_count} segments ({total_kobe_sec:.1f}s / {total_kobe_sec/60:.2f} min)")

if __name__ == "__main__":
    target_ids = [795, 807, 808, 810]
    diarize_recordings_grouped(target_ids)
