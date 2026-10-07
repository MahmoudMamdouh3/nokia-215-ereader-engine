"""
Nokia 215 4G - Tafsir Al-Mukhtasar (تفسير المختصر) Pipeline
Renders all 114 Surahs in both Arabic and English into 240x320 portrait images.
"""

import os
import sys
import json
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"E:\nokia"
RAW_DIR = os.path.join(BASE_DIR, "books_raw")
OUT_DIR = os.path.join(BASE_DIR, "books_out")

AR_TAFSIR_RAW = os.path.join(RAW_DIR, "tafsir_mokhtasar_ar")
EN_TAFSIR_RAW = os.path.join(RAW_DIR, "tafsir_mokhtasar_en")

OUT_AR_DIR = os.path.join(OUT_DIR, "01_Quran_And_Tafsir", "03_Tafsir_Al_Mukhtasar_Arabic")
OUT_EN_DIR = os.path.join(OUT_DIR, "01_Quran_And_Tafsir", "04_Tafsir_Al_Mukhtasar_English")

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

FONT_AR_PATH = os.path.join(BASE_DIR, "fonts", "Amiri-Regular.ttf")
FONT_EN_BODY_PATH = r"C:\Windows\Fonts\segoeui.ttf"
FONT_EN_HEAD_PATH = r"C:\Windows\Fonts\arial.ttf"

ar_reshaper = arabic_reshaper.ArabicReshaper({
    'delete_harakat': False,
    'support_ligatures': True,
})

def to_ar_num(num):
    ar_digits = '٠١٢٣٤٥٦٧٨٩'
    return ''.join(ar_digits[int(d)] for d in str(num))

def load_surah_meta():
    with open(os.path.join(RAW_DIR, "quran.json"), "r", encoding="utf-8") as f:
        surahs = json.load(f)
    meta = {}
    for s in surahs:
        meta[s['id']] = {
            'name': s['name'],
            'translit': s['transliteration'].replace("'", "").replace(" ", "_")
        }
    return meta

