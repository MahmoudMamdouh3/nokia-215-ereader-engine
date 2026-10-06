# -*- coding: utf-8 -*-
"""
Nokia 215 4G (2024) - Image Viewer Screen-Area Calibration Kit
==============================================================

PROBLEM
-------
The S30+ photo viewer always draws a status bar (top) and a softkey bar
(bottom, "Options" / "Back"). HMD does not publish the pixel size of these
bars, so every book page that is rendered as a full 240x320 image loses part
of its content (or gets shrunk) when opened on the phone.

This tool generates test images so the REAL usable viewing area can be
measured on the physical phone instead of guessed.

USAGE
-----
    python screen_calibration.py              # build kit (+ copy to F:\\Calibration if the phone is mounted)
    python screen_calibration.py fine 264     # round 2: 2-px steps around a measured height of 264

KIT CONTENTS (calibration_out/)
-------------------------------
    1_Ruler/RULER_240x320.jpg   Full-size 240x320 image with a numbered pixel ruler on every side.
                                Tells you which rows/columns are hidden or scaled.
    2_Fit_Test/FIT_240xNNN.jpg  Same width, different heights. The image whose red frame touches
                                BOTH bars with no black gap is the exact usable-area aspect ratio.

See docs/SCREEN_AREA_ISSUE.md for the full procedure and results.
"""

import os
import sys
import shutil

from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"E:\nokia"
OUT_DIR = os.path.join(BASE_DIR, "calibration_out")
PHONE_DIR = r"F:\Calibration"

SCREEN_W = 240
SCREEN_H = 320

FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"

RED = (220, 0, 0)
BLACK = (0, 0, 0)
GRAY = (190, 190, 190)
DARK = (60, 60, 60)
BLUE = (0, 70, 220)
GREEN = (0, 150, 0)
ORANGE = (230, 120, 0)
WHITE = (255, 255, 255)


def font(size):
    return ImageFont.truetype(FONT_BOLD, size)


