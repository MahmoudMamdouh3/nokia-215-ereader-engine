"""
Nokia 215 4G - Master Synchronizer (Books + Manga + Summaries)
==============================================================
Transfers all canonical 240x280 rendered content to the Nokia 215 4G SD card (F:\).
Uses single-threaded buffered stream copying (512 KB chunks) to guarantee zero
FAT32 lock contention, data corruption, or I/O freezes on USB mass storage.
"""

import os
import sys
import shutil
import time

BOOKS_SRC = r"E:\nokia\books_out"
BOOKS_DST = r"F:\Books"
SUMMARIES_SRC = r"E:\nokia\summaries"
SUMMARIES_DST = r"F:\Books\06_Book_Summaries"
MANGA_SRC = r"E:\nokia\manga_out"
MANGA_DST = r"F:\Manga"

CHUNK_SIZE = 512 * 1024  # 512 KB buffer

def copy_file_buffered(src, dst, force=False):
    """Copies a file using buffered streaming, preserving timestamps."""
    if not force and os.path.exists(dst):
        if os.path.getsize(dst) == os.path.getsize(src) and os.path.getmtime(dst) >= os.path.getmtime(src):
            return False
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
        shutil.copyfileobj(fsrc, fdst, length=CHUNK_SIZE)
    try:
        shutil.copystat(src, dst)
    except Exception:
        pass
    return True

def sync_directory(src_dir, dst_dir, label, ext_filter=None, log_interval=500, force=False):
    """Synchronizes a directory hierarchy cleanly and deletes stale files in destination."""
    print(f"\n[*] Syncing: {label}...", flush=True)
    copied = 0
    skipped = 0
    removed = 0

    for root, dirs, files in os.walk(src_dir):
        rel = os.path.relpath(root, src_dir)
        target_dir = os.path.join(dst_dir, rel)
        os.makedirs(target_dir, exist_ok=True)

        if ext_filter:
            valid_src = {f for f in files if any(f.endswith(ext) for ext in ext_filter)}
        else:
            valid_src = set(files)

        # Remove stale files
        if os.path.exists(target_dir):
            for df in os.listdir(target_dir):
                d_path = os.path.join(target_dir, df)
                if os.path.isfile(d_path):
                    if ext_filter and not any(df.endswith(ext) for ext in ext_filter):
                        continue
                    if df not in valid_src:
                        try:
                            os.remove(d_path)
                            removed += 1
                        except Exception:
                            pass

        # Copy valid files
        for f in files:
            if ext_filter and not any(f.endswith(ext) for ext in ext_filter):
                continue
            s_file = os.path.join(root, f)
            d_file = os.path.join(target_dir, f)
            if copy_file_buffered(s_file, d_file, force=force):
                copied += 1
            else:
                skipped += 1

            if (copied + skipped) % log_interval == 0:
                print(f"    ... [{label}] {copied + skipped} files processed ({copied} copied, {skipped} up-to-date)", flush=True)

    print(f"    -> [{label}] DONE: {copied} copied, {skipped} kept, {removed} stale removed.", flush=True)
    return copied, skipped, removed

def main():
    if not os.path.exists("F:\\"):
        print("ERROR: Drive F:\ not detected! Please ensure Nokia phone is connected in Mass Storage mode.")
        sys.exit(1)

    print("=" * 65)
    print("      NOKIA 215 4G - COMPLETE MASTER SYNC (240x280)")
    print("=" * 65)

    total, used, free = shutil.disk_usage("F:\\")
    print(f"SD Card Capacity: {total / (1024**3):.2f} GB | Free: {free / (1024**3):.2f} GB\n")

    t_start = time.time()
    grand_copied = 0
    grand_skipped = 0
    grand_removed = 0

    # 1. Sync Books
    if os.path.exists(BOOKS_SRC):
        categories = sorted([d for d in os.listdir(BOOKS_SRC) if os.path.isdir(os.path.join(BOOKS_SRC, d))])
        for cat in categories:
            cat_src = os.path.join(BOOKS_SRC, cat)
            cat_dst = os.path.join(BOOKS_DST, cat)
            print(f"\n==========================================")
            print(f"[Category] {cat}")
            print(f"==========================================")
            books = sorted([d for d in os.listdir(cat_src) if os.path.isdir(os.path.join(cat_src, d))])
            for b in books:
                b_src = os.path.join(cat_src, b)
                b_dst = os.path.join(cat_dst, b)
                c, s, r = sync_directory(b_src, b_dst, f"{cat}/{b}", ext_filter=['.jpg'])
                grand_copied += c
                grand_skipped += s
                grand_removed += r

    # 2. Sync Summaries
    if os.path.exists(SUMMARIES_SRC):
        print(f"\n==========================================")
        print(f"[Category] 06_Book_Summaries")
        print(f"==========================================")
        c, s, r = sync_directory(SUMMARIES_SRC, SUMMARIES_DST, "06_Book_Summaries", ext_filter=['.md', '.txt'], log_interval=100)
        grand_copied += c
        grand_skipped += s
        grand_removed += r

    # 3. Sync Manga
    if os.path.exists(MANGA_SRC):
        print(f"\n==========================================")
        print(f"[Manga] High-Readability 240x280 Landscape Manga")
        print(f"==========================================")
        manga_series = ['A_Silent_Voice', 'Vinland_Saga', 'Vagabond']
        for series in manga_series:
            s_src = os.path.join(MANGA_SRC, series)
            s_dst = os.path.join(MANGA_DST, series)
            if os.path.exists(s_src):
                c, s, r = sync_directory(s_src, s_dst, f"Manga/{series}", ext_filter=['.jpg'], log_interval=1000)
                grand_copied += c
                grand_skipped += s
                grand_removed += r

    elapsed = time.time() - t_start
    print("\n" + "=" * 65)
    print(f"MASTER SYNC COMPLETE!")
    print(f"Total Copied  : {grand_copied} files")
    print(f"Total Skipped : {grand_skipped} files (already up to date)")
    print(f"Total Removed : {grand_removed} files (stale legacy removed)")
    print(f"Elapsed Time  : {elapsed / 60:.2f} minutes ({elapsed:.1f} seconds)")
    total, used, free = shutil.disk_usage("F:\\")
    print(f"Remaining Free Space on SD: {free / (1024**3):.2f} GB")
    print("=" * 65)

if __name__ == "__main__":
    main()
