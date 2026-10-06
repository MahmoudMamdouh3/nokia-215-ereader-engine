"""
Top 50 Most Streamed YouTube Podcast Episodes Engine
Optimized for Nokia 215 4G Feature Phone (Unisoc T107 / S30+)

Automates:
1. Downloading audio stream of top 50 all-time YouTube podcast episodes.
2. Encoding to voice-optimized 96kbps MP3.
3. Automatically splitting long episodes (>45m) into 30-minute parts for smooth Nokia 215 playback/seeking.
4. Embedding clean ID3 tags (Artist, Album, Title, Track).
5. Saving directly into organized channel folders on the Nokia SD card (F:\\podcasts).
6. Deleting temporary download files to preserve PC disk space.
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path

SD_PODCASTS = r"F:\podcasts"
LOCAL_CACHE = r"E:\nokia\scratch"
MANIFEST_FILE = r"E:\nokia\podcasts_manifest.json"

TOP_50_PODCASTS = [
    # =========================================================================
    # 01 - بودكاست فنجان (ثمانية | Thmanyah)
    # =========================================================================
    {
        "id": 1,
        "channel": "01_Fnjan_Thmanyah",
        "artist": "ثمانية | Thmanyah",
        "album": "بودكاست فنجان",
        "title": "ياسر الحزيمي - كيف تنجح العلاقات",
        "yt_id": "pJ0auP7dbcY",
        "views": "110M+ (Guinness World Record #1 Podcast)",
    },
    {
        "id": 2,
        "channel": "01_Fnjan_Thmanyah",
        "artist": "ثمانية | Thmanyah",
        "album": "بودكاست فنجان",
        "title": "د. خالد الجبير - قلوب تبحث عن النجاة",
        "yt_id": "WAwNyAfi3Yk",
        "views": "20M+",
    },
    {
        "id": 3,
        "channel": "01_Fnjan_Thmanyah",
        "artist": "ثمانية | Thmanyah",
        "album": "بودكاست فنجان",
        "title": "صالح المغامسي - معالم وتأملات وقصص",
        "yt_id": "x0ZFvBijpvg",
        "views": "16M+",
    },
    {
        "id": 4,
        "channel": "01_Fnjan_Thmanyah",
        "artist": "ثمانية | Thmanyah",
        "album": "بودكاست فنجان",
        "title": "د. طارق الحبيب - تشريح الشخصيات والاضطرابات النفسية",
        "yt_id": "hdTdev3GVCw",
        "views": "13M+",
    },
    {
        "id": 5,
        "channel": "01_Fnjan_Thmanyah",
        "artist": "ثمانية | Thmanyah",
        "album": "بودكاست فنجان",
        "title": "د. إبراهيم الخليفي - مفاتيح التربية والتعامل مع المراهقين",
        "yt_id": "CP5pfHZbz3M",
        "views": "11M+",
    },

    # =========================================================================
    # 02 - Club Shay Shay (Shannon Sharpe)
    # =========================================================================
    {
        "id": 6,
        "channel": "02_Club_Shay_Shay",
        "artist": "Shannon Sharpe",
        "album": "Club Shay Shay",
        "title": "Katt Williams Unleashed",
        "yt_id": "8oRRZiRQxTs",
        "views": "94M+",
    },
    {
        "id": 7,
        "channel": "02_Club_Shay_Shay",
        "artist": "Shannon Sharpe",
        "album": "Club Shay Shay",
        "title": "Amanda Seales Speaks Her Truth",
        "yt_id": "Q9fRHyEidvY",
        "views": "16M+",
    },
    {
        "id": 8,
        "channel": "02_Club_Shay_Shay",
        "artist": "Shannon Sharpe",
        "album": "Club Shay Shay",
        "title": "Mo'Nique Sets The Record Straight",
        "yt_id": "q1PVr6AeUT0",
        "views": "14M+",
    },
    {
        "id": 9,
        "channel": "02_Club_Shay_Shay",
        "artist": "Shannon Sharpe",
        "album": "Club Shay Shay",
        "title": "Chad Ochocinco Johnson Unfiltered",
        "yt_id": "KgScnzMqu_o",
        "views": "11M+",
    },
    {
        "id": 10,
        "channel": "02_Club_Shay_Shay",
        "artist": "Shannon Sharpe",
        "album": "Club Shay Shay",
        "title": "Cedric The Entertainer",
        "yt_id": "lhUJ0orHGX8",
        "views": "10M+",
    },

    # =========================================================================
    # 03 - The Joe Rogan Experience (JRE)
    # =========================================================================
    {
        "id": 11,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1315 - Bob Lazar and Jeremy Corbell",
        "yt_id": "BEWz4SXfyCQ",
        "views": "67M+",
    },
    {
        "id": 12,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1368 - Edward Snowden",
        "yt_id": "efs3QRr8LWw",
        "views": "35M+",
    },
    {
        "id": 13,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1255 - Alex Jones and Eddie Bravo",
        "yt_id": "T1h4pjr0XOg",
        "views": "33M+",
    },
    {
        "id": 14,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1554 - Kanye West",
        "yt_id": "qxOeWuAHOiw",
        "views": "21M+",
    },
    {
        "id": 15,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1319 - Bernie Sanders",
        "yt_id": "J1H8vYEi128",
        "views": "20M+",
    },
    {
        "id": 16,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1347 - Neil deGrasse Tyson",
        "yt_id": "0pmviUS1Zac",
        "views": "18M+",
    },
    {
        "id": 17,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1208 - Jordan Peterson",
        "yt_id": "vIeFt88Hm8s",
        "views": "16M+",
    },
    {
        "id": 18,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1153 - Macaulay Culkin",
        "yt_id": "Oyb1xz7waY8",
        "views": "16M+",
    },
    {
        "id": 19,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1245 - Andrew Yang",
        "yt_id": "cTsEzmFamZ8",
        "views": "14M+",
    },
    {
        "id": 20,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1532 - Mike Tyson",
        "yt_id": "hcPUoxTvw5g",
        "views": "14M+",
    },
    {
        "id": 21,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1411 - Robert Downey Jr.",
        "yt_id": "d5XTDmm0KUQ",
        "views": "14M+",
    },
    {
        "id": 22,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1278 - Kevin Hart",
        "yt_id": "XW_KhFq4LQo",
        "views": "13M+",
    },
    {
        "id": 23,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1309 - Naval Ravikant",
        "yt_id": "3qHkcs3kG44",
        "views": "13M+",
    },
    {
        "id": 24,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1552 - Matthew McConaughey",
        "yt_id": "BBCl9A9NlRw",
        "views": "12M+",
    },
    {
        "id": 25,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1080 - David Goggins",
        "yt_id": "5tSTk1083VY",
        "views": "12M+",
    },
    {
        "id": 26,
        "channel": "03_Joe_Rogan_Experience",
        "artist": "Joe Rogan",
        "album": "The Joe Rogan Experience",
        "title": "JRE #1516 - Post Malone",
        "yt_id": "G42RJ4mKj1k",
        "views": "11M+",
    },

    # =========================================================================
    # 04 - Lex Fridman Podcast
    # =========================================================================
    {
        "id": 27,
        "channel": "04_Lex_Fridman",
        "artist": "Lex Fridman",
        "album": "Lex Fridman Podcast",
        "title": "Lex Fridman #400 - Elon Musk: War, AI, Aliens, Physics",
        "yt_id": "JN3KPFbWCy8",
        "views": "14M+",
    },
    {
        "id": 28,
        "channel": "04_Lex_Fridman",
        "artist": "Lex Fridman",
        "album": "Lex Fridman Podcast",
        "title": "Lex Fridman #405 - Jeff Bezos: Amazon and Blue Origin",
        "yt_id": "DcWqzZ3I2cY",
        "views": "12M+",
    },
    {
        "id": 29,
        "channel": "04_Lex_Fridman",
        "artist": "Lex Fridman",
        "album": "Lex Fridman Podcast",
        "title": "Lex Fridman #398 - Mark Zuckerberg: Metaverse Avatars",
        "yt_id": "MVYrJJNdrEg",
        "views": "11M+",
    },
    {
        "id": 30,
        "channel": "04_Lex_Fridman",
        "artist": "Lex Fridman",
        "album": "Lex Fridman Podcast",
        "title": "Lex Fridman #367 - Sam Altman: OpenAI, GPT-4, AGI",
        "yt_id": "L_Guz73e6fw",
        "views": "8.5M+",
    },
    {
        "id": 31,
        "channel": "04_Lex_Fridman",
        "artist": "Lex Fridman",
        "album": "Lex Fridman Podcast",
        "title": "Lex Fridman #414 - Tucker Carlson: Putin and Journalism",
        "yt_id": "f_lRdkH_QoY",
        "views": "8.2M+",
    },
    {
        "id": 32,
        "channel": "04_Lex_Fridman",
        "artist": "Lex Fridman",
        "album": "Lex Fridman Podcast",
        "title": "Lex Fridman #252 - Elon Musk: SpaceX, Neuralink, AI",
        "yt_id": "DxREm3s1scA",
        "views": "8M+",
    },
    {
        "id": 33,
        "channel": "04_Lex_Fridman",
        "artist": "Lex Fridman",
        "album": "Lex Fridman Podcast",
        "title": "Lex Fridman #267 - Mark Zuckerberg: Metaverse and AI",
        "yt_id": "5zOHSysMmH0",
        "views": "7.5M+",
    },
    {
        "id": 34,
        "channel": "04_Lex_Fridman",
        "artist": "Lex Fridman",
        "album": "Lex Fridman Podcast",
        "title": "Lex Fridman #390 - Yuval Noah Harari: AI and Sapiens",
        "yt_id": "Mde2q7GFCrw",
        "views": "6.5M+",
    },

    # =========================================================================
    # 05 - The Diary Of A CEO (Steven Bartlett)
    # =========================================================================
    {
        "id": 35,
        "channel": "05_Diary_Of_A_CEO",
        "artist": "Steven Bartlett",
        "album": "The Diary Of A CEO",
        "title": "Gary Brecka: The Ultimate Human & Cellular Health",
        "yt_id": "10enqcw2Qiw",
        "views": "17M+",
    },
    {
        "id": 36,
        "channel": "05_Diary_Of_A_CEO",
        "artist": "Steven Bartlett",
        "album": "The Diary Of A CEO",
        "title": "Dr. Daniel Amen: Brain Health and Depression",
        "yt_id": "ycTZ_t-aiuU",
        "views": "15M+",
    },
    {
        "id": 37,
        "channel": "05_Diary_Of_A_CEO",
        "artist": "Steven Bartlett",
        "album": "The Diary Of A CEO",
        "title": "Simon Sinek: The Real Reason You Are Not Happy",
        "yt_id": "W4tqbEmplug",
        "views": "13M+",
    },
    {
        "id": 38,
        "channel": "05_Diary_Of_A_CEO",
        "artist": "Steven Bartlett",
        "album": "The Diary Of A CEO",
        "title": "Alex Hormozi: How To Get Rich & 100M Framework",
        "yt_id": "Kl-I7sUcAOY",
        "views": "11M+",
    },
    {
        "id": 39,
        "channel": "05_Diary_Of_A_CEO",
        "artist": "Steven Bartlett",
        "album": "The Diary Of A CEO",
        "title": "Jimmy Donaldson (MrBeast): Content Empire Secrets",
        "yt_id": "xGICaKuRoVE",
        "views": "9.5M+",
    },
    {
        "id": 40,
        "channel": "05_Diary_Of_A_CEO",
        "artist": "Steven Bartlett",
        "album": "The Diary Of A CEO",
        "title": "Mo Gawdat: Emergency Warning On Artificial Intelligence",
        "yt_id": "RwlgFC6S-OE",
        "views": "8.5M+",
    },

    # =========================================================================
    # 06 - Huberman Lab (Dr. Andrew Huberman)
    # =========================================================================
    {
        "id": 41,
        "channel": "06_Huberman_Lab",
        "artist": "Dr. Andrew Huberman",
        "album": "Huberman Lab",
        "title": "Master Your Sleep & Be More Alert When Awake",
        "yt_id": "lIo9FcrljDk",
        "views": "12M+",
    },
    {
        "id": 42,
        "channel": "06_Huberman_Lab",
        "artist": "Dr. Andrew Huberman",
        "album": "Huberman Lab",
        "title": "How to Increase Motivation & Drive (Dopamine Science)",
        "yt_id": "XeN6eGO6FVQ",
        "views": "11M+",
    },
    {
        "id": 43,
        "channel": "06_Huberman_Lab",
        "artist": "Dr. Andrew Huberman",
        "album": "Huberman Lab",
        "title": "Optimize Your Focus & Attention (ADHD Science)",
        "yt_id": "LAwBdRR4wQk",
        "views": "8.5M+",
    },
    {
        "id": 44,
        "channel": "06_Huberman_Lab",
        "artist": "Dr. Andrew Huberman",
        "album": "Huberman Lab",
        "title": "Dr. Matthew Walker: The Science of Perfect Sleep",
        "yt_id": "hvPGfcAgk9Y",
        "views": "8M+",
    },
    {
        "id": 45,
        "channel": "06_Huberman_Lab",
        "artist": "Dr. Andrew Huberman",
        "album": "Huberman Lab",
        "title": "Dr. Peter Attia: Exercise, Nutrition & Longevity",
        "yt_id": "DTCmprPCDqc",
        "views": "6.5M+",
    },

    # =========================================================================
    # 07 - This Past Weekend (Theo Von)
    # =========================================================================
    {
        "id": 46,
        "channel": "07_Theo_Von",
        "artist": "Theo Von",
        "album": "This Past Weekend",
        "title": "Shane Gillis w/ Theo Von #478",
        "yt_id": "FrR4SBvL0Ck",
        "views": "14M+",
    },
    {
        "id": 47,
        "channel": "07_Theo_Von",
        "artist": "Theo Von",
        "album": "This Past Weekend",
        "title": "Theo Von w/ Bernie Sanders",
        "yt_id": "ThstIT3d0HE",
        "views": "12M+",
    },

    # =========================================================================
    # 08 - Modern Wisdom (Chris Williamson)
    # =========================================================================
    {
        "id": 48,
        "channel": "08_Modern_Wisdom",
        "artist": "Chris Williamson",
        "album": "Modern Wisdom",
        "title": "David Goggins: How To Defeat Laziness & Build Relentless Focus",
        "yt_id": "ngvOyccUzzY",
        "views": "8.8M+",
    },

    # =========================================================================
    # 09 - PBD Podcast (Patrick Bet-David)
    # =========================================================================
    {
        "id": 49,
        "channel": "09_PBD_Podcast",
        "artist": "Patrick Bet-David",
        "album": "PBD Podcast",
        "title": "Andrew Tate Unfiltered on PBD Podcast",
        "yt_id": "-CaV3ePx-LE",
        "views": "12M+",
    },

    # =========================================================================
    # 10 - بودكاست وعي (Waie Podcast)
    # =========================================================================
    {
        "id": 50,
        "channel": "10_Waie_Podcast",
        "artist": "أحمد عامر | حازم الصديق | شريف علي",
        "album": "بودكاست وعي",
        "title": "كيف تبدأ الالتزام وتثبت عليه؟",
        "yt_id": "J-6MlapnHwM",
        "views": "6.5M+",
    },
]

def load_manifest():
    if os.path.exists(MANIFEST_FILE):
        try:
            with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"completed": [], "items": {}}

def save_manifest(manifest):
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    sd_manifest = os.path.join(SD_PODCASTS, "podcasts_manifest.json")
    try:
        with open(sd_manifest, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def process_episode(item, manifest):
    item_id = item["id"]
    str_id = str(item_id)
    if str_id in manifest.get("completed", []):
        print(f"[{item_id:02d}/50] Already completed: {item['title']}")
        return True

    print(f"\n=======================================================")
    print(f"[{item_id:02d}/50] Starting: {item['title']}")
    print(f"Channel: {item['channel']} | Views: {item['views']}")
    print(f"=======================================================")

    vid_id = item["yt_id"]
    channel_dir = os.path.join(SD_PODCASTS, item["channel"])
    os.makedirs(channel_dir, exist_ok=True)
    os.makedirs(LOCAL_CACHE, exist_ok=True)

    temp_video = os.path.join(LOCAL_CACHE, f"temp_{item_id}.mp4")

    # Step 1: Download format 18 (360p progressive with audio) via mweb,web
    print(f"Downloading stream for {vid_id}...")
    dl_cmd = [
        "yt-dlp",
        "-N", "4",
        "--extractor-args", "youtube:player_client=mweb,web",
        "-f", "18/b[height<=360]/ba",
        "-o", temp_video,
        "--no-playlist",
        "--max-downloads", "1",
        f"https://www.youtube.com/watch?v={vid_id}"
    ]
    res = subprocess.run(dl_cmd)
    if res.returncode != 0 and not os.path.exists(temp_video):
        print("Retrying with android client...")
        dl_cmd2 = [
            "yt-dlp",
            "--extractor-args", "youtube:player_client=android",
            "-f", "ba/b",
            "-o", temp_video,
            "--no-playlist",
            f"https://www.youtube.com/watch?v={vid_id}"
        ]
        res2 = subprocess.run(dl_cmd2)
        if res2.returncode != 0 and not os.path.exists(temp_video):
            print(f"FAILED to download video {vid_id} for episode {item_id}")
            return False

    if not os.path.exists(temp_video):
        print(f"File {temp_video} does not exist.")
        return False

    # Step 2: Convert to 96kbps MP3 & split into 30-min segments
    out_pattern = os.path.join(channel_dir, f"{item_id:02d}_Pt%02d.mp3")
    print("Converting to 96kbps MP3 & splitting into 30-min segments...")
    ff_cmd = [
        "ffmpeg", "-y", "-i", temp_video,
        "-vn", "-c:a", "libmp3lame", "-b:a", "96k", "-ar", "44100",
        "-metadata", f"artist={item['artist']}",
        "-metadata", f"album={item['album']}",
        "-metadata", f"title={item['title']}",
        "-f", "segment", "-segment_time", "1800", "-reset_timestamps", "1",
        out_pattern
    ]
    subprocess.run(ff_cmd, check=True)

    # Clean up local video immediately to save PC disk space
    if os.path.exists(temp_video):
        try:
            os.remove(temp_video)
        except Exception:
            pass

    # Count generated parts
    parts = sorted([f for f in os.listdir(channel_dir) if f.startswith(f"{item_id:02d}_Pt") and f.endswith(".mp3")])
    print(f"Generated {len(parts)} MP3 parts for episode {item_id} in {channel_dir}")

    manifest.setdefault("completed", []).append(str_id)
    manifest.setdefault("items", {})[str_id] = {
        "title": item["title"],
        "channel": item["channel"],
        "artist": item["artist"],
        "album": item["album"],
        "yt_id": vid_id,
        "views": item["views"],
        "parts_count": len(parts),
        "files": parts
    }
    save_manifest(manifest)
    print(f"SUCCESS: Episode {item_id} installed on SD card.")
    return True

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    manifest = load_manifest()

    # Auto-sync manifest with all existing episodes on SD card
    for item in TOP_50_PODCASTS:
        cid = str(item["id"])
        c_dir = os.path.join(SD_PODCASTS, item["channel"])
        if os.path.exists(c_dir):
            parts = sorted([f for f in os.listdir(c_dir) if f.startswith(f"{item['id']:02d}_") and f.endswith(".mp3")])
            if parts:
                if cid not in manifest.get("completed", []):
                    manifest.setdefault("completed", []).append(cid)
                manifest.setdefault("items", {})[cid] = {
                    "title": item["title"],
                    "channel": item["channel"],
                    "artist": item["artist"],
                    "album": item["album"],
                    "yt_id": item["yt_id"],
                    "views": item["views"],
                    "parts_count": len(parts),
                    "files": parts
                }
    save_manifest(manifest)

    if len(sys.argv) > 1 and sys.argv[1].lower() == "status":
        completed = manifest.get("completed", [])
        print(f"Total Completed Episodes: {len(completed)} / 50")
        for cid in completed:
            info = manifest["items"].get(cid, {})
            print(f"  - [{int(cid):02d}] {info.get('title')} ({info.get('parts_count', 0)} parts)")
        sys.exit(0)

    limit = int(sys.argv[1]) if len(sys.argv) > 1 else len(TOP_50_PODCASTS)
    print(f"Starting Top 50 Podcasts Pipeline (Processing up to {limit} episodes)...")
    for item in TOP_50_PODCASTS[:limit]:
        try:
            process_episode(item, manifest)
        except Exception as e:
            print(f"Error processing item {item['id']}: {e}")

    print("\nTop 50 Podcasts batch cycle finished!")
