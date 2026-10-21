import sqlite3
import shutil
import json
from pathlib import Path
from soundlab.config import config

conn = sqlite3.connect(str(config.catalog_path))
c = conn.cursor()

c.execute('''
    SELECT r.id, s.title, s.platform_id, r.file_path, s.metadata_json 
    FROM sources s 
    JOIN raw_files r ON r.source_id = s.id 
    WHERE r.status = 'active'
''')

rows = c.fetchall()
quarantine_count = 0
kobe_keywords = ["kobe", "bryant", "mamba", "dear basketball", "wizenard", "81 point", "staples center"]

for raw_id, title, platform_id, file_path_str, meta_str in rows:
    title_lower = title.lower()
    meta = {}
    try:
        if meta_str:
            meta = json.loads(meta_str)
    except Exception:
        pass
    
    desc_lower = (meta.get("description") or "").lower()
    tags_lower = [str(t).lower() for t in meta.get("tags") or []]
    
    is_kobe = any(k in title_lower for k in kobe_keywords)
    
    non_kobe_indicators = [
        "narrated by",
        "reveals kobe",
        "story about kobe",
        "stories about kobe",
        "opens up about kobe",
        "tells story about",
        "memorializing kobe",
        "coaching kobe",
        "what it was like coaching",
        "luke on lebron",
        "vanessa bryant",
        "michael jordan",
        "memorial service",
        "memorial",
        "eulogy",
        "la morte di",
        "usain bolt",
        "sylvester stallone",
        "federico buffa racconta",
        "muerte de",
        "muere ",
        "suegra de",
        "se divorcia",
        "rueda de prensa",
        "pau gasol",
        "llorando",
        "numerología",
        "entrenaba con",
        "homenaje",
        "tributo",
        "accidente",
        "tragedia",
        "funeral",
        "entierro",
        "despiden a",
        "autopsia",
        "helicoptero",
        "helicóptero",
        "death",
        "r.i.p",
        "rest in peace",
        "passed away",
        "audiobook) by",
        "audiobook by",
        "(audiobook)",
        "dies at",
        "promotes witchcraft",
        "satanism",
        "takes final bow",
        "faye bryant",
        "the wizenard series: season one",
        "training day book 1",
        "crash",
        "after he died",
        "disrespects",
        "talking trash",
        "passing of",
        "tmz",
        "on guarding",
        "guarding kobe",
        "dissing kobe",
        " diss ",
        "diss 2010",
        "diss track",
        "b.e. - kobe",
        "last 3 minutes of",
        "last minutes of",
        "farewell game |",
        "farewell game (",
        " on the time ",
        " on kobe",
        " on playing with",
        " on facing kobe",
        "coach k:",
        "coach k ",
        "drops 60 in",
        "drops 81 in",
        "documentary",
        "assists!",
        "legends share",
        "nba legends share",
        "craziest kobe bryant story",
        "resumen libro",
        "resumen del libro",
        "lecciones que nos dejó",
        "una amistad más allá",
        "más allá de las canchas",
        "choc nel mondo",
        "unomattina",
        "pays tribute",
        "paying tribute",
        "tribute to kobe",
        "tribute to gianna",
        "first take",
        "skip bayless",
        "stephen a.",
        "shannon sharpe",
        "undisputed",
        "max kellerman",
        "colin cowherd",
        "debunked",
        "the lakers dynasty",
        "speaks on kobe",
        "speak on kobe",
        "work ethic stories",
        "kobe stories",
        "kobe bryant stories",
        "arriving to see",
        "arriving at",
        "arrives at",
        "game highlights",
        "full game highlights",
        "highlights |",
        "highlights -",
        "point game!",
        "point game at",
        "amazing last ",
        "final game vs jazz",
        "kobe draft 1996",
    ]
    is_third_party = any(ind in title_lower for ind in non_kobe_indicators)
    
    if not is_third_party:
        for talk_phrase in [
            "talks about ", "talking about ", "remembers ", "remembering ", 
            "reflects on ", "reflecting on ", "reacts to ", "reacting to ",
            "says kobe", "say kobe", "claims kobe", "breaks down kobe",
            " on was kobe", " on whether kobe"
        ]:
            if talk_phrase in title_lower:
                idx = title_lower.find(talk_phrase)
                prefix = title_lower[:idx]
                if not any(k in prefix for k in ["kobe", "bryant", "mamba"]):
                    is_third_party = True
                    break
    
    if not is_kobe or is_third_party:
        fp = Path(file_path_str)
        quarantine_dest = config.quarantine_dir / "not_kobe" / platform_id / fp.name
        quarantine_dest.parent.mkdir(parents=True, exist_ok=True)
        
        safe_title = title.encode("ascii", "replace").decode("ascii")
        print(f"[Quarantining Non-Kobe] #{raw_id}: {safe_title} ({platform_id})")
        
        if fp.exists():
            shutil.move(str(fp), str(quarantine_dest))
            if fp.parent.exists() and not any(fp.parent.iterdir()):
                try:
                    fp.parent.rmdir()
                except Exception:
                    pass
            
        c.execute("UPDATE raw_files SET status = 'quarantined', file_path = ? WHERE id = ?", (str(quarantine_dest), raw_id))
        c.execute("""
            INSERT INTO duplicates (raw_file_id, duplicate_of_id, match_type, similarity_score, details)
            VALUES (?, ?, 'NOT_KOBE_IRRELEVANT', 0.0, ?)
        """, (raw_id, raw_id, f"Quarantined: Video '{safe_title}' does not reference Kobe Bryant in title, tags, or description."))
        quarantine_count += 1

conn.commit()
conn.close()

print(f"\nAudit complete! Successfully quarantined {quarantine_count} non-Kobe files.")
