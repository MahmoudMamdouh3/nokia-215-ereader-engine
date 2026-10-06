"""
Nokia 215 4G (2024) - Robert Greene Complete Collection Pipeline
Generates crisp 240x320 portrait JPEG images for all 7 books by Robert Greene:
1. The 48 Laws of Power (1998)
2. The Art of Seduction (2001)
3. The 33 Strategies of War (2006)
4. The 50th Law (2009)
5. Mastery (2012)
6. The Laws of Human Nature (2018)
7. The Daily Laws (2021)
"""

import os
import re
import sys
import zipfile
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import warnings
warnings.filterwarnings("ignore")

BASE_DIR = r"E:\nokia"
RAW_RG_DIR = os.path.join(BASE_DIR, "books_raw", "robert_greene")
OUT_RG_DIR = os.path.join(BASE_DIR, "books_out", "Robert_Greene")

FONT_BODY_PATH = r"C:\Windows\Fonts\georgia.ttf"
FONT_HEAD_PATH = r"C:\Windows\Fonts\arial.ttf"

WIDTH = 240
HEIGHT = 320
USABLE_WIDTH = 216
USABLE_HEIGHT = 256
HEADER_Y = 9
HEADER_LINE_Y = 25
BODY_TOP_Y = 33
FOOTER_LINE_Y = 297
FOOTER_Y = 302

def clean_text(text):
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = text.replace('”', '"').replace('“', '"').replace('’', "'").replace('‘', "'")
    text = text.replace('—', ' - ').replace('–', '-')
    text = re.sub(r'_[^_]+_', lambda m: m.group(0)[1:-1], text)
    paras = re.split(r'\n\s*\n', text)
    cleaned = []
    for p in paras:
        p_clean = ' '.join(p.split())
        if p_clean:
            cleaned.append(p_clean)
    return cleaned

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

