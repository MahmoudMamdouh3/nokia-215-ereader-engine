"""
Generates master-level study guides for:
- 13_The_Holy_Quran
- 14_Tafsir_Al_Mukhtasar
- 15_The_Holy_Bible
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

EN_DIR = r"E:\nokia\summaries\english"
AR_DIR = r"E:\nokia\summaries\arabic"

GUIDES = [
    # 13 The Holy Quran
    {
        "id": "13_The_Holy_Quran",
        "content_en": """# Comprehensive Master Guide: The Holy Qur'an
**Scripture:** The Direct Word of Allah (God)  
**Revealed to:** Prophet Muhammad (peace and blessings be upon him)  
**Period:** 610 CE – 632 CE (23 Years)  
**Classification:** Revelation / Divine Theology / Sacred Law & Guidance  

---

## 1. Structural Overview and Revelation Periods
The Holy Qur'an consists of **114 Surahs (chapters)** and **6,236 Ayahs (verses)**, divided into **30 equal Juz' (parts)** for recitation and study. It was revealed gradually over 23 years in two distinct phases:

### 1. The Meccan Phase (approx. 13 years - 86 Surahs):
- **Core Focus**: Monotheism (*Tawhid*), the reality of the Day of Judgment (*Akhirah*), resurrection, spiritual purification, patience under severe persecution, and the historical lessons of earlier Prophets (Noah, Abraham, Moses, Jesus, etc.).
- **Style**: Powerful, rhythmic, poetic, and intense warnings against polytheism and injustice.

### 2. The Medinan Phase (approx. 10 years - 28 Surahs):
- **Core Focus**: Community organization, civil law, judicial rulings, marriage and inheritance, financial ethics (prohibition of usury/riba), governance, international relations, treaties, defense, and interactions with the People of the Book.
- **Style**: Detailed, prescriptive, legislative, and establishing an egalitarian society.

---

## 2. Central Themes and Doctrinal Pillars

