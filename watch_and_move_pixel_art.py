import os
import time
import shutil
import glob
import subprocess

DOWNLOADS_DIR = os.path.expanduser(r"~\Downloads")
TARGET_DIR = os.path.join(DOWNLOADS_DIR, "pixel art thing")
os.makedirs(TARGET_DIR, exist_ok=True)

PART_LINKS = {
    "P1": "https://send.now/i2gduql8qxbw",
    "P2": "https://send.now/pk21c4z3x4dg",
    "P3": "https://send.now/msgdb89lb3bc"
}

print(f"[Watcher Started] Fully Automated Course Downloader & Mover Active", flush=True)
print(f"Monitoring: {DOWNLOADS_DIR}", flush=True)
print(f"Destination: {TARGET_DIR}", flush=True)

moved_parts = set()
p1_triggered = False

while True:
    try:
        # Check files already in TARGET_DIR
        for fname in os.listdir(TARGET_DIR):
            if fname.endswith(".zip"):
                lower = fname.lower()
                if "p3" in lower:
                    moved_parts.add("P3")
                if "p2" in lower:
                    moved_parts.add("P2")
                if "p1" in lower:
                    moved_parts.add("P1")

        # Check for completed files in Downloads to move into TARGET_DIR
        for fname in os.listdir(DOWNLOADS_DIR):
            full_path = os.path.join(DOWNLOADS_DIR, fname)
            if not os.path.isfile(full_path):
                continue
            
            # Skip in-progress downloads
            if fname.endswith(".crdownload") or fname.endswith(".tmp") or fname.endswith(".part"):
                continue

            lower = fname.lower()
            if "pixel art" in lower or ("vfxmed" in lower and any(p in lower for p in ["p1", "p2", "p3"])):
                dest_path = os.path.join(TARGET_DIR, fname)
                print(f"[Automated Move] Completed file detected: {fname} -> {dest_path}", flush=True)
                time.sleep(2)
                try:
                    shutil.move(full_path, dest_path)
                    print(f"[Success] Moved {fname} to {TARGET_DIR}!", flush=True)

                    if "p3" in lower:
                        moved_parts.add("P3")
                    elif "p2" in lower:
                        moved_parts.add("P2")
                    elif "p1" in lower:
                        moved_parts.add("P1")

                except Exception as err:
                    print(f"[Error moving {fname}]: {err}", flush=True)

        # As requested by user: trigger Part 1 the moment Part 3 finishes!
        if ("P3" in moved_parts) and not p1_triggered:
            p1_triggered = True
            print(f"[Auto-Chain] Part 3 finished! Triggering Part 1 download now: {PART_LINKS['P1']}", flush=True)
            subprocess.Popen(["cmd.exe", "/c", "start", PART_LINKS["P1"]])

        if len(moved_parts) == 3 or ({"P1", "P2", "P3"}.issubset(moved_parts)):
            print("[Auto-Chain] ALL 3 PARTS OF PIXEL ART MASTER COURSE COMPLETED & READY IN pixel art thing!", flush=True)

        # Log active download progress
        cr_downloads = glob.glob(os.path.join(DOWNLOADS_DIR, "*Pixel Art*.crdownload"))
        for cr in cr_downloads:
            sz_mb = os.path.getsize(cr) / (1024 * 1024)
            bname = os.path.basename(cr)
            print(f"[Edge Active Download] {bname}: {sz_mb:.1f} MB / ~2800 MB ({sz_mb/2800*100:.1f}%)", flush=True)

        cr_target = glob.glob(os.path.join(TARGET_DIR, "*.crdownload"))
        for cr in cr_target:
            sz_mb = os.path.getsize(cr) / (1024 * 1024)
            bname = os.path.basename(cr)
            print(f"[Brave Active Download in Target] {bname}: {sz_mb:.1f} MB", flush=True)

    except Exception as e:
        print(f"[Watcher Exception]: {e}", flush=True)

    time.sleep(4)