def build_arabic_tafsir():
    print("\n==================================================")
    print(" BUILDING TAFSIR AL-MUKHTASAR (ARABIC - 114 SURAHS)")
    print("==================================================")
    os.makedirs(OUT_AR_DIR, exist_ok=True)
    meta = load_surah_meta()

    font_body = ImageFont.truetype(FONT_AR_PATH, 15)
    font_ayah = ImageFont.truetype(FONT_AR_PATH, 16)
    font_head = ImageFont.truetype(FONT_AR_PATH, 13)
    font_foot = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)

    dummy_img = Image.new('RGB', (1, 1))
    draw_dummy = ImageDraw.Draw(dummy_img)
    total_all_pages = 0

    for s_id in range(1, 115):
        json_file = os.path.join(AR_TAFSIR_RAW, f"{s_id}.json")
        if not os.path.exists(json_file):
            continue

        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        s_info = meta.get(s_id, {'name': f'سورة {s_id}', 'translit': f'Surah_{s_id}'})
        folder_name = f"Surah_{s_id:03d}_{s_info['translit']}"
        ch_dir = os.path.join(OUT_AR_DIR, folder_name)
        os.makedirs(ch_dir, exist_ok=True)

        lines = []
        for item in data['result']:
            aya_num = item['aya']
            ayah_text = item.get('arabic_text', '').strip()
            tafsir_text = item.get('translation', '').strip()

            # Format Ayah line
            if ayah_text:
                aya_header = f"﴿{to_ar_num(aya_num)}﴾ {ayah_text}"
                words_ayah = aya_header.split()
                cur_words = []
                for w in words_ayah:
                    test_str = ' '.join(cur_words + [w])
                    disp = get_display(ar_reshaper.reshape(test_str))
                    bbox = draw_dummy.textbbox((0, 0), disp, font=font_ayah)
                    if (bbox[2] - bbox[0]) <= USABLE_WIDTH:
                        cur_words.append(w)
                    else:
                        if cur_words:
                            lines.append(("AYAH", ' '.join(cur_words)))
                            cur_words = [w]
                        else:
                            lines.append(("AYAH", w))
                            cur_words = []
                if cur_words:
                    lines.append(("AYAH", ' '.join(cur_words)))

            # Format Tafsir words
            if tafsir_text:
                words = tafsir_text.split()
                cur_words = []
                for w in words:
                    test_str = ' '.join(cur_words + [w])
                    disp = get_display(ar_reshaper.reshape(test_str))
                    bbox = draw_dummy.textbbox((0, 0), disp, font=font_body)
                    if (bbox[2] - bbox[0]) <= USABLE_WIDTH:
                        cur_words.append(w)
                    else:
                        if cur_words:
                            lines.append(("TAFSIR", ' '.join(cur_words)))
                            cur_words = [w]
                        else:
                            lines.append(("TAFSIR", w))
                            cur_words = []
                if cur_words:
                    lines.append(("TAFSIR", ' '.join(cur_words)))

            lines.append(("GAP", ""))

        # Paginate
        pages = []
        cur_page = []
        cur_h = 0
        for l_type, l_text in lines:
            if l_type == "GAP":
                needed_h = 8
            elif l_type == "AYAH":
                needed_h = 28
            else:
                needed_h = 23

            if cur_h + needed_h > (FOOTER_LINE_Y - BODY_TOP_Y - 4):
                if cur_page:
                    pages.append(cur_page)
                    cur_page = []
                    cur_h = 0
            if l_type != "GAP" or (l_type == "GAP" and cur_page):
                cur_page.append((l_type, l_text))
                cur_h += needed_h
        if cur_page:
            pages.append(cur_page)

        total_pages = len(pages)
        total_all_pages += total_pages

        # Header string
        h_raw = f"تَفْسِيرُ سُورَةِ {s_info['name']} • Al-Mukhtasar"
        disp_h = get_display(ar_reshaper.reshape(h_raw))

        for p_idx, page_lines in enumerate(pages):
            p_num = p_idx + 1
            out_file = os.path.join(ch_dir, f"page_{p_num:03d}.jpg")

            img = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
            d = ImageDraw.Draw(img)

            # Header
            bbox_h = d.textbbox((0, 0), disp_h, font=font_head)
            w_h = bbox_h[2] - bbox_h[0]
            d.text(((WIDTH - w_h) // 2, HEADER_Y), disp_h, fill=(70, 70, 70), font=font_head)
            d.line([(12, HEADER_LINE_Y), (228, HEADER_LINE_Y)], fill=(220, 220, 220), width=1)

            # Body
            y = BODY_TOP_Y + 2
            for l_type, l_text in page_lines:
                if l_type == "GAP":
                    y += 8
                    continue
                disp = get_display(ar_reshaper.reshape(l_text))
                if l_type == "AYAH":
                    bbox = d.textbbox((0, 0), disp, font=font_ayah)
                    w = bbox[2] - bbox[0]
                    d.text(((WIDTH - w) // 2, y), disp, fill=(0, 65, 35), font=font_ayah)
                    y += 28
                else:
                    bbox = d.textbbox((0, 0), disp, font=font_body)
                    w = bbox[2] - bbox[0]
                    d.text((WIDTH - 12 - w, y), disp, fill=(15, 15, 15), font=font_body)
                    y += 23

            # Footer
            d.line([(12, FOOTER_LINE_Y), (228, FOOTER_LINE_Y)], fill=(220, 220, 220), width=1)
            f_str = f"{p_num} / {total_pages}"
            bbox_f = d.textbbox((0, 0), f_str, font=font_foot)
            w_f = bbox_f[2] - bbox_f[0]
            d.text(((WIDTH - w_f) // 2, FOOTER_Y), f_str, fill=(120, 120, 120), font=font_foot)

            img.save(out_file, "JPEG", quality=92)

        print(f"  [+] Arabic Tafsir {folder_name}: {total_pages} pages")

    print(f"-> Arabic Tafsir Al-Mukhtasar complete: {total_all_pages} total pages.")

def build_english_tafsir():
    print("\n==================================================")
    print(" BUILDING TAFSIR AL-MUKHTASAR (ENGLISH - 114 SURAHS)")
    print("==================================================")
    os.makedirs(OUT_EN_DIR, exist_ok=True)
    meta = load_surah_meta()

    font_body = ImageFont.truetype(FONT_EN_BODY_PATH, 13)
    font_head = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)

    dummy_img = Image.new('RGB', (1, 1))
    draw_dummy = ImageDraw.Draw(dummy_img)
    total_all_pages = 0

    for s_id in range(1, 115):
        json_file = os.path.join(EN_TAFSIR_RAW, f"{s_id}.json")
        if not os.path.exists(json_file):
            continue

        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        s_info = meta.get(s_id, {'name': f'Surah {s_id}', 'translit': f'Surah_{s_id}'})
        folder_name = f"Surah_{s_id:03d}_{s_info['translit']}"
        ch_dir = os.path.join(OUT_EN_DIR, folder_name)
        os.makedirs(ch_dir, exist_ok=True)

        paras = []
        for item in data['result']:
            aya_num = item['aya']
            tafsir_text = item.get('translation', '').strip()
            # Clean English text
            tafsir_clean = tafsir_text.replace('\r\n', '\n').replace('\r', '\n')
            tafsir_clean = tafsir_clean.replace('”', '"').replace('“', '"').replace('’', "'").replace('‘', "'")
            tafsir_clean = ' '.join(tafsir_clean.split())
            paras.append(f"[{aya_num}] {tafsir_clean}")

        # Paginate
        pages = []
        cur_page = []
        cur_h = 0
        line_height = 19
        para_gap = 6

        for p in paras:
            words = p.split()
            if not words:
                continue
            p_lines = []
            cur_line = []
            for w in words:
                test_str = ' '.join(cur_line + [w])
                bbox = draw_dummy.textbbox((0, 0), test_str, font=font_body)
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
                needed = line_height + (para_gap if (idx == 0 and len(cur_page) > 0) else 0)
                if cur_h + needed > (FOOTER_LINE_Y - BODY_TOP_Y - 4):
                    pages.append(cur_page)
                    cur_page = []
                    cur_h = 0
                    needed = line_height
                is_para = (idx == 0 and len(cur_page) > 0)
                cur_page.append((line, is_para))
                cur_h += needed

        if cur_page:
            pages.append(cur_page)

        total_pages = len(pages)
        total_all_pages += total_pages

        h_title = f"TAFSIR • SURAH {s_id}: {s_info['translit'].upper()}"

        for p_idx, page_lines in enumerate(pages):
            p_num = p_idx + 1
            out_file = os.path.join(ch_dir, f"page_{p_num:03d}.jpg")

            img = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
            d = ImageDraw.Draw(img)

            # Header
            head_txt = h_title
            bbox_h = d.textbbox((0, 0), head_txt, font=font_head)
            while (bbox_h[2] - bbox_h[0]) > USABLE_WIDTH and len(head_txt) > 10:
                head_txt = head_txt[:-4] + "..."
                bbox_h = d.textbbox((0, 0), head_txt, font=font_head)

            d.text((12, HEADER_Y), head_txt, fill=(90, 90, 90), font=font_head)
            d.line([(12, HEADER_LINE_Y), (228, HEADER_LINE_Y)], fill=(220, 220, 220), width=1)

            # Body
            y = BODY_TOP_Y + 1
            for line, is_para in page_lines:
                if is_para:
                    y += 5
                d.text((12, y), line, fill=(15, 15, 15), font=font_body)
                y += line_height

            # Footer
            d.line([(12, FOOTER_LINE_Y), (228, FOOTER_LINE_Y)], fill=(220, 220, 220), width=1)
            f_str = f"{p_num} / {total_pages}"
            bbox_f = d.textbbox((0, 0), f_str, font=font_foot)
            w_f = bbox_f[2] - bbox_f[0]
            d.text(((WIDTH - w_f) // 2, FOOTER_Y), f_str, fill=(120, 120, 120), font=font_foot)

            img.save(out_file, "JPEG", quality=92)

        print(f"  [+] English Tafsir {folder_name}: {total_pages} pages")

    print(f"-> English Tafsir Al-Mukhtasar complete: {total_all_pages} total pages.")

if __name__ == "__main__":
    build_arabic_tafsir()
    build_english_tafsir()
