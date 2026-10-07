"""
Nokia 215 4G - Programming Books Pipeline
Renders:
1. The Pragmatic Programmer (Andrew Hunt & David Thomas) -> 10_The_Pragmatic_Programmer
2. Programming: Principles and Practice Using C++ (Bjarne Stroustrup) -> 11_Programming_Principles_And_Practice_Using_CPP
"""

import os
import sys
import re
import shutil
import zipfile
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"E:\nokia"
RAW_DIR = os.path.join(BASE_DIR, "books_raw")
OUT_DIR = os.path.join(BASE_DIR, "books_out")

# Screen Specs (Calibrated 240x280 for Nokia 215 4G S30+ Persistent UI)
WIDTH = 240
HEIGHT = 280
USABLE_WIDTH = 216
USABLE_HEIGHT = 224
HEADER_Y = 7
HEADER_LINE_Y = 23
BODY_TOP_Y = 29
FOOTER_LINE_Y = 257
FOOTER_Y = 262

FONT_BODY_PATH = r"C:\Windows\Fonts\georgia.ttf"
FONT_HEAD_PATH = r"C:\Windows\Fonts\arial.ttf"

def clean_en_text(text):
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = text.replace('”', '"').replace('“', '"').replace('’', "'").replace('‘', "'")
    text = text.replace('—', ' - ').replace('–', '-')
    text = re.sub(r'_[^_]+_', lambda m: m.group(0)[1:-1], text)
    paras = re.split(r'\n\s*\n', text)
    cleaned = []
    for p in paras:
        p_clean = ' '.join(p.split())
        if p_clean and not p_clean.startswith('http://') and not p_clean.startswith('www.'):
            cleaned.append(p_clean)
    return cleaned

def extract_epub_pages_text(epub_path, start_page, end_page):
    texts = []
    with zipfile.ZipFile(epub_path) as z:
        for p_num in range(start_page, end_page + 1):
            name = f"EPUB/page_{p_num}.html"
            if name in z.namelist():
                soup = BeautifulSoup(z.read(name), 'html.parser')
                p_text = soup.get_text().strip()
                p_text = re.sub(r'^Page\s+\d+\s*', '', p_text)
                if p_text:
                    texts.append(p_text)
    return '\n\n'.join(texts)

def paginate_chapter(paras, font_body, line_height=21, para_gap=8):
    dummy_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    pages = []
    current_page = []
    current_h = 0

    for p in paras:
        words = p.split()
        if not words:
            continue
        p_lines = []
        cur_line = []
        for w in words:
            test_str = ' '.join(cur_line + [w])
            bbox = draw.textbbox((0, 0), test_str, font=font_body)
            if (bbox[2] - bbox[0]) <= USABLE_WIDTH:
                cur_line.append(w)
            else:
                if cur_line:
                    p_lines.append(' '.join(cur_line))
                    cur_line = [w]
                else:
                    p_lines.append(w)
                    cur_line = []
        if cur_line:
            p_lines.append(' '.join(cur_line))

        for idx, line in enumerate(p_lines):
            needed = line_height + (para_gap if (idx == 0 and len(current_page) > 0) else 0)
            if current_h + needed > (FOOTER_LINE_Y - BODY_TOP_Y - 4):
                pages.append(current_page)
                current_page = []
                current_h = 0
                needed = line_height
            is_para = (idx == 0 and len(current_page) > 0)
            current_page.append((line, is_para))
            current_h += needed

    if current_page:
        pages.append(current_page)
    return pages