def render_pages(pages, chapter_dir, header_title, font_body, font_head, font_foot):
    os.makedirs(chapter_dir, exist_ok=True)
    total_pages = len(pages)
    
    for p_idx, page_lines in enumerate(pages):
        page_num = p_idx + 1
        out_path = os.path.join(chapter_dir, f"page_{page_num:03d}.jpg")
            
        img = Image.new('RGB', (WIDTH, HEIGHT), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        # Header (truncate if too long)
        h_text = header_title
        bbox_head = draw.textbbox((0, 0), h_text, font=font_head)
        while (bbox_head[2] - bbox_head[0]) > (USABLE_WIDTH + 6) and len(h_text) > 10:
            h_text = h_text[:-4] + "..."
            bbox_head = draw.textbbox((0, 0), h_text, font=font_head)
            
        draw.text((12, HEADER_Y), h_text, fill=(100, 100, 100), font=font_head)
        draw.line([(12, HEADER_LINE_Y), (228, HEADER_LINE_Y)], fill=(225, 225, 225), width=1)
        
        # Body text
        y = BODY_TOP_Y
        for line, is_para_start in page_lines:
            if is_para_start:
                y += 7
            draw.text((12, y), line, fill=(15, 15, 15), font=font_body)
            y += 21
            
        # Footer
        draw.line([(12, FOOTER_LINE_Y), (228, FOOTER_LINE_Y)], fill=(225, 225, 225), width=1)
        foot_str = f"{page_num} / {total_pages}"
        bbox_foot = draw.textbbox((0, 0), foot_str, font=font_foot)
        foot_w = bbox_foot[2] - bbox_foot[0]
        draw.text(((WIDTH - foot_w) // 2, FOOTER_Y), foot_str, fill=(120, 120, 120), font=font_foot)
        
        img.save(out_path, "JPEG", quality=92)
    return total_pages

def extract_epub_range(epub_path, start_page, end_page):
    texts = []
    with zipfile.ZipFile(epub_path) as z:
        for p_num in range(start_page, end_page + 1):
            name = f"EPUB/page_{p_num}.html"
            if name in z.namelist():
                soup = BeautifulSoup(z.read(name), 'html.parser')
                p_text = soup.get_text().strip()
                p_text = re.sub(r'^Page\s+\d+\s+', '', p_text)
                if p_text:
                    texts.append(p_text)
    return '\n\n'.join(texts)

def build_50th_law():
    print("\n--- Processing The 50th Law (2009) ---")
    epub_path = os.path.join(RAW_RG_DIR, "04_50th_law.epub")
    chapters = [
        ("Ch_00_Foreword_And_Introduction", 2, 22),
        ("Ch_01_See_Things_For_What_They_Are_Intense_Realism", 23, 36),
        ("Ch_02_Make_Everything_Your_Own_Self_Reliance", 37, 50),
        ("Ch_03_Turn_Shit_Into_Sugar_Opportunism", 51, 64),
        ("Ch_04_Keep_Moving_Calculated_Momentum", 65, 81),
        ("Ch_05_Know_When_To_Be_Bad_Aggression", 82, 100),
        ("Ch_06_Lead_From_The_Front_Authority", 101, 118),
        ("Ch_07_Know_Your_Environment_Connection", 119, 136),
        ("Ch_08_Respect_The_Process_Mastery", 137, 155),
        ("Ch_09_Push_Beyond_Your_Limits_Self_Belief", 156, 175),
        ("Ch_10_Confront_Your_Mortality_The_Sublime", 176, 195)
    ]
    
    font_body = ImageFont.truetype(FONT_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_HEAD_PATH, 10)
    book_dir = os.path.join(OUT_RG_DIR, "04_The_50th_Law")
    total_pages = 0
    
    for ch_name, sp, ep in chapters:
        text = extract_epub_range(epub_path, sp, ep)
        paras = clean_text(text)
        pages = paginate_chapter(paras, font_body)
        ch_dir = os.path.join(book_dir, ch_name)
        title = "50TH LAW • " + ch_name.replace("_", " ")
        cnt = render_pages(pages, ch_dir, title, font_body, font_head, font_foot)
        total_pages += cnt
        print(f"  [+] {ch_name}: {cnt} pages")
    print(f"-> The 50th Law complete: {total_pages} total pages.")

def build_mastery():
    print("\n--- Processing Mastery (2012) ---")
    epub_path = os.path.join(RAW_RG_DIR, "05_mastery.epub")
    chapters = [
        ("Ch_00_Introduction_The_Ultimate_Power", 5, 33),
        ("Ch_01_Discover_Your_Calling_The_Lifes_Task", 34, 60),
        ("Ch_02_Submit_To_Reality_The_Ideal_Apprenticeship", 61, 134),
        ("Ch_03_Absorb_The_Masters_Power_The_Mentor_Dynamic", 135, 175),
        ("Ch_04_See_People_As_They_Are_Social_Intelligence", 176, 215),
        ("Ch_05_Awaken_The_Dimensional_Mind_Creative_Active", 216, 253),
        ("Ch_06_Fuse_The_Intuitive_With_The_Rational_Mastery", 254, 335)
    ]
    font_body = ImageFont.truetype(FONT_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_HEAD_PATH, 10)
    book_dir = os.path.join(OUT_RG_DIR, "05_Mastery")
    total_pages = 0
    
    for ch_name, sp, ep in chapters:
        text = extract_epub_range(epub_path, sp, ep)
        paras = clean_text(text)
        pages = paginate_chapter(paras, font_body)
        ch_dir = os.path.join(book_dir, ch_name)
        title = "MASTERY • " + ch_name.replace("_", " ")
        cnt = render_pages(pages, ch_dir, title, font_body, font_head, font_foot)
        total_pages += cnt
        print(f"  [+] {ch_name}: {cnt} pages")
    print(f"-> Mastery complete: {total_pages} total pages.")

def build_laws_of_human_nature():
    print("\n--- Processing The Laws of Human Nature (2018) ---")
    epub_path = os.path.join(RAW_RG_DIR, "06_laws_of_human_nature.epub")
    laws = [
        ("Law_00_Introduction", 5, 20),
        ("Law_01_Master_Your_Emotional_Self_Irrationality", 21, 51),
        ("Law_02_Transform_Self_Love_Into_Empathy_Narcissism", 52, 84),
        ("Law_03_See_Through_Peoples_Masks_Role_Playing", 85, 116),
        ("Law_04_Determine_Strength_Of_Character_Compulsion", 117, 147),
        ("Law_05_Become_An_Elusive_Object_Of_Desire_Covetousness", 148, 167),
        ("Law_06_Elevate_Your_Perspective_Shortsightedness", 168, 190),
        ("Law_07_Soften_Peoples_Resistance_Defensiveness", 191, 223),
        ("Law_08_Change_Your_Circumstances_Self_Delusion", 224, 254),
        ("Law_09_Confront_Your_Dark_Side_Repression", 255, 287),
        ("Law_10_Beware_The_Fragile_Ego_Envy", 288, 320),
        ("Law_11_Know_Your_Limits_Grandiosity", 321, 351),
        ("Law_12_Reconnect_To_The_Masculine_Or_Feminine", 352, 390),
        ("Law_13_Advance_With_A_Sense_Of_Purpose_Aimlessness", 391, 428),
        ("Law_14_Resist_Downward_Pull_Of_Group_Conformity", 429, 479),
        ("Law_15_Make_Them_Want_To_Follow_You_Fickleness", 480, 520),
        ("Law_16_See_The_Hostility_Behind_Facade_Aggression", 521, 568),
        ("Law_17_Seize_The_Historical_Moment_Generational_Myopia", 569, 615),
        ("Law_18_Meditate_On_Common_Mortality_Death_Denial", 616, 675)
    ]
    font_body = ImageFont.truetype(FONT_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_HEAD_PATH, 10)
    book_dir = os.path.join(OUT_RG_DIR, "06_The_Laws_Of_Human_Nature")
    total_pages = 0
    
    for ch_name, sp, ep in laws:
        text = extract_epub_range(epub_path, sp, ep)
        paras = clean_text(text)
        pages = paginate_chapter(paras, font_body)
        ch_dir = os.path.join(book_dir, ch_name)
        title = "HUMAN NATURE • " + ch_name.replace("_", " ")
        cnt = render_pages(pages, ch_dir, title, font_body, font_head, font_foot)
        total_pages += cnt
        print(f"  [+] {ch_name}: {cnt} pages")
    print(f"-> The Laws of Human Nature complete: {total_pages} total pages.")

def build_daily_laws():
    print("\n--- Processing The Daily Laws (2021) ---")
    epub_path = os.path.join(RAW_RG_DIR, "07_daily_laws.epub")
    months = [
        ("Month_01_January_Your_Lifes_Task", 13, 50),
        ("Month_02_February_The_Ideal_Apprenticeship", 51, 85),
        ("Month_03_March_The_Master_At_Work", 86, 122),
        ("Month_04_April_The_Perfect_Courtier", 123, 160),
        ("Month_05_May_The_Corrupt_And_The_Cruel", 161, 198),
        ("Month_06_June_The_Divine_Art_Of_War", 199, 236),
        ("Month_07_July_The_Seductive_Mind", 237, 274),
        ("Month_08_August_The_Master_Persuader", 275, 312),
        ("Month_09_September_The_Grand_Strategist", 313, 350),
        ("Month_10_October_The_Emotional_Self", 351, 388),
        ("Month_11_November_The_Rational_Human", 389, 426),
        ("Month_12_December_The_Cosmic_Sublime", 427, 485)
    ]
    font_body = ImageFont.truetype(FONT_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_HEAD_PATH, 10)
    book_dir = os.path.join(OUT_RG_DIR, "07_The_Daily_Laws")
    total_pages = 0
    
    for ch_name, sp, ep in months:
        text = extract_epub_range(epub_path, sp, ep)
        paras = clean_text(text)
        pages = paginate_chapter(paras, font_body)
        ch_dir = os.path.join(book_dir, ch_name)
        title = "DAILY LAWS • " + ch_name.replace("_", " ")
        cnt = render_pages(pages, ch_dir, title, font_body, font_head, font_foot)
        total_pages += cnt
        print(f"  [+] {ch_name}: {cnt} pages")
    print(f"-> The Daily Laws complete: {total_pages} total pages.")

def build_48_laws_of_power():
    print("\n--- Processing The 48 Laws of Power (1998) ---")
    epub_path = os.path.join(RAW_RG_DIR, "01_48_laws_of_power.epub")
    
    # 48 laws page mapping (approx 12-15 pages per law)
    # Total pages: 709. Preface is pages 10-31.
    laws_sp = [
        ("Ch_00_Preface", 10, 31),
        ("Law_01_Never_Outshine_The_Master", 32, 43),
        ("Law_02_Never_Put_Too_Much_Trust_In_Friends", 44, 53),
        ("Law_03_Conceal_Your_Intentions", 54, 73),
        ("Law_04_Always_Say_Less_Than_Necessary", 74, 82),
        ("Law_05_So_Much_Depends_On_Reputation", 83, 94),
        ("Law_06_Court_Attention_At_All_Cost", 95, 108),
        ("Law_07_Get_Others_To_Do_The_Work_For_You", 109, 117),
        ("Law_08_Make_Other_People_Come_To_You", 118, 126),
        ("Law_09_Win_Through_Your_Actions_Never_Argument", 127, 135),
        ("Law_10_Infection_Avoid_The_Unhappy_And_Unlucky", 136, 144),
        ("Law_11_Learn_To_Keep_People_Dependent_On_You", 145, 154),
        ("Law_12_Use_Selective_Honesty_To_Disarm_Victim", 155, 163),
        ("Law_13_When_Asking_For_Help_Appeal_To_Self_Interest", 164, 172),
        ("Law_14_Pose_As_A_Friend_Work_As_A_Spy", 173, 179),
        ("Law_15_Crush_Your_Enemy_Totally", 180, 190),
        ("Law_16_Use_Absence_To_Increase_Respect_And_Honor", 191, 201),
        ("Law_17_Keep_Others_In_Suspended_Terror", 202, 210),
        ("Law_18_Do_Not_Build_Fortresses_To_Protect_Yourself", 211, 221),
        ("Law_19_Know_Who_Youre_Dealing_With", 222, 232),
        ("Law_20_Do_Not_Commit_To_Anyone", 233, 248),
        ("Law_21_Play_A_Sucker_To_Catch_A_Sucker", 249, 257),
        ("Law_22_Use_The_Surrender_Tactic", 258, 267),
        ("Law_23_Concentrate_Your_Forces", 268, 276),
        ("Law_24_Play_The_Perfect_Courtier", 277, 292),
        ("Law_25_Recreate_Yourself", 293, 303),
        ("Law_26_Keep_Your_Hands_Clean", 304, 319),
        ("Law_27_Play_On_Peoples_Need_To_Believe", 320, 331),
        ("Law_28_Enter_Action_With_Boldness", 332, 344),
        ("Law_29_Plan_All_The_Way_To_The_End", 345, 355),
        ("Law_30_Make_Your_Accomplishments_Seem_Effortless", 356, 368),
        ("Law_31_Control_The_Options", 369, 381),
        ("Law_32_Play_To_Peoples_Fantasies", 382, 391),
        ("Law_33_Discover_Each_Mans_Thumbscrew", 392, 404),
        ("Law_34_Be_Royal_In_Your_Own_Fashion", 405, 417),
        ("Law_35_Master_The_Art_Of_Timing", 418, 429),
        ("Law_36_Disdain_Things_You_Cannot_Have", 430, 439),
        ("Law_37_Create_Compelling_Spectacles", 440, 449),
        ("Law_38_Think_As_You_Like_But_Behave_Like_Others", 450, 461),
        ("Law_39_Stir_Up_Waters_To_Catch_Fish", 462, 471),
        ("Law_40_Despise_The_Free_Lunch", 472, 488),
        ("Law_41_Avoid_Stepping_Into_A_Great_Mans_Shoes", 489, 502),
        ("Law_42_Strike_The_Shepherd_And_The_Sheep_Scatter", 503, 513),
        ("Law_43_Work_On_The_Hearts_And_Minds_Of_Others", 514, 526),
        ("Law_44_Disarm_And_Infuriate_With_The_Mirror_Effect", 527, 547),
        ("Law_45_Preach_The_Need_For_Change_Never_Reform_Too_Much", 548, 558),
        ("Law_46_Never_Appear_Too_Perfect", 559, 570),
        ("Law_47_Do_Not_Go_Past_The_Mark_You_Aimed_For", 571, 581),
        ("Law_48_Assume_Formlessness", 582, 600)
    ]
    font_body = ImageFont.truetype(FONT_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_HEAD_PATH, 10)
    book_dir = os.path.join(OUT_RG_DIR, "01_The_48_Laws_Of_Power")
    total_pages = 0
    
    for ch_name, sp, ep in laws_sp:
        text = extract_epub_range(epub_path, sp, ep)
        paras = clean_text(text)
        pages = paginate_chapter(paras, font_body)
        ch_dir = os.path.join(book_dir, ch_name)
        title = "48 LAWS • " + ch_name.replace("_", " ")
        cnt = render_pages(pages, ch_dir, title, font_body, font_head, font_foot)
        total_pages += cnt
        print(f"  [+] {ch_name}: {cnt} pages")
    print(f"-> The 48 Laws of Power complete: {total_pages} total pages.")

def build_art_of_seduction():
    print("\n--- Processing The Art of Seduction (2001) ---")
    epub_path = os.path.join(RAW_RG_DIR, "02_art_of_seduction.epub")
    sections = [
        ("Ch_00_Preface_And_Introduction", 5, 25),
        ("Part1_01_The_Siren", 26, 42),
        ("Part1_02_The_Rake", 43, 58),
        ("Part1_03_The_Ideal_Lover", 59, 74),
        ("Part1_04_The_Dandy", 75, 90),
        ("Part1_05_The_Natural", 91, 107),
        ("Part1_06_The_Coquette", 108, 124),
        ("Part1_07_The_Charmer", 125, 140),
        ("Part1_08_The_Charismatic", 141, 160),
        ("Part1_09_The_Star", 161, 178),
        ("Part1_10_The_Anti_Seducer", 179, 193),
        ("Part2_01_Choose_The_Right_Victim", 194, 203),
        ("Part2_02_Create_A_False_Sense_Of_Security", 204, 211),
        ("Part2_03_Send_Mixed_Signals", 212, 221),
        ("Part2_04_Appear_To_Be_An_Object_Of_Desire", 222, 231),
        ("Part2_05_Create_A_Need_Stir_Anxiety", 232, 241),
        ("Part2_06_Master_The_Art_Of_Insinuation", 242, 255),
        ("Part2_07_Enter_Their_Spirit", 256, 267),
        ("Part2_08_Create_Temptation", 268, 277),
        ("Part2_09_Keep_Them_In_Suspense", 278, 287),
        ("Part2_10_Use_Demonic_Power_Of_Words", 288, 299),
        ("Part2_11_Pay_Attention_To_Detail", 300, 311),
        ("Part2_12_Poeticize_Your_Presence", 312, 323),
        ("Part2_13_Disarm_Through_Strategic_Weakness", 324, 335),
        ("Part2_14_Confuse_Desire_And_Reality", 336, 347),
        ("Part2_15_Isolate_The_Victim", 348, 359),
        ("Part2_16_Prove_Yourself", 360, 371),
        ("Part2_17_Effect_A_Regression", 372, 385),
        ("Part2_18_Stir_The_Transgressive_And_Taboo", 386, 397),
        ("Part2_19_Use_Spiritual_Lures", 398, 408),
        ("Part2_20_Mix_Pleasure_With_Pain", 409, 418),
        ("Part2_21_Give_Them_Space_To_Fall", 419, 426),
        ("Part2_22_Use_Physical_Lures", 427, 432),
        ("Part2_23_Master_The_Art_Of_The_Bold_Move", 433, 437)
    ]
    font_body = ImageFont.truetype(FONT_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_HEAD_PATH, 10)
    book_dir = os.path.join(OUT_RG_DIR, "02_The_Art_Of_Seduction")
    total_pages = 0
    
    for ch_name, sp, ep in sections:
        text = extract_epub_range(epub_path, sp, ep)
        paras = clean_text(text)
        pages = paginate_chapter(paras, font_body)
        ch_dir = os.path.join(book_dir, ch_name)
        title = "SEDUCTION • " + ch_name.replace("_", " ")
        cnt = render_pages(pages, ch_dir, title, font_body, font_head, font_foot)
        total_pages += cnt
        print(f"  [+] {ch_name}: {cnt} pages")
    print(f"-> The Art of Seduction complete: {total_pages} total pages.")

def build_33_strategies_of_war():
    print("\n--- Processing The 33 Strategies of War (2006) ---")
    epub_path = os.path.join(RAW_RG_DIR, "03_33_strategies_of_war.epub")
    strategies = [
        ("Part1_01_Declare_War_On_Your_Enemies_Polarity", 26, 42),
        ("Part1_02_Do_Not_Fight_The_Last_War_Guerrilla", 43, 58),
        ("Part1_03_Amidst_Turmoil_Do_Not_Lose_Presence", 59, 75),
        ("Part1_04_Create_A_Sense_Of_Urgency_Death_Ground", 76, 94),
        ("Part2_05_Avoid_Traps_Of_Groupthink_Command_Control", 95, 110),
        ("Part2_06_Segment_Your_Forces_Controlled_Chaos", 111, 126),
        ("Part2_07_Transform_Your_War_Into_A_Crusade_Morale", 127, 145),
        ("Part3_08_Pick_Your_Battles_Carefully_Economy", 146, 160),
        ("Part3_09_Turn_The_Tables_The_Counterattack", 161, 175),
        ("Part3_10_Create_A_Threatening_Presence_Deterrence", 176, 190),
        ("Part3_11_Trade_Space_For_Time_Nonengagement", 191, 206),
        ("Part4_12_Lose_Battles_But_Win_The_War_Grand_Strategy", 207, 222),
        ("Part4_13_Know_Your_Enemy_Intelligence", 223, 238),
        ("Part4_14_Overwhelm_Resistance_With_Speed", 239, 252),
        ("Part4_15_Control_The_Dynamic_Forcing", 253, 268),
        ("Part4_16_Hit_Them_Where_It_Hurts_Center_Of_Gravity", 269, 283),
        ("Part4_17_Defeat_Them_In_Detail_Divide_And_Conquer", 284, 298),
        ("Part4_18_Expose_And_Attack_Soft_Flank_Turning", 299, 314),
        ("Part4_19_Envelop_The_Enemy_Annihilation", 315, 330),
        ("Part4_20_Maneuver_Them_Into_Weakness_Riposte", 331, 345),
        ("Part4_21_Negotiate_While_Advancing_War_Diplomacy", 346, 360),
        ("Part4_22_Know_How_To_End_Things_The_Exit_Strategy", 361, 393),
        ("Part5_23_Weave_A_Seamless_Blend_Of_Fact_And_Fiction", 394, 412),
        ("Part5_24_Take_The_Line_Of_Least_Expectation_Unorthodox", 413, 430),
        ("Part5_25_Occupy_The_Moral_High_Ground_Righteous", 431, 450),
        ("Part5_26_Deny_Them_Targets_The_Void", 451, 470),
        ("Part5_27_Seem_To_Work_For_Others_Alliance", 471, 490),
        ("Part5_28_Give_Your_Rivals_Rope_To_Hang_Themselves", 491, 510),
        ("Part5_29_Take_Small_Bites_Fait_Accompli", 511, 530),
        ("Part5_30_Penetrate_Their_Minds_Communication", 531, 550),
        ("Part5_31_Destroy_From_Within_The_Trojan_Horse", 551, 575),
        ("Part5_32_Seem_To_Yield_While_Dominating_Passive_Aggression", 576, 605),
        ("Part5_33_Sow_Uncertainty_And_Panic_Terror", 606, 644)
    ]
    font_body = ImageFont.truetype(FONT_BODY_PATH, 15)
    font_head = ImageFont.truetype(FONT_HEAD_PATH, 10)
    font_foot = ImageFont.truetype(FONT_HEAD_PATH, 10)
    book_dir = os.path.join(OUT_RG_DIR, "03_The_33_Strategies_Of_War")
    total_pages = 0
    
    for ch_name, sp, ep in strategies:
        text = extract_epub_range(epub_path, sp, ep)
        paras = clean_text(text)
        pages = paginate_chapter(paras, font_body)
        ch_dir = os.path.join(book_dir, ch_name)
        title = "33 STRATEGIES • " + ch_name.replace("_", " ")
        cnt = render_pages(pages, ch_dir, title, font_body, font_head, font_foot)
        total_pages += cnt
        print(f"  [+] {ch_name}: {cnt} pages")
    print(f"-> The 33 Strategies of War complete: {total_pages} total pages.")

def main():
    os.makedirs(OUT_RG_DIR, exist_ok=True)
    print("==================================================")
    print("     ROBERT GREENE COMPLETE WORKS PIPELINE        ")
    print("==================================================")
    
    build_48_laws_of_power()
    build_art_of_seduction()
    build_33_strategies_of_war()
    build_50th_law()
    build_mastery()
    build_laws_of_human_nature()
    build_daily_laws()

    print("\n==================================================")
    print(" ALL 7 ROBERT GREENE BOOKS SUCCESSFULLY FINISHED! ")
    print("==================================================")

if __name__ == "__main__":
    main()
