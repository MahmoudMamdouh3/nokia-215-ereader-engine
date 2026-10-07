#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
manga_pipeline.py — Nokia 215 4G High-Readability Landscape Manga Pipeline (v3.0)
==================================================================================
Optimized specifically for landscape reading on the Nokia 215 4G:
1. Auto-crops empty white borders and margins (gains 15-25% more active content).
2. Splits each page into 2 halves (top half / bottom half).
   - A manga half-page has an aspect ratio of ~4:3, which perfectly matches
     the 320x240 landscape screen of the Nokia 215 4G!
   - Fills ~302-320px wide by 240px tall (nearly 100% of the display).
3. Applies UnsharpMask (radius 1.2, percent 140%) and Contrast enhancement (1.20x)
   to ensure dialogue text and speech bubbles are razor-sharp.
4. Centers on a clean, pure WHITE 320x240 canvas.
5. Rotates 90° CW to save as 240x320, so when the phone is held horizontally
   (with keypad in right hand), the manga fills the screen in glorious landscape.
6. Handles double-page spreads by splitting right/left first (manga reading order).
7. High-quality JPEG output (quality=92).

Series supported:
  - A Silent Voice (62 ch)
  - Vinland Saga (223 ch)
  - Vagabond (327 ch)
  - Berserk (403 ch)

Usage:
  python manga_pipeline.py --series A_Silent_Voice
  python manga_pipeline.py --series Vinland_Saga
  python manga_pipeline.py --series Vagabond
  python manga_pipeline.py --series Berserk
  python manga_pipeline.py --series all
  python manga_pipeline.py --copy-sd
  python manga_pipeline.py --verify
