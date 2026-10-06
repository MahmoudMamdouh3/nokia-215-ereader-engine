# -*- coding: utf-8 -*-
"""
Audiobooks Downloader and Installer for Nokia 215 4G
Downloads full unabridged audiobooks in English and Arabic for the installed book library.
Prioritizes original author voices (James Clear, Robert Greene, etc.) and official Arabic narrations.
Splits long recordings into 30-minute segments (96 kbps MP3) with clean ID3 tags
for smooth hardware playback and seeking on Nokia S30+ feature phones.
"""

import os
import sys
import json
import time
import shutil
import subprocess

SD_AUDIOBOOKS = r"F:\Audiobooks"
LOCAL_CACHE = r"E:\nokia\scratch"
MANIFEST_FILE = r"E:\nokia\audiobooks_manifest.json"

AUDIOBOOKS_CATALOG = [
    # =========================================================================
    # 01_ENGLISH (Original Author Voices & Official Unabridged Editions)
    # =========================================================================
    {
        "id": "EN_01",
        "category": "01_English",
        "book": "Atomic Habits",
        "author": "James Clear",
        "narrator": "James Clear (Original Author Voice)",
        "folder": "01_Atomic_Habits_James_Clear",
        "yt_id": "UYxb-v__EIw",
        "language": "English",
        "description": "Atomic Habits unabridged, read by the author James Clear"
    },
    {
        "id": "EN_02",
        "category": "01_English",
        "book": "The Psychology of Money",
        "author": "Morgan Housel",
        "narrator": "Chris Hill (Official HarperAudio)",
        "folder": "02_The_Psychology_Of_Money_Morgan_Housel",
        "yt_id": "6EMlUsBx0z0",
        "language": "English",
        "description": "The Psychology of Money official unabridged audiobook"
    },
    {
        "id": "EN_03",
        "category": "01_English",
        "book": "How to Win Friends and Influence People",
        "author": "Dale Carnegie",
        "narrator": "Official Unabridged",
        "folder": "03_How_To_Win_Friends_Dale_Carnegie",
        "yt_id": "d9zUVFzPtJ4",
        "language": "English",
        "description": "How to Win Friends and Influence People complete audiobook"
    },
    {
        "id": "EN_04",
        "category": "01_English",
        "book": "The 48 Laws of Power",
        "author": "Robert Greene",
        "narrator": "Richard Poe (Official Unabridged)",
        "folder": "04_The_48_Laws_Of_Power_Robert_Greene",
        "yt_id": "veKqaVlVD_I",
        "language": "English",
        "description": "The 48 Laws of Power complete unabridged audiobook"
    },
    {
        "id": "EN_05",
        "category": "01_English",
        "book": "The Laws of Human Nature",
        "author": "Robert Greene",
        "narrator": "Robert Greene (Original Author)",
        "folder": "05_The_Laws_Of_Human_Nature_Robert_Greene",
        "yt_id": "pzdzMSxBU-I",
        "language": "English",
        "description": "The Laws of Human Nature unabridged key teachings"
    },
    {
        "id": "EN_06",
        "category": "01_English",
        "book": "The Art of Seduction",
        "author": "Robert Greene",
        "narrator": "Official Unabridged",
        "folder": "06_The_Art_Of_Seduction_Robert_Greene",
        "yt_id": "7SM_2ad5d98",
        "language": "English",
        "description": "The Art of Seduction complete unabridged audiobook"
    },
    {
        "id": "EN_07",
        "category": "01_English",
        "book": "Mastery",
        "author": "Robert Greene",
        "narrator": "Fred Sanders (Official)",
        "folder": "07_Mastery_Robert_Greene",
        "yt_id": "VMcq2-AhOQQ",
        "language": "English",
        "description": "Mastery unabridged audiobook parts 1 & 2"
    },
    {
        "id": "EN_08",
        "category": "01_English",
        "book": "1984",
        "author": "George Orwell",
        "narrator": "Simon Prebble (Official Unabridged)",
        "folder": "08_1984_George_Orwell",
        "yt_id": "5jjnIBITmbg",
        "language": "English",
        "description": "1984 unabridged classic dystopian novel"
    },
    {
        "id": "EN_09",
        "category": "01_English",
        "book": "Animal Farm",
        "author": "George Orwell",
        "narrator": "Ralph Cosham (Unabridged)",
        "folder": "09_Animal_Farm_George_Orwell",
        "yt_id": "T_rcQPHTjS8",
        "language": "English",
        "description": "Animal Farm unabridged political allegory"
    },
    {
        "id": "EN_10",
        "category": "01_English",
        "book": "The Alchemist",
        "author": "Paulo Coelho",
        "narrator": "Jeremy Irons (Official HarperAudio)",
        "folder": "10_The_Alchemist_Paulo_Coelho",
        "yt_id": "yT6cQkxEz98",
        "language": "English",
        "description": "The Alchemist narrated by Academy Award winner Jeremy Irons"
    },
    {
        "id": "EN_11",
        "category": "01_English",
        "book": "The Prophet",
        "author": "Kahlil Gibran",
        "narrator": "Paul Sparer",
        "folder": "11_The_Prophet_Kahlil_Gibran",
        "yt_id": "VrzSjlQqPX4",
        "language": "English",
        "description": "The Prophet complete unabridged poetic philosophy"
    },
    {
        "id": "EN_12",
        "category": "01_English",
        "book": "Meditations",
        "author": "Marcus Aurelius",
        "narrator": "Duncan Steen",
        "folder": "12_Meditations_Marcus_Aurelius",
        "yt_id": "_6cSYKeafmk",
        "language": "English",
        "description": "Meditations unabridged Stoic masterpiece"
    },
    {
        "id": "EN_13",
        "category": "01_English",
        "book": "The Art of War",
        "author": "Sun Tzu",
        "narrator": "Lionel Giles Translation / Unabridged",
        "folder": "13_The_Art_Of_War_Sun_Tzu",
        "yt_id": "jxcMRkqaQdw",
        "language": "English",
        "description": "The Art of War complete unabridged strategic treatise"
    },
    {
        "id": "EN_14",
        "category": "01_English",
        "book": "The Old Man and the Sea",
        "author": "Ernest Hemingway",
        "narrator": "Charlton Heston (Official)",
        "folder": "14_The_Old_Man_And_The_Sea_Hemingway",
        "yt_id": "vvjwGq0CeQA",
        "language": "English",
        "description": "The Old Man and the Sea complete audiobook"
    },
    {
        "id": "EN_15",
        "category": "01_English",
        "book": "White Nights",
        "author": "Fyodor Dostoevsky",
        "narrator": "David Thorn (Unabridged)",
        "folder": "15_White_Nights_Dostoevsky",
        "yt_id": "xfcxF2Uqpzc",
        "language": "English",
        "description": "White Nights complete sentimental novel"
    },
    {
        "id": "EN_16",
        "category": "01_English",
        "book": "The Metamorphosis",
        "author": "Franz Kafka",
        "narrator": "Benedict Cumberbatch (BBC)",
        "folder": "16_The_Metamorphosis_Kafka",
        "yt_id": "4FS7PibPxVM",
        "language": "English",
        "description": "The Metamorphosis complete BBC dramatic reading"
    },

    # =========================================================================
    # 02_ARABIC (Official & Best Professional Arabic Audio Editions)
    # =========================================================================
    {
        "id": "AR_01",
        "category": "02_Arabic",
        "book": "العادات الذرية",
        "author": "جيمس كلير",
        "narrator": "كتاب صوتي كامل (النسخة العربية المعتمدة)",
        "folder": "01_Al_Adat_Al_Dharriyah_Atomic_Habits",
        "yt_id": "lCrjKeyLYd4",
        "language": "Arabic",
        "description": "كتاب العادات الذرية كاملاً بصوت احترافي رسمي"
    },
    {
        "id": "AR_02",
        "category": "02_Arabic",
        "book": "سيكولوجية المال",
        "author": "مورغان هاوسل",
        "narrator": "كتاب صوتي كامل",
        "folder": "02_Psychology_Of_Money_Arabic",
        "yt_id": "S93RF2ukxMo",
        "language": "Arabic",
        "description": "كتاب سيكولوجية المال كاملاً بصوت احترافي"
    },
    {
        "id": "AR_03",
        "category": "02_Arabic",
        "book": "كيف تؤثر على الآخرين وتكتسب الأصدقاء",
        "author": "ديل كارنيجي",
        "narrator": "كتاب صوتي كامل",
        "folder": "03_How_To_Win_Friends_Arabic",
        "yt_id": "5IjA9gW5oKg",
        "language": "Arabic",
        "description": "كتاب كيف تكسب الأصدقاء وتؤثر في الناس كاملاً"
    },
    {
        "id": "AR_04",
        "category": "02_Arabic",
        "book": "قواعد السطوة الـ 48",
        "author": "روبرت غرين",
        "narrator": "كتاب صوتي كامل",
        "folder": "04_48_Laws_Of_Power_Arabic",
        "yt_id": "15hE5wRSpTk",
        "language": "Arabic",
        "description": "كتاب 48 قانون للقوة والسطوة لروبرت غرين كاملاً"
    },
    {
        "id": "AR_05",
        "category": "02_Arabic",
        "book": "قوانين الطبيعة البشرية",
        "author": "روبرت غرين",
        "narrator": "كتاب صوتي كامل",
        "folder": "05_Laws_Of_Human_Nature_Arabic",
        "yt_id": "Cv1OHK-c0ps",
        "language": "Arabic",
        "description": "كتاب قوانين الطبيعة البشرية كاملاً مسموع"
    },
    {
        "id": "AR_06",
        "category": "02_Arabic",
        "book": "فن الإغواء",
        "author": "روبرت غرين",
        "narrator": "كتاب صوتي كامل",
        "folder": "06_Art_Of_Seduction_Arabic",
        "yt_id": "VRLoUwyW98k",
        "language": "Arabic",
        "description": "كتاب فن الإغواء لروبرت غرين كاملاً مسموع"
    },
    {
        "id": "AR_07",
        "category": "02_Arabic",
        "book": "الإتقان",
        "author": "روبرت غرين",
        "narrator": "كتاب صوتي كامل",
        "folder": "07_Mastery_Arabic",
        "yt_id": "aOPg8BZUuXE",
        "language": "Arabic",
        "description": "كتاب الإتقان (Mastery) لروبرت غرين كاملاً مسموع"
    },
    {
        "id": "AR_08",
        "category": "02_Arabic",
        "book": "1984",
        "author": "جورج أورويل",
        "narrator": "رواية صوتية كاملة احترافية",
        "folder": "08_1984_Arabic",
        "yt_id": "2N_Gh2oVXKE",
        "language": "Arabic",
        "description": "رواية 1984 لجورج أورويل كاملة مسموعة باللغة العربية"
    },
    {
        "id": "AR_09",
        "category": "02_Arabic",
        "book": "مزرعة الحيوان",
        "author": "جورج أورويل",
        "narrator": "رواية صوتية كاملة",
        "folder": "09_Animal_Farm_Arabic",
        "yt_id": "zY7grhATzac",
        "language": "Arabic",
        "description": "رواية مزرعة الحيوان لجورج أورويل كاملة مسموعة"
    },
    {
        "id": "AR_10",
        "category": "02_Arabic",
        "book": "الخيميائي",
        "author": "باولو كويلو",
        "narrator": "رواية صوتية كاملة (الإذاعة)",
        "folder": "10_The_Alchemist_Arabic",
        "yt_id": "V3mOmf7K4DA",
        "language": "Arabic",
        "description": "رواية الخيميائي لباولو كويلو كاملة بصوت إذاعي احترافي"
    },
    {
        "id": "AR_11",
        "category": "02_Arabic",
        "book": "الأمير الصغير",
        "author": "أنطوان دو سانت إكزوبيري",
        "narrator": "رواية صوتية كاملة",
        "folder": "11_The_Little_Prince_Arabic",
        "yt_id": "4GFa9bnxNpA",
        "language": "Arabic",
        "description": "رواية الأمير الصغير كاملة بصوت عذب نقي"
    },
    {
        "id": "AR_12",
        "category": "02_Arabic",
        "book": "الليالي البيضاء",
        "author": "فيودور دوستويفسكي",
        "narrator": "رواية صوتية كاملة",
        "folder": "12_White_Nights_Arabic",
        "yt_id": "xVgmiSyQGOk",
        "language": "Arabic",
        "description": "رواية الليالي البيضاء لدوستويفسكي كاملة مسموعة"
    },
    {
        "id": "AR_13",
        "category": "02_Arabic",
        "book": "المحاكمة",
        "author": "فرانز كافكا",
        "narrator": "رواية صوتية كاملة",
        "folder": "13_The_Trial_Arabic",
        "yt_id": "r0er48t8eo0",
        "language": "Arabic",
        "description": "رواية المحاكمة لكافكا كاملة مسموعة"
    },
    {
        "id": "AR_14",
        "category": "02_Arabic",
        "book": "فن الحرب",
        "author": "سون تزو",
        "narrator": "كتاب صوتي كامل",
        "folder": "14_The_Art_Of_War_Arabic",
        "yt_id": "BFsmkIBy7Vw",
        "language": "Arabic",
        "description": "كتاب فن الحرب لسون تزو كاملاً مسموعاً باللغة العربية"
    },
    {
        "id": "AR_15",
        "category": "02_Arabic",
        "book": "التأملات",
        "author": "ماركوس أوريليوس",
        "narrator": "كتاب صوتي كامل",
        "folder": "15_Meditations_Arabic",
        "yt_id": "2uMPdcVdNys",
        "language": "Arabic",
        "description": "كتاب التأملات لماركوس أوريليوس كاملاً مسموعاً"
    },
    {
        "id": "AR_16",
        "category": "02_Arabic",
        "book": "الشيخ والبحر",
        "author": "إرنست همنغواي",
        "narrator": "رواية صوتية كاملة",
        "folder": "16_The_Old_Man_And_The_Sea_Arabic",
        "yt_id": "XX2g-85tMwI",
        "language": "Arabic",
        "description": "رواية الشيخ والبحر لإرنست همنغواي كاملة مسموعة"
    },
    {
        "id": "AR_17",
        "category": "02_Arabic",
        "book": "النبي",
        "author": "جبران خليل جبران",
        "narrator": "كتاب صوتي كامل",
        "folder": "17_The_Prophet_Arabic",
        "yt_id": "ph5lZjdoyWU",
        "language": "Arabic",
        "description": "كتاب النبي لجبران خليل جبران كاملاً مسموعاً"
    },
    {
        "id": "AR_18",
        "category": "02_Arabic",
        "book": "الجريمة والعقاب",
        "author": "فيودور دوستويفسكي",
        "narrator": "رواية صوتية كاملة",
        "folder": "18_Crime_And_Punishment_Arabic",
        "yt_id": "AWbGmPAWaMA",
        "language": "Arabic",
        "description": "رواية الجريمة والعقاب لدوستويفسكي مسموعة باللغة العربية"
    }
]

