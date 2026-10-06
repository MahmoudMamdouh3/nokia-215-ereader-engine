"""
Holy Quran Audio Downloader and Installer for Nokia 215 4G
Downloads full 114 Surahs recitations from verified CDN (mp3quran.net)
Embeds clean ID3 tags and stores them in F:\\Quran with canonical 3-digit order.
"""

import os
import sys
import json
import time
import subprocess
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

SD_QURAN = r"F:\Quran"
LOCAL_CACHE = r"E:\nokia\scratch"
QURAN_META_FILE = r"E:\nokia\books_raw\quran.json"
MANIFEST_FILE = r"E:\nokia\quran_manifest.json"

RECITERS = [
    {
        "id": 1,
        "folder": "01_Mohamed_Siddiq_El_Minshawi_Mujawwad",
        "artist": "الشيخ محمد صديق المنشاوي",
        "album": "المصحف المجود",
        "server": "https://cdn.mp3quran.net/audio/muhammad-minshawi/r2/",
        "total_surahs": 114,
        "description": "الختمة المجودة للشيخ محمد صديق المنشاوي"
    },
    {
        "id": 2,
        "folder": "02_Mohamed_Siddiq_El_Minshawi_Murattal",
        "artist": "الشيخ محمد صديق المنشاوي",
        "album": "المصحف المرتل",
        "server": "https://cdn.mp3quran.net/audio/muhammad-minshawi/r1/",
        "total_surahs": 114,
        "description": "المصحف المرتل للشيخ محمد صديق المنشاوي"
    },
    {
        "id": 3,
        "folder": "03_Fares_Abbad",
        "artist": "الشيخ فارس عباد",
        "album": "القرآن الكريم",
        "server": "https://cdn.mp3quran.net/audio/fares-abbad/r1/",
        "total_surahs": 114,
        "description": "المصحف المرتل كاملاً للشيخ فارس عباد"
    },
    {
        "id": 4,
        "folder": "04_Mahmoud_Khalil_Al_Hussary_Murattal",
        "artist": "الشيخ محمود خليل الحصري",
        "album": "المصحف المرتل",
        "server": "https://cdn.mp3quran.net/audio/mahmoud-husary/r1/",
        "total_surahs": 114,
        "description": "المصحف المرتل للشيخ محمود خليل الحصري (حفص عن عاصم)"
    },
    {
        "id": 5,
        "folder": "05_Mahmoud_Khalil_Al_Hussary_Mujawwad",
        "artist": "الشيخ محمود خليل الحصري",
        "album": "المصحف المجود",
        "server": "https://cdn.mp3quran.net/audio/mahmoud-husary/r2/",
        "total_surahs": 114,
        "description": "المصحف المجود للشيخ محمود خليل الحصري"
    }
]

def load_surah_names():
    if os.path.exists(QURAN_META_FILE):
        with open(QURAN_META_FILE, "r", encoding="utf-8") as f:
            surahs = json.load(f)
            names = {}
            for s in surahs:
                sid = s["id"]
                ar = s["name"]
                en = s.get("transliteration", f"Surah_{sid}").replace("'", "").replace(" ", "-")
                names[sid] = (ar, en)
            return names
    # Fallback to standard 114
    return {i: (f"سورة_{i}", f"Surah_{i}") for i in range(1, 115)}

def load_manifest():
    if os.path.exists(MANIFEST_FILE):
        try:
            with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"completed_reciters": [], "details": {}}