"""
import os
import re
import sys
import io
import time
import shutil
import logging
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

import requests
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

STAGING_ROOT = Path(r"E:\nokia\manga_out")
SD_ROOT      = Path(r"F:\Manga")

SERIES_CONFIG = {
    "A_Silent_Voice": {
        "display":        "A Silent Voice (Koe no Katachi)",
        "weebcentral_id": "01J76XY9BSRSBCTQ5XP68H64BJ",
        "expected_ch":    62,
    },
    "Vinland_Saga": {
        "display":        "Vinland Saga",
        "weebcentral_id": "01J76XY7FQY59WRK2YWX5T4E5N",
        "expected_ch":    223,
    },
    "Vagabond": {
        "display":        "Vagabond",
        "weebcentral_id": "01J76XY7J8BMXD4D0FM50MJHQG",
        "expected_ch":    327,
    },
    "Berserk": {
        "display":        "Berserk",
        "weebcentral_id": "01J76XY7EF75DJNQCV04HTPDZK",
        "expected_ch":    403,
    },
}

PAGE_WORKERS           = 4
DELAY_BETWEEN_CHAPTERS = 0.4   # seconds
RETRY_COUNT            = 12
RETRY_BACKOFF          = 2     # seconds

# Screen dimensions in landscape orientation (Calibrated 280x240 for 240x280 active viewer)
LANDSCAPE_W = 280
LANDSCAPE_H = 240

STAGING_ROOT.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(
            str(STAGING_ROOT / "pipeline_landscape.log"),
            encoding="utf-8",
            mode="a",
        ),
    ],
)
log = logging.getLogger("manga_landscape")

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
})


def http_get(url, stream=False, extra_headers=None, timeout=30):
    headers = extra_headers or {}
    for attempt in range(RETRY_COUNT):
        try:
            r = SESSION.get(url, headers=headers, timeout=timeout, stream=stream)
            if r.status_code == 429:
                wait = int(r.headers.get("Retry-After", RETRY_BACKOFF * (attempt + 1)))
                log.warning("Rate-limited -> waiting %ds ...", wait)
                time.sleep(wait)
                continue
            r.raise_for_status()
            return r
        except requests.exceptions.RequestException as exc:
            if attempt == RETRY_COUNT - 1:
                raise
            sleep_s = min(30, RETRY_BACKOFF * (attempt + 1))
            log.warning("Request failed (%s). Retry %d/%d in %ds ...",
                        exc, attempt + 1, RETRY_COUNT, sleep_s)
            time.sleep(sleep_s)


def get_chapter_list(series_key):
    cfg = SERIES_CONFIG[series_key]
    wc_id = cfg["weebcentral_id"]
    url = f"https://weebcentral.com/series/{wc_id}/full-chapter-list"
    log.info("[%s] Fetching chapter list from WeebCentral...", series_key)

    r = http_get(url)
    items = re.findall(
        r'href="(/chapters/([A-Z0-9]+))"[\s\S]*?<span class="">([^<]+)</span>',
        r.text
    )
    items.reverse()  # oldest chapter first

    entries = []
    seen_ids = set()
    for href, cid, label_raw in items:
        if cid in seen_ids:
            continue
        seen_ids.add(cid)
        label = label_raw.strip()

        # Prologue handling (Berserk)
        m_pro = re.match(r"^Prologue\s*(\d+(?:\.\d+)?)$", label, re.I)
        if m_pro:
            p_num = float(m_pro.group(1))
            if p_num == int(p_num):
                dir_name = f"Ch_00_Prologue_{int(p_num):02d}"
            else:
                dir_name = f"Ch_00_Prologue_{p_num:.1f}".replace(".", "_")
            entries.append({
                "num": p_num * 0.001,
                "sort_key": p_num * 0.001,
                "dir_name": dir_name,
                "wc_id": cid,
                "label": label,
            })
            continue

        # Chapter or # handling
        m_ch = re.search(r"(?:Chapter|#)\s*(\d+(?:\.\d+)?)", label, re.I)
        if m_ch:
            ch_num = float(m_ch.group(1))
            if ch_num == int(ch_num):
                if int(ch_num) < 100:
                    dir_name = f"Ch_{int(ch_num):02d}"
                else:
                    dir_name = f"Ch_{int(ch_num)}"
            else:
                dir_name = f"Ch_{ch_num:.1f}".replace(".", "_")
            entries.append({
                "num": ch_num,
                "sort_key": ch_num,
                "dir_name": dir_name,
                "wc_id": cid,
                "label": label,
            })
            continue

        # Fallback
        safe_label = re.sub(r"[^a-zA-Z0-9_.-]", "_", label)
        entries.append({
            "num": 0.0,
            "sort_key": 0.0,
            "dir_name": f"Ch_{safe_label}",
            "wc_id": cid,
            "label": label,
        })

    log.info("[%s] Found %d chapters total.", series_key, len(entries))
    return entries


def get_chapter_images(wc_id):
    url = f"https://weebcentral.com/chapters/{wc_id}/images?is_prev=False&current_page=1&reading_style=long_strip"
    for attempt in range(RETRY_COUNT):
        try:
            r = http_get(url)
            imgs = re.findall(r'<img[^>]+src="([^"]+)"', r.text)
            valid = [
                im for im in imgs
                if im.startswith("http") and not any(k in im.lower() for k in ["brand", "404", "logo", "icon"])
            ]
            if valid:
                return valid
            log.warning("No valid images found for chapter %s (attempt %d)", wc_id, attempt + 1)
        except Exception as exc:
            log.warning("Error fetching images for %s: %s", wc_id, exc)
        time.sleep(min(30, 2.0 * (attempt + 1)))
    return []


def auto_crop(im, threshold=242, margin=2):
    """Detect bounding box of actual ink to strip empty scanner margins."""
    try:
        gray = im.convert("L")
        arr = np.array(gray)
        non_white = arr < threshold
        rows = np.any(non_white, axis=1)
        cols = np.any(non_white, axis=0)
        if not rows.any() or not cols.any():
            return im
        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]
        h, w = arr.shape
        if (rmax - rmin) < h * 0.3 or (cmax - cmin) < w * 0.3:
            return im  # avoid over-cropping nearly blank splash pages
        rmin = max(0, rmin - margin)
        rmax = min(h - 1, rmax + margin)
        cmin = max(0, cmin - margin)
        cmax = min(w - 1, cmax + margin)
        return im.crop((cmin, rmin, cmax + 1, rmax + 1))
    except Exception:
        return im


def process_half_landscape(strip_im, target_w=LANDSCAPE_W, target_h=LANDSCAPE_H):
    """
    Scale strip to fill 320x240 landscape (width or height constrained),
    apply unsharp mask and contrast boost, paste on white canvas,
    and rotate 90° CW so it displays in full landscape on Nokia 215 4G.
    """
    w, h = strip_im.size
    scale = min(target_w / w, target_h / h)
    new_w = int(w * scale)
    new_h = int(h * scale)

    # Downscale with high quality Lanczos filter
    resized = strip_im.resize((new_w, new_h), Image.LANCZOS)

    # Crisp text enhancement
    sharpened = resized.filter(ImageFilter.UnsharpMask(radius=1.2, percent=140, threshold=2))
    enhanced = ImageEnhance.Contrast(sharpened).enhance(1.20)

    # Pure white background canvas (matches phone display)
    canvas = Image.new("RGB", (target_w, target_h), (255, 255, 255))
    x_offset = (target_w - new_w) // 2
    y_offset = (target_h - new_h) // 2
    canvas.paste(enhanced, (x_offset, y_offset))

    # Rotate 90° CW (ROTATE_270 in PIL) -> saved as 240x320 portrait file.
    # When user holds phone horizontally (landscape), image fills full 320x240 screen!
    final = canvas.transpose(Image.ROTATE_270)
    return final


def slice_and_save_page(raw_im, chapter_dir, page_num):
    """
    Handles a single manga page in landscape mode:
    - Double spreads: splits right/left first, then 2 halves each.
    - Regular pages: auto-crops borders, splits into 2 halves (top, bottom).
    """
    cw_raw, ch_raw = raw_im.size

    # Check for double-page spread (landscape)
    if cw_raw > ch_raw * 1.15:
        # Manga is right-to-left: right page first, left page second
        half_w = cw_raw // 2
        pages = [
            raw_im.crop((half_w, 0, cw_raw, ch_raw)),  # Right half
            raw_im.crop((0, 0, half_w, ch_raw)),       # Left half
        ]
        sub_indices = [(1, 2), (3, 4)]
    else:
        pages = [raw_im]
        sub_indices = [(1, 2)]

    saved_files = []
    for p_idx, p_img in enumerate(pages):
        cropped = auto_crop(p_img)
        cw, ch = cropped.size
        half_h = ch // 2
        idxs = sub_indices[p_idx]

        # Top half
        top = cropped.crop((0, 0, cw, half_h))
        top_img = process_half_landscape(top)
        out_top = chapter_dir / f"p{page_num:03d}_{idxs[0]}.jpg"
        top_img.save(out_top, format="JPEG", quality=92, optimize=True)
        saved_files.append(out_top)

        # Bottom half
        bot = cropped.crop((0, half_h, cw, ch))
        bot_img = process_half_landscape(bot)
        out_bot = chapter_dir / f"p{page_num:03d}_{idxs[1]}.jpg"
        bot_img.save(out_bot, format="JPEG", quality=92, optimize=True)
        saved_files.append(out_bot)

    return len(saved_files) > 0


def process_page(img_url, chapter_dir, page_num):
    """Download image into memory and slice into 2 landscape halves."""
    p2 = chapter_dir / f"p{page_num:03d}_2.jpg"
    if p2.exists() and p2.stat().st_size > 500:
        return True

    for attempt in range(RETRY_COUNT):
        try:
            r = http_get(img_url, extra_headers={
                "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
                "Referer": "https://weebcentral.com/",
            })
            if len(r.content) < 1024:
                log.warning("  p%03d: tiny response (%d bytes) - retry", page_num, len(r.content))
                time.sleep(1)
                continue

            with Image.open(io.BytesIO(r.content)) as raw_im:
                raw_rgb = raw_im.convert("RGB")
                ok = slice_and_save_page(raw_rgb, chapter_dir, page_num)
                return ok
        except Exception as exc:
            if attempt == RETRY_COUNT - 1:
                log.error("  p%03d: download failed from %s: %s", page_num, img_url, exc)
                return False
            time.sleep(min(30, 2.0 * (attempt + 1)))
    return False


def download_chapter(series_key, ch_entry, chapter_dir):
    label = ch_entry["label"]
    chapter_dir.mkdir(parents=True, exist_ok=True)
    marker = chapter_dir / ".landscape_v3"

    if marker.exists():
        existing = list(chapter_dir.glob("p*_2.jpg"))
        if len(existing) > 5:
            return True

    img_urls = get_chapter_images(ch_entry["wc_id"])
    if not img_urls:
        log.warning("  %s: 0 image URLs found!", label)
        return False

    total_pages = len(img_urls)

    # Clean up any old portrait or v2 format files
    if not marker.exists():
        for old_f in chapter_dir.glob("*.jpg"):
            old_f.unlink(missing_ok=True)
        for old_marker in chapter_dir.glob(".*"):
            old_marker.unlink(missing_ok=True)

    missing = []
    for page_num in range(1, total_pages + 1):
        p2 = chapter_dir / f"p{page_num:03d}_2.jpg"
        if not (p2.exists() and p2.stat().st_size > 500):
            missing.append(page_num)

    if not missing:
        marker.touch()
        return True

    log.info("  %s (%s): processing %d/%d pages in crisp landscape...", label, ch_entry["dir_name"], len(missing), total_pages)

    results = []
    with ThreadPoolExecutor(max_workers=PAGE_WORKERS) as pool:
        futures = [
            pool.submit(process_page, img_urls[p - 1], chapter_dir, p)
            for p in missing
        ]
        for fut in futures:
            results.append(fut.result())

    success_count = (total_pages - len(missing)) + sum(1 for r in results if r)
    ok = success_count >= max(1, int(total_pages * 0.90))
    if ok:
        marker.touch()
    log.info("  %s: %d/%d pages OK (status: %s)", label, success_count, total_pages, "OK" if ok else "FAILED")
    return ok


def sync_chapter_to_sd(series_key, ch_dir_name, src_dir):
    """Immediately copy completed chapter to SD card so it is readable on phone right away."""
    sd_drive = SD_ROOT.drive + "\\"
    if not Path(sd_drive).exists():
        return
    try:
        sd_ch_dir = SD_ROOT / series_key / ch_dir_name
        sd_ch_dir.mkdir(parents=True, exist_ok=True)
        src_files = {f.name for f in src_dir.glob("*.jpg")}
        for old_dst in sd_ch_dir.glob("*.jpg"):
            if old_dst.name not in src_files:
                old_dst.unlink(missing_ok=True)
        for img in src_dir.glob("*.jpg"):
            d = sd_ch_dir / img.name
            if not d.exists() or d.stat().st_size != img.stat().st_size:
                shutil.copy2(img, d)
    except Exception as exc:
        log.warning("Could not sync %s/%s to SD: %s", series_key, ch_dir_name, exc)


def run_series(series_key, chapter_range=None):
    cfg = SERIES_CONFIG[series_key]
    series_dir = STAGING_ROOT / series_key
    series_dir.mkdir(parents=True, exist_ok=True)

    log.info("")
    log.info("=" * 70)
    log.info("SERIES: %s [LANDSCAPE MODE]", cfg["display"])
    log.info("Staging: %s", series_dir)
    log.info("=" * 70)

    chapters = get_chapter_list(series_key)
    if not chapters:
        log.error("No chapters found for %s!", series_key)
        return []

    if chapter_range:
        lo, hi = chapter_range
        chapters = [c for c in chapters if lo <= c["sort_key"] <= hi]
        log.info("Chapter range filter %.1f-%.1f -> %d chapters.", lo, hi, len(chapters))

    failed = []
    for idx, ch in enumerate(chapters, 1):
        chapter_dir = series_dir / ch["dir_name"]
        log.info("[%d/%d] %s -> %s", idx, len(chapters), series_key, ch["dir_name"])

        ok = download_chapter(series_key, ch, chapter_dir)
        if not ok:
            failed.append(ch["dir_name"])
        else:
            sync_chapter_to_sd(series_key, ch["dir_name"], chapter_dir)

        time.sleep(DELAY_BETWEEN_CHAPTERS)

    if failed:
        log.warning("[%s] Failed chapters: %s", series_key, failed)
    else:
        log.info("[%s] All chapters complete!", series_key)
    return failed


def copy_to_sd(target_keys=None):
    sd_drive = SD_ROOT.drive + "\\"
    if not Path(sd_drive).exists():
        log.error("SD card not found at %s - aborting copy.", sd_drive)
        return False

    SD_ROOT.mkdir(parents=True, exist_ok=True)
    keys = target_keys or list(SERIES_CONFIG)
    total = 0

    for key in keys:
        src = STAGING_ROOT / key
        dst = SD_ROOT / key
        if not src.exists():
            log.warning("Staging dir not found: %s", src)
            continue
        dst.mkdir(parents=True, exist_ok=True)
        n = 0
        for ch_dir in sorted(src.iterdir()):
            if not ch_dir.is_dir() or ch_dir.name.startswith("."):
                continue
            target_ch_dir = dst / ch_dir.name
            target_ch_dir.mkdir(exist_ok=True)
            # Remove any old files in target that don't match
            src_files = {f.name for f in ch_dir.glob("*.jpg")}
            for old_dst in target_ch_dir.glob("*.jpg"):
                if old_dst.name not in src_files:
                    old_dst.unlink(missing_ok=True)

            for img in sorted(ch_dir.glob("*.jpg")):
                d = target_ch_dir / img.name
                if not d.exists() or d.stat().st_size != img.stat().st_size:
                    shutil.copy2(img, d)
                    n += 1
        log.info("Copied %d new/updated files: %s -> %s", n, src, dst)
        total += n

    log.info("SD copy complete. Total synchronized files: %d", total)
    return True


def verify_output(root, target_keys=None):
    keys = target_keys or list(SERIES_CONFIG)
    all_ok = True

    print()
    print("=" * 70)
    print("VERIFICATION REPORT (v3.0 Landscape 320x240)")
    print(f"Root: {root}")
    print("=" * 70)

    for key in keys:
        series_dir = root / key
        if not series_dir.exists():
            print(f"\n  {key}: *** MISSING ***")
            all_ok = False
            continue

        chapters = sorted(d for d in series_dir.iterdir() if d.is_dir() and not d.name.startswith("."))
        total_imgs = 0
        v3_chapters = 0
        bad = []

        for ch in chapters:
            v3_flag = (ch / ".landscape_v3").exists() or (ch / "p001_2.jpg").exists()
            if v3_flag:
                v3_chapters += 1
            for img in sorted(ch.glob("*.jpg")):
                total_imgs += 1
                try:
                    with Image.open(img) as im:
                        w, h = im.size
                        # Saved as 240x280 file (rotated 90° CW for landscape viewing in 240x280 canvas)
                        if w != 240 or h != 280:
                            bad.append(f"{ch.name}/{img.name}: {w}x{h}")
                except Exception as exc:
                    bad.append(f"{ch.name}/{img.name}: probe error: {exc}")

        status = "OK" if not bad else f"{len(bad)} BAD"
        print(f"\n  {key}")
        print(f"    Chapters : {len(chapters)} (v3 landscape: {v3_chapters})")
        print(f"    Images   : {total_imgs}")
        print(f"    Status   : {status}")
        if bad:
            all_ok = False
            for b in bad[:10]:
                print(f"    BAD: {b}")
            if len(bad) > 10:
                print(f"    ... and {len(bad)-10} more")
        else:
            if total_imgs > 0:
                print(f"    All {total_imgs} images are strictly 240x280 landscape-ready [OK]")

    print()
    return all_ok


def main():
    p = argparse.ArgumentParser(
        description="Nokia 215 4G High-Readability Landscape Manga Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--series",
        choices=["Vinland_Saga", "Berserk", "Vagabond", "A_Silent_Voice", "all"],
        default="all",
        help="Which series to process (default: all)",
    )
    p.add_argument(
        "--chapter-start", type=float, metavar="N",
        help="Only process chapters >= N",
    )
    p.add_argument(
        "--chapter-end", type=float, metavar="N",
        help="Only process chapters <= N",
    )
    p.add_argument(
        "--copy-sd", action="store_true",
        help="Copy staging (E:\\nokia\\manga_out) to SD card (F:\\Manga)",
    )
    p.add_argument(
        "--verify", action="store_true",
        help="Verify staging output",
    )
    p.add_argument(
        "--verify-sd", action="store_true",
        help="Verify SD card output",
    )
    args = p.parse_args()

    if args.series == "all":
        target = ["A_Silent_Voice", "Vinland_Saga", "Vagabond", "Berserk"]
    else:
        target = [args.series]

    if args.copy_sd:
        copy_to_sd(target)
        return

    if args.verify:
        ok = verify_output(STAGING_ROOT, target)
        sys.exit(0 if ok else 1)

    if args.verify_sd:
        ok = verify_output(SD_ROOT, target)
        sys.exit(0 if ok else 1)

    ch_range = None
    if args.chapter_start or args.chapter_end:
        ch_range = (args.chapter_start or 0.0, args.chapter_end or 99999.0)

    all_failed = {}
    for key in target:
        failed = run_series(key, chapter_range=ch_range)
        if failed:
            all_failed[key] = failed

    sd_drive = SD_ROOT.drive + "\\"
    if Path(sd_drive).exists():
        log.info("SD card detected at %s - synchronizing ...", sd_drive)
        copy_to_sd(target)
    else:
        log.info("SD card not mounted at %s. Connect phone/card and run: python manga_pipeline.py --copy-sd", sd_drive)

    if all_failed:
        log.warning("Some chapters failed:")
        for k, chs in all_failed.items():
            log.warning("  %s: %s", k, chs)
        sys.exit(1)


if __name__ == "__main__":
    main()