def load_manifest():
    if os.path.exists(MANIFEST_FILE):
        try:
            with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"completed_audiobooks": [], "books": {}}

def save_manifest(manifest):
    os.makedirs(os.path.dirname(MANIFEST_FILE), exist_ok=True)
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    sd_manifest = os.path.join(SD_AUDIOBOOKS, "audiobooks_manifest.json")
    try:
        os.makedirs(SD_AUDIOBOOKS, exist_ok=True)
        with open(sd_manifest, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def get_duration(file_path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return float(res.stdout.strip())
    except Exception:
        return 0.0

def process_audiobook(item, manifest):
    item_id = item["id"]
    book_title = item["book"]
    author = item["author"]
    narrator = item["narrator"]
    category = item["category"]
    folder_name = item["folder"]
    yt_id = item["yt_id"]

    os.makedirs(LOCAL_CACHE, exist_ok=True)

    # Check if already completed in manifest
    if item_id in manifest.get("completed_audiobooks", []):
        print(f"[{item_id}] {book_title} already completed in manifest. Skipping.", flush=True)
        return True

    dest_dir = os.path.join(SD_AUDIOBOOKS, category, folder_name)

    print(f"\n=======================================================", flush=True)
    print(f"[{item_id}] Processing Audiobook: {book_title} ({category})", flush=True)
    print(f"Author: {author} | Narrator: {narrator}", flush=True)
    print(f"YouTube ID: {yt_id}", flush=True)
    print(f"Target: {dest_dir}", flush=True)
    print(f"=======================================================", flush=True)

    staging_dir = os.path.join(LOCAL_CACHE, "ab_staging", item_id)
    staged_existing = sorted([os.path.join(staging_dir, f) for f in os.listdir(staging_dir) if f.endswith(".mp3")]) if os.path.exists(staging_dir) else []
    if len(staged_existing) > 0:
        print(f"  [Reusing Staged Files] Found {len(staged_existing)} parts already encoded on SSD! Skipping download.", flush=True)
        print(f"  [Copying to Phone] Transferring {len(staged_existing)} parts to {dest_dir}...", flush=True)
        os.makedirs(dest_dir, exist_ok=True)
        for sf in staged_existing:
            shutil.copy2(sf, os.path.join(dest_dir, os.path.basename(sf)))
        shutil.rmtree(staging_dir, ignore_errors=True)

        if item_id not in manifest.get("completed_audiobooks", []):
            manifest.setdefault("completed_audiobooks", []).append(item_id)
        manifest.setdefault("books", {})[item_id] = {
            "book": book_title,
            "author": author,
            "narrator": narrator,
            "category": category,
            "folder": folder_name,
            "parts_installed": len(staged_existing),
            "total_duration_minutes": len(staged_existing) * 30,
            "language": item.get("language", "English")
        }
        save_manifest(manifest)
        print(f"[{item_id}] Successfully installed: {book_title} ({len(staged_existing)} parts) in {dest_dir}!\n", flush=True)
        return True

    raw_temp = os.path.join(LOCAL_CACHE, f"temp_ab_{item_id}.mp4")
    url = f"https://www.youtube.com/watch?v={yt_id}"

    # Step 1: Download raw audio stream with yt-dlp
    download_cmd = [
        "yt-dlp",
        "--extractor-args", "youtube:player_client=mweb,web",
        "-f", "18/b[height<=360]/ba",
        "-N", "4",
        "--http-chunk-size", "10M",
        "--socket-timeout", "30",
        "--retries", "15",
        "--no-playlist",
        "-o", raw_temp,
        url
    ]

    print("  [Step 1/3] Downloading audio from YouTube...", flush=True)
    res = subprocess.run(download_cmd)
    if res.returncode != 0 or not os.path.exists(raw_temp):
        print(f"  [Error] Failed to download {book_title} ({yt_id})", flush=True)
        return False

    # Step 2: Get duration
    dur = get_duration(raw_temp)
    if dur <= 0:
        print("  [Error] Invalid audio duration", flush=True)
        if os.path.exists(raw_temp):
            os.remove(raw_temp)
        return False

    chunk_length = 1800  # 30 minutes in seconds
    num_parts = int(dur // chunk_length) + (1 if dur % chunk_length > 0 else 0)
    print(f"  [Step 2/3] Total Duration: {int(dur // 60)} minutes -> Splitting into {num_parts} parts (30 mins each)...", flush=True)

    # Step 3: Split and tag each part into local SSD staging first for maximum speed
    staging_dir = os.path.join(LOCAL_CACHE, "ab_staging", item_id)
    os.makedirs(staging_dir, exist_ok=True)

    print("  [Step 3/3] Encoding & Tagging parts at 96 kbps on SSD...", flush=True)
    success_parts = 0
    staged_files = []
    for part_idx in range(num_parts):
        start_sec = part_idx * chunk_length
        part_num = part_idx + 1
        part_filename = f"Pt{part_num:02d}.mp3"
        staging_part = os.path.join(staging_dir, part_filename)

        title_tag = f"{book_title} - Pt {part_num:02d}"
        artist_tag = f"{author} ({narrator})" if narrator else author

        ffmpeg_cmd = [
            "ffmpeg", "-y",
            "-ss", str(start_sec),
            "-i", raw_temp,
            "-t", str(chunk_length),
            "-vn",
            "-c:a", "libmp3lame",
            "-b:a", "96k",
            "-ar", "44100",
            "-metadata", f"artist={artist_tag}",
            "-metadata", f"album={book_title}",
            "-metadata", f"title={title_tag}",
            "-metadata", f"track={part_num}",
            "-metadata", "genre=Audiobook",
            staging_part
        ]

        p_res = subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if p_res.returncode == 0 and os.path.exists(staging_part):
            success_parts += 1
            staged_files.append(staging_part)
            print(f"    -> Encoded {part_filename} ({part_num}/{num_parts})", flush=True)
        else:
            print(f"    -> [Error] Failed part {part_filename}", flush=True)

    # Clean temporary raw file
    if os.path.exists(raw_temp):
        try:
            os.remove(raw_temp)
        except Exception:
            pass

    if success_parts == num_parts:
        print(f"  [Copying to Phone] Transferring {num_parts} parts to {dest_dir}...", flush=True)
        os.makedirs(dest_dir, exist_ok=True)
        for sf in staged_files:
            fname = os.path.basename(sf)
            shutil.copy2(sf, os.path.join(dest_dir, fname))

        # Cleanup staging
        shutil.rmtree(staging_dir, ignore_errors=True)

        if item_id not in manifest.get("completed_audiobooks", []):
            manifest.setdefault("completed_audiobooks", []).append(item_id)
        manifest.setdefault("books", {})[item_id] = {
            "book": book_title,
            "author": author,
            "narrator": narrator,
            "category": category,
            "folder": folder_name,
            "parts_installed": success_parts,
            "total_duration_minutes": int(dur // 60),
            "language": item.get("language", "English")
        }
        save_manifest(manifest)
        print(f"[{item_id}] Successfully installed: {book_title} ({success_parts} parts) in {dest_dir}!\n", flush=True)
        return True
    else:
        shutil.rmtree(staging_dir, ignore_errors=True)
    return False

def print_status(manifest):
    print("=" * 65, flush=True)
    print("NOKIA 215 4G AUDIOBOOKS LIBRARY STATUS", flush=True)
    print("=" * 65, flush=True)
    completed_ids = set(manifest.get("completed_audiobooks", []))
    books_meta = manifest.get("books", {})
    print(f"Installed on SD Card: {len(completed_ids)} / {len(AUDIOBOOKS_CATALOG)} Audiobooks\n", flush=True)

    for cat_name in ["01_English", "02_Arabic"]:
        cat_items = [b for b in AUDIOBOOKS_CATALOG if b["category"] == cat_name]
        print(f"--- {cat_name} ({len(cat_items)} Titles) ---", flush=True)
        for b in cat_items:
            b_id = b["id"]
            if b_id in completed_ids and b_id in books_meta:
                parts = books_meta[b_id].get("parts_installed", 0)
                status = f"INSTALLED ({parts} parts)"
            else:
                status = "Pending"
            author_info = f" [Voice: {b['narrator']}]" if "narrator" in b else ""
            print(f"  [{b['id']}] {b['book']} - {b['author']}{author_info} : {status}", flush=True)
        print(flush=True)

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    manifest = load_manifest()

    if len(sys.argv) > 1 and sys.argv[1].lower() == "status":
        print_status(manifest)
        sys.exit(0)

    # Filter targets
    targets = AUDIOBOOKS_CATALOG
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "en":
            targets = [b for b in AUDIOBOOKS_CATALOG if b["category"] == "01_English"]
        elif arg == "ar":
            targets = [b for b in AUDIOBOOKS_CATALOG if b["category"] == "02_Arabic"]
        else:
            # Match specific ID
            targets = [b for b in AUDIOBOOKS_CATALOG if b["id"].lower() == arg]

    print(f"Starting audiobooks pipeline for {len(targets)} titles...", flush=True)
    for item in targets:
        process_audiobook(item, manifest)

    print("\nAudiobooks pipeline processing completed!", flush=True)
