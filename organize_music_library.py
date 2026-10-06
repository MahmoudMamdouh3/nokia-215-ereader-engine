"""
Music Library Organizer for Nokia 215 4G
Organizes large flat playlists into A-Z letter buckets and artist subfolders.
Enables fast T9 keypad navigation on S30+ feature phone file manager.
"""

import os
import sys
import re
import json
import shutil
from collections import defaultdict

PLAYLIST_DIR = r"F:\Music\My Playlist #38 - Mahmoud Mamdouh"
MAP_FILE = os.path.join(PLAYLIST_DIR, "playlist_organization_map.json")
LOCAL_MAP = r"E:\nokia\playlist_organization_map.json"

def clean_name(s):
    # Remove filesystem illegal characters
    s = re.sub(r'[<>:"/\\|?*]', '', s)
    return s.strip()

def extract_primary_artist(filename):
    name = filename[:-4]
    if " - " in name:
        artist_part = name.split(" - ")[-1].strip()
        # strip [spotify_id]
        if "[" in artist_part and artist_part.endswith("]"):
            artist_part = artist_part[:artist_part.rfind("[")].strip()
        # primary artist before comma or feat / ft.
        primary = re.split(r",|\bft\.|\bfeat\.", artist_part, flags=re.IGNORECASE)[0].strip()
        primary = clean_name(primary)
        if primary:
            return primary
    return "Unknown Artist"

def get_bucket(artist):
    if not artist:
        return "#_Symbols"
    if re.search(r'[\u0600-\u06FF]', artist):
        return "عربي_Arabic"
    first = artist[0].upper()
    if 'A' <= first <= 'W':
        return first
    if first in ['X', 'Y', 'Z']:
        return "XYZ"
    if '0' <= first <= '9':
        return "#_Numbers"
    return "#_Symbols"

def organize_playlist(dry_run=False):
    if not os.path.exists(PLAYLIST_DIR):
        print(f"Error: {PLAYLIST_DIR} not found!")
        return

    files = [f for f in os.listdir(PLAYLIST_DIR) if f.endswith(".mp3") and os.path.isfile(os.path.join(PLAYLIST_DIR, f))]
    print(f"Found {len(files)} MP3 files in '{PLAYLIST_DIR}'")

    plan = []
    for f in files:
        artist = extract_primary_artist(f)
        bucket = get_bucket(artist)
        target_dir = os.path.join(PLAYLIST_DIR, bucket, artist)
        src_path = os.path.join(PLAYLIST_DIR, f)
        dst_path = os.path.join(target_dir, f)
        plan.append({
            "filename": f,
            "artist": artist,
            "bucket": bucket,
            "src": src_path,
            "dst": dst_path,
            "rel_dst": os.path.join(bucket, artist, f)
        })

    print(f"Total files to organize: {len(plan)}")

    if dry_run:
        print("DRY RUN completed. No files were moved.")
        return

    # Execute move
    mapping = {}
    moved_count = 0
    error_count = 0

    for item in plan:
        target_dir = os.path.dirname(item["dst"])
        os.makedirs(target_dir, exist_ok=True)
        try:
            shutil.move(item["src"], item["dst"])
            mapping[item["filename"]] = item["rel_dst"]
            moved_count += 1
        except Exception as e:
            print(f"Error moving {item['filename']}: {e}")
            error_count += 1

    # Save mapping
    with open(MAP_FILE, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
    with open(LOCAL_MAP, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)

    print(f"\n==========================================")
    print(f"ORGANIZATION COMPLETE!")
    print(f"Successfully moved: {moved_count} songs")
    print(f"Errors: {error_count}")
    print(f"Mapping saved to: {MAP_FILE}")
    print(f"==========================================")

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    dry = "--dry-run" in sys.argv
    organize_playlist(dry_run=dry)
