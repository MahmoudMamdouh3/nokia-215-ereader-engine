"""
Nokia 215 4G - Clean Single-Threaded Books Synchronizer
Safely copies rendered book images to SD card (F:\\Books) without FAT32 lock contention.
Deletes stale pages and synchronizes all books cleanly.
"""

import os
import sys
import shutil
import time

SRC_BASE = r"E:\nokia\books_out"
DST_BASE = r"F:\Books"

def copy_file_buffered(src, dst, force=False):
    if not force and os.path.exists(dst):
        # Skip only if exact same size and destination is not older than source
        if os.path.getsize(dst) == os.path.getsize(src) and os.path.getmtime(dst) >= os.path.getmtime(src):
            return False
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
        shutil.copyfileobj(fsrc, fdst, length=512*1024)
    # preserve timestamp
    try:
        shutil.copystat(src, dst)
    except Exception:
        pass
    return True

def sync_book_dir(src_dir, dst_dir, book_name, force=False):
    print(f"[*] Syncing: {book_name}...", flush=True)
    b_copied = 0
    b_skipped = 0
    b_removed = 0

    for root, dirs, files in os.walk(src_dir):
        rel = os.path.relpath(root, src_dir)
        dest_dir = os.path.join(dst_dir, rel)
        os.makedirs(dest_dir, exist_ok=True)

        # Remove stale files in destination that do not exist in source
        src_files_set = set(files)
        if os.path.exists(dest_dir):
            for df in os.listdir(dest_dir):
                if df.endswith('.jpg') and df not in src_files_set:
                    try:
                        os.remove(os.path.join(dest_dir, df))
                        b_removed += 1
                    except Exception:
                        pass

        for f in files:
            if f.endswith('.jpg'):
                s_file = os.path.join(root, f)
                d_file = os.path.join(dest_dir, f)
                if copy_file_buffered(s_file, d_file, force=force):
                    b_copied += 1
                else:
                    b_skipped += 1
                if (b_copied + b_skipped) % 500 == 0:
                    print(f"    ... {book_name}: {b_copied + b_skipped} pages processed", flush=True)

    print(f"    -> {book_name}: {b_copied} copied, {b_skipped} kept, {b_removed} stale removed.", flush=True)
    return b_copied, b_skipped, b_removed

def sync_all(force=False):
    if not os.path.exists(r"F:\Books") and not os.path.exists(r"F:\\"):
        print("ERROR: Drive F:\\ not detected.")
        print("Please connect your Nokia phone via USB cable and select 'Mass Storage' or 'Memory Card' mode.")
        return False

    print("==================================================")
    print("      SYNCING ALL BOOKS TO NOKIA 215 4G SD CARD   ")
    print("==================================================")

    total, used, free = shutil.disk_usage(r"F:\\")
    print(f"SD Card Free Space: {free / (1024**3):.2f} GB / {total / (1024**3):.2f} GB\n")

    categories = sorted([d for d in os.listdir(SRC_BASE) if os.path.isdir(os.path.join(SRC_BASE, d))])
    
    total_copied = 0
    total_skipped = 0
    total_removed = 0
    start_time = time.time()

    for cat in categories:
        cat_src = os.path.join(SRC_BASE, cat)
        cat_dst = os.path.join(DST_BASE, cat)
        print(f"\n[Category] {cat}")
        
        books = sorted([d for d in os.listdir(cat_src) if os.path.isdir(os.path.join(cat_src, d))])
        for b in books:
            b_src = os.path.join(cat_src, b)
            b_dst = os.path.join(cat_dst, b)
            c, s, r = sync_book_dir(b_src, b_dst, f"{cat}/{b}", force=force)
            total_copied += c
            total_skipped += s
            total_removed += r

    # Sync Summaries as well if F:\Books\06_Book_Summaries can be placed
    sum_src = r"E:\nokia\summaries"
    if os.path.exists(sum_src):
        sum_dst = os.path.join(DST_BASE, "06_Book_Summaries")
        print("\n[Category] 06_Book_Summaries")
        for sub in ["english", "arabic"]:
            sub_src = os.path.join(sum_src, sub)
            sub_dst = os.path.join(sum_dst, sub)
            if os.path.exists(sub_src):
                os.makedirs(sub_dst, exist_ok=True)
                for sf in os.listdir(sub_src):
                    if sf.endswith('.md') or sf.endswith('.txt'):
                        copy_file_buffered(os.path.join(sub_src, sf), os.path.join(sub_dst, sf), force=force)
                        total_copied += 1

    elapsed = time.time() - start_time
    print("\n==================================================")
    print(f" SYNC COMPLETE: {total_copied} copied, {total_skipped} unchanged, {total_removed} cleaned up in {elapsed:.1f}s")
    print("==================================================")
    return True

if __name__ == "__main__":
    force_sync = "--force" in sys.argv
    sync_all(force=force_sync)
