# 📌 Nokia 215 4G Media Engine — Checkpoint & Resume Guide

> **Current Status**: All audio, podcast, and book pipelines cleanly paused at user command. Every piece of media installed, exact stopping points, and single-command resume instructions are cataloged below.

---

## 🗂️ 1. Phone Storage & Installed Media Inventory (`F:\`)

**SD Card Storage Status**:
- **Total Capacity**: 29.28 GB (FAT32)
- **Used**: 20.32 GB
- **Free Space Remaining**: **8.96 GB**

---

### A. Unabridged Audiobooks (`F:\Audiobooks\`) — 16 Complete Titles / 146 Parts (~72 Hours)
All audiobooks are encoded in hardware-friendly **96 kbps MP3** (44.1 kHz, CBR), segmented strictly into **30-minute parts** (`Pt01.mp3`, `Pt02.mp3`, ...) to prevent Series 30+ media player firmware memory heap overflow crashes, with complete embedded ID3 tags (`Artist`, `Album`, `Title`, `Track`, `Genre="Audiobook"`).

#### 🇬🇧 English Audiobooks (`F:\Audiobooks\01_English\`) — 14 Titles / 120 Parts (~59.5 Hours):
1. `EN_01`: **Atomic Habits** — James Clear (*Original Author Voice*) — 12 parts, 335 mins
2. `EN_02`: **The Psychology of Money** — Morgan Housel (*Official HarperAudio / Chris Hill*) — 8 parts, 238 mins
3. `EN_03`: **How to Win Friends and Influence People** — Dale Carnegie (*Official Unabridged*) — 15 parts, 442 mins
4. `EN_05`: **The Laws of Human Nature** — Robert Greene (*Original Author Voice*) — 3 parts, 86 mins
5. `EN_07`: **Mastery** — Robert Greene (*Official Unabridged / Fred Sanders*) — 9 parts, 264 mins
6. `EN_08`: **1984** — George Orwell (*Official Unabridged / Simon Prebble*) — 19 parts, 568 mins
7. `EN_09`: **Animal Farm** — George Orwell (*Official Unabridged / Ralph Cosham*) — 7 parts, 196 mins
8. `EN_10`: **The Alchemist** — Paulo Coelho (*Official HarperAudio / Jeremy Irons*) — 9 parts, 245 mins
9. `EN_11`: **The Prophet** — Kahlil Gibran (*Official Unabridged / Paul Sparer*) — 3 parts, 78 mins
10. `EN_12`: **Meditations** — Marcus Aurelius (*Official Unabridged*) — 15 parts, 432 mins
11. `EN_13`: **The Art of War** — Sun Tzu (*Official Unabridged*) — 3 parts, 85 mins
12. `EN_14`: **The Old Man and the Sea** — Ernest Hemingway (*Narrated by Charlton Heston*) — 6 parts, 153 mins
13. `EN_15`: **White Nights** — Fyodor Dostoevsky (*Narrated by David Thorn*) — 6 parts, 168 mins
14. `EN_16`: **The Metamorphosis** — Franz Kafka (*Narrated by Benedict Cumberbatch*) — 5 parts, 128 mins

#### 🇸🇦 Arabic Audiobooks (`F:\Audiobooks\02_Arabic\`) — 2 Titles / 26 Parts (~12.6 Hours):
1. `AR_01`: **العادات الذرية** (Atomic Habits Arabic) — جيمس كلير — 15 parts, 438 mins
2. `AR_02`: **سيكولوجية المال** (The Psychology of Money Arabic) — مورغان هاوسل — 11 parts, 317 mins

---

