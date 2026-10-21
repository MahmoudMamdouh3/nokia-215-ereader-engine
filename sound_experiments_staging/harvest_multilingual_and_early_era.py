import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from soundlab.ingestion import IngestionEngine

queries = [
    "Kobe Bryant habla espanol entrevista completa Univision uncut",
    "Kobe Bryant entrevista completa espanol ESPN Deportes uncut",
    "Kobe Bryant Milan AC Milan football uncut interview Italian",
    "Kobe Bryant parla italiano intervista integrale Radio Deejay",
    "Kobe Bryant rookie interview 1996 raw uncut",
    "Kobe Bryant 1997 slam dunk contest post contest interview uncut",
    "Kobe Bryant 1998 all star game interview uncut",
    "Kobe Bryant USA Basketball mini camp interview Las Vegas raw",
]

print(f"Searching candidate URLs across {len(queries)} multilingual & early-era vectors...")

def search_query(q):
    cmd = ['yt-dlp', f'ytsearch3:{q}', '--print', '%(webpage_url)s', '--no-playlist']
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=60)
        return [l.strip() for l in res.stdout.strip().splitlines() if l.strip().startswith('http')]
    except Exception as e:
        print(f"Search failed for {q}: {e}")
        return []

all_urls = set()
for q in queries:
    urls = search_query(q)
    print(f"Query '{q}' found {len(urls)} URLs")
    for u in urls:
        all_urls.add(u)

print(f"\nDiscovered {len(all_urls)} unique candidate URLs. Starting parallel ingestion with 3 worker threads...")

def ingest_url(u):
    engine = IngestionEngine()
    try:
        res = engine.download_url(u)
        return (u, res)
    except Exception as e:
        return (u, f"Error: {e}")

with ThreadPoolExecutor(max_workers=3) as pool:
    futures = [pool.submit(ingest_url, u) for u in all_urls]
    for fut in as_completed(futures):
        u, res = fut.result()
        print(f"Finished {u} -> {res}")

print("Multilingual & Early-era harvest batch finished!")
