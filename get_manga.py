import os
import re
import subprocess
import requests

SERIES_NAME = "A_Silent_Voice"
SERIES_URL = "https://chapmanganato.to/manga-oa952283"
DEST_ROOT = f"/f/Manga/{SERIES_NAME}"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://chapmanganato.to/"
}

os.makedirs(DEST_ROOT, exist_ok=True)

print(f"[*] Fetching {SERIES_NAME}...")
res = requests.get(SERIES_URL, headers=HEADERS)

if res.status_code != 200:
    print(f"[!] HTTP error {res.status_code}")
    exit(1)

# Grab all chapter URLs regardless of HTML attribute order
raw_links = re.findall(r'href="([^"]+/chapter-[^"]+)"', res.text)
chapters = list(dict.fromkeys(raw_links))
chapters.reverse()

print(f"[+] Found {len(chapters)} chapters.")

for ch_idx, ch_url in enumerate(chapters, start=1):
    ch_folder = os.path.join(DEST_ROOT, f"Ch_{ch_idx:02d}")
    os.makedirs(ch_folder, exist_ok=True)

    if len(os.listdir(ch_folder)) > 10:
        print(f"[-] Skipping Chapter {ch_idx} (already done)")
        continue

    print(f"[*] Downloading Chapter {ch_idx}...")
    ch_res = requests.get(ch_url, headers=HEADERS)
    
    # Capture both src and lazy-loaded data-src images
    img_urls = re.findall(r'(?:src|data-src)="([^"]+\.(?:jpg|png|webp|jpeg)[^"]*)"', ch_res.text)
    img_urls = list(dict.fromkeys([u for u in img_urls if "chapter" in u or "manga" in u or "image" in u]))

    for p_idx, img_url in enumerate(img_urls, start=1):
        raw_tmp = f"temp_{ch_idx}_{p_idx}.jpg"
        out_top = os.path.join(ch_folder, f"p{p_idx:02d}_1.jpg")
        out_bot = os.path.join(ch_folder, f"p{p_idx:02d}_2.jpg")

        if os.path.exists(out_top) and os.path.exists(out_bot):
            continue

        try:
            img_data = requests.get(img_url, headers=HEADERS, timeout=15).content
            with open(raw_tmp, "wb") as f:
                f.write(img_data)

            # Top half -> Scale to 320x240 -> Rotate 90° clockwise
            subprocess.run([
                "ffmpeg", "-y", "-loglevel", "error", "-i", raw_tmp,
                "-vf", "crop=iw:ih/2:0:0,scale=320:240:force_original_aspect_ratio=decrease,pad=320:240:(ow-iw)/2:(oh-ih)/2:color=black,transpose=1",
                "-q:v", "4", out_top
            ], check=True)

            # Bottom half -> Scale to 320x240 -> Rotate 90° clockwise
            subprocess.run([
                "ffmpeg", "-y", "-loglevel", "error", "-i", raw_tmp,
                "-vf", "crop=iw:ih/2:0:ih/2,scale=320:240:force_original_aspect_ratio=decrease,pad=320:240:(ow-iw)/2:(oh-ih)/2:color=black,transpose=1",
                "-q:v", "4", out_bot
            ], check=True)

            os.remove(raw_tmp)
        except Exception as e:
            if os.path.exists(raw_tmp):
                os.remove(raw_tmp)

print("[✓] Finished converting all chapters to SD card.")
