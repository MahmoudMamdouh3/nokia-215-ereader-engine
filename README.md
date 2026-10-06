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
Rather than relying on non-existent mobile document viewers, every book chapter is rendered into sequential, crisp **240×320 QVGA images** (standard Nokia screen resolution):
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

## 📝 Master Study Guides & Analytical Summaries (66 Books - Bilingual)

Located in `summaries/`, this directory contains comprehensive, university-grade analytical study guides for the **entirety of the library (66 books)** in both **English** (`summaries/english/`) and **Arabic** (`summaries/arabic/`).

To eliminate physical scrolling fatigue on the Nokia 215 4G keypad, the summaries are ergonomically organized into **9 thematic sub-categories**:

1. **`01_Computer_Science/`**:
   - *The Pragmatic Programmer* (Official 20th Anniv. Tips & Craftsmanship)
   - *Programming: Principles and Practice Using C++* (Stroustrup C++20/C++23)
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

### 4. Sync Cleanly to Your Phone
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