1. **Tawhid (Absolute Divine Oneness)**:
   - *Tawhid ar-Rububiyyah*: God as the sole Creator, Sustainer, and Sovereign.
   - *Tawhid al-Uluhiyyah*: God alone is worthy of worship and submission.
   - *Tawhid al-Asma' was-Sifat*: God's transcendent, perfect Names and Attributes without anthropomorphism (*Tashbih*) or negation (*Ta'til*).
2. **Risalah (Prophethood and Continuity of Revelation)**:
   - The Qur'an affirms all previous divine revelations (Torah, Psalms, Gospel) in their original divine forms and confirms the line of Prophets ending with Muhammad as the Seal of the Prophets.
3. **Al-Akhirah (Resurrection and Accountability)**:
   - Complete personal moral accountability; every deed recorded, ultimate justice in Paradise (*Jannah*) or Hellfire (*Jahannam*).
4. **Adl wa Ihsan (Justice, Benevolence, and Social Welfare)**:
   - Strict defense of the vulnerable, orphans, widows, travelers, and the poor through Zakat and fair distribution of wealth.

---

## 3. Preservation & The Uthmanic Mus-haf
Unlike previous texts transmitted via written fragments subject to recopying errors, the Qur'an was preserved from the very beginning through a dual mechanism:
- **Mass Oral Memorization (*Tawatur*)**: Thousands of companions memorized the text verbatim directly from the Prophet.
- **Official Written Codification**: Scribes recorded every verse under direct prophetic oversight; standardized into the unified Uthmanic Codex (*Rasm Uthmani*) during the Caliphate of Uthman ibn Affan (RA).
""",
        "content_ar": """# الدليل الدراسي والتعريفي الشامل: القرآن الكريم
**الوصف:** كلام الله المعجز المنزل على نبيه محمد صلى الله عليه وسلم  
**فترة التنزيل:** 610 م – 632 م (على مدار 23 عاماً)  
**المجال:** الوحي الإلهي / العقيدة والشريعة والأخلاق / الهداية الإنسانية  

---

## 1. الهيكل العام وأطوار التنزيل القرآني
يتألف القرآن الكريم من **114 سورة** تضم **6,236 آية**، مرتبة ومقسمة إلى **30 جزءاً** لتيسير التلاوة والحفظ والتدبر. نزل القرآن منجماً (مفرقاً) على مرحلتين أساسيتين:

### 1. العهد المكي (13 عاماً تقريباً - 86 سورة):
- **المحاور الأساسية**: ترسيخ عقيدة التوحيد الخالص، وإثبات البعث والجزاء والحساب في اليوم الآخر، وتزكية النفوس ومكارم الأخلاق، وضرب الأمثال بقصص الأنبياء السابقين (نوح، وإبراهيم، وموسى، وعيسى عليهم السلام) لتثبيت قلوب المؤمنين في مواجهة الاضطهاد.
- **الأسلوب**: إيقاع فصيح آسر، وقوارع تهز الوجدان، وآيات تهدم الشرك والظلم الطبقي.

### 2. العهد المدني (10 أعوام تقريباً - 28 سورة):
- **المحاور الأساسية**: بناء المجتمع والدولة، والتشريعات المدنية والجنائية، وأحكام الأسرة (الزواج، الطلاق، المواريث)، والمعاملات المالية وحرمة الربا، وقواعد السلم والحرب والمعاهدات، والحوار مع أهل الكتاب.
- **الأسلوب**: تشريعي، تفصيلي، يبني أمة العدل والشورى والتكافل الاجتماعي.

---

## 2. المحاور العقدية والتشريعية الكبرى

1. **التوحيد الخالص**:
   - *توحيد الربوبية*: إفراد الله بالخلق والرزق والملك والتدبير.
   - *توحيد الألوهية*: إفراد الله وحده بالعبادة والدعاء والخضوع.
   - *توحيد الأسماء والصفات*: إثبات ما أثبته الله لنفسه من كمال الأسماء ونعوت الجلال بلا تمثيل ولا تعطيل: ﴿لَيْسَ كَمِثْلِهِ شَيْءٌ ۖ وَهُوَ السَّمِيعُ الْبَصِيرُ﴾.
2. **الرسالة والنبوات**:
   - تأكيد وحدة الرسالات السماوية في أصل التوحيد، وتصديق ما أنزل الله على الأنبياء السابقين، وختم النبوة بمحمد ﷺ رحمة للعالمين.
3. **اليوم الآخر والعدالة الإلهية**:
   - حتمية البعث والحساب؛ موازين القسط، وأن كل مثقال ذرة من خير أو شر مسجل ومجزى به.
4. **العدل والإحسان والأخلاق**:
   - إقامة القسط ومحاربة الظلم؛ رعاية اليتامى والمساكين، وفريضة الزكاة، والتأكيد على أن أكرم الناس عند الله أتقاهم بلا تمييز لعرق أو لون.

---

## 3. التوثيق والمصحف العثماني
حُفظ القرآن الكريم منذ تنزيله بآليتين متوازيتين فريدتين في تاريخ الأديان:
- **التواتر الشفهي الجمعي**: حفظ مئات الآلاف للنص غيباً وتناقله صوتاً وحرفاً جيلاً بعد جيل.
- **التدوين الكتابي الرسمي**: جمع القرآن في عهد أبي بكر الصديق، ثم نسخه وتوحيده في المصاحف العثمانية بإشراف كبار الصحابة رضوان الله عليهم.
"""
    },

    # 14 Tafsir Al Mukhtasar
    {
        "id": "14_Tafsir_Al_Mukhtasar",
        "content_en": """# Comprehensive Master Guide: Tafsir Al-Mukhtasar (The Abridged Tafsir)
**Publisher / Origin:** Markaz Tafsir for Quranic Studies / King Fahd Complex  
**Language:** Arabic & Global Languages (QuranEnc Project)  
**Field:** Quranic Exegesis / Hermeneutics / Applied Tafsir  

---

## 1. Background & Scholarly Methodology
*Al-Mukhtasar fi Tafsir al-Qur'an al-Karim* was compiled by a prestigious committee of senior Quranic scholars to produce an accessible, highly authentic, verse-by-verse commentary free of esoteric disputes, unverified tales (*Isra'iliyyat*), and dense linguistic digressions.

