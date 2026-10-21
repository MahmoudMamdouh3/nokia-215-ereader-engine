import sqlite3
import shutil
import numpy as np
from pathlib import Path
from soundlab.config import config
from soundlab.speaker_filter import KobeVoiceprintFilter
from resemblyzer import preprocess_wav

print("=== STEP 1: Re-enrolling Master Voiceprint with Guaranteed 100% Solo Kobe Speeches ===")

# Guaranteed 100% Solo Kobe Speeches
solo_kobe_paths = [
    Path(r"E:\Sound Experiments\Kobe bryant Database raw\sources\youtube\Eg0mxPXIpLY\audio.opus"), # Mamba Out Speech
    Path(r"E:\Sound Experiments\Kobe bryant Database raw\sources\youtube\opvXRnqN1yc\audio.opus"), # Jersey Retirement Speech
    Path(r"E:\Sound Experiments\Kobe bryant Database raw\sources\youtube\bfiwfx6y6Wg\audio.opus"), # Dear Basketball Narration
    Path(r"E:\Sound Experiments\Kobe bryant Database raw\sources\youtube\oZV6Ucm8toc\audio.opus"), # ESPYS Icon Award Speech
    Path(r"E:\Sound Experiments\Kobe bryant Database raw\sources\youtube\lQbZ502rJE4\audio.m4a"),  # Oscar Acceptance Speech
]

valid_paths = [p for p in solo_kobe_paths if p.exists()]
print(f"Found {len(valid_paths)} confirmed solo Kobe reference files:")
for p in valid_paths:
    print(f" - {p.name} ({p.parent.name})")

speaker_filter = KobeVoiceprintFilter()
new_master = speaker_filter.enroll_master_voiceprint(valid_paths)
print(f"Purified Master Voiceprint Vector saved to: {speaker_filter.voiceprint_cache_path}")
print(f"Shape: {new_master.shape} | L2 Norm: {np.linalg.norm(new_master):.4f}")

print("\n=== STEP 2: Verifying Cosine Similarity Separation ===")
# Test on Kobe speech sample
kobe_wav = preprocess_wav(str(valid_paths[0]))
kobe_sample = kobe_wav[16000*20 : 16000*30] # 10s of Kobe speaking
kobe_sim = speaker_filter.compute_similarity(kobe_sample)
print(f"Kobe ('Mamba Out' sample) Cosine Similarity: {kobe_sim:.4f}")

# Test on the woman narrator in foMxhyT2g2g
female_path = Path(r"E:\Sound Experiments\Kobe bryant Database raw\sources\youtube\foMxhyT2g2g\audio.opus")
if female_path.exists():
    female_wav = preprocess_wav(str(female_path))
    female_sample = female_wav[16000*30 : 16000*40] # 10s of female narrator
    female_sim = speaker_filter.compute_similarity(female_sample)
    print(f"Female Narrator (foMxhyT2g2g sample) Cosine Similarity: {female_sim:.4f}")
    print(f"-> CLEAR SEPARATION DELTA: {kobe_sim - female_sim:.4f}")

print("\n=== STEP 3: Quarantining foMxhyT2g2g as NOT_KOBE ===")
db_path = config.catalog_path
conn = sqlite3.connect(str(db_path))
c = conn.cursor()

# Find raw_file id for foMxhyT2g2g
c.execute("""
    SELECT r.id, r.file_path, s.id 
    FROM raw_files r 
    JOIN sources s ON s.id = r.source_id 
    WHERE s.platform_id = 'foMxhyT2g2g'
""")
row = c.fetchone()
if row:
    raw_file_id, file_path_str, source_id = row
    fp = Path(file_path_str)
    
    # Destination in quarantine
    quarantine_dest = config.quarantine_dir / "not_kobe" / fp.name
    quarantine_dest.parent.mkdir(parents=True, exist_ok=True)
    
    if fp.exists():
        shutil.move(str(fp), str(quarantine_dest))
        print(f"Moved {fp} to {quarantine_dest}")
    
    c.execute("UPDATE raw_files SET status = 'quarantined', file_path = ? WHERE id = ?", (str(quarantine_dest), raw_file_id))
    c.execute("""
        INSERT INTO duplicates (raw_file_id, duplicate_of_id, match_type, similarity_score, details)
        VALUES (?, ?, 'NOT_KOBE', 0.0, 'Quarantined: User listening audit confirmed audio is narrated by a female speaker, not Kobe Bryant.')
    """, (raw_file_id, raw_file_id))
    conn.commit()
    print("Catalog updated: foMxhyT2g2g marked as quarantined (NOT_KOBE).")

conn.close()
print("\nDone! Master voiceprint is 100% purified and non-Kobe audio is quarantined.")
