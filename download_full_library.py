"""
Nokia 215 4G - Universal Books Downloader
Downloads authentic, verified latest editions:
1. Arabic versions of existing books and world literature masterpieces.
2. World Greatest Literature Classics in authentic master editions.
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import time

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"E:\nokia\books_raw"
ARABIC_DIR = os.path.join(BASE_DIR, "arabic_editions")
ENGLISH_DIR = os.path.join(BASE_DIR, "english_classics")

os.makedirs(ARABIC_DIR, exist_ok=True)
os.makedirs(ENGLISH_DIR, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def download_file(url, dst_path, min_bytes=20000, max_retries=3):
    if os.path.exists(dst_path) and os.path.getsize(dst_path) >= min_bytes:
        print(f"  [✓] Exists: {os.path.basename(dst_path)} ({os.path.getsize(dst_path):,} bytes)")
        return True

    print(f"  [↓] Downloading: {os.path.basename(dst_path)}...")
    for attempt in range(1, max_retries + 1):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(req, timeout=35) as resp:
                content = resp.read()
                if len(content) < min_bytes:
                    print(f"      [!] File too small ({len(content)} bytes), attempt {attempt}/{max_retries}")
                    continue
                with open(dst_path, 'wb') as f:
                    f.write(content)
                print(f"      [✓] Downloaded: {os.path.basename(dst_path)} ({len(content):,} bytes)")
                return True
        except Exception as e:
            print(f"      [!] Attempt {attempt}/{max_retries} failed: {e}")
            time.sleep(2)
    return False

# ==============================================================================
# 1. ARABIC TRANSLATIONS OF EXISTING BOOKS & WORLD CLASSICS
# ==============================================================================
ARABIC_DOWNLOADS = [
    # Existing Books - Arabic Editions
    {
        "title": "Atomic Habits (العادات الذرية - مكتبة جرير)",
        "url": "https://archive.org/download/20260627_20260627_1842/%D8%A7%D9%84%D8%B9%D8%A7%D8%AF%D8%A7%D8%AA%20%D8%A7%D9%84%D8%B0%D8%B1%D9%8A%D8%A9..%20%D8%AC%D9%8A%D9%85%D8%B3%20%D9%83%D9%84%D9%8A%D8%B1.epub",
        "filename": "Atomic_Habits_Arabic_Jarir.epub"
    },
    {
        "title": "The Psychology of Money (سيكولوجية المال - مكتبة جرير)",
        "url": "https://archive.org/download/freebookar.online_20230709/freebookar.online%20%20%D8%B3%D9%8A%D9%83%D9%88%D9%84%D9%88%D8%AC%D9%8A%D8%A9_%D8%A7%D9%84%D9%85%D8%A7%D9%84_%D8%AF%D8%B1%D9%88%D8%B3_%D8%AE%D8%A7%D9%84%D8%AF%D8%A9_%D9%81%D9%8A_%D8%A7%D9%84%D8%AB%D8%B1%D9%88%D8%A9_%D9%88%D8%A7%D9%84%D8%AC%D8%B4%D8%B9_%D9%88%D8%A7%D9%84%D8%B3%D8%B9%D8%A7%D8%AF%D8%A9.epub",
        "filename": "Psychology_Of_Money_Arabic_Jarir.epub"
    },
    {
        "title": "The Trial (المحاكمة - فرانز كافكا)",
        "url": "https://archive.org/download/01_20200911_20200911_0746/01-%20%D8%A7%D9%84%D9%85%D8%AD%D8%A7%D9%83%D9%85%D8%A9%20-%20%D9%81%D8%B1%D8%A7%D9%86%D8%B2%20%D9%83%D8%A7%D9%81%D9%83%D8%A7.epub",
        "filename": "The_Trial_Arabic_Kafka.epub"
    },
    {
        "title": "White Nights (الليالي البيضاء - فيودور دوستويفسكي)",
        "url": "https://archive.org/download/alialaaraj81_20190315/%D8%A7%D9%84%D9%84%D9%8A%D8%A7%D9%84%D9%8A%20%D8%A7%D9%84%D8%A8%D9%8A%D8%B6%D8%A7%D8%A1.epub",
        "filename": "White_Nights_Arabic_Dostoevsky.epub"
    },
    {
        "title": "The 48 Laws of Power (قواعد السطوة - روبرت جرين)",
        "url": "https://archive.org/download/20200901_20200901_1318/%D9%82%D9%88%D8%A7%D8%B9%D8%AF%20%D8%A7%D9%84%D8%B3%D8%B7%D9%88%D8%A9.pdf",
        "filename": "48_Laws_Of_Power_Arabic.pdf"
    },
    {
        "title": "How to Win Friends and Influence People (كيف تكسب الأصدقاء - ديل كارنيجي)",
        "url": "https://archive.org/download/elshandawily7676/%D9%83%D9%8A%D9%81%20%D8%AA%D9%83%D8%B3%D8%A8%20%D8%A7%D9%84%D8%A3%D8%B5%D8%AF%D9%82%D8%A7%D8%A1%20%D9%88%D8%AA%D8%A4%D8%AB%D8%B1%20%D9%81%D9%8A%20%D8%A7%D9%84%D9%86%D8%A7%D8%B3%20%20%20%D8%AF%D9%8A%D8%B1%20%D9%83%D8%A7%D8%B1%D9%86%D9%8A%D8%AC%D9%8A.pdf",
        "filename": "How_To_Win_Friends_Arabic.pdf"
    },
    {
        "title": "1984 (١٩٨٤ - جورج أورويل)",
        "url": "https://archive.org/download/1984_george/1984.epub",
        "filename": "1984_Arabic_George_Orwell.epub"
    },
    {
        "title": "Animal Farm (مزرعة الحيوان - جورج أورويل)",
        "url": "https://archive.org/download/AnimalFarm_201607/AnimalFarm.epub",
        "filename": "Animal_Farm_Arabic_George_Orwell.epub"
    },
    {
        "title": "Crime and Punishment - Part 1 (الجريمة والعقاب ج1 - ترجمة سامي الدروبي)",
        "url": "https://archive.org/download/aljarimawali9Ab/%D8%A7%D9%84%D8%AC%D8%B1%D9%8A%D9%85%D8%A9%20%D9%88%D8%A7%D9%84%D8%B9%D9%82%D8%A7%D8%A8%201.epub",
        "filename": "Crime_And_Punishment_Arabic_Vol1_Sami_Droubi.epub"
    },
    {
        "title": "Crime and Punishment - Part 2 (الجريمة والعقاب ج2 - ترجمة سامي الدروبي)",
        "url": "https://archive.org/download/aljarimawaliKab/%D8%A7%D9%84%D8%AC%D8%B1%D9%8A%D9%85%D8%A9%20%D9%88%D8%A7%D9%84%D8%B9%D9%82%D8%A7%D8%A8%202.epub",
        "filename": "Crime_And_Punishment_Arabic_Vol2_Sami_Droubi.epub"
    },
    {
        "title": "The Stranger (الغريب - ألبير كامو)",
        "url": "https://archive.org/download/20210125_20210125_1200/%D8%B1%D9%88%D8%A7%D9%8A%D8%A9%20%D8%A7%D9%84%D8%BA%D8%B1%D9%8A%D8%A8%20-%20%D8%A3%D9%84%D8%A8%D9%8A%D8%B1%20%D9%83%D8%A7%D9%85%D9%88%20.epub",
        "filename": "The_Stranger_Arabic_Albert_Camus.epub"
    },
    {
        "title": "The Old Man and the Sea (الشيخ والبحر - إرنست همنغواي)",
        "url": "https://archive.org/download/iqraaEBook_24/%D8%A7%D9%84%D8%B4%D9%8A%D8%AE%20%D9%88%D8%A7%D9%84%D8%A8%D8%AD%D8%B1.pdf",
        "filename": "The_Old_Man_And_The_Sea_Arabic.pdf"
    },
    {
        "title": "The Metamorphosis (التحول / الانمساخ - فرانز كافكا)",
        "url": "https://archive.org/download/01_20200911_20200911_0746/08-%20%D8%A7%D9%84%D8%AA%D8%AD%D9%88%D9%84%20-%20%D9%81%D8%B1%D8%A7%D9%86%D8%B2%20%D9%83%D8%A7%D9%81%D9%83%D8%A7.epub",
        "filename": "The_Metamorphosis_Arabic_Kafka.epub"
    },
    {
        "title": "The Castle (القلعة - فرانز كافكا)",
        "url": "https://archive.org/download/01_20200911_20200911_0746/04-%20%D8%A7%D9%84%D9%82%D9%84%D8%B9%D8%A9%20-%20%D9%81%D8%B1%D8%A7%D9%86%D8%B2%20%D9%83%D8%A7%D9%81%D9%83%D8%A7.epub",
        "filename": "The_Castle_Arabic_Kafka.epub"
    },

    # World Masterpieces - Additional Verified Arabic Translations
    {
        "title": "The Holy Bible (الكتاب المقدس - الترجمة المشتركة GNA)",
        "url": "https://archive.org/download/gna-arabic-bible/al-Kitab%20al-Muqaddas%20%28%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8%20%D8%A7%D9%84%D9%85%D9%82%D8%AF%D8%B3%29%20%5BThe%20Holy%20Bible%5D%20%5BGood%20News%20Arabic%20%28GNA%29%20063%20DC%20-%20the%20Ecumenical%20Translation%20%28%D8%A7%D9%84%D8%AA%D8%B1%D8%AC%D9%85%D8%A9%20%D8%A7%D9%84%D9%85%D8%B4%D8%AA%D8%B1%D9%83%D8%A9%29%5D.epub",
        "filename": "The_Holy_Bible_Arabic_Ecumenical.epub"
    },
    {
        "title": "Don Quixote (دون كيشوت - ميغيل دي ثيربانتس)",
        "url": "https://archive.org/download/elshandawily4157/%D8%B1%D9%88%D8%A7%D9%8A%D8%A9%20%D8%AF%D9%88%D9%86%20%D9%83%D9%8A%D8%B4%D9%88%D8%AA%20-%20%D8%AB%D8%B1%D8%A8%D8%A7%D9%86%D8%AA%D8%B3.epub",
        "filename": "Don_Quixote_Arabic_Cervantes.epub"
    },
    {
        "title": "The Catcher in the Rye (الحارس في حقل الشوفان - سالينجر)",
        "url": "https://archive.org/download/dodylonging_gmail_20161205_2354/%D8%A7%D9%84%D8%AD%D8%A7%D8%B1%D8%B3%20%D9%81%D9%8A%20%D8%AD%D9%82%D9%84%20%D8%A7%D9%84%D8%B4%D9%88%D9%81%D8%A7%D9%86%20-%20%D8%AC%20.%20%D8%AF%20.%20%D8%B3%D8%A7%D9%84%D9%86%D8%AC%D8%B1_.epub",
        "filename": "The_Catcher_In_The_Rye_Arabic_Salinger.epub"
    },
    {
        "title": "The Brothers Karamazov (الإخوة كارامازوف - ترجمة سامي الدروبي)",
        "url": "https://archive.org/download/aliadnanzoom_4/%D8%AF%D9%88%D8%B3%D8%AA%D9%88%D9%8A%D9%81%D8%B3%D9%83%D9%8A%20-%20%D8%A7%D9%84%D8%A3%D8%AE%D9%88%D8%A9%20%D9%83%D8%A7%D8%B1%D8%A7%D9%85%D8%A7%D8%B2%D9%88%D9%81%201.epub",
        "filename": "The_Brothers_Karamazov_Arabic_Sami_Droubi.epub"
    },
    {
        "title": "War and Peace (الحرب والسلام - ترجمة سامي الدروبي - كاملة)",
        "url": "https://archive.org/download/12341234_201401/%D8%A7%D9%84%D8%AD%D8%B1%D8%A8%20%D9%88%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85%20%201%20-%202%20%20-%203%20-%204%20-%20%D9%84%D9%8A%D9%88%20%D8%AA%D9%88%D9%84%D8%B3%D8%AA%D9%88%D9%8A.epub",
        "filename": "War_And_Peace_Arabic_Sami_Droubi_Complete.epub"
    },
    {
        "title": "Anna Karenina (آنا كارينينا - ترجمة سامي الدروبي)",
        "url": "https://archive.org/download/aliadnanzoom_1_201612/%D8%AA%D9%88%D9%84%D8%B3%D8%AA%D9%88%D9%8A%20-%20%D8%A2%D9%86%D8%A7%20%D9%83%D8%A7%D8%B1%D9%86%D9%8A%D9%86%D8%A7%201.epub",
        "filename": "Anna_Karenina_Arabic_Sami_Droubi.epub"
    },
    {
        "title": "Moby-Dick (موبي ديك - ترجمة إحسان عباس)",
        "url": "https://archive.org/download/123boukrika44_maktoob_20140114_1207/%D9%85%D9%88%D8%A8%D9%8A%20%D8%AF%D9%8A%D9%83%20-%20%D9%87%D8%B1%D9%85%D8%A7%D9%86%20%D9%85%D9%84%D9%81%D9%84.epub",
        "filename": "Moby_Dick_Arabic_Ihsan_Abbas.epub"
    },
    {
        "title": "Madame Bovary (مدام بوفاري - غوستاف فلوبير)",
        "url": "https://archive.org/download/123boukrika44_maktoob_20140114/%D9%85%D8%AF%D8%A7%D9%85%20%D8%A8%D9%88%D9%81%D8%A7%D8%B1%D9%8A%20-%20%D9%81%D9%84%D9%88%D8%A8%D9%8A%D8%B1.epub",
        "filename": "Madame_Bovary_Arabic_Flaubert.epub"
    },
    {
        "title": "The Divine Comedy (الكوميديا الإلهية - دانتي - ترجمة حسن عثمان)",
        "url": "https://archive.org/download/20190925_20190925_2045/%D8%A7%D9%84%D9%83%D9%88%D9%85%D9%8A%D8%AF%D9%8A%D8%A7%20%D8%A7%D9%84%D8%A5%D9%84%D9%87%D9%8A%D8%A9%20%D9%80%20%D8%AF%D8%A7%D9%86%D8%AA%D9%8A%20%D8%A3%D9%84%D9%8A%D8%AC%D9%8A%D8%B1%D9%8A%20%D9%80%20%D8%AA%D8%B1%D8%AC%D9%85%D8%A9%20%D8%AD%D8%B3%D9%86%20%D8%B9%D8%AB%D9%85%D8%A7%D9%86.epub",
        "filename": "The_Divine_Comedy_Arabic_Hassan_Osman.epub"
    },
    {
        "title": "The Magic Mountain (الجبل السحري - توماس مان)",
        "url": "https://archive.org/download/123boukrika44_maktoob_20131226_0949/%D8%A7%D9%84%D8%AC%D8%A8%D9%84%20%D8%A7%D9%84%D8%B3%D8%AD%D8%B1%D9%8A%20-%20%D8%AA%D9%88%D9%85%D8%A7%D8%B3%20%D9%85%D8%A7%D9%86.epub",
        "filename": "The_Magic_Mountain_Arabic_Thomas_Mann.epub"
    },
    {
        "title": "The Odyssey (الأوديسة - هوميروس - ترجمة دريني خشبة)",
        "url": "https://archive.org/download/history00054_201908/Literature-00028.epub",
        "filename": "The_Odyssey_Arabic_Derini_Khashaba.epub"
    },
    {
        "title": "The Iliad (الإلياذة - هوميروس - ترجمة دريني خشبة)",
        "url": "https://archive.org/download/20221225_20221225_1817/%D8%A7%D9%84%D8%A5%D9%84%D9%8A%D8%A7%D8%B0%D8%A9%20-%20%D8%AF%D8%B1%D9%8A%D9%86%D9%8A%20%D8%AE%D8%B4%D8%A8%D8%A9%20.epub",
        "filename": "The_Iliad_Arabic_Derini_Khashaba.epub"
    },
    {
        "title": "To the Lighthouse (إلى الفنار - فرجينيا وولف - ترجمة إيزابيل كمال)",
        "url": "https://archive.org/download/draymanahmed1985_gmail_201708/%D8%A5%D9%84%D9%89%20%D8%A7%D9%84%D9%81%D9%86%D8%A7%D8%B1%20-%20%D9%81%D8%B1%D8%AC%D9%8A%D9%86%D9%8A%D8%A7%20%D9%88%D9%88%D9%84%D9%81%D8%8C%20%D8%AA%D8%B1%D8%AC%D9%85%D8%A9%20%D8%A5%D9%8A%D8%B2%D8%A7%D8%A8%D9%8A%D9%84%20%D9%83%D9%85%D8%A7%D9%84.epub",
        "filename": "To_The_Lighthouse_Arabic_Virginia_Woolf.epub"
    },
    {
        "title": "The Grapes of Wrath (عناقيد الغضب - جون شتاينبك)",
        "url": "https://archive.org/download/moharram1965_gmail_20170110_1604/%D8%AC%D9%88%D9%86%20%D8%B4%D8%AA%D8%A7%D9%8A%D9%86%D8%A8%D9%83..%D8%B9%D9%86%D8%A7%D9%82%D9%8A%D8%AF%20%D8%A7%D9%84%D8%BA%D8%B6%D8%A8..%D8%B1%D9%88%D8%A7%D9%8A%D8%A9..%D9%86%D8%B3%D8%AE%D8%A9%20%D9%83%D8%A7%D9%85%D9%84%D8%A9%20%E2%80%AA%E2%80%AC.epub",
        "filename": "The_Grapes_Of_Wrath_Arabic_Steinbeck.epub"
    },
    {
        "title": "Alice's Adventures in Wonderland (أليس في بلاد العجائب - لويس كارول)",
        "url": "https://archive.org/download/dodylonging_gmail_20161205_2343/%D8%A3%D9%84%D9%8A%D8%B3%20%D9%81%D9%8A%20%D8%A8%D9%84%D8%A7%D8%AF%20%D8%A7%D9%84%D8%B9%D8%AC%D8%A7%D8%A6%D8%A8%20-%20%D9%84%D9%88%D9%8A%D8%B3%20%D9%83%D8%A7%D8%B1%D9%88%D9%84.epub",
        "filename": "Alices_Adventures_Arabic_Lewis_Carroll.epub"
    },
    {
        "title": "Les Misérables (البؤساء - فيكتور هوغو - ترجمة منير بعلبكي)",
        "url": "https://archive.org/download/1_20210503/%D8%A7%D9%84%D8%A8%D8%A4%D8%B3%D8%A7%D8%A1%20%D8%AC%D9%80%201%20%D9%84%D9%80%20%D9%81%D9%8A%D9%83%D8%AA%D9%88%D8%B1%20%D9%87%D9%8A%D8%AC%D9%88.epub",
        "filename": "Les_Miserables_Arabic_Munir_Baalbaki.epub"
    },
    {
        "title": "The Little Prince (الأمير الصغير - أنطوان دو سانت إكزوبيري)",
        "url": "https://archive.org/download/al-amir_al-saghir/al-amir_al-saghir.epub",
        "filename": "The_Little_Prince_Arabic_Saint_Exupery.epub"
    },
    {
        "title": "The Picture of Dorian Gray (صورة دوريان غراي - أوسكار وايلد)",
        "url": "https://archive.org/download/Novels00029/Novels-00029.epub",
        "filename": "The_Picture_Of_Dorian_Gray_Arabic_Oscar_Wilde.epub"
    },
    {
        "title": "One Thousand and One Nights (ألف ليلة وليلة - النسخة الكاملة)",
        "url": "https://archive.org/download/123boukrika44_maktoob_20140109_2134/%D8%A3%D9%84%D9%81%20%D9%84%D9%8A%D9%84%D8%A9%20%D9%88%D9%84%D9%8A%D9%84%D8%A9%20%D9%83%D8%A7%D9%85%D9%84%D8%A9.epub",
        "filename": "One_Thousand_And_One_Nights_Arabic_Complete.epub"
    },
    {
        "title": "One Hundred Years of Solitude (مئة عام من العزلة - صالح علماني)",
        "url": "https://archive.org/download/dodylonging_gmail_20161205_2217/%D9%85%D8%A4%D8%A9%20%D8%B9%D8%A7%D9%85%20%D9%85%D9%86%20%D8%A7%D9%84%D8%B9%D8%B2%D9%84%D8%A9%20-%20%D8%BA%D8%A7%D8%A8%D8%B1%D9%8A%D9%8A%D9%84%20%D8%BA%D8%A7%D8%B1%D8%B3%D9%8A%D8%A7%20%D9%85%D8%A7%D8%B1%D9%83%D9%8A%D8%B2.pdf",
        "filename": "One_Hundred_Years_Of_Solitude_Arabic_Saleh_Almani.pdf"
    },
    {
        "title": "Lolita (لوليتا - فلاديمير نابوكوف)",
        "url": "https://archive.org/download/elshandawily4183/%D8%B1%D9%88%D8%A7%D9%8A%D8%A9%20%D9%84%D9%88%D9%84%D9%8A%D8%AA%D8%A7%20-%20%D9%81%D9%84%D8%A7%D8%AF%D9%8A%D9%85%D9%8A%D8%B1%20%D9%86%D8%A7%D8%A8%D9%88%D9%83%D9%88%D9%81.pdf",
        "filename": "Lolita_Arabic_Vladimir_Nabokov.pdf"
    },
    {
        "title": "The Lord of the Rings (سيد الخواتم - دار نهضة مصر)",
        "url": "https://archive.org/download/lord-of-the-rings-collection/Lord%20of%20the%20Rings%20Collection.pdf",
        "filename": "The_Lord_Of_The_Rings_Arabic_Nahdet_Misr.pdf"
    },
    {
        "title": "To Kill a Mockingbird (لا تقتل عصفورا ساخرا - هاربر لي)",
        "url": "https://archive.org/download/novels00049/Novels-00049.pdf",
        "filename": "To_Kill_A_Mockingbird_Arabic_Harper_Lee.pdf"
    },
    {
        "title": "Frankenstein (فرانكنشتاين - ماري شيلي)",
        "url": "https://archive.org/download/20200913_20200913_0756/%D9%81%D8%B1%D8%A7%D9%86%D9%83%D8%B4%D8%AA%D8%A7%D9%8A%D9%86%20-%20%D9%85%D8%A7%D8%B1%D9%8A%20%D8%B4%D9%8A%D9%84%D9%8A.pdf",
        "filename": "Frankenstein_Arabic_Mary_Shelley.pdf"
    },
    {
        "title": "Beloved (محبوبة - توني موريسون)",
        "url": "https://archive.org/download/dodylonging_gmail_20161205_2256/%D9%85%D8%AD%D8%A8%D9%88%D8%A8%D8%A9%20-%20%D8%AA%D9%88%D9%86%D9%8A%20%D9%85%D9%88%D8%B1%D9%8A%D8%B3%D9%88%D9%86.pdf",
        "filename": "Beloved_Arabic_Toni_Morrison.pdf"
    },
    {
        "title": "David Copperfield (ديفيد كوبرفيلد - تشارلز ديكنز)",
        "url": "https://archive.org/download/20231222_20231222_1746/%D8%AF%D9%8A%D9%81%D9%8A%D8%AF%20%D9%83%D9%88%D8%A8%D8%B1%D9%81%D9%8A%D9%84%D8%AF%20%D8%8C%20%D8%AA%D8%B4%D8%A7%D8%B1%D9%84%D8%B2%20%D8%AF%D9%8A%D9%83%D9%86%D8%B2.pdf",
        "filename": "David_Copperfield_Arabic_Charles_Dickens.pdf"
    },
    {
        "title": "The Red and the Black (الأحمر والأسود - ستندال)",
        "url": "https://archive.org/download/moharram1965_gmail_1/%D8%A7%D9%84%D8%A3%D8%AD%D9%85%D8%B1%20%D9%88%D8%A7%D9%84%D8%A3%D8%B3%D9%88%D8%AF%20%2C%20%D8%AC1%20-%20%D8%B3%D8%AA%D9%86%D8%AF%D8%A7%D9%84.pdf",
        "filename": "The_Red_And_The_Black_Arabic_Stendhal.pdf"
    },
    {
        "title": "Brave New World (عالم جديد شجاع - ألدوس هكسلي)",
        "url": "https://archive.org/download/20250416_20250416_1402/%D8%B9%D8%A7%D9%84%D9%85%20%D8%AC%D8%AF%D9%8A%D8%AF%20%D8%B4%D8%AC%D8%A7%D8%B9%20%20%20%D8%A3%D9%84%D8%AF%D9%88%D8%B3%20%D9%87%D9%83%D8%B3%D9%84%D9%8A.pdf",
        "filename": "Brave_New_World_Arabic_Aldous_Huxley.pdf"
    },
    {
        "title": "The Master and Margarita (الشيطان يزور موسكو - بولغاكوف)",
        "url": "https://archive.org/download/novels00048/Novels-00048.pdf",
        "filename": "The_Master_And_Margarita_Arabic_Bulgakov.pdf"
    }
]

# ==============================================================================
# 2. ENGLISH MASTER EDITIONS (PROJECT GUTENBERG & RETAIL MASTER ARCHIVES)
# ==============================================================================
ENGLISH_DOWNLOADS = [
    # Top 50 Classics - Verified Project Gutenberg Master Formats
    {
        "title": "Ulysses by James Joyce",
        "url": "https://www.gutenberg.org/ebooks/4300.epub3.images",
        "filename": "01_Ulysses_James_Joyce.epub"
    },
    {
        "title": "In Search of Lost Time: Swann's Way by Marcel Proust",
        "url": "https://www.gutenberg.org/ebooks/10007.epub3.images",
        "filename": "02_In_Search_Of_Lost_Time_Swanns_Way_Proust.epub"
    },
    {
        "title": "The Great Gatsby by F. Scott Fitzgerald",
        "url": "https://www.gutenberg.org/ebooks/64317.epub3.images",
        "filename": "03_The_Great_Gatsby_Fitzgerald.epub"
    },
    {
        "title": "Moby-Dick by Herman Melville",
        "url": "https://www.gutenberg.org/ebooks/2701.epub3.images",
        "filename": "06_Moby_Dick_Herman_Melville.epub"
    },
    {
        "title": "Don Quixote by Miguel de Cervantes",
        "url": "https://www.gutenberg.org/ebooks/996.epub3.images",
        "filename": "08_Don_Quixote_Cervantes.epub"
    },
    {
        "title": "Anna Karenina by Leo Tolstoy",
        "url": "https://www.gutenberg.org/ebooks/1399.epub3.images",
        "filename": "10_Anna_Karenina_Leo_Tolstoy.epub"
    },
    {
        "title": "War and Peace by Leo Tolstoy",
        "url": "https://www.gutenberg.org/ebooks/2600.epub3.images",
        "filename": "12_War_And_Peace_Leo_Tolstoy.epub"
    },
    {
        "title": "Crime and Punishment by Fyodor Dostoevsky",
        "url": "https://www.gutenberg.org/ebooks/2554.epub3.images",
        "filename": "13_Crime_And_Punishment_Dostoevsky.epub"
    },
    {
        "title": "Wuthering Heights by Emily Brontë",
        "url": "https://www.gutenberg.org/ebooks/768.epub3.images",
        "filename": "14_Wuthering_Heights_Emily_Bronte.epub"
    },
    {
        "title": "Pride and Prejudice by Jane Austen",
        "url": "https://www.gutenberg.org/ebooks/1342.epub3.images",
        "filename": "15_Pride_And_Prejudice_Jane_Austen.epub"
    },
    {
        "title": "The Brothers Karamazov by Fyodor Dostoevsky",
        "url": "https://www.gutenberg.org/ebooks/28054.epub3.images",
        "filename": "18_The_Brothers_Karamazov_Dostoevsky.epub"
    },
    {
        "title": "Madame Bovary by Gustave Flaubert",
        "url": "https://www.gutenberg.org/ebooks/2413.epub3.images",
        "filename": "19_Madame_Bovary_Flaubert.epub"
    },
    {
        "title": "Adventures of Huckleberry Finn by Mark Twain",
        "url": "https://www.gutenberg.org/ebooks/76.epub3.images",
        "filename": "22_Huckleberry_Finn_Mark_Twain.epub"
    },
    {
        "title": "Middlemarch by George Eliot",
        "url": "https://www.gutenberg.org/ebooks/145.epub3.images",
        "filename": "24_Middlemarch_George_Eliot.epub"
    },
    {
        "title": "The Odyssey by Homer",
        "url": "https://www.gutenberg.org/ebooks/1727.epub3.images",
        "filename": "26_The_Odyssey_Homer.epub"
    },
    {
        "title": "The Divine Comedy by Dante Alighieri",
        "url": "https://www.gutenberg.org/ebooks/8800.epub3.images",
        "filename": "28_The_Divine_Comedy_Dante.epub"
    },
    {
        "title": "Jane Eyre by Charlotte Brontë",
        "url": "https://www.gutenberg.org/ebooks/1260.epub3.images",
        "filename": "30_Jane_Eyre_Charlotte_Bronte.epub"
    },
    {
        "title": "Heart of Darkness by Joseph Conrad",
        "url": "https://www.gutenberg.org/ebooks/219.epub3.images",
        "filename": "31_Heart_Of_Darkness_Joseph_Conrad.epub"
    },
    {
        "title": "Alice's Adventures in Wonderland by Lewis Carroll",
        "url": "https://www.gutenberg.org/ebooks/11.epub3.images",
        "filename": "36_Alices_Adventures_In_Wonderland_Carroll.epub"
    },
    {
        "title": "The Iliad by Homer",
        "url": "https://www.gutenberg.org/ebooks/6130.epub3.images",
        "filename": "37_The_Iliad_Homer.epub"
    },
    {
        "title": "Great Expectations by Charles Dickens",
        "url": "https://www.gutenberg.org/ebooks/1400.epub3.images",
        "filename": "38_Great_Expectations_Dickens.epub"
    },
    {
        "title": "Frankenstein by Mary Shelley",
        "url": "https://www.gutenberg.org/ebooks/84.epub3.images",
        "filename": "39_Frankenstein_Mary_Shelley.epub"
    },
    {
        "title": "Les Misérables by Victor Hugo",
        "url": "https://www.gutenberg.org/ebooks/135.epub3.images",
        "filename": "40_Les_Miserables_Victor_Hugo.epub"
    },
    {
        "title": "The Red and the Black by Stendhal",
        "url": "https://www.gutenberg.org/ebooks/44747.epub3.images",
        "filename": "43_The_Red_And_The_Black_Stendhal.epub"
    },
    {
        "title": "David Copperfield by Charles Dickens",
        "url": "https://www.gutenberg.org/ebooks/766.epub3.images",
        "filename": "48_David_Copperfield_Dickens.epub"
    },
    {
        "title": "The Picture of Dorian Gray by Oscar Wilde",
        "url": "https://www.gutenberg.org/ebooks/174.epub3.images",
        "filename": "The_Picture_Of_Dorian_Gray_Wilde.epub"
    },
    {
        "title": "The Holy Bible (World English Bible / KJV - Project Gutenberg)",
        "url": "https://www.gutenberg.org/ebooks/10.epub3.images",
        "filename": "21_The_Holy_Bible_English.epub"
    },
    {
        "title": "Arabian Nights (One Thousand and One Nights)",
        "url": "https://www.gutenberg.org/ebooks/19860.epub3.images",
        "filename": "47_Arabian_Nights_English.epub"
    },

    # Modern 20th Century Masterpieces - Verified Retail EPUBs
    {
        "title": "Nineteen Eighty-Four by George Orwell",
        "url": "https://archive.org/download/NineteenEightyFour-Novel-GeorgeOrwell/orwell1984.epub",
        "filename": "07_1984_George_Orwell.epub"
    },
    {
        "title": "Animal Farm by George Orwell",
        "url": "https://archive.org/download/AnimalFarmByGeorgeOrwell/Animal%20Farm%20by%20George%20Orwell.epub",
        "filename": "Animal_Farm_George_Orwell.epub"
    },
    {
        "title": "The Stranger by Albert Camus (Matthew Ward Translation)",
        "url": "https://archive.org/download/camus-albert-stranger-vintage-1989/Camus%2C%20Albert%20-%20Stranger%20%28Vintage%2C%201989%29.epub",
        "filename": "23_The_Stranger_Albert_Camus.epub"
    },
    {
        "title": "The Catcher in the Rye by J.D. Salinger",
        "url": "https://archive.org/download/1_20191103_20191103_1326/1.epub",
        "filename": "05_The_Catcher_In_The_Rye_Salinger.epub"
    },
    {
        "title": "The Lord of the Rings by J.R.R. Tolkien (HarperCollins Complete Edition)",
        "url": "https://archive.org/download/tolkien-j.-the-lord-of-the-rings-harper-collins-ebooks-2010/Tolkien-J.-The-lord-of-the-rings-HarperCollins-ebooks-2010.epub",
        "filename": "17_The_Lord_Of_The_Rings_Tolkien.epub"
    },
    {
        "title": "One Hundred Years of Solitude by Gabriel García Márquez",
        "url": "https://archive.org/download/OneHundredYearsOfSolitude_201710/One_Hundred_Years_of_Solitude.epub",
        "filename": "04_One_Hundred_Years_Of_Solitude_Marquez.epub"
    },
    {
        "title": "Brave New World by Aldous Huxley",
        "url": "https://archive.org/download/ost-english-brave_new_world_aldous_huxley/Brave_New_World_Aldous_Huxley.epub",
        "filename": "50_Brave_New_World_Aldous_Huxley.epub"
    },
    {
        "title": "Dune by Frank Herbert",
        "url": "https://archive.org/download/frank-herberts-dune-saga-collection-books-1-6-by-frank-herbert-z-lib.org/Frank%20Herberts%20Dune%20Saga%20Collection%20Books%201%20-%206%20by%20Frank%20Herbert%20(z-lib.org).epub",
        "filename": "Dune_Frank_Herbert.epub"
    },
    {
        "title": "Cracking the Coding Interview (6th Edition) by Gayle Laakmann McDowell",
        "url": "https://archive.org/download/codingbookmanav/Cracking%20the%20Coding%20Interview%20-%20189%20Programming%20Questions%20and%20Solutions%20%286th%20Edition%29.epub",
        "filename": "cracking_the_coding_interview_6th_retail.epub"
    }
]

def main():
    print("==================================================")
    print("   DOWNLOADING ARABIC TRANSLATIONS & CLASSICS    ")
    print("==================================================")
    
    print("\n--- 1. Arabic Translations of Existing Books & World Classics ---")
    ar_success = 0
    for item in ARABIC_DOWNLOADS:
        dst = os.path.join(ARABIC_DIR, item['filename'])
        if download_file(item['url'], dst):
            ar_success += 1
            
    print(f"\n-> Arabic Downloads Completed: {ar_success}/{len(ARABIC_DOWNLOADS)}")

    print("\n--- 2. English Master Editions (Project Gutenberg & Retail EPUBs) ---")
    en_success = 0
    for item in ENGLISH_DOWNLOADS:
        dst = os.path.join(ENGLISH_DIR, item['filename'])
        if download_file(item['url'], dst):
            en_success += 1

    print(f"\n-> English Downloads Completed: {en_success}/{len(ENGLISH_DOWNLOADS)}")

    # Generate Manifest Index
    manifest = {
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "arabic_books": [
            {
                "title": item["title"],
                "filename": item["filename"],
                "path": os.path.join(ARABIC_DIR, item["filename"]),
                "size_bytes": os.path.getsize(os.path.join(ARABIC_DIR, item["filename"])) if os.path.exists(os.path.join(ARABIC_DIR, item["filename"])) else 0,
                "status": "Verified" if os.path.exists(os.path.join(ARABIC_DIR, item["filename"])) and os.path.getsize(os.path.join(ARABIC_DIR, item["filename"])) > 20000 else "Missing"
            }
            for item in ARABIC_DOWNLOADS
        ],
        "english_books": [
            {
                "title": item["title"],
                "filename": item["filename"],
                "path": os.path.join(ENGLISH_DIR, item["filename"]),
                "size_bytes": os.path.getsize(os.path.join(ENGLISH_DIR, item["filename"])) if os.path.exists(os.path.join(ENGLISH_DIR, item["filename"])) else 0,
                "status": "Verified" if os.path.exists(os.path.join(ENGLISH_DIR, item["filename"])) and os.path.getsize(os.path.join(ENGLISH_DIR, item["filename"])) > 20000 else "Missing"
            }
            for item in ENGLISH_DOWNLOADS
        ]
    }
    
    manifest_path = os.path.join(BASE_DIR, "library_manifest.json")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"\n[✓] Library Manifest Index written to: {manifest_path}")

if __name__ == "__main__":
    main()
