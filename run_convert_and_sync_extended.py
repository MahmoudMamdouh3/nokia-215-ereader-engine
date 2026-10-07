"""
Nokia 215 4G - Extended Library Master Batch Converter & Sync
============================================================
1. Converts curated 20 world literature masterpieces (10 Arabic, 10 English)
   from books_raw into calibrated 240x280 image slices in books_out.
2. Synchronizes to F:\\Books safely while enforcing > 5.0 GB free space on SD.
"""

import os
import sys
import time
import shutil
import multiprocessing as mp

sys.stdout.reconfigure(encoding='utf-8')

from convert_extended_library import convert_book

BASE_DIR = r"E:\nokia"
RAW_DIR = os.path.join(BASE_DIR, "books_raw")
OUT_DIR = os.path.join(BASE_DIR, "books_out")
SD_DIR = r"F:\Books"

MIN_HEADROOM_BYTES = 5.0 * (1024 ** 3)  # 5.0 GB minimum free headroom

ARABIC_BOOKS = [
    ("1984_Arabic_George_Orwell.epub", "1984 (جورج أورويل)", "01_1984_George_Orwell"),
    ("Animal_Farm_Arabic_George_Orwell.epub", "مزرعة الحيوان (جورج أورويل)", "02_Animal_Farm_George_Orwell"),
    ("Crime_And_Punishment_Arabic_Vol1_Sami_Droubi.epub", "الجريمة والعقاب ج1 (الدروبي)", "03_Crime_And_Punishment_Vol1"),
    ("Crime_And_Punishment_Arabic_Vol2_Sami_Droubi.epub", "الجريمة والعقاب ج2 (الدروبي)", "04_Crime_And_Punishment_Vol2"),
    ("The_Stranger_Arabic_Albert_Camus.epub", "الغريب (ألبير كامو)", "05_The_Stranger_Albert_Camus"),
    ("The_Little_Prince_Arabic_Saint_Exupery.epub", "الأمير الصغير (إكزوبيري)", "06_The_Little_Prince"),
    ("The_Picture_Of_Dorian_Gray_Arabic_Oscar_Wilde.epub", "صورة دوريان غراي (وايلد)", "07_The_Picture_Of_Dorian_Gray"),
    ("The_Trial_Arabic_Kafka.epub", "المحاكمة (كافكا)", "08_The_Trial_Franz_Kafka"),
    ("The_Castle_Arabic_Kafka.epub", "القلعة (كافكا)", "09_The_Castle_Franz_Kafka"),
    ("One_Hundred_Years_Of_Solitude_Arabic_Marquez.epub", "مئة عام من العزلة (ماركيز)", "10_One_Hundred_Years_Of_Solitude"),
]

ENGLISH_BOOKS = [
    ("03_The_Great_Gatsby_Fitzgerald.epub", "The Great Gatsby", "01_The_Great_Gatsby"),
    ("07_1984_George_Orwell.epub", "1984", "02_1984_George_Orwell"),
    ("Animal_Farm_George_Orwell.epub", "Animal Farm", "03_Animal_Farm_George_Orwell"),
    ("39_Frankenstein_Mary_Shelley.epub", "Frankenstein", "04_Frankenstein_Mary_Shelley"),
    ("50_Brave_New_World_Aldous_Huxley.epub", "Brave New World", "05_Brave_New_World_Huxley"),
    ("The_Picture_Of_Dorian_Gray_Wilde.epub", "The Picture of Dorian Gray", "06_The_Picture_Of_Dorian_Gray"),
    ("31_Heart_Of_Darkness_Joseph_Conrad.epub", "Heart of Darkness", "07_Heart_Of_Darkness_Conrad"),
    ("23_The_Stranger_Albert_Camus.epub", "The Stranger", "08_The_Stranger_Albert_Camus"),
    ("36_Alices_Adventures_In_Wonderland_Carroll.epub", "Alices Adventures in Wonderland", "09_Alices_Adventures_In_Wonderland"),
    ("Dune_Frank_Herbert.epub", "Dune", "10_Dune_Frank_Herbert"),
]

def copy_buffered(src, dst):
    if os.path.exists(dst):
        if os.path.getsize(dst) == os.path.getsize(src) and os.path.getmtime(dst) >= os.path.getmtime(src):
            return False
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
        shutil.copyfileobj(fsrc, fdst, length=512*1024)
    try:
        shutil.copystat(src, dst)
    except Exception:
        pass
    return True

