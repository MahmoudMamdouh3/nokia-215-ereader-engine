from concurrent.futures import ThreadPoolExecutor, as_completed
from soundlab.ingestion import IngestionEngine

candidate_urls = [
    "https://www.youtube.com/watch?v=IRVlFr2IyOQ", # 2010 Finals Game 7 press conference (593s)
    "https://www.youtube.com/watch?v=V-qOe_XSgIo", # 2010 Finals Game 7 interview (311s)
    "https://www.youtube.com/watch?v=81D1TD1nkFg", # Postgame Presser: Kobe Bryant Game 6 (403s)
    "https://www.youtube.com/watch?v=0y6WVfthPW4", # Kobe Bryant 19 on Leno (424s)
    "https://www.youtube.com/watch?v=Xy-LTRCo4Pk", # Kobe Bryant on The Tonight Show with Jay Leno 1996 (350s)
    "https://www.youtube.com/watch?v=vSeSGx2SDnI", # Kobe Bryant Interview Part 01 - Conan on TBS (283s)
    "https://www.youtube.com/watch?v=ZOXo4Z8josI", # Kobe Bryant Jimmy Fallon 1996 story (144s)
    "https://www.youtube.com/watch?v=0zJh2FMTaDE", # Kobe Bryant Fallon kids tips (181s)
]

print(f"Starting parallel ingestion for {len(candidate_urls)} late-night & championship presser candidates...")

def ingest(u):
    engine = IngestionEngine()
    try:
        res = engine.download_url(u)
        return (u, res)
    except Exception as e:
        return (u, f"Error: {e}")

with ThreadPoolExecutor(max_workers=3) as pool:
    futures = [pool.submit(ingest, u) for u in candidate_urls]
    for fut in as_completed(futures):
        u, res = fut.result()
        print(f"Result for {u}: {res}")

print("Batch complete!")
