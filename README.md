# 📱 Nokia 215 4G Universal E-Reader & Media Engine

> **Turn any 240×320 QVGA feature phone / "dumbphone" into a world-class offline digital library, manga reader, and spiritual study workstation.**

---

## 🌟 Overview

Modern feature phones like the **Nokia 215 4G**, **Nokia 225 4G**, **Nokia 6300 4G**, and similar Series 30+ / KaiOS devices are celebrated for minimalism, long battery life, and digital detox. However, their software ecosystem suffers from major limitations:
- **No Native EPUB or PDF Readers**: Most devices only support bare `.txt` files (with strict file size limits and zero formatting).
- **Broken Non-Latin Text Rendering**: Arabic, Persian, and Urdu text either render backwards, disconnected, or completely lack diacritics (Harakat / Tashkeel).
- **Unreadable Technical Code**: Programming books wrap code lines unpredictably, making indentation and syntax unreadable.
- **D-Pad File Browsing Fatigue**: Scrolling through flat directories of 100+ files on a keypad is exhausting.

This repository provides an **end-to-end automated publishing and rendering pipeline**. It converts world literature, religious texts, programming books, and manga into **high-contrast, perfectly paginated 240×320 image pages**, organized into an ergonomic hierarchical directory tree specifically engineered for physical D-pad navigation.

---

## 🏗️ Core Architecture & Design

### 1. The Image-Page Rendering Paradigm
Rather than relying on non-existent mobile document viewers, every book chapter and manga page is rendered into sequential, crisp **240×280 images** calibrated for the active Nokia S30+ viewer canvas:

> ✅ **Screen-Area Calibration Resolved (240 × 280):** The physical TFT LCD is 240×320, but the S30+ photo viewer permanently reserves a 20 px top status bar (battery/clock/signal) and a 20 px bottom softkey bar ("Options"/"Back"). Rendering at the calibrated **240 × 280 pixels** via [`screen_spec.py`](screen_spec.py) completely eliminates black side letterboxing bars and ensures 100% visible, razor-sharp typography. Full empirical measurements and hardware verification: **[docs/SCREEN_AREA_ISSUE.md](docs/SCREEN_AREA_ISSUE.md)**.
- **TFT High-Contrast Typography**: Off-white text on deep black or stark crisp black on pure white to prevent screen ghosting.
- **Proportional Margins**: 8px horizontal padding, 10px vertical header/footer reserve, maximizing readability while preventing clipping under rounded bezel corners.
- **Dynamic Headers & Footers**: Every page displays `[Book Title | Chapter X]` at the top and `Page X of Y` at the bottom for instant navigation context.

### 2. Bilingual RTL & Harakat Engine
Rendering Arabic literature and Quranic verses accurately on embedded displays requires specialized text shaping:
- **Bidirectional Shaping**: Integration with `arabic_reshaper` and `bidi.algorithm` to ensure correct ligature connections and Right-to-Left alignment.
- **Vertical Tashkeel Cushioning**: Increased line spacing (`1.45×`) prevents diacritics (Fatha, Damma, Kasra, Shaddah) from colliding with glyph baselines.
- **Embedded Amiri Typographic Engine**: Leverages Google's `Amiri-Regular` font for authentic Naskh calligraphy.

