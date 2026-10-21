"""
Ingestion Engine:
- Web discovery & download via yt-dlp (YouTube, Vimeo, SoundCloud, Internet Archive, web archives)
- Local media import & audio extraction via ffmpeg (movie files, DVD/Blu-ray rips, raw archives)
- Automatic deduplication and cataloging
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional

from soundlab.catalog import CatalogDB
from soundlab.config import config
from soundlab.dedup import DeduplicationEngine
from soundlab.storage import StorageManager


KOBE_DISCOVERY_QUERIES = [
    # Long-Form Podcasts & In-Depth Sit-Downs
    "Kobe Bryant All The Smoke podcast full episode Matt Barnes",
    "Kobe Bryant on Jimmy Kimmel Live full interview uncut",
    "Kobe Bryant Graham Bensinger in-depth interview uncut",
    "Kobe Bryant Lewis Howes School of Greatness podcast",
    "Kobe Bryant Patrick Bet-David Valuetainment full interview",
    "Kobe Bryant The Corp podcast Alex Rodriguez full episode",
    "Kobe Bryant Jay Shetty On Purpose podcast full interview",
    "Kobe Bryant Dan Patrick Show full interview audio",
    "Kobe Bryant Howard Stern interview uncut audio",
    "Kobe Bryant The Daily Show Trevor Noah interview uncut",

    # University & Leadership Keynotes / Seminars
    "Kobe Bryant Stanford Graduate School of Business interview",
    "Kobe Bryant Boston College chief executives club speech",
    "Kobe Bryant USC Annenberg School speech interview uncut",
    "Kobe Bryant Wharton business school talk audio",
    "Kobe Bryant Mamba Mentality seminar keynote full uncut",

    # Documentaries, Studio Audiobooks, & Screenplays
    "Kobe Bryant Muse documentary raw voiceover narration audio",
    "Kobe Bryant Dear Basketball original studio narration voice",
    "Kobe Bryant The Wizenard Series audiobook narration audio",
    "Kobe Bryant Detail ESPN analysis breakdown uncut audio",
    "Kobe Bryant Oscar acceptance speech backstage interview 2018",

    # Multilingual & International Phonation
    "Kobe Bryant parla italiano intervista completa Rai Sky",
    "Kobe Bryant intervista integrale italiano Radio Deejay",
    "Kobe Bryant habla espanol entrevista completa Univision",
    "Kobe Bryant entrevista completa espanol ESPN Deportes",
    "Kobe Bryant Milan AC Milan football uncut interview Italian",
    "Kobe Bryant China tour Beijing Shanghai press conference raw",

    # NBA Finals & Championship Press Conferences (Uncut Raw)
    "Kobe Bryant 2000 NBA finals post game uncut audio",
    "Kobe Bryant 2001 NBA finals post game press conference uncut",
    "Kobe Bryant 2002 NBA finals post game press conference uncut",
    "Kobe Bryant 2008 Western Conference Finals post game uncut",
    "Kobe Bryant 2009 NBA finals Game 5 trophy ceremony press conference",
    "Kobe Bryant 2010 NBA finals Game 7 press conference uncut raw",

    # Historic Milestones & Career Eras
    "Kobe Bryant 81 point game post game press conference uncut audio",
    "Kobe Bryant 60 point final game post game press conference uncut",
    "Kobe Bryant retirement ceremony speech Staples Center full audio",
    "Kobe Bryant 1996 NBA draft day press conference uncut",
    "Kobe Bryant rookie interview 1996 1997 uncut audio",
    "Kobe Bryant 1997 Slam Dunk contest post contest interview",
    "Kobe Bryant Lower Merion state championship speech raw",

    # Olympic Gold Medal Campaigns & Team USA
    "Kobe Bryant 2008 Beijing Olympics Redeem Team uncut postgame",
    "Kobe Bryant 2008 Beijing Olympic press conference USA Basketball",
    "Kobe Bryant 2012 London Olympics press conference uncut audio",
    "Kobe Bryant 2012 Team USA practice interview uncut",

    # On-Court Mic'd Up, Wiring, & Coaching
    "Kobe Bryant wired for sound mic'd up full season uncut",
    "Kobe Bryant trash talk on court microphone audio raw",
    "Kobe Bryant coaching Mamba Sports Academy practice instruction audio",
    "Kobe Bryant commercial Nike puppet voiceover uncut audio",
    "Kobe Bryant radio interview ESPN uncut audio",
    "Kobe Bryant post game press conference full uncut raw 2008",
]


class IngestionEngine:
    """Manages audio downloads from internet sources and local inbox imports."""

    def __init__(
        self,
        catalog: Optional[CatalogDB] = None,
        storage: Optional[StorageManager] = None,
        dedup: Optional[DeduplicationEngine] = None,
    ):
        self.catalog = catalog or CatalogDB()
        self.storage = storage or StorageManager()
        self.dedup = dedup or DeduplicationEngine(self.catalog, self.storage)

    def download_url(self, url: str, platform: str = "web") -> Optional[Path]:
        """
        Download audio from any URL supported by yt-dlp, extract best audio stream,
        compute fingerprints, check for duplicates, and register into catalog.
        """
        # Fast pre-check: if URL is already cataloged, skip downloading
        with self.catalog.get_connection() as conn:
            existing = conn.execute("SELECT id FROM sources WHERE url = ?;", (url,)).fetchone()
            if existing:
                print(f"[Skipping] Already in catalog: {url}")
                return None

        # Fetch metadata first
        meta_cmd = ["yt-dlp", "--dump-json", "--no-warnings", url]
        try:
            meta_res = subprocess.run(meta_cmd, capture_output=True, text=True, check=True, timeout=90)
            meta = json.loads(meta_res.stdout)
        except Exception as e:
            print(f"[Ingest Error] Failed to fetch metadata for {url}: {e}")
            return None

        video_id = meta.get("id", "unknown_id")
        title = meta.get("title", "Untitled")
        safe_title = title.encode("ascii", "replace").decode("ascii")
        duration = meta.get("duration", 0.0)
        uploader = meta.get("uploader", "unknown")
        upload_date = meta.get("upload_date", "")
        extractor = meta.get("extractor", platform)

        # Strict Pre-Download Relevance Guard: Ensure title explicitly features Kobe Bryant
        title_lower = title.lower()
        kobe_keywords = ["kobe", "bryant", "mamba", "dear basketball", "wizenard"]

        matches_kobe = any(k in title_lower for k in kobe_keywords)
        if not matches_kobe:
            print(f"[Rejected Non-Kobe] Skipping '{safe_title}' ({url}): Video title does not reference Kobe Bryant.")
            return None

        # Exclude third-party videos where others talk *about* Kobe rather than Kobe speaking
        non_kobe_indicators = [
            "narrated by",
            "reveals kobe",
            "reflects on kobe",
            "reacts to kobe",
            "remembers kobe",
            "remembering kobe",
            "talks about kobe",
            "talking about kobe",
            "memorializing kobe",
            "coaching kobe",
            "what it was like coaching",
            "vanessa bryant",
            "michael jordan",
            "memorial service",
            "memorial",
            "eulogy",
            "la morte di kobe",
            "morte di kobe",
            "racconta:",
            "hommage",
            "muerte de",
            "muere ",
            "suegra de",
            "se divorcia",
            "rueda de prensa",
            "pau gasol",
            "llorando",
            "numerología",
            "entrenaba con",
            "homenaje",
            "tributo",
            "accidente",
            "tragedia",
            "funeral",
            "entierro",
            "despiden a",
            "autopsia",
            "helicoptero",
            "helicóptero",
            "death",
            "r.i.p",
            "rest in peace",
            "passed away",
            "audiobook) by",
            "audiobook by",
            "(audiobook)",
            "dies at",
            "promotes witchcraft",
            "satanism",
            "takes final bow",
            "faye bryant",
            "the wizenard series: season one",
            "training day book 1",
            "crash",
            "after he died",
            "disrespects",
            "talking trash",
            "passing of",
            "tmz",
            "on guarding",
            "guarding kobe",
            "dissing kobe",
            " diss ",
            "diss 2010",
            "diss track",
            "b.e. - kobe",
            "last 3 minutes of",
            "last minutes of",
            "farewell game |",
            "farewell game (",
            " on the time ",
            " on kobe",
            " on playing with",
            " on facing kobe",
            "coach k:",
            "coach k ",
            "drops 60 in",
            "drops 81 in",
            "documentary",
            "assists!",
            "legends share",
            "nba legends share",
            "craziest kobe bryant story",
            "resumen libro",
            "resumen del libro",
            "lecciones que nos dejó",
            "una amistad más allá",
            "más allá de las canchas",
            "choc nel mondo",
            "unomattina",
            "pays tribute",
            "paying tribute",
            "tribute to kobe",
            "tribute to gianna",
            "first take",
            "skip bayless",
            "stephen a.",
            "shannon sharpe",
            "undisputed",
            "max kellerman",
            "colin cowherd",
            "debunked",
            "the lakers dynasty",
            "speaks on kobe",
            "speak on kobe",
            "work ethic stories",
            "kobe stories",
            "kobe bryant stories",
            "arriving to see",
            "arriving at",
            "arrives at",
            "game highlights",
            "full game highlights",
            "highlights |",
            "highlights -",
            "point game!",
            "point game at",
            "amazing last ",
            "final game vs jazz",
            "kobe draft 1996",
            "la lettera di",
            "lettera di",
            "kobe taught ",
            "behind the scenes:",
            "behind the scenes -",
            " on interviewing ",
            "honors kobe",
            "honoring kobe",
            "duel highlights",
            "epic duel",
            "rubin report",
        ]
        is_third_party = any(ind in title_lower for ind in non_kobe_indicators)
        if not is_third_party:
            for talk_phrase in [
                "talks about ", "talking about ", "remembers ", "remembering ",
                "reflects on ", "reflecting on ", "reacts to ", "reacting to ",
                "reactions to ", "honors kobe", "honoring kobe",
                "says kobe", "say kobe", "claims kobe", "breaks down kobe",
                " on was kobe", " on whether kobe", "discusses ", "discussing ",
                "told kobe ", "tells kobe ",
            ]:
                if talk_phrase in title_lower:
                    idx = title_lower.find(talk_phrase)
                    prefix = title_lower[:idx]
                    if not any(k in prefix for k in ["kobe", "bryant", "mamba"]):
                        is_third_party = True
                        break

        if is_third_party:
            print(f"[Rejected Third-Party Tribute] Skipping '{safe_title}' ({url}): Video appears to be others talking about Kobe.")
            return None
        temp_dir = config.derived_dir / "tmp_downloads"
        temp_dir.mkdir(parents=True, exist_ok=True)
        out_template = str(temp_dir / f"{video_id}.%(ext)s")

        # Download best audio stream without forced re-encoding
        dl_cmd = [
            "yt-dlp",
            "-x",
            "--audio-quality", "0",
            "-o", out_template,
            "--no-playlist",
            "--retries", "10",
            url,
        ]
        try:
            subprocess.run(dl_cmd, check=True, timeout=600)
        except Exception as e:
            print(f"[Ingest Error] Download failed for {url}: {e}")
            return None

        # Find downloaded audio file
        downloaded_files = list(temp_dir.glob(f"{video_id}.*"))
        if not downloaded_files:
            print(f"[Ingest Error] Downloaded file not found for id {video_id}")
            return None

        temp_audio = downloaded_files[0]
        ext = temp_audio.suffix.lstrip(".")

        # Step 1: Compute hashes & acoustic fingerprint
        sha256, fp, dur = self.dedup.inspect_file(temp_audio)
        duration_final = dur or duration

        # Step 2: Check for duplicates against the catalog
        dup_match = self.dedup.check_duplicate(sha256, fp, duration_final)

        # Step 3: Register source
        source_id = self.catalog.register_source(
            platform=extractor,
            platform_id=video_id,
            url=url,
            title=title,
            duration_sec=duration_final,
            uploader=uploader,
            upload_date=upload_date,
            metadata=meta,
        )

        # Step 4: Resolve destination storage
        dest_path = self.storage.resolve_destination(extractor, video_id, f"audio.{ext}")
        final_path = self.storage.atomic_move(temp_audio, dest_path)
        file_size = final_path.stat().st_size

        # Step 5: Register raw file
        raw_id = self.catalog.register_raw_file(
            source_id=source_id,
            file_path=final_path,
            file_size_bytes=file_size,
            duration_sec=duration_final,
            sha256_hash=sha256,
            chromaprint_fp=fp,
            audio_format=ext,
        )

        if dup_match:
            dup_of_id, m_type, score, details = dup_match
            print(f"[Dedup Alert] File is duplicate of raw #{dup_of_id} ({m_type}, score: {score:.2f})")
            self.catalog.record_duplicate(raw_id, dup_of_id, m_type, score, details)
            # Move to quarantine
            self.storage.quarantine(final_path, str(dup_of_id))
            return None

        print(f"[Ingested] Registered clean recording #{raw_id}: {safe_title} ({final_path.name})")
        return final_path

    def ingest_pending_downloads(self) -> List[Path]:
        """
        Process any completed audio files sitting in the tmp_downloads directory.
        """
        temp_dir = config.derived_dir / "tmp_downloads"
        candidates = [
            f for f in temp_dir.glob("*.*")
            if f.is_file() and not f.name.endswith(".part") and f.suffix.lower() in [".opus", ".m4a", ".mp3", ".webm", ".wav"]
        ]
        results = []
        for f in candidates:
            video_id = f.stem
            ext = f.suffix.lstrip(".")
            sha256, fp, dur = self.dedup.inspect_file(f)
            dup_match = self.dedup.check_duplicate(sha256, fp, dur)

            source_id = self.catalog.register_source(
                platform="youtube",
                platform_id=video_id,
                url=f"https://www.youtube.com/watch?v={video_id}",
                title=f"YouTube Recording {video_id}",
                duration_sec=dur or 0.0,
            )

            dest_path = self.storage.resolve_destination("youtube", video_id, f"audio.{ext}")
            final_path = self.storage.atomic_move(f, dest_path)
            file_size = final_path.stat().st_size

            raw_id = self.catalog.register_raw_file(
                source_id=source_id,
                file_path=final_path,
                file_size_bytes=file_size,
                duration_sec=dur,
                sha256_hash=sha256,
                chromaprint_fp=fp,
                audio_format=ext,
            )

            if dup_match:
                dup_of_id, m_type, score, details = dup_match
                self.catalog.record_duplicate(raw_id, dup_of_id, m_type, score, details)
                self.storage.quarantine(final_path, str(dup_of_id))
            else:
                results.append(final_path)

        return results


    def process_inbox(self) -> List[Path]:
        """
        Scan inbox/ directory for manually dropped audio/video files (e.g. film/doc extractions),
        extract clean audio, hash, deduplicate, and catalog them.
        """
        inbox_files = [
            f for f in config.inbox_dir.rglob("*")
            if f.is_file() and f.suffix.lower() in [".wav", ".flac", ".mp3", ".m4a", ".mp4", ".mkv", ".mov", ".aac", ".opus"]
        ]
        processed = []

        for f in inbox_files:
            file_id = f.stem
            ext = f.suffix.lower().lstrip(".")
            temp_extracted = f

            # If it's a video container, extract audio stream with ffmpeg
            if ext in ["mp4", "mkv", "mov"]:
                temp_audio_path = config.derived_dir / "tmp_inbox" / f"{file_id}.wav"
                temp_audio_path.parent.mkdir(parents=True, exist_ok=True)
                ff_cmd = [
                    "ffmpeg", "-y", "-i", str(f),
                    "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "1",
                    str(temp_audio_path)
                ]
                try:
                    subprocess.run(ff_cmd, check=True, capture_output=True)
                    temp_extracted = temp_audio_path
                    ext = "wav"
                except Exception as e:
                    print(f"[Inbox Error] Failed to extract audio from {f}: {e}")
                    continue

            sha256, fp, dur = self.dedup.inspect_file(temp_extracted)
            dup_match = self.dedup.check_duplicate(sha256, fp, dur)

            source_id = self.catalog.register_source(
                platform="local_inbox",
                platform_id=file_id,
                url=f"file://{f.name}",
                title=f.name,
                duration_sec=dur or 0.0,
            )

            dest_path = self.storage.resolve_destination("inbox", file_id, f"audio.{ext}")
            final_path = self.storage.atomic_move(temp_extracted, dest_path)
            file_size = final_path.stat().st_size

            raw_id = self.catalog.register_raw_file(
                source_id=source_id,
                file_path=final_path,
                file_size_bytes=file_size,
                duration_sec=dur,
                sha256_hash=sha256,
                chromaprint_fp=fp,
                audio_format=ext,
            )

            if dup_match:
                dup_of_id, m_type, score, details = dup_match
                self.catalog.record_duplicate(raw_id, dup_of_id, m_type, score, details)
                self.storage.quarantine(final_path, str(dup_of_id))
            else:
                processed.append(final_path)

        return processed