def save_jpg(img, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # 4:4:4 chroma + q95 keeps 1-px lines and colours crisp on the tiny LCD
    img.save(path, "JPEG", quality=95, subsampling=0)


def corner_markers(draw, w, h, size=12):
    """Colour-coded corner squares: TL red, TR green, BL blue, BR orange."""
    draw.rectangle([0, 0, size - 1, size - 1], fill=RED)
    draw.rectangle([w - size, 0, w - 1, size - 1], fill=GREEN)
    draw.rectangle([0, h - size, size - 1, h - 1], fill=BLUE)
    draw.rectangle([w - size, h - size, w - 1, h - 1], fill=ORANGE)


def build_ruler():
    """
    240x320 numbered ruler.
      - Horizontal line every 10 px, heavier every 50 px.
      - Row numbers are staggered over two columns (0,20,40.. left / 10,30,50.. right-of-centre)
        so every 10 px has a label while each label stays big enough to read.
      - Column numbers (x) are printed at three heights so a hidden top/bottom bar cannot hide all of them.
      - Colour-coded corner squares + a 1-px outer frame at the extreme pixel edges.
    """
    img = Image.new("RGB", (SCREEN_W, SCREEN_H), WHITE)
    d = ImageDraw.Draw(img)
    f_lbl = font(10)
    f_title = font(11)

    # Vertical rules every 20 px (light) - drawn first so text stays on top
    for x in range(0, SCREEN_W, 20):
        d.line([(x, 0), (x, SCREEN_H - 1)], fill=(205, 205, 255), width=1)

    # Horizontal rules every 10 px, heavier every 50 px
    for y in range(0, SCREEN_H, 10):
        major = (y % 50 == 0)
        d.line([(0, y), (SCREEN_W - 1, y)], fill=(BLACK if major else GRAY), width=(2 if major else 1))

    # Row labels = absolute Y of the line they sit just under. Left and right edge.
    for y in range(0, SCREEN_H, 10):
        txt = str(y)
        colour = RED if y % 50 == 0 else DARK
        d.text((14, y + 1), txt, fill=colour, font=f_lbl)
        tw = d.textlength(txt, font=f_lbl)
        d.text((SCREEN_W - 14 - tw, y + 1), txt, fill=colour, font=f_lbl)

    # Column labels = absolute X, printed in the clear centre band at three heights
    for yy in (41, 151, 261):
        d.rectangle([40, yy - 1, 59, yy + 11], fill=WHITE)
        d.text((42, yy), "X:", fill=GREEN, font=f_lbl)
        for x in range(60, 200, 20):
            d.rectangle([x, yy - 1, x + 19, yy + 11], fill=WHITE)
            d.text((x + 2, yy), str(x), fill=GREEN, font=f_lbl)

    # Outer frame at the extreme edges + corner squares
    d.rectangle([0, 0, SCREEN_W - 1, SCREEN_H - 1], outline=BLACK, width=1)
    corner_markers(d, SCREEN_W, SCREEN_H)

    # Title block (centre of the image, safe from any bar)
    d.rectangle([62, 100, 178, 124], fill=WHITE, outline=BLACK)
    d.text((68, 105), "RULER 240x320", fill=BLACK, font=f_title)
    return img


def build_fit(h):
    """
    240 x h fit-test image.
    Thick red frame on all four edges + corner squares + crosshair + big size label.
    If the viewer shows this image with the frame flush against BOTH bars and the
    screen edges (no black gaps), 240 x h matches the usable area exactly.
    """
    img = Image.new("RGB", (SCREEN_W, h), WHITE)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, SCREEN_W - 1, h - 1], outline=RED, width=3)
    d.rectangle([5, 5, SCREEN_W - 6, h - 6], outline=GRAY, width=1)
    corner_markers(d, SCREEN_W, h, size=14)

    cx, cy = SCREEN_W // 2, h // 2
    d.line([(0, cy), (SCREEN_W - 1, cy)], fill=GRAY, width=1)
    d.line([(cx, 0), (cx, h - 1)], fill=GRAY, width=1)
    d.line([(0, 0), (SCREEN_W - 1, h - 1)], fill=(235, 235, 235), width=1)
    d.line([(SCREEN_W - 1, 0), (0, h - 1)], fill=(235, 235, 235), width=1)

    label = f"240x{h}"
    f_big = font(34)
    tw = d.textlength(label, font=f_big)
    d.rectangle([cx - tw / 2 - 6, cy - 26, cx + tw / 2 + 6, cy + 22], fill=WHITE, outline=BLACK)
    d.text((cx - tw / 2, cy - 22), label, fill=BLACK, font=f_big)

    f_s = font(11)
    d.text((22, 22), "TOP edge", fill=DARK, font=f_s)
    t = "BOTTOM edge"
    d.text((SCREEN_W - 22 - d.textlength(t, font=f_s), h - 36), t, fill=DARK, font=f_s)
    return img


def build_kit(fit_heights):
    if os.path.exists(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    ruler_path = os.path.join(OUT_DIR, "1_Ruler", "RULER_240x320.jpg")
    save_jpg(build_ruler(), ruler_path)
    for h in fit_heights:
        save_jpg(build_fit(h), os.path.join(OUT_DIR, "2_Fit_Test", f"FIT_240x{h:03d}.jpg"))
    return OUT_DIR


def copy_to_phone():
    if not os.path.exists("F:\\"):
        print("[!] Phone (F:\\) not detected - kit left in", OUT_DIR)
        return False
    if os.path.exists(PHONE_DIR):
        shutil.rmtree(PHONE_DIR, ignore_errors=True)
    for root, _dirs, files in os.walk(OUT_DIR):
        rel = os.path.relpath(root, OUT_DIR)
        dst = os.path.join(PHONE_DIR, rel)
        os.makedirs(dst, exist_ok=True)
        for fn in sorted(files):
            with open(os.path.join(root, fn), "rb") as fs, open(os.path.join(dst, fn), "wb") as fd:
                shutil.copyfileobj(fs, fd, length=256 * 1024)
    print("[OK] Calibration kit copied to", PHONE_DIR)
    return True


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1].lower() == "fine":
        centre = int(sys.argv[2])
        heights = sorted({h for h in range(centre - 8, centre + 9, 2) if 160 <= h <= SCREEN_H})
        print("Round 2 (2-px steps):", heights)
    else:
        heights = list(range(240, SCREEN_H + 1, 8))
        print("Round 1 (8-px steps):", heights)
    out = build_kit(heights)
    for r, _d, fs in os.walk(out):
        for fn in sorted(fs):
            p = os.path.join(r, fn)
            with Image.open(p) as im:
                print(f"  {os.path.relpath(p, out):35s} {im.size[0]}x{im.size[1]}")
    copy_to_phone()
