import sqlite3
from soundlab.config import config
from soundlab.speaker_filter import KobeVoiceprintFilter
from resemblyzer import preprocess_wav
import numpy as np

conn = sqlite3.connect(str(config.catalog_path))
c = conn.cursor()

c.execute("SELECT COUNT(*) FROM raw_files WHERE status = 'active'")
print(f"Total Active Clean Audio Files: {c.fetchone()[0]}")

c.execute("SELECT r.id, s.title, r.file_path, r.duration_sec, r.file_size_bytes FROM raw_files r JOIN sources s ON r.source_id = s.id WHERE r.id = 823")
rows = c.fetchall()

filter_tool = KobeVoiceprintFilter()

for r_id, title, fpath, dur, size in rows:
    size_mb = size / (1024 * 1024)
    print(f"\n=== #{r_id}: {title} ({dur:.1f}s, {size_mb:.2f}MB) ===")
    wav = preprocess_wav(fpath)
    total_len = len(wav)
    sims = []
    chunk_size = 16000 * 15
    for start in range(0, min(total_len, 16000 * 240), chunk_size):
        end = min(start + chunk_size, total_len)
        if end - start >= 16000 * 2:
            s = filter_tool.compute_similarity(wav[start:end])
            sims.append(s)
    if sims:
        print(f"  Biometric Similarity: Mean={np.mean(sims):.4f}, Max={np.max(sims):.4f}")
        for idx, s in enumerate(sims[:6]):
            print(f"    Sample {idx+1}: {s:.4f}")