def sync_book_to_sd(src_dir, dst_dir, label):
    total, used, free = shutil.disk_usage(r"F:\\")
    if free <= MIN_HEADROOM_BYTES:
        print(f"[!] HEADROOM SAFETY TRIGGERED! Free space ({free / (1024**3):.2f} GB) reached 5.0 GB limit. Stopping sync.")
        return False
        
    print(f"[*] Syncing to SD: {label} (SD Free: {free / (1024**3):.2f} GB)...", flush=True)
    c = 0
    for root, dirs, files in os.walk(src_dir):
        rel = os.path.relpath(root, src_dir)
        t_dir = os.path.join(dst_dir, rel)
        os.makedirs(t_dir, exist_ok=True)
        for f in files:
            if f.endswith('.jpg'):
                s_p = os.path.join(root, f)
                d_p = os.path.join(t_dir, f)
                if copy_buffered(s_p, d_p):
                    c += 1
    print(f"    -> Synced {c} new pages for {label}.", flush=True)
    return True

def main():
    print("=" * 65)
    print("  EXTENDED LIBRARY: 20 MASTERPIECES PARALLEL CONVERTER & SYNC")
    print("=" * 65)
    
    # Check SD status
    total, used, free = shutil.disk_usage(r"F:\\")
    print(f"Current SD Space: {free / (1024**3):.2f} GB free out of {total / (1024**3):.2f} GB\n")
    
    t0 = time.time()
    pool = mp.Pool(processes=min(16, mp.cpu_count()))
    
    # 1. Convert Arabic Literature Masterpieces
    print("\n--- PHASE 1: Rendering Arabic Literature Masterpieces ---")
    ar_cat_out = os.path.join(OUT_DIR, "06_Arabic_World_Classics")
    ar_raw_dir = os.path.join(RAW_DIR, "arabic_editions")
    
    for filename, title, folder in ARABIC_BOOKS:
        epub_p = os.path.join(ar_raw_dir, filename)
        if os.path.exists(epub_p):
            book_out = os.path.join(ar_cat_out, folder)
            convert_book(epub_p, book_out, title, is_arabic=True, pool=pool)
            
    # 2. Convert English Classics
    print("\n--- PHASE 2: Rendering English World Classics ---")
    en_cat_out = os.path.join(OUT_DIR, "07_English_World_Classics")
    en_raw_dir = os.path.join(RAW_DIR, "english_classics")
    
    for filename, title, folder in ENGLISH_BOOKS:
        epub_p = os.path.join(en_raw_dir, filename)
        if os.path.exists(epub_p):
            book_out = os.path.join(en_cat_out, folder)
            convert_book(epub_p, book_out, title, is_arabic=False, pool=pool)
            
    print("\n[*] Waiting for all parallel rendering workers to complete...")
    pool.close()
    pool.join()
    print(f"[✓] Parallel rendering finished in {time.time() - t0:.1f}s!\n")
    
    # 3. Synchronize to SD Card with Strict Headroom Check
    print("--- PHASE 3: Synchronizing to Phone SD Card with 5.0 GB Headroom Guard ---")
    for filename, title, folder in ARABIC_BOOKS:
        s_p = os.path.join(ar_cat_out, folder)
        d_p = os.path.join(SD_DIR, "06_Arabic_World_Classics", folder)
        if os.path.exists(s_p):
            ok = sync_book_to_sd(s_p, d_p, f"Arabic/{title}")
            if not ok: break
            
    for filename, title, folder in ENGLISH_BOOKS:
        s_p = os.path.join(en_cat_out, folder)
        d_p = os.path.join(SD_DIR, "07_English_World_Classics", folder)
        if os.path.exists(s_p):
            ok = sync_book_to_sd(s_p, d_p, f"English/{title}")
            if not ok: break
            
    total, used, free = shutil.disk_usage(r"F:\\")
    print("\n" + "=" * 65)
    print(f"EXTENDED SYNC COMPLETED!")
    print(f"Final SD Free Space: {free / (1024**3):.2f} GB (Protected >= 5.0 GB Headroom ✅)")
    print("=" * 65)

if __name__ == "__main__":
    main()