def save_manifest(manifest):
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    sd_manifest = os.path.join(SD_QURAN, "quran_manifest.json")
    try:
        os.makedirs(SD_QURAN, exist_ok=True)
        with open(sd_manifest, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def download_and_tag_surah(reciter, surah_num, surah_names):
    ar_name, en_name = surah_names.get(surah_num, (f"سورة_{surah_num}", f"Surah_{surah_num}"))
    out_dir = os.path.join(SD_QURAN, reciter["folder"])
    filename = f"{surah_num:03d}_{en_name}_{ar_name}.mp3"
    final_path = os.path.join(out_dir, filename)

    if os.path.exists(final_path) and os.path.getsize(final_path) > 50000:
        return True, surah_num, "Already exists"

    url = f"{reciter['server']}{surah_num:03d}.mp3"
    temp_raw = os.path.join(LOCAL_CACHE, f"q_{reciter['id']}_{surah_num:03d}.mp3")

    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            with open(temp_raw, "wb") as f_out:
                f_out.write(resp.read())
    except Exception as e:
        if os.path.exists(temp_raw):
            os.remove(temp_raw)
        return False, surah_num, str(e)

    # Use ffmpeg to tag with clean ID3 tags
    title_tag = f"{surah_num:03d} - سورة {ar_name} ({en_name})"
    cmd = [
        "ffmpeg", "-y", "-i", temp_raw,
        "-c", "copy",
        "-metadata", f"artist={reciter['artist']}",
        "-metadata", f"album={reciter['album']}",
        "-metadata", f"title={title_tag}",
        "-metadata", f"track={surah_num}",
        "-metadata", "genre=Quran",
        final_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(temp_raw):
        try:
            os.remove(temp_raw)
        except Exception:
            pass

    if res.returncode == 0 and os.path.exists(final_path):
        return True, surah_num, "Success"
    return False, surah_num, "FFmpeg tagging error"

def download_reciter(reciter, surah_names, manifest):
    rec_id = str(reciter["id"])
    print(f"\n=======================================================")
    print(f"[{reciter['id']}/5] Reciter: {reciter['artist']} - {reciter['album']}")
    print(f"Description: {reciter['description']}")
    print(f"Server: {reciter['server']}")
    print(f"=======================================================")

    out_dir = os.path.join(SD_QURAN, reciter["folder"])
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(LOCAL_CACHE, exist_ok=True)

    success_count = 0
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {
            executor.submit(download_and_tag_surah, reciter, s_num, surah_names): s_num
            for s_num in range(1, 115)
        }
        for fut in as_completed(futures):
            s_num = futures[fut]
            try:
                ok, num, msg = fut.result()
                if ok:
                    success_count += 1
                    if success_count % 15 == 0 or success_count == 114:
                        print(f"  [Progress] {success_count}/114 Surahs downloaded...")
                else:
                    print(f"  [Warning] Surah {s_num}: {msg}")
            except Exception as e:
                print(f"  [Error] Surah {s_num}: {e}")

    print(f"Reciter {reciter['id']} finished: {success_count}/114 surahs installed in {out_dir}")
    if success_count >= 110:
        if rec_id not in manifest.get("completed_reciters", []):
            manifest.setdefault("completed_reciters", []).append(rec_id)
        manifest.setdefault("details", {})[rec_id] = {
            "artist": reciter["artist"],
            "album": reciter["album"],
            "folder": reciter["folder"],
            "surahs_installed": success_count
        }
        save_manifest(manifest)
    return success_count

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    surah_names = load_surah_names()
    manifest = load_manifest()

    if len(sys.argv) > 1 and sys.argv[1].lower() == "status":
        print(f"Completed Quran Recitations: {len(manifest.get('completed_reciters', []))} / {len(RECITERS)}")
        for rec in RECITERS:
            r_dir = os.path.join(SD_QURAN, rec["folder"])
            count = len([f for f in os.listdir(r_dir) if f.endswith('.mp3')]) if os.path.exists(r_dir) else 0
            print(f"  - [{rec['id']}] {rec['artist']} ({rec['album']}): {count}/114 Surahs")
        sys.exit(0)

    selected_ids = [int(arg) for arg in sys.argv[1:] if arg.isdigit()]
    targets = [r for r in RECITERS if not selected_ids or r["id"] in selected_ids]

    for rec in targets:
        download_reciter(rec, surah_names, manifest)

    print("\nHoly Quran recitations processing complete!")