### B. Top Educational & Philosophy Podcasts (`F:\podcasts\`) — 15 Series / 72 Episodes
- **Channel 01: ثمانية / فنجان (`01_Fnjan_Thmanyah`)** — 22 files (including Guinness Record #1 Yasser Alhazimi 7-part deep dive, Dr. Khalid Al-Jubeir, Saleh Al-Maghamsi, Dr. Tariq Al-Habib)
- **Channel 02: Club Shay Shay (`02_Club_Shay_Shay`)** — 26 files (Katt Williams viral cultural interview 8-part edition, Shannon Sharpe sports/culture)
- **Channel 03: The Joe Rogan Experience (`03_Joe_Rogan_Experience`)** — 24 files (Elon Musk, Paul Stamets, Matthew Walker sleep science)

---

### C. Holy Quran Full Recitations (`F:\Quran\`) — 1 Reciter / 114 Canonical Surahs
- **الشيخ محمد صديق المنشاوي (المصحف المجود)**: Complete 114 Surahs (`001_Al_Fatihah.mp3` through `114_An_Nas.mp3`) with embedded Quranic Arabic metadata and canonical numbering.

---

### D. Books & Analytical Summaries (`books_out/` & `summaries/`)
- **Rendered QVGA Image Library (`books_out/`)**: 67 master literary and technical works paginated into 240×320 high-contrast images, shaped with Arabic RTL Harakat cushioning and monospace code indentation preservation.
- **Academic Analytical Study Guides (`summaries/`)**: 67 bilingual study guides in English (`summaries/english/`) and Arabic (`summaries/arabic/`) across 9 thematic sub-categories.

---

## ⏸️ 2. Exact Checkpoint (Where We Stopped)

All pipelines have been safely concluded or paused without corrupting active manifests or filesystems:

| Media Pipeline | Stopped At | Next Item Upon Resuming |
| :--- | :--- | :--- |
| **English Audiobooks** | 14 Completed (`EN_01`-`EN_03`, `EN_05`, `EN_07`-`EN_16`) | `EN_04` (*The 48 Laws of Power* by Robert Greene) / `EN_06` (*The Art of Seduction*) |
| **Arabic Audiobooks** | 2 Completed (`AR_01`, `AR_02`) | `AR_03` (*فن الحرب* لسن تزو) through `AR_18` (*الجريمة والعقاب*) |
| **Podcasts** | 15 Series Completed | Series #16 through #50 |
| **Holy Quran** | Reciter 1 Completed (المنشاوي مجود) | Reciter 2 (المنشاوي مرتل) through Reciter 5 (الحصري مجود) |
| **Anime (Side Task)** | **Active in Background** | *Witch Hat Atelier* Season 1 (13 episodes, 1080p Dual Audio + Arabic/English subs) |

---

## ▶️ 3. How to Resume Later (Commands)

Whenever you give the command to resume, execute any of the following CLI commands:

### Resume Audiobooks:
```bash
# Resume all remaining audiobooks (English & Arabic) automatically:
python download_audiobooks.py

# Or resume only Arabic titles:
python download_audiobooks.py ar

# Or resume only English titles:
python download_audiobooks.py en

# Or run a specific title (e.g. EN_04):
python download_audiobooks.py EN_04

# Inspect live status of installed audiobooks:
python download_audiobooks.py status
```

### Resume Podcasts:
```bash
# Continues downloading and splitting from series #16 through #50:
python build_top50_podcasts.py
```

### Resume Quran Reciters:
```bash
# Continues with reciters 2 through 5:
python download_holy_quran.py
```

### Re-Sync E-Reader Books to Phone:
```bash
# Single-threaded, buffered transfer to SD card (F:\):
python sync_books_to_phone.py
```

---

## 🎬 4. Side Download: Witch Hat Atelier Season 1
- **Target Folder**: `C:\Users\mahmo\Downloads\witch hat ateleier\`
- **Release**: `[Judas] Witch Hat Atelier (Tongari Boushi no Atelier) (Season 01) [1080p][HEVC x265 10bit][Dual-Audio][Multi-Subs]`
- **Contents**: All 13 episodes (S01E01 to S01E13v2) in 1080p HEVC 10-bit with Japanese audio, English audio, and Arabic soft subtitles (`ara`).
- **Downloader**: High-speed multi-peer BitTorrent via `aria2c`.
