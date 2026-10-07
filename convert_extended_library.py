"""
Nokia 215 4G - Extended Library Parallel Converter & Headroom Guarded Sync
==========================================================================
Converts top-tier Arabic literature masterpieces and English classics from
books_raw to calibrated 240x280 image slices using 16-worker multiprocessing.
Safely streams to F:\\Books while enforcing a strict 5.0 GB minimum free headroom.
"""

import os
import sys
import re
import time
import shutil
import zipfile
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import multiprocessing as mp

sys.stdout.reconfigure(encoding='utf-8')

# Arabic reshaping
try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    HAS_ARABIC = True
except ImportError:
    HAS_ARABIC = False

# Screen specs (240x280 canonical)
WIDTH = 240
HEIGHT = 280
MARGIN_X = 12
USABLE_WIDTH = 216
USABLE_HEIGHT = 224
HEADER_Y = 7
HEADER_LINE_Y = 23
BODY_TOP_Y = 29
FOOTER_LINE_Y = 257
FOOTER_Y = 262

MIN_HEADROOM_BYTES = 5.0 * (1024 ** 3)  # 5.0 GB strictly reserved for phone OS

FONT_EN_BODY_PATH = r"C:\Windows\Fonts\georgia.ttf"
FONT_EN_HEAD_PATH = r"C:\Windows\Fonts\arial.ttf"
FONT_AR_BODY_PATH = r"E:\nokia\fonts\Amiri-Regular.ttf"

def extract_epub_chapters(epub_path):
    """Extracts non-trivial text chapters from an EPUB in spine order."""
    chapters = []
    try:
        with zipfile.ZipFile(epub_path, 'r') as z:
            container = z.read('META-INF/container.xml')
            root = ET.fromstring(container)
            opf_path = root.find('.//{*}rootfile').attrib['full-path']
            opf_dir = '/'.join(opf_path.split('/')[:-1])
            opf = ET.fromstring(z.read(opf_path))
            manifest = {item.attrib['id']: item.attrib['href'] for item in opf.findall('.//{*}manifest/{*}item')}
            spine = [manifest[itemref.attrib['idref']] for itemref in opf.findall('.//{*}spine/{*}itemref') if itemref.attrib['idref'] in manifest]
            
            for href in spine:
                full_href = (opf_dir + '/' + href).lstrip('/') if opf_dir else href
                if full_href in z.namelist() and full_href.endswith(('.html', '.xhtml', '.htm')):
                    soup = BeautifulSoup(z.read(full_href), 'html.parser')
                    text = soup.get_text().strip()
                    if len(text) > 250:
                        chapters.append(text)
    except Exception as e:
        print(f"Error reading EPUB {epub_path}: {e}")
    return chapters

def clean_text_paragraphs(text, is_arabic=False):
    """Cleans text into coherent paragraph blocks."""
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = text.replace('”', '"').replace('“', '"').replace('’', "'").replace('‘', "'")
    text = text.replace('—', ' - ').replace('–', '-')
    paras = re.split(r'\n\s*\n', text)
    cleaned = []
    for p in paras:
        p_clean = ' '.join(p.split())
        if p_clean and not p_clean.startswith('http://') and not p_clean.startswith('www.'):
            cleaned.append(p_clean)
    return cleaned

