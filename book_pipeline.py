"""
Nokia 215 4G (2024) - High-Definition Portrait Book-to-Images Pipeline
Generates crisp 240x320 portrait JPEG images organized by Book and Chapter.
"""

import os
import re
import sys
import json
import zipfile
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

# Try importing Arabic support
try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    HAS_ARABIC = True
except ImportError:
    HAS_ARABIC = False

# Paths
BASE_DIR = r"E:\nokia"
RAW_DIR = os.path.join(BASE_DIR, "books_raw")
OUT_DIR = os.path.join(BASE_DIR, "books_out")
FONTS_DIR = os.path.join(BASE_DIR, "fonts")

# Fonts
FONT_EN_BODY_PATH = r"C:\Windows\Fonts\georgia.ttf"
FONT_EN_HEAD_PATH = r"C:\Windows\Fonts\arial.ttf"
FONT_AR_BODY_PATH = os.path.join(FONTS_DIR, "Amiri-Regular.ttf")

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

def clean_en_text(text):
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = text.replace('”', '"').replace('“', '"').replace('’', "'").replace('‘', "'")
    text = text.replace('—', ' - ').replace('–', '-')
    text = re.sub(r'_[^_]+_', lambda m: m.group(0)[1:-1], text) # remove underscores
    paras = re.split(r'\n\s*\n', text)
    cleaned = []
    for p in paras:
        p_clean = ' '.join(p.split())
        if p_clean:
            cleaned.append(p_clean)
    return cleaned

def paginate_en_chapter(paras, font_body, line_height=21, para_gap=8):
    dummy_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    
    pages = []
    current_page = []
    current_h = 0
    
    for p in paras:
        words = p.split()
        if not words:
            continue
        
        # Word wrap
        p_lines = []
        cur_line = []
        for w in words:
            test_line = ' '.join(cur_line + [w])
            bbox = draw.textbbox((0, 0), test_line, font=font_body)
            line_w = bbox[2] - bbox[0]
            if line_w <= USABLE_WIDTH:
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
            
        # Fit into pages
        for idx, line in enumerate(p_lines):
            needed_h = line_height + (para_gap if (idx == 0 and len(current_page) > 0) else 0)
            if current_h + needed_h > USABLE_HEIGHT:
                pages.append(current_page)
                current_page = []
                current_h = 0
                needed_h = line_height
            
            is_para_start = (idx == 0 and len(current_page) > 0)
            current_page.append((line, is_para_start))
            current_h += needed_h
            
    if current_page:
        pages.append(current_page)
        
    return pages

