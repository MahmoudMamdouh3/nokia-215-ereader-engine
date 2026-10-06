"""
Downloader for Tafsir Al-Mukhtasar (تفسير المختصر) - Arabic and English
Fetches all 114 Surahs from QuranEnc API.
"""

import os
import sys
import json
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"E:\nokia\books_raw"
AR_DIR = os.path.join(BASE_DIR, "tafsir_mokhtasar_ar")
EN_DIR = os.path.join(BASE_DIR, "tafsir_mokhtasar_en")

os.makedirs(AR_DIR, exist_ok=True)
os.makedirs(EN_DIR, exist_ok=True)

def fetch_sura(key, sura_num, out_path):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 100:
        return sura_num, True, "cached"
    url = f"https://quranenc.com/api/v1/translation/sura/{key}/{sura_num}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                # Verify valid json
                json.loads(data.decode('utf-8'))
                with open(out_path, 'wb') as f:
                    f.write(data)
                return sura_num, True, "downloaded"
        except Exception as e:
            time.sleep(1 + attempt)
    return sura_num, False, "failed"

def download_edition(name, key, out_dir):
    print(f"\n==================================================")
    print(f" Downloading Tafsir Al-Mukhtasar: {name}")
    print(f"==================================================")
    tasks = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        for s in range(1, 115):
            out_file = os.path.join(out_dir, f"{s}.json")
            tasks.append(executor.submit(fetch_sura, key, s, out_file))
        
        success = 0
        for future in as_completed(tasks):
            s_num, ok, status = future.result()
            if ok:
                success += 1
            else:
                print(f"  [!] Failed Surah {s_num}")
                
    print(f"-> {name}: {success}/114 Surahs successfully downloaded & verified.")

if __name__ == "__main__":
    download_edition("Arabic Mokhtasar (المختصر في تفسير القرآن)", "arabic_mokhtasar", AR_DIR)
    download_edition("English Mokhtasar", "english_mokhtasar", EN_DIR)