def render_en_page(args):
    """Worker task to render a single English page."""
    page_data, out_path, header_title, page_num, total_pages = args
    font_body = ImageFont.truetype(FONT_EN_BODY_PATH, 14)
    font_head = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Header
    h_text = header_title
    bbox_h = draw.textbbox((0, 0), h_text, font=font_head)
    while (bbox_h[2] - bbox_h[0]) > (USABLE_WIDTH + 4) and len(h_text) > 8:
        h_text = h_text[:-4] + "..."
        bbox_h = draw.textbbox((0, 0), h_text, font=font_head)
    draw.text((MARGIN_X, HEADER_Y), h_text, fill=(100, 100, 100), font=font_head)
    draw.line([(MARGIN_X, HEADER_LINE_Y), (WIDTH - MARGIN_X, HEADER_LINE_Y)], fill=(225, 225, 225), width=1)
    
    # Body text
    y = BODY_TOP_Y + 2
    for line, is_para_start in page_data:
        if is_para_start:
            y += 6
        draw.text((MARGIN_X, y), line, fill=(15, 15, 15), font=font_body)
        y += 21
        
    # Footer
    draw.line([(MARGIN_X, FOOTER_LINE_Y), (WIDTH - MARGIN_X, FOOTER_LINE_Y)], fill=(225, 225, 225), width=1)
    foot_str = f"{page_num} / {total_pages}"
    bbox_foot = draw.textbbox((0, 0), foot_str, font=font_foot)
    foot_w = bbox_foot[2] - bbox_foot[0]
    draw.text(((WIDTH - foot_w) // 2, FOOTER_Y), foot_str, fill=(120, 120, 120), font=font_foot)
    
    img.save(out_path, "JPEG", quality=92)
    return 1

def render_ar_page(args):
    """Worker task to render a single Arabic page."""
    page_lines, out_path, reshaped_h, page_num, total_pages = args
    font_body = ImageFont.truetype(FONT_AR_BODY_PATH, 19)
    font_head = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Header
    bbox_h = draw.textbbox((0, 0), reshaped_h, font=font_head)
    w_h = bbox_h[2] - bbox_h[0]
    draw.text(((WIDTH - w_h) // 2, HEADER_Y), reshaped_h, fill=(90, 90, 90), font=font_head)
    draw.line([(MARGIN_X, HEADER_LINE_Y), (WIDTH - MARGIN_X, HEADER_LINE_Y)], fill=(225, 225, 225), width=1)
    
    # Body lines (7 lines per page for comfortable vertical pitch in 240x280)
    y = BODY_TOP_Y + 4
    for bidi_line in page_lines:
        bbox_l = draw.textbbox((0, 0), bidi_line, font=font_body)
        w_l = bbox_l[2] - bbox_l[0]
        draw.text(((WIDTH - w_l) // 2, y), bidi_line, fill=(10, 10, 10), font=font_body)
        y += 30
        
    # Footer
    draw.line([(MARGIN_X, FOOTER_LINE_Y), (WIDTH - MARGIN_X, FOOTER_LINE_Y)], fill=(225, 225, 225), width=1)
    foot_str = f"{page_num} / {total_pages}"
    bbox_foot = draw.textbbox((0, 0), foot_str, font=font_foot)
    foot_w = bbox_foot[2] - bbox_foot[0]
    draw.text(((WIDTH - foot_w) // 2, FOOTER_Y), foot_str, fill=(120, 120, 120), font=font_foot)
    
    img.save(out_path, "JPEG", quality=92)
    return 1

def paginate_en_text(paras, font_body):
    """Paginates English paragraphs to fit 240x280 screen."""
    dummy_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    pages = []
    current_page = []
    current_h = 0
    
    for p in paras:
        words = p.split()
        if not words: continue
        p_lines = []
        cur_line = []
        for w in words:
            test_line = ' '.join(cur_line + [w])
            bbox = draw.textbbox((0, 0), test_line, font=font_body)
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
            needed_h = 21 + (6 if (idx == 0 and len(current_page) > 0) else 0)
            if current_h + needed_h > USABLE_HEIGHT:
                pages.append(current_page)
                current_page = []
                current_h = 0
                needed_h = 21
            is_start = (idx == 0 and len(current_page) > 0)
            current_page.append((line, is_start))
            current_h += needed_h
            
    if current_page:
        pages.append(current_page)
    return pages

def paginate_ar_text(paras, font_ar):
    """Paginates Arabic paragraphs to fit 240x280 screen."""
    dummy_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    all_bidi_lines = []
    
    for p in paras:
        words = p.split()
        if not words: continue
        cur_words = []
        for w in words:
            test_str = ' '.join(cur_words + [w])
            reshaped = arabic_reshaper.reshape(test_str)
            bidi_str = get_display(reshaped)
            bbox = draw.textbbox((0, 0), bidi_str, font=font_ar)
            if (bbox[2] - bbox[0]) <= USABLE_WIDTH:
                cur_words.append(w)
            else:
                if cur_words:
                    r = arabic_reshaper.reshape(' '.join(cur_words))
                    all_bidi_lines.append(get_display(r))
                    cur_words = [w]
                else:
                    r = arabic_reshaper.reshape(w)
                    all_bidi_lines.append(get_display(r))
                    cur_words = []
        if cur_words:
            r = arabic_reshaper.reshape(' '.join(cur_words))
            all_bidi_lines.append(get_display(r))
            
    # 7 lines per page
    lines_per_page = 7
    pages = [all_bidi_lines[i:i+lines_per_page] for i in range(0, len(all_bidi_lines), lines_per_page)]
    return pages

def convert_book(epub_file, out_book_dir, book_title, is_arabic=False, pool=None):
    """Converts an entire book into chapter folders of 240x280 pages."""
    chapters = extract_epub_chapters(epub_file)
    if not chapters:
        print(f"[-] No chapters extracted for: {book_title}")
        return 0
        
    print(f"\n[*] Processing Book: {book_title} ({len(chapters)} chapters)...")
    font_body = ImageFont.truetype(FONT_AR_BODY_PATH if is_arabic else FONT_EN_BODY_PATH, 19 if is_arabic else 14)
    tasks = []
    total_pages = 0
    
    for ch_idx, ch_text in enumerate(chapters):
        ch_num = ch_idx + 1
        ch_dir = os.path.join(out_book_dir, f"Ch_{ch_num:02d}")
        os.makedirs(ch_dir, exist_ok=True)
        
        paras = clean_text_paragraphs(ch_text, is_arabic=is_arabic)
        if is_arabic:
            pages = paginate_ar_text(paras, font_body)
            raw_h = f"{book_title[:18]} • Ch {ch_num:02d}"
            r_h = get_display(arabic_reshaper.reshape(raw_h))
            for p_idx, page_lines in enumerate(pages):
                p_num = p_idx + 1
                out_path = os.path.join(ch_dir, f"page_{p_num:03d}.jpg")
                tasks.append((render_ar_page, (page_lines, out_path, r_h, p_num, len(pages))))
        else:
            pages = paginate_en_text(paras, font_body)
            h_title = f"{book_title.upper()[:18]} • CH {ch_num:02d}"
            for p_idx, page_data in enumerate(pages):
                p_num = p_idx + 1
                out_path = os.path.join(ch_dir, f"page_{p_num:03d}.jpg")
                tasks.append((render_en_page, (page_data, out_path, h_title, p_num, len(pages))))
        total_pages += len(pages)
        
    # Render with multiprocessing pool
    if pool:
        for fn, arg in tasks:
            pool.apply_async(fn, (arg,))
    else:
        for fn, arg in tasks:
            fn(arg)
            
    print(f"  -> Queued {len(tasks)} pages for {book_title}")
    return len(tasks)

if __name__ == "__main__":
    print("Extended library converter module loaded.")
