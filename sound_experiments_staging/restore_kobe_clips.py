import sqlite3
import shutil
from pathlib import Path
from soundlab.config import config

conn = sqlite3.connect(str(config.catalog_path))
c = conn.cursor()

falsely_quarantined_ids = [44, 112, 121, 314, 316, 321, 618]

for rid in falsely_quarantined_ids:
    c.execute("""
        SELECT r.id, s.title, s.platform_id, r.file_path 
        FROM raw_files r 
        JOIN sources s ON s.id = r.source_id 
        WHERE r.id = ?
    """, (rid,))
    row = c.fetchone()
    if not row:
        continue
    raw_id, title, platform_id, current_path_str = row
    curr_p = Path(current_path_str)
    
    # Destination back in sources/youtube/
    dest_dir = config.raw_dir / "sources" / "youtube" / platform_id
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_file = dest_dir / curr_p.name
    
    if curr_p.exists():
        shutil.move(str(curr_p), str(dest_file))
        # Remove empty quarantine stub if empty
        if curr_p.parent.exists() and not any(curr_p.parent.iterdir()):
            try:
                curr_p.parent.rmdir()
            except Exception:
                pass
                
    c.execute("UPDATE raw_files SET status = 'active', file_path = ? WHERE id = ?", (str(dest_file), raw_id))
    c.execute("DELETE FROM duplicates WHERE raw_file_id = ? AND match_type = 'NOT_KOBE_IRRELEVANT'", (raw_id,))
    safe_title = title.encode("ascii", "replace").decode("ascii")
    print(f"Restored #{raw_id} to active: {safe_title}")

conn.commit()
conn.close()
print("Restoration complete!")
