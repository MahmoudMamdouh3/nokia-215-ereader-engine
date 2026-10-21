import sqlite3
import shutil
from pathlib import Path
from soundlab.config import config

old_not_kobe = config.quarantine_dir / "duplicates" / "not_kobe"
new_not_kobe = config.quarantine_dir / "not_kobe"

if old_not_kobe.exists():
    print(f"Migrating {old_not_kobe} to {new_not_kobe}")
    for p in list(old_not_kobe.rglob("*")):
        if p.is_file():
            rel = p.relative_to(old_not_kobe)
            dest = new_not_kobe / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(p), str(dest))
    shutil.rmtree(str(old_not_kobe), ignore_errors=True)

conn = sqlite3.connect(str(config.catalog_path))
c = conn.cursor()
c.execute("SELECT id, file_path FROM raw_files WHERE file_path LIKE '%_quarantine%duplicates%not_kobe%'")
rows = c.fetchall()
print(f"Updating {len(rows)} records in database...")
for rid, fp in rows:
    new_fp = fp.replace("_quarantine\\duplicates\\not_kobe", "_quarantine\\not_kobe")
    c.execute("UPDATE raw_files SET file_path = ? WHERE id = ?", (new_fp, rid))

conn.commit()
conn.close()
print("Migration and DB path update complete!")
