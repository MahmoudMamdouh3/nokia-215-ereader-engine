import os
import shutil
import sqlite3
import time
from pathlib import Path
from soundlab.config import config

targets = [
    (816, "Narrated sports documentary essay (Buzzer Beaters) by third-party journalist, not Kobe Bryant."),
    (819, "Charles Barkley speaking on TNT Inside the NBA discussing Kobe, not Kobe Bryant speaking.")
]

conn = sqlite3.connect(str(config.catalog_path))
c = conn.cursor()

for raw_id, reason in targets:
    row = c.execute("SELECT r.id, s.title, r.file_path, s.platform_id FROM raw_files r JOIN sources s ON r.source_id = s.id WHERE r.id = ?", (raw_id,)).fetchone()
    if not row:
        print(f"#{raw_id} not found")
        continue
        
    _, title, fpath_str, pid = row
    fp = Path(fpath_str)
    
    # Target in quarantine
    dest_dir = config.quarantine_dir / "not_kobe" / pid
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_file = dest_dir / fp.name
    
    if fp.exists():
        for attempt in range(5):
            try:
                shutil.move(str(fp), str(dest_file))
                print(f"Moved {fp} to {dest_file}")
                # Prune empty parent dir in sources
                parent = fp.parent
                if parent.exists() and not any(parent.iterdir()):
                    parent.rmdir()
                    print(f"Pruned empty stub dir: {parent}")
                break
            except PermissionError as e:
                print(f"File locked on attempt {attempt+1}, retrying in 2s...")
                time.sleep(2)
                
    # Update catalog
    c.execute("UPDATE raw_files SET status = 'quarantined', file_path = ? WHERE id = ?", (str(dest_file), raw_id))
    c.execute("""
        INSERT INTO duplicates (raw_file_id, duplicate_of_id, match_type, similarity_score, details)
        VALUES (?, ?, 'NOT_KOBE', 0.0, ?)
    """, (raw_id, raw_id, f"Quarantined: {reason}"))
    conn.commit()
    print(f"Catalog updated: #{raw_id} marked as quarantined (NOT_KOBE).")

# Update pre-download filter hardening in ingestion.py & purge_irrelevant_files.py
print("Quarantine completed successfully.")