### Methodological Principles:
1. **Adherence to Orthodox Ahl al-Sunnah Creed**: Explaining divine attributes directly without allegory (*Ta'wil*) or denial (*Ta'til*).
2. **Tafsir of the Qur'an by the Qur'an and Sunnah**: Prioritizing authentic Hadith and Sahaba understandings (Ibn Abbas, Ibn Mas'ud).
3. **Clarity & Brevity**: Providing clear modern phrasing so ordinary readers can grasp the direct meaning of every verse while reciting.
4. **Marginal Page Layout**: Designed specifically to accompany the standard Madinah Mus-haf page-for-page.
5. **Practical Guidance**: Highlighting spiritual and jurisprudential lessons (*Fawa'id*) from each page.
""",
        "content_ar": """# الدليل الدراسي والمنهجي الشامل: التفسير المختصر (المختصر في تفسير القرآن الكريم)
**الجهة المصدرة:** مركز تفسير للدراسات القرآنية / مجمع الملك فهد لطباعة المصحف الشريف  
**المجال:** التفسير وعلوم القرآن / التفسير التطبيقي المعاصر  

---

## 1. السياق العلمي والمنهجية المتبعة
أعدّ كتاب *المختصر في تفسير القرآن الكريم* نخبة من كبار علماء التفسير تحت إشراف علمي دقيق، ليكون تفسيراً ميسراً، محرراً، يناسب عموم المسلمين في مشارق الأرض ومغاربها، متجرداً من الخلافات الفقهية المعقدة، والمسائل اللغوية الجدلية، والإسرائيليات الدخيلة.

### الركائز المنهجية للتفسير:
1. **اتباع منهج أهل السنة والجماعة**: إثبات أسماء الله وصفاته على الوجه اللائق بجلاله دون تحريف أو تأويل أو تعطيل.
2. **تفسير القرآن بالقرآن والحديث الصحيح**: الاعتماد على ما صح عن النبي ﷺ وأقوال الصحابة الكرام (كابن عباس وابن مسعود) والتابعين.
3. **الوضوح والإيجاز**: صياغة المعاني بأسلوب عربي معاصر وسلس يسهل على القارئ فهم معنى الآية أثناء التلاوة مباشرة.
4. **التوافق مع صفحات المصحف الشريف**: صُمم التفسير ليكون حاشية موافقة تماماً لصفحات مصحف المدينة النبوية.
5. **استخراج الفوائد والهدايات**: إبراز الدروس الإيمانية والتربوية والعملية المستفادة من كل صفحة.
"""
    },

    # 15 The Holy Bible
    {
        "id": "15_The_Holy_Bible",
        "content_en": """# Comprehensive Master Guide: The Holy Bible
**Scripture:** The Old and New Testaments  
**Languages of Origin:** Hebrew, Aramaic, Ancient Greek (Koine)  
**Traditions:** Judaism (Hebrew Bible/Tanakh), Christianity (Catholic, Protestant, Orthodox)  
**Field:** Comparative Theology / Sacred Scriptures / Ancient Near East Literature  

---

## 1. Canon & Structural Division
The Bible is a library of sacred texts composed across roughly 1,500 years by dozens of authors across the Ancient Near East and Greco-Roman Mediterranean.

### The Old Testament (Hebrew Scripture / Tanakh):
Contains 39 books (Protestant canon) / 46 books (Catholic canon):
1. **The Pentateuch / Torah (5 Books of Moses)**: Genesis (Creation, Patriarchs), Exodus (Liberation, Sinai Covenant, Law), Leviticus (Priesthood, Purity), Numbers (Wilderness Wandering), Deuteronomy (Renewal of Covenant).
2. **Historical Books**: Joshua, Judges, Samuel, Kings, Chronicles, Ezra, Nehemiah, Esther (conquest, monarchies, exile, restoration).
3. **Wisdom & Poetic Books**: Job (The problem of suffering), Psalms (Hymns and prayers of David), Proverbs (Practical wisdom of Solomon), Ecclesiastes (Existential vanity), Song of Songs (Divine love allegory).
4. **Prophetic Books**: Major Prophets (Isaiah, Jeremiah, Ezekiel, Daniel) and Minor Prophets (The Twelve: Hosea to Malachi), proclaiming social justice, covenant fidelity, and messianic expectations.

### The New Testament (27 Books):
1. **The Four Gospels**: Matthew, Mark, Luke, John — chronicling the life, teachings, parables, crucifixion, and resurrection of Jesus of Nazareth.
2. **Acts of the Apostles**: History of the early church, the descent of the Holy Spirit at Pentecost, and missionary journeys of Peter and Paul.
3. **The Epistles (Letters)**: 14 Pauline Epistles (Romans, Corinthians, Galatians, Ephesians, etc.) and General Epistles (James, Peter, John, Jude) formulating Christian theology, grace, and community ethics.
4. **Book of Revelation (Apocalypse of John)**: Eschatological vision of spiritual warfare, divine judgment, and the renewal of all creation.
""",
        "content_ar": """# الدليل الدراسي واللاهوتي الشامل: الكتاب المقدس (The Holy Bible)
**الوصف:** العهد القديم والعهد الجديد  
**لغات الأصل:** العبرية، الآرامية، اليونانية القديمة (الكوينه)  
**المجال:** تاريخ الأديان / دراسات مقارنة الأديان / نصوص الشرق الأدنى القديم  

---

## 1. الهيكل القانوني وأقسام الكتاب المقدس
الكتاب المقدس مكتبة دينية جامعة لنصوص دُوّنت على مدار ما يقارب 1500 عام بواسطة كتّاب متعددين في الشرق الأدنى وحوض البحر المتوسط:

### أولاً: العهد القديم (الكتب العبرية / التناخ)
يضم 39 سفراً (في القانون البروتستانتي) أو 46 سفراً (في القانون الكاثوليكي والشرقي):
1. **أسفار الشريعة (التوراة - أسفار موسى الخمسة)**: التكوين (الخلق، الطوفان، الآباء إبراهيم وإسحاق ويعقوب)، الخروج (التحرر من مصر، عهد سيناء)، اللاويين (الكهنوت والطقوس)، العدد (التيه في البرية)، التثنية (تجديد العهد والشريعة).
2. **الأسفار التاريخية**: يشوع، القضاة، صموئيل، الملوك، أخبار الأيام، عزرا، نحميا، أستير (تاريخ الممالك والحروب والسبي البابلي والعودة).
3. **الأسفار الشعرية والحكمية**: أيوب (معضلة الألم والشر)، المزامير (أناشيد وتسابيح داود)، الأمثال (حكمة سليمان)، الجامعة (فلسفة الوجود والزوال)، نشيد الأنشاد (رمزية المحبة).
4. **أسفار الأنبياء**: الأنبياء الكبار (إشعياء، إرميا، حزقيال، دانيال) والأنبياء الصغار الاثنا عشر (هوشع إلى ملاخي)؛ تتركز حول الدعوة للعدالة والتحذير من الفساد ونبوءات الخلاص المسياني.

### ثانياً: العهد الجديد (27 سفراً)
1. **الأناجيل الأربعة**: متى، مرقس، لوقا، يوحنا؛ تسرد حياة يسوع المسيح، ومعجزاته، وتعاليمه وأمثاله، وصلبه وقيامته.
2. **أعمال الرسل**: تاريخ الكنيسة الأولى، وحلول الروح القدس، ورحلات بولس الرسول التبشيرية عبر الإمبراطورية الرومانية.
3. **الرسائل الجامعة**: رسائل بولس الرسول (رومية، كورنثوس، غلاطية، إلخ) ورسائل بطرس ويعقوب ويوحنا ويهوذا؛ تؤسس لعقيدة الفداء والخلاص والنعمة والأخلاق المسيحية.
4. **سفر الرؤيا (رؤيا يوحنا اللاهوتي)**: رؤى أخروية رمزية تتناول الصراع بين الخير والشر ونهاية الزمان وقيام السماء الجديدة والأرض الجديدة.
"""
    }
]

def main():
    for g in GUIDES:
        file_id = g['id']
        en_path = os.path.join(EN_DIR, f"{file_id}.md")
        ar_path = os.path.join(AR_DIR, f"{file_id}_Arabic.md")
        with open(en_path, 'w', encoding='utf-8') as f:
            f.write(g['content_en'].strip() + "\n")
        with open(ar_path, 'w', encoding='utf-8') as f:
            f.write(g['content_ar'].strip() + "\n")
        print(f"  [✓] Successfully upgraded master study guide: {file_id}")

if __name__ == "__main__":
    main()