def render_en_pages(pages, chapter_dir, header_title, font_body, font_head, font_foot):
    os.makedirs(chapter_dir, exist_ok=True)
    total_pages = len(pages)
    
    for p_idx, page_lines in enumerate(pages):
        page_num = p_idx + 1
        out_path = os.path.join(chapter_dir, f"page_{page_num:03d}.jpg")
            
        img = Image.new('RGB', (WIDTH, HEIGHT), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        # Header (truncate if too long)
        header_text = header_title
        bbox_head = draw.textbbox((0, 0), header_text, font=font_head)
        while (bbox_head[2] - bbox_head[0]) > (USABLE_WIDTH + 6) and len(header_text) > 10:
            header_text = header_text[:-4] + "..."
            bbox_head = draw.textbbox((0, 0), header_text, font=font_head)
            
        draw.text((12, HEADER_Y), header_text, fill=(100, 100, 100), font=font_head)
        draw.line([(12, HEADER_LINE_Y), (228, HEADER_LINE_Y)], fill=(225, 225, 225), width=1)
        
        # Body text
        y = BODY_TOP_Y
        for line, is_para_start in page_lines:
            if is_para_start:
                y += 6
            draw.text((12, y), line, fill=(15, 15, 15), font=font_body)
            y += 20
            
        # Footer
        draw.line([(12, FOOTER_LINE_Y), (228, FOOTER_LINE_Y)], fill=(225, 225, 225), width=1)
        foot_str = f"{page_num} / {total_pages}"
        bbox_foot = draw.textbbox((0, 0), foot_str, font=font_foot)
        foot_w = bbox_foot[2] - bbox_foot[0]
        draw.text(((WIDTH - foot_w) // 2, FOOTER_Y), foot_str, fill=(120, 120, 120), font=font_foot)
        
        img.save(out_path, "JPEG", quality=92)
    return total_pages

def build_white_nights():
    print("\n--- Processing White Nights by Fyodor Dostoevsky ---")
    txt_path = os.path.join(RAW_DIR, "white_nights_full.txt")
    with open(txt_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    chapters = [
        ('Ch_01_First_Night', 'FIRST NIGHT', 'SECOND NIGHT'),
        ('Ch_02_Second_Night', 'SECOND NIGHT', 'NASTENKA'),
        ('Ch_03_Nastenkas_Story', 'NASTENKA', 'THIRD NIGHT'),
        ('Ch_04_Third_Night', 'THIRD NIGHT', 'FOURTH NIGHT'),
        ('Ch_05_Fourth_Night', 'FOURTH NIGHT', 'MORNING\n'),
        ('Ch_06_Morning', 'MORNING\n', 'NOTES FROM UNDERGROUND')
    ]
    
    font_body = ImageFont.truetype(FONT_EN_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    
    book_dir = os.path.join(OUT_DIR, "05_Literary_Classics", "01_White_Nights")
    total_book_pages = 0
    
    for ch_folder, start_kw, end_kw in chapters:
        s_idx = raw.find(start_kw)
        e_idx = raw.find(end_kw, s_idx + len(start_kw))
        ch_text = raw[s_idx:e_idx].strip()
        paras = clean_en_text(ch_text)
        pages = paginate_en_chapter(paras, font_body)
        
        ch_name_clean = ch_folder.replace('_', ' ').replace('Ch ', 'CH. ')
        ch_dir = os.path.join(book_dir, ch_folder)
        rendered = render_en_pages(pages, ch_dir, f"WHITE NIGHTS • {ch_name_clean}", font_body, font_head, font_foot)
        total_book_pages += rendered
        print(f"  [+] {ch_folder}: {rendered} pages")
        
    print(f"-> White Nights complete: {total_book_pages} total pages.")

def build_the_trial():
    print("\n--- Processing The Trial by Franz Kafka ---")
    txt_path = os.path.join(RAW_DIR, "the_trial.txt")
    with open(txt_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    pattern = r'(Chapter\s+(?:One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten)\b[^\n]*)'
    splits = list(re.finditer(pattern, raw))
    
    end_idx = raw.find('*** END OF THE PROJECT GUTENBERG EBOOK')
    if end_idx == -1:
        end_idx = raw.find('End of the Project Gutenberg')

    ch_titles = [
        "Ch_01_Arrest",
        "Ch_02_First_Cross_Examination",
        "Ch_03_In_The_Empty_Courtroom",
        "Ch_04_Miss_Buerstners_Friend",
        "Ch_05_The_Whip_Man",
        "Ch_06_Ks_Uncle_Leni",
        "Ch_07_Lawyer_Manufacturer_Painter",
        "Ch_08_Block_The_Tradesman",
        "Ch_09_In_The_Cathedral",
        "Ch_10_End"
    ]

    font_body = ImageFont.truetype(FONT_EN_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    
    book_dir = os.path.join(OUT_DIR, "05_Literary_Classics", "02_The_Trial")
    total_book_pages = 0

    for i in range(len(splits)):
        s_pos = splits[i].start()
        e_pos = splits[i+1].start() if i+1 < len(splits) else end_idx
        ch_text = raw[s_pos:e_pos].strip()
        paras = clean_en_text(ch_text)
        pages = paginate_en_chapter(paras, font_body)
        
        ch_folder = ch_titles[i] if i < len(ch_titles) else f"Ch_{i+1:02d}"
        ch_dir = os.path.join(book_dir, ch_folder)
        ch_name_clean = ch_folder.replace('_', ' ').replace('Ch ', 'CH. ')
        rendered = render_en_pages(pages, ch_dir, f"THE TRIAL • {ch_name_clean}", font_body, font_head, font_foot)
        total_book_pages += rendered
        print(f"  [+] {ch_folder}: {rendered} pages")

    print(f"-> The Trial complete: {total_book_pages} total pages.")

def extract_epub_pages_text(epub_path, start_page, end_page):
    texts = []
    with zipfile.ZipFile(epub_path) as z:
        for p_num in range(start_page, end_page + 1):
            name = f"EPUB/page_{p_num}.html"
            if name in z.namelist():
                soup = BeautifulSoup(z.read(name), 'html.parser')
                p_text = soup.get_text().strip()
                # Remove leading 'Page X' line
                p_text = re.sub(r'^Page\s+\d+\s+', '', p_text)
                if p_text:
                    texts.append(p_text)
    return '\n\n'.join(texts)

def build_atomic_habits():
    print("\n--- Processing Atomic Habits by James Clear ---")
    epub_path = os.path.join(RAW_DIR, "atomic_habits_retail.epub")
    
    chapters = [
        ("Ch_00_Introduction_My_Story", 7, 15),
        ("Ch_01_The_Surprising_Power_Of_Atomic_Habits", 16, 29),
        ("Ch_02_How_Your_Habits_Shape_Your_Identity", 30, 41),
        ("Ch_03_How_To_Build_Better_Habits_In_4_Steps", 42, 54),
        ("Ch_04_The_Man_Who_Didnt_Look_Right", 55, 62),
        ("Ch_05_The_Best_Way_To_Start_A_New_Habit", 63, 73),
        ("Ch_06_Motivation_Is_Overrated", 74, 82),
        ("Ch_07_The_Secret_To_Self_Control", 83, 88),
        ("Ch_08_How_To_Make_A_Habit_Irresistible", 89, 98),
        ("Ch_09_Role_Of_Family_And_Friends", 99, 107),
        ("Ch_10_Causes_Of_Your_Bad_Habits", 108, 117),
        ("Ch_11_Walk_Slowly_But_Never_Backward", 118, 124),
        ("Ch_12_The_Law_Of_Least_Effort", 125, 133),
        ("Ch_13_The_Two_Minute_Rule", 134, 141),
        ("Ch_14_Make_Good_Habits_Inevitable", 142, 150),
        ("Ch_15_Cardinal_Rule_Of_Behavior_Change", 151, 159),
        ("Ch_16_How_To_Stick_With_Good_Habits", 160, 168),
        ("Ch_17_How_An_Accountability_Partner_Helps", 169, 176),
        ("Ch_18_The_Truth_About_Talent", 177, 186),
        ("Ch_19_The_Goldilocks_Rule", 187, 193),
        ("Ch_20_The_Downside_Of_Creating_Good_Habits", 194, 203),
        ("Ch_21_Conclusion_Results_That_Last", 204, 220)
    ]

    font_body = ImageFont.truetype(FONT_EN_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    
    book_dir = os.path.join(OUT_DIR, "02_Productivity_And_Finance", "01_Atomic_Habits")
    total_book_pages = 0

    for ch_folder, sp, ep in chapters:
        raw_text = extract_epub_pages_text(epub_path, sp, ep)
        paras = clean_en_text(raw_text)
        pages = paginate_en_chapter(paras, font_body)
        ch_dir = os.path.join(book_dir, ch_folder)
        ch_name_clean = ch_folder.replace('_', ' ').replace('Ch ', 'CH. ')
        rendered = render_en_pages(pages, ch_dir, f"ATOMIC HABITS • {ch_name_clean}", font_body, font_head, font_foot)
        total_book_pages += rendered
        print(f"  [+] {ch_folder}: {rendered} pages")

    print(f"-> Atomic Habits complete: {total_book_pages} total pages.")

def build_psychology_of_money():
    print("\n--- Processing The Psychology of Money by Morgan Housel ---")
    epub_path = os.path.join(RAW_DIR, "psychology_of_money_retail.epub")
    
    chapters = [
        ("Ch_00_Introduction", 9, 16),
        ("Ch_01_No_Ones_Crazy", 17, 29),
        ("Ch_02_Luck_And_Risk", 30, 40),
        ("Ch_03_Never_Enough", 41, 50),
        ("Ch_04_Confounding_Compounding", 51, 60),
        ("Ch_05_Getting_Wealthy_Vs_Staying_Wealthy", 61, 72),
        ("Ch_06_Tails_You_Win", 73, 83),
        ("Ch_07_Freedom", 84, 92),
        ("Ch_08_Man_In_The_Car_Paradox", 93, 95),
        ("Ch_09_Wealth_Is_What_You_Dont_See", 96, 100),
        ("Ch_10_Save_Money", 101, 109),
        ("Ch_11_Reasonable_Over_Rational", 110, 117),
        ("Ch_12_Surprise", 118, 131),
        ("Ch_13_Room_For_Error", 132, 142),
        ("Ch_14_Youll_Change", 143, 149),
        ("Ch_15_Nothings_Free", 150, 158),
        ("Ch_16_You_And_Me", 159, 165),
        ("Ch_17_The_Seduction_Of_Pessimism", 166, 178),
        ("Ch_18_When_Youll_Believe_Anything", 179, 191),
        ("Ch_19_All_Together_Now", 192, 198),
        ("Ch_20_Confessions", 199, 206),
        ("Ch_21_Postscript_Consumer_History", 207, 225)
    ]

    font_body = ImageFont.truetype(FONT_EN_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    
    book_dir = os.path.join(OUT_DIR, "02_Productivity_And_Finance", "02_The_Psychology_Of_Money")
    total_book_pages = 0

    for ch_folder, sp, ep in chapters:
        raw_text = extract_epub_pages_text(epub_path, sp, ep)
        paras = clean_en_text(raw_text)
        pages = paginate_en_chapter(paras, font_body)
        ch_dir = os.path.join(book_dir, ch_folder)
        ch_name_clean = ch_folder.replace('_', ' ').replace('Ch ', 'CH. ')
        rendered = render_en_pages(pages, ch_dir, f"PSYCHOLOGY OF MONEY • {ch_name_clean}", font_body, font_head, font_foot)
        total_book_pages += rendered
        print(f"  [+] {ch_folder}: {rendered} pages")

    print(f"-> The Psychology of Money complete: {total_book_pages} total pages.")

def build_how_to_win_friends():
    print("\n--- Processing How to Win Friends and Influence People by Dale Carnegie ---")
    epub_path = os.path.join(RAW_DIR, "how_to_win_friends.epub")
    
    chapters = [
        ("Ch_00_Biographical_Sketch_Of_Dale_Carnegie", 4, 13),
        ("Ch_01_How_This_Book_Was_Written", 14, 19),
        ("Ch_02_Nine_Suggestions_To_Get_The_Most", 20, 23),
        ("Ch_03_Part1_1_If_You_Want_To_Gather_Honey", 24, 35),
        ("Ch_04_Part1_2_The_Big_Secret_Of_Dealing_With_People", 36, 46),
        ("Ch_05_Part1_3_He_Who_Can_Do_This_Has_The_World", 47, 63),
        ("Ch_06_Part2_1_Do_This_And_Youll_Be_Welcome", 64, 73),
        ("Ch_07_Part2_2_A_Simple_Way_To_Make_First_Impression", 74, 80),
        ("Ch_08_Part2_3_If_You_Dont_Do_This_Trouble", 81, 87),
        ("Ch_09_Part2_4_Easy_Way_To_Be_Good_Conversationalist", 88, 95),
        ("Ch_10_Part2_5_How_To_Interest_People", 96, 99),
        ("Ch_11_Part2_6_How_To_Make_People_Like_You", 100, 110),
        ("Ch_12_Part3_1_You_Cant_Win_An_Argument", 111, 116),
        ("Ch_13_Part3_2_A_Sure_Way_Of_Making_Enemies", 117, 125),
        ("Ch_14_Part3_3_If_Youre_Wrong_Admit_It", 126, 132),
        ("Ch_15_Part3_4_A_Drop_Of_Honey", 133, 139),
        ("Ch_16_Part3_5_The_Secret_Of_Socrates", 140, 144),
        ("Ch_17_Part3_6_The_Safety_Valve_In_Complaints", 145, 148),
        ("Ch_18_Part3_7_How_To_Get_Cooperation", 149, 153),
        ("Ch_19_Part3_8_A_Formula_That_Works_Wonders", 154, 157),
        ("Ch_20_Part3_9_What_Everybody_Wants", 158, 164),
        ("Ch_21_Part3_10_An_Appeal_Everybody_Likes", 165, 169),
        ("Ch_22_Part3_11_The_Movies_Do_It_Tv_Does_It", 170, 173),
        ("Ch_23_Part3_12_When_Nothing_Else_Works", 174, 177),
        ("Ch_24_Part4_1_If_You_Must_Find_Fault", 178, 182),
        ("Ch_25_Part4_2_How_To_Criticize_And_Not_Be_Hated", 183, 185),
        ("Ch_26_Part4_3_Talk_About_Your_Own_Mistakes_First", 186, 189),
        ("Ch_27_Part4_4_No_One_Likes_To_Take_Orders", 190, 191),
        ("Ch_28_Part4_5_Let_The_Other_Person_Save_Face", 192, 194),
        ("Ch_29_Part4_6_How_To_Spur_People_On_To_Success", 195, 198),
        ("Ch_30_Part4_7_Give_A_Dog_A_Good_Name", 199, 202),
        ("Ch_31_Part4_8_Make_The_Fault_Seem_Easy_To_Correct", 203, 206),
        ("Ch_32_Part4_9_Making_People_Glad_To_Do_What_You_Want", 207, 214)
    ]

    font_body = ImageFont.truetype(FONT_EN_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    
    book_dir = os.path.join(OUT_DIR, "02_Productivity_And_Finance", "03_How_To_Win_Friends_And_Influence_People")
    total_book_pages = 0

    for ch_folder, sp, ep in chapters:
        raw_text = extract_epub_pages_text(epub_path, sp, ep)
        paras = clean_en_text(raw_text)
        pages = paginate_en_chapter(paras, font_body)
        ch_dir = os.path.join(book_dir, ch_folder)
        ch_name_clean = ch_folder.replace('_', ' ').replace('Ch ', 'CH. ')
        rendered = render_en_pages(pages, ch_dir, f"HOW TO WIN FRIENDS • {ch_name_clean}", font_body, font_head, font_foot)
        total_book_pages += rendered
        print(f"  [+] {ch_folder}: {rendered} pages")

    print(f"-> How to Win Friends complete: {total_book_pages} total pages.")

def to_ar_num(num):
    ar_digits = '٠١٢٣٤٥٦٧٨٩'
    return ''.join(ar_digits[int(d)] for d in str(num))

def build_holy_quran_arabic():
    print("\n--- Processing The Holy Quran (Arabic Text) ---")
    if not HAS_ARABIC:
        print("Error: arabic_reshaper or python-bidi not installed!")
        return

    quran_path = os.path.join(RAW_DIR, "quran.json")
    with open(quran_path, 'r', encoding='utf-8') as f:
        surahs = json.load(f)

    font_ar = ImageFont.truetype(FONT_AR_BODY_PATH, 18)
    font_head = ImageFont.truetype(FONT_AR_BODY_PATH, 14)
    font_foot = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    
    ar_reshaper = arabic_reshaper.ArabicReshaper({
        'delete_harakat': False,
        'support_ligatures': True,
    })
    
    dummy_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(dummy_img)

    book_dir = os.path.join(OUT_DIR, "01_Quran_And_Tafsir", "01_The_Holy_Quran_Arabic")
    os.makedirs(book_dir, exist_ok=True)
    total_quran_pages = 0

    for surah in surahs:
        s_id = surah['id']
        s_name_ar = surah['name']
        s_translit = surah['transliteration'].replace("'", "").replace(" ", "_")
        folder_name = f"Surah_{s_id:03d}_{s_translit}"
        ch_dir = os.path.join(book_dir, folder_name)
        os.makedirs(ch_dir, exist_ok=True)

        # Build full continuous text with authentic ornate Ayah markers ﴿١﴾
        full_text = []
        if s_id != 9 and s_id != 1:
            full_text.append("بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ")

        for v in surah['verses']:
            full_text.append(f"{v['text']} ﴿{to_ar_num(v['id'])}﴾")

        words = ' '.join(full_text).split()

        # Word wrap lines
        lines = []
        cur_words = []
        for w in words:
            test_str = ' '.join(cur_words + [w])
            reshaped = ar_reshaper.reshape(test_str)
            bidi_str = get_display(reshaped)
            bbox = draw.textbbox((0, 0), bidi_str, font=font_ar)
            if (bbox[2] - bbox[0]) <= USABLE_WIDTH:
                cur_words.append(w)
            else:
                if cur_words:
                    lines.append(' '.join(cur_words))
                    cur_words = [w]
                else:
                    lines.append(w)
                    cur_words = []
        if cur_words:
            lines.append(' '.join(cur_words))

        # 6 lines per page for optimal Tashkeel vertical breathing room in 240x280
        lines_per_page = 6
        pages = [lines[i:i+lines_per_page] for i in range(0, len(lines), lines_per_page)]
        total_pages = len(pages)
        total_quran_pages += total_pages

        # Render pages
        header_raw = f"سُورَةُ {s_name_ar} • {surah['transliteration']}"
        reshaped_h = ar_reshaper.reshape(header_raw)
        bidi_h = get_display(reshaped_h)

        for p_idx, page_lines in enumerate(pages):
            page_num = p_idx + 1
            out_path = os.path.join(ch_dir, f"page_{page_num:03d}.jpg")

            img = Image.new('RGB', (WIDTH, HEIGHT), color=(255, 255, 255))
            draw_p = ImageDraw.Draw(img)

            # Header
            bbox_h = draw_p.textbbox((0, 0), bidi_h, font=font_head)
            w_h = bbox_h[2] - bbox_h[0]
            draw_p.text(((WIDTH - w_h) // 2, HEADER_Y), bidi_h, fill=(80, 80, 80), font=font_head)
            draw_p.line([(12, HEADER_LINE_Y), (228, HEADER_LINE_Y)], fill=(225, 225, 225), width=1)

            # Body lines
            y = BODY_TOP_Y + 4
            for l in page_lines:
                reshaped_l = ar_reshaper.reshape(l)
                bidi_l = get_display(reshaped_l)
                bbox_l = draw_p.textbbox((0, 0), bidi_l, font=font_ar)
                w_l = bbox_l[2] - bbox_l[0]
                draw_p.text(((WIDTH - w_l) // 2, y), bidi_l, fill=(0, 0, 0), font=font_ar)
                y += 33

            # Footer
            draw_p.line([(12, FOOTER_LINE_Y), (228, FOOTER_LINE_Y)], fill=(225, 225, 225), width=1)
            foot_str = f"{page_num} / {total_pages}"
            bbox_foot = draw_p.textbbox((0, 0), foot_str, font=font_foot)
            foot_w = bbox_foot[2] - bbox_foot[0]
            draw_p.text(((WIDTH - foot_w) // 2, FOOTER_Y), foot_str, fill=(120, 120, 120), font=font_foot)

            img.save(out_path, "JPEG", quality=92)

        print(f"  [+] {folder_name}: {total_pages} pages")

    print(f"-> Holy Quran Arabic complete: {total_quran_pages} total pages.")

def build_holy_quran_english():
    print("\n--- Processing The Holy Quran (English Translation) ---")
    en_dir = os.path.join(RAW_DIR, "quran_en")
    
    font_body = ImageFont.truetype(FONT_EN_BODY_PATH, 14)
    font_head = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_EN_HEAD_PATH, 10)
    
    book_dir = os.path.join(OUT_DIR, "01_Quran_And_Tafsir", "02_The_Holy_Quran_English")
    os.makedirs(book_dir, exist_ok=True)
    total_quran_pages = 0

    for s_id in range(1, 115):
        json_path = os.path.join(en_dir, f"{s_id}.json")
        if not os.path.exists(json_path):
            continue
        with open(json_path, 'r', encoding='utf-8') as f:
            surah_data = json.load(f)

        s_translit = surah_data['transliteration'].replace("'", "").replace(" ", "_")
        folder_name = f"Surah_{s_id:03d}_{s_translit}"
        ch_dir = os.path.join(book_dir, folder_name)
        os.makedirs(ch_dir, exist_ok=True)

        # Build paragraphs (one per verse)
        paras = []
        for v in surah_data['verses']:
            paras.append(f"[{v['id']}] {v['translation']}")

        pages = paginate_en_chapter(paras, font_body, line_height=20, para_gap=6)
        header_title = f"QURAN • SURAH {s_id}: {surah_data['transliteration'].upper()}"
        rendered = render_en_pages(pages, ch_dir, header_title, font_body, font_head, font_foot)
        total_quran_pages += rendered
        print(f"  [+] {folder_name}: {rendered} pages")

    print(f"-> Holy Quran English complete: {total_quran_pages} total pages.")

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print("==================================================")
    print("      NOKIA 215 4G PORTRAIT BOOK PROCESSOR        ")
    print("==================================================")
    
    build_white_nights()
    build_the_trial()
    build_atomic_habits()
    build_psychology_of_money()
    build_how_to_win_friends()
    build_holy_quran_arabic()
    build_holy_quran_english()

    print("\n==================================================")
    print(" ALL 6 BOOKS + QURAN (ARABIC & ENGLISH) FINISHED! ")
    print("==================================================")

if __name__ == "__main__":
    main()