### 3. Monospace Code Block Pagination
Technical manuals (*The Pragmatic Programmer*, Bjarne Stroustrup's *Programming: Principles and Practice Using C++*) feature strict code blocks:
- Automatic detection of `<code>` and `<pre>` tags.
- Dedicated monospace font rendering with syntax indent preservation.
- Smart pagination that breaks code blocks cleanly at logical boundaries rather than splitting keywords across pages.

### 4. D-Pad Ergonomic Folder Hierarchy
To eliminate scrolling fatigue on physical phone keypads, the generated output is grouped into **5 structured top-level categories**, each containing no more than 3–7 items:

```text
books_out/
├── 01_Quran_And_Tafsir/
│   ├── 01_The_Holy_Quran_Arabic/
│   ├── 02_The_Holy_Quran_English/
│   ├── 03_Tafsir_Al_Mukhtasar_Arabic/
│   └── 04_Tafsir_Al_Mukhtasar_English/
├── 02_Productivity_And_Finance/
│   ├── 01_Atomic_Habits/
│   ├── 02_The_Psychology_Of_Money/
│   └── 03_How_To_Win_Friends_And_Influence_People/
├── 03_Power_And_Strategy/
│   ├── 01_48_Laws_Of_Power/
│   ├── 02_33_Strategies_Of_War/
│   ├── 03_Mastery/
│   ├── 04_The_Laws_Of_Human_Nature/
│   ├── 05_The_Art_Of_Seduction/
│   ├── 06_The_50th_Law/
│   └── 07_The_Daily_Laws/
├── 04_Computer_Science/
│   ├── 01_The_Pragmatic_Programmer/
│   └── 02_Programming_Principles_And_Practice_Using_CPP/
└── 05_Literary_Classics/
    ├── 01_White_Nights/
    └── 02_The_Trial/
```

---

## 📚 Book Catalog & Authenticity Verification

The library contains authentic master editions:
- **English Master Editions**: Master releases from Project Gutenberg and verified retail releases (*Ulysses*, *In Search of Lost Time*, *The Great Gatsby*, *1984*, *The Catcher in the Rye*, *Moby-Dick*, *The Lord of the Rings*, *War and Peace*, *Dune*, *Brave New World*).
- **Renowned Arabic Translations**: Authentic literary translations from distinguished translators and prestigious publishing houses (Dr. Sami Al-Droubi, Salah Niazi, Saleh Almani, Ihsan Abbas, Munir Baalbaki, Dr. Abd Al-Rahman Badawi; published by Dar Al-Tanweer, Dar Al-Mada, Nahdet Misr, and Hindawi Foundation).
- **Verified Software Editions**:
  - *The Pragmatic Programmer*: 20th Anniversary Edition (2nd Edition, 2019/2020) by David Thomas & Andrew Hunt.
  - *Programming: Principles and Practice Using C++*: 3rd Edition (May 2024, C++20/C++23) by Bjarne Stroustrup.
- **Spiritual & Religious Texts**:
  - Full Holy Quran (Uthmani Arabic text with complete Harakat).
  - Bilingual Quran Translation (Saheeh International).
  - Complete Tafsir Al-Mukhtasar (30 Juz, 114 Surahs) direct from the official QuranEnc API.

---

## 📝 Master Study Guides & Analytical Summaries (67 Books - Bilingual)

Located in `summaries/`, this directory contains comprehensive, university-grade analytical study guides for the **entirety of the library (67 books)** in both **English** (`summaries/english/`) and **Arabic** (`summaries/arabic/`).

To eliminate physical scrolling fatigue on the Nokia 215 4G keypad, the summaries are ergonomically organized into **9 thematic sub-categories**:

1. **`01_Computer_Science/`**:
   - *The Pragmatic Programmer* (Official 20th Anniv. Tips & Craftsmanship)
   - *Programming: Principles and Practice Using C++* (Stroustrup C++20/C++23)
   - *Cracking the Coding Interview* (6th Edition - 189 Programming Questions & Solutions)
2. **`02_Productivity_And_Finance/`**:
   - *Atomic Habits* (The 4 Laws, Inversion Framework, 2-Minute Rule)
   - *The Psychology of Money* (All 20 Core Lessons & Behavioral Principles)
   - *How to Win Friends and Influence People* (Carnegie's Complete 4-Part System)
3. **`03_Power_And_Strategy/`**:
   - *The 48 Laws of Power*, *The 33 Strategies of War*, *Mastery*, *The Laws of Human Nature*, *The Art of Seduction*, *The 50th Law*, *The Daily Laws*
4. **`04_Spiritual_And_Religious/`**:
   - *The Holy Quran* (Makki/Madani structural overview and theological core)
   - *Tafsir Al-Mukhtasar* (Verse-by-verse methodology of King Fahd Complex)
   - *The Holy Bible* (Old and New Testament canons and narrative arcs)
5. **`05_Russian_Literature/`**:
   - *Crime and Punishment*, *The Brothers Karamazov*, *White Nights*, *War and Peace*, *Anna Karenina*, *The Master and Margarita*
6. **`06_French_Literature/`**:
   - *In Search of Lost Time: Swann's Way*, *Les Misérables*, *Madame Bovary*, *The Stranger*, *The Little Prince*, *The Red and the Black*, *Journey to the End of the Night*
7. **`07_British_And_Irish_Literature/`**:
   - *Ulysses*, *1984*, *Animal Farm*, *Pride and Prejudice*, *Wuthering Heights*, *Jane Eyre*, *Great Expectations*, *David Copperfield*, *Frankenstein*, *The Picture of Dorian Gray*, *Heart of Darkness*, *To the Lighthouse*, *Mrs. Dalloway*, *The Lord of the Rings*, *Middlemarch*
8. **`08_American_Literature/`**:
   - *The Great Gatsby*, *Moby-Dick*, *The Catcher in the Rye*, *To Kill a Mockingbird*, *Adventures of Huckleberry Finn*, *The Grapes of Wrath*, *The Sound and the Fury*, *Lolita*, *Beloved*, *The Old Man and the Sea*
9. **`09_World_Classics_And_SciFi/`**:
   - *Brave New World*, *Dune*, *Don Quixote*, *One Hundred Years of Solitude*, *Love in the Time of Cholera*, *The Trial*, *The Metamorphosis*, *The Castle*, *The Odyssey*, *The Iliad*, *The Divine Comedy*, *The Magic Mountain*, *One Thousand and One Nights*

Each study guide features:
- **Historical, Cultural & Philosophical Context**
- **In-Depth Chapter-by-Chapter Plot & Analytical Breakdown**
- **Major Character Psychology & Archetypes**
- **Central Themes, Epistemology & Symbolism**
- **Memorable Quotes & Enduring Takeaways**

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Install required dependencies:
```bash
pip install pillow arabic-reshaper python-bidi beautifulsoup4 ebooklib requests
```

### 1. Download Master Books
Run the universal catalog downloader to fetch all authenticated English and Arabic literature:
```bash
python download_full_library.py
```

### 2. Download Quran & Tafsir Al-Mukhtasar
Fetch the complete verified verse-by-verse Tafsir from the QuranEnc API:
```bash
python download_tafsir.py
```

### 3. Generate Book Pages
Run the appropriate pipeline depending on the book type:
- **General Literature & EPUBs**:
  ```bash
  python book_pipeline.py
  ```
- **Technical & Programming Books (Code Formatting)**:
  ```bash
  python build_programming_books.py
  ```
- **Robert Greene Collection**:
  ```bash
  python robert_greene_pipeline.py
  ```
- **Quran & Tafsir (Arabic Tashkeel Shaping)**:
  ```bash
  python tafsir_pipeline.py
  ```

### 4. Top 50 YouTube Podcasts Pipeline (Voice-Tuned & Split)
Download, convert to 96 kbps voice-optimized MP3, auto-split long episodes (>45m) into 30-minute parts, and tag ID3 metadata for the Nokia Music player:
```bash
python build_top50_podcasts.py
```
*To inspect current download progress and completed episodes:*
```bash
python build_top50_podcasts.py status
```

### 5. Large Music Library Organizer (A–Z T9 Keypad Jumping)
Organize massive flat playlists into 27 alphabetical letter buckets with dedicated artist subfolders so songs can be navigated in seconds using T9 keypad jumps:
```bash
python organize_music_library.py
```

### 6. Holy Quran Full Audio Recitations (114 Surahs Canonical)
Download and install full 114 Surah recitations with embedded ID3 metadata directly from verified CDNs into `F:\Quran\`:
```bash
python download_holy_quran.py
```
*To inspect current download status:*
```bash
python download_holy_quran.py status
```
*Supported Reciters:*
- الشيخ محمد صديق المنشاوي (المصحف المجود)
- الشيخ محمد صديق المنشاوي (المصحف المرتل)
- الشيخ فارس عباد (المصحف المرتل)
- الشيخ محمود خليل الحصري (المصحف المرتل)
- الشيخ محمود خليل الحصري (المصحف المجود)

### 7. Audiobooks Library (Original Author Voices & Official Arabic Editions)
Download, voice-tune (96 kbps MP3), and auto-split complete unabridged audiobooks into 30-minute segments into `F:\Audiobooks\01_English\` and `F:\Audiobooks\02_Arabic\`:
```bash
python download_audiobooks.py
```
*To inspect status or run specific language subsets:*
```bash
python download_audiobooks.py status
python download_audiobooks.py en
python download_audiobooks.py ar
```
*Installed Audiobooks on Phone (16 Complete Titles / 146 Parts / ~72 Hours):*
- **English Editions (14 Titles / 120 Parts)**:
  - *Atomic Habits* — James Clear (Original Author Voice, 12 parts)
  - *The Psychology of Money* — Morgan Housel (Official HarperAudio / Chris Hill, 8 parts)
  - *How to Win Friends and Influence People* — Dale Carnegie (15 parts)
  - *The Laws of Human Nature* — Robert Greene (Original Author Voice, 3 parts)
  - *Mastery* — Robert Greene (Official Unabridged / Fred Sanders, 9 parts)
  - *1984* — George Orwell (Official Unabridged / Simon Prebble, 19 parts)
  - *Animal Farm* — George Orwell (Official Unabridged / Ralph Cosham, 7 parts)
  - *The Alchemist* — Paulo Coelho (Official HarperAudio / Jeremy Irons, 9 parts)
  - *The Prophet* — Kahlil Gibran (Official Unabridged / Paul Sparer, 3 parts)
  - *Meditations* — Marcus Aurelius (15 parts)
  - *The Art of War* — Sun Tzu (3 parts)
  - *The Old Man and the Sea* — Ernest Hemingway (Narrated by Charlton Heston, 6 parts)
  - *White Nights* — Fyodor Dostoevsky (Narrated by David Thorn, 6 parts)
  - *The Metamorphosis* — Franz Kafka (Narrated by Benedict Cumberbatch, 5 parts)
- **Arabic Editions (2 Titles / 26 Parts)**:
  - *العادات الذرية* — جيمس كلير (15 parts, 438 mins)
  - *سيكولوجية المال* — مورغان هاوسل (11 parts, 317 mins)

### 8. Checkpoint & Resume System
All audio and media pipelines support persistent JSON manifests (`audiobooks_manifest.json`, `podcasts_manifest.json`) and safe resume. For full inventory details and exact commands to resume paused pipelines, refer to:
👉 **[CHECKPOINT_RESUME_GUIDE.md](file:///e:/nokia/CHECKPOINT_RESUME_GUIDE.md)**

### 9. Sync Cleanly to Your Phone
Connect your Nokia 215 4G (or SD card) via USB and select **Mass Storage / Memory Card Mode** (mounted as `F:\`):
```bash
python sync_books_to_phone.py
```
*The script uses buffered, single-threaded copying to eliminate FAT32 file system lock contention, automatically removes obsolete pages, and mirrors the categorized directory structure.*

---

## 🎮 Phone Navigation Tips (Nokia 215 4G)

1. **Viewing Books**: Open **Gallery / Photos** or the **File Manager** on your phone.
2. **Navigating Pages**:
   - Use the **Right / Left D-Pad keys** to turn pages instantly.
   - Use **Zoom (5 key)** if you need to inspect dense code snippets or intricate diagrams.
3. **Brightness & Battery**: Because pages use a clean dark/high-contrast palette, battery consumption on the 2.4-inch QVGA display is minimal, allowing weeks of reading on a single charge.

---

## 🔒 Privacy & Safety Note
This repository contains zero personal identifiers, private credentials, or proprietary tokens. All book downloads are pulled directly from open cultural heritage archives (Project Gutenberg, Archive.org, and public domain cultural repositories).

---

## 📄 License
This tooling is released under the **MIT License**. Literary texts and translations remain the intellectual property of their respective authors, translators, and publishers.
