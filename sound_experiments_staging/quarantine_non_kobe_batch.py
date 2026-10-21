import os
import shutil
import sqlite3
import time
from pathlib import Path
from soundlab.config import config

targets = [
    (824, "Shaq and KG speaking on bench during 1998 ASG (similarity 0.63), not Kobe."),
    (825, "LeBron James recounting Redeem Team story on Netflix, not Kobe."),
    (827, "Teammates recounting Vegas club story about Kobe, not Kobe."),
    (829, "Noisy All-Star arena audio (similarity 0.77, below 0.82 threshold)."),
    (831, "Italian news memorial clip ('Morto Kobe Bryant')."),
    (833, "TV play-by-play broadcast commentary ('Kobe waves off Karl Malone', similarity 0.68)."),
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

print("Batch quarantine completed successfully.")