def render_pages(pages, chapter_dir, header_title, font_body, font_head, font_foot):
    os.makedirs(chapter_dir, exist_ok=True)
    total_pages = len(pages)
    for p_idx, page_lines in enumerate(pages):
        page_num = p_idx + 1
        out_path = os.path.join(chapter_dir, f"page_{page_num:03d}.jpg")

        img = Image.new('RGB', (WIDTH, HEIGHT), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        # Header
        h_text = header_title
        bbox_h = draw.textbbox((0, 0), h_text, font=font_head)
        while (bbox_h[2] - bbox_h[0]) > USABLE_WIDTH and len(h_text) > 10:
            h_text = h_text[:-4] + "..."
            bbox_h = draw.textbbox((0, 0), h_text, font=font_head)

        draw.text((12, HEADER_Y), h_text, fill=(100, 100, 100), font=font_head)
        draw.line([(12, HEADER_LINE_Y), (228, HEADER_LINE_Y)], fill=(225, 225, 225), width=1)

        # Body
        y = BODY_TOP_Y
        for line, is_para in page_lines:
            if is_para:
                y += 6
            draw.text((12, y), line, fill=(15, 15, 15), font=font_body)
            y += 20

        # Footer
        draw.line([(12, FOOTER_LINE_Y), (228, FOOTER_LINE_Y)], fill=(225, 225, 225), width=1)
        foot_str = f"{page_num} / {total_pages}"
        bbox_f = draw.textbbox((0, 0), foot_str, font=font_foot)
        foot_w = bbox_f[2] - bbox_f[0]
        draw.text(((WIDTH - foot_w) // 2, FOOTER_Y), foot_str, fill=(120, 120, 120), font=font_foot)

        img.save(out_path, "JPEG", quality=92)
    return total_pages

# ==============================================================================
# 1. THE PRAGMATIC PROGRAMMER (20TH ANNIVERSARY EDITION / 2ND EDITION)
# ==============================================================================
def build_pragmatic_programmer():
    print("\n==================================================")
    print("   BUILDING THE PRAGMATIC PROGRAMMER (20TH ANNIV) ")
    print("==================================================")
    epub_path = os.path.join(RAW_DIR, "pragmatic_programmer.epub")
    book_dir = os.path.join(OUT_DIR, "04_Computer_Science", "01_The_Pragmatic_Programmer")

    # Clean previous stale files
    if os.path.exists(book_dir):
        shutil.rmtree(book_dir)
    os.makedirs(book_dir, exist_ok=True)

    chapters_def = [
        ("Ch_00_Foreword_And_Preface", 11, 27),
        ("Ch_01_A_Pragmatic_Philosophy", 28, 59),
        ("Ch_02_A_Pragmatic_Approach", 60, 114),
        ("Ch_03_The_Basic_Tools", 115, 146),
        ("Ch_04_Pragmatic_Paranoia", 147, 176),
        ("Ch_05_Bend_Or_Break", 177, 224),
        ("Ch_06_Concurrency", 225, 250),
        ("Ch_07_While_You_Are_Coding", 251, 313),
        ("Ch_08_Before_The_Project", 314, 337),
        ("Ch_09_Pragmatic_Projects", 338, 361),
        ("Ch_10_Postface", 362, 366),
        ("Ch_11_Appendix_A_Bibliography", 367, 368),
        ("Ch_12_Appendix_B_Possible_Answers", 369, 376),
    ]

    font_body = ImageFont.truetype(FONT_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_HEAD_PATH, 10)
    total_book_pages = 0

    for ch_name, sp, ep in chapters_def:
        raw_text = extract_epub_pages_text(epub_path, sp, ep)
        paras = clean_en_text(raw_text)
        pages = paginate_chapter(paras, font_body)
        ch_dir = os.path.join(book_dir, ch_name)
        title = "PRAGMATIC PROGRAMMER • " + ch_name.replace("_", " ")
        cnt = render_pages(pages, ch_dir, title, font_body, font_head, font_foot)
        total_book_pages += cnt
        print(f"  [+] {ch_name}: {cnt} pages")

    print(f"-> The Pragmatic Programmer (20th Anniv.) complete: {total_book_pages} total pages.")

# ==============================================================================
# 2. PROGRAMMING: PRINCIPLES AND PRACTICE USING C++ (BJARNE STROUSTRUP - 3RD ED)
# ==============================================================================
def build_programming_principles_cpp():
    print("\n==================================================")
    print(" BUILDING PROGRAMMING: PRINCIPLES & PRACTICE (C++)")
    print("==================================================")
    epub_path = os.path.join(RAW_DIR, "cpp_3rd.epub")
    book_dir = os.path.join(OUT_DIR, "04_Computer_Science", "02_Programming_Principles_And_Practice_Using_CPP")
    
    if os.path.exists(book_dir):
        shutil.rmtree(book_dir)
    os.makedirs(book_dir, exist_ok=True)

    font_body = ImageFont.truetype(FONT_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_HEAD_PATH, 10)
    total_book_pages = 0

    with zipfile.ZipFile(epub_path, "r") as z:
        # Get all chapter xhtml files
        ch_files = sorted([f for f in z.namelist() if f.startswith('OEBPS/xhtml/ch') and not f.endswith('_images.xhtml')])
        
        # Include preface
        target_files = [('pref01.xhtml', 'Ch_00_Preface_And_Notes')] + [(os.path.basename(f), f"Ch_{idx:02d}") for idx, f in enumerate(ch_files, 1)]

        for fname, ch_prefix in target_files:
            full_zip_name = f"OEBPS/xhtml/{fname}"
            if full_zip_name not in z.namelist():
                continue

            content = z.read(full_zip_name).decode('utf-8', errors='ignore')
            soup = BeautifulSoup(content, 'html.parser')

            # Extract title
            h1 = soup.find(['h1', 'h2', 'title'])
            raw_title = h1.get_text().strip() if h1 else fname
            clean_title = re.sub(r'^\d+\.\s*', '', raw_title)
            safe_title = re.sub(r'[^a-zA-Z0-9_]', '_', clean_title).strip('_')
            safe_title = re.sub(r'_+', '_', safe_title)
            if len(safe_title) > 35:
                safe_title = safe_title[:35]

            folder_name = f"{ch_prefix}_{safe_title}"
            ch_dir = os.path.join(book_dir, folder_name)

            # Extract text elements
            paras = []
            for tag in soup.find_all(['p', 'li', 'pre', 'h2', 'h3', 'h4']):
                t = tag.get_text().strip()
                if t:
                    # Clean text
                    t_clean = t.replace('\r\n', '\n').replace('\r', '\n')
                    t_clean = t_clean.replace('”', '"').replace('“', '"').replace('’', "'").replace('‘', "'")
                    t_clean = ' '.join(t_clean.split())
                    paras.append(t_clean)

            pages = paginate_chapter(paras, font_body)
            title = f"C++ PRINCIPLES • {clean_title}"
            cnt = render_pages(pages, ch_dir, title, font_body, font_head, font_foot)
            total_book_pages += cnt
            print(f"  [+] {folder_name}: {cnt} pages")

    print(f"-> Programming: Principles & Practice Using C++ complete: {total_book_pages} total pages.")

if __name__ == "__main__":
    build_pragmatic_programmer()
    build_programming_principles_cpp()
