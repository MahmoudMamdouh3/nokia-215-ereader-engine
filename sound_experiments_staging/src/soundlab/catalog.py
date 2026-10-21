"""
SQLite Catalog: single source of truth for all recordings, checksums,
fingerprints, duplicates, and voice segments.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from soundlab.config import config


class CatalogDB:
    """Interface to the SQLite metadata catalog in WAL mode."""

    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = db_path or config.catalog_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def get_connection(self) -> sqlite3.Connection:
        """Get an active SQLite connection configured with WAL and busy timeout."""
        conn = sqlite3.connect(str(self.db_path), timeout=30.0)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode = WAL;")
        conn.execute("PRAGMA synchronous = NORMAL;")
        conn.execute("PRAGMA busy_timeout = 30000;")
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def _init_db(self) -> None:
        """Create schema tables and indexes if they do not exist."""
        with self.get_connection() as conn:
            conn.executescript("""
            CREATE TABLE IF NOT EXISTS sources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                platform_id TEXT NOT NULL,
                url TEXT NOT NULL UNIQUE,
                title TEXT,
                duration_sec REAL,
                uploader TEXT,
                upload_date TEXT,
                metadata_json TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS raw_files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_id INTEGER REFERENCES sources(id) ON DELETE CASCADE,
                file_path TEXT NOT NULL UNIQUE,
                file_size_bytes INTEGER NOT NULL,
                duration_sec REAL,
                sha256_hash TEXT NOT NULL,
                chromaprint_fp TEXT,
                audio_format TEXT,
                sample_rate INTEGER,
                channels INTEGER,
                bitrate INTEGER,
                status TEXT NOT NULL DEFAULT 'active',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE INDEX IF NOT EXISTS idx_raw_files_sha256 ON raw_files(sha256_hash);
            CREATE INDEX IF NOT EXISTS idx_raw_files_status ON raw_files(status);

            CREATE TABLE IF NOT EXISTS duplicates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                raw_file_id INTEGER NOT NULL REFERENCES raw_files(id) ON DELETE CASCADE,
                duplicate_of_id INTEGER NOT NULL REFERENCES raw_files(id) ON DELETE CASCADE,
                match_type TEXT NOT NULL,
                similarity_score REAL NOT NULL,
                details TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE INDEX IF NOT EXISTS idx_duplicates_target ON duplicates(duplicate_of_id);

            CREATE TABLE IF NOT EXISTS kobe_segments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                raw_file_id INTEGER NOT NULL REFERENCES raw_files(id) ON DELETE CASCADE,
                start_sec REAL NOT NULL,
                end_sec REAL NOT NULL,
                duration_sec REAL NOT NULL,
                speaker_score REAL NOT NULL,
                era_tag TEXT,
                snr_db REAL,
                transcription TEXT,
                verified_by_human INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE INDEX IF NOT EXISTS idx_segments_raw_file ON kobe_segments(raw_file_id);
            CREATE INDEX IF NOT EXISTS idx_segments_score ON kobe_segments(speaker_score);
            """)

            # Ensure duration_sec exists in raw_files
            cursor = conn.execute("PRAGMA table_info(raw_files);")
            cols = [r["name"] for r in cursor.fetchall()]
            if "duration_sec" not in cols:
                conn.execute("ALTER TABLE raw_files ADD COLUMN duration_sec REAL;")

    def register_source(
        self,
        platform: str,
        platform_id: str,
        url: str,
        title: Optional[str] = None,
        duration_sec: Optional[float] = None,
        uploader: Optional[str] = None,
        upload_date: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> int:
        """Register or retrieve an existing source URL."""
        with self.get_connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO sources (platform, platform_id, url, title, duration_sec, uploader, upload_date, metadata_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(url) DO UPDATE SET
                    title = coalesce(excluded.title, sources.title),
                    duration_sec = coalesce(excluded.duration_sec, sources.duration_sec),
                    uploader = coalesce(excluded.uploader, sources.uploader),
                    upload_date = coalesce(excluded.upload_date, sources.upload_date),
                    metadata_json = coalesce(excluded.metadata_json, sources.metadata_json)
                RETURNING id;
                """,
                (
                    platform,
                    platform_id,
                    url,
                    title,
                    duration_sec,
                    uploader,
                    upload_date,
                    json.dumps(metadata or {}),
                ),
            )
            row = cursor.fetchone()
            return row["id"]

    def register_raw_file(
        self,
        source_id: int,
        file_path: Path,
        file_size_bytes: int,
        sha256_hash: str,
        duration_sec: Optional[float] = None,
        chromaprint_fp: Optional[str] = None,
        audio_format: Optional[str] = None,
        sample_rate: Optional[int] = None,
        channels: Optional[int] = None,
        bitrate: Optional[int] = None,
    ) -> int:
        """Register a downloaded raw audio recording."""
        with self.get_connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO raw_files (
                    source_id, file_path, file_size_bytes, duration_sec, sha256_hash,
                    chromaprint_fp, audio_format, sample_rate, channels, bitrate, status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'active')
                RETURNING id;
                """,
                (
                    source_id,
                    str(file_path),
                    file_size_bytes,
                    duration_sec,
                    sha256_hash,
                    chromaprint_fp,
                    audio_format,
                    sample_rate,
                    channels,
                    bitrate,
                ),
            )
            row = cursor.fetchone()
            return row["id"]


    def find_by_sha256(self, sha256_hash: str) -> Optional[sqlite3.Row]:
        """Find an active raw file by exact SHA-256."""
        with self.get_connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM raw_files WHERE sha256_hash = ? AND status = 'active' LIMIT 1;",
                (sha256_hash,),
            )
            return cursor.fetchone()

    def record_duplicate(
        self,
        raw_file_id: int,
        duplicate_of_id: int,
        match_type: str,
        similarity_score: float,
        details: Optional[str] = None,
    ) -> None:
        """Log a duplicate detection link and mark duplicate file status."""
        with self.get_connection() as conn:
            conn.execute(
                """
                INSERT INTO duplicates (raw_file_id, duplicate_of_id, match_type, similarity_score, details)
                VALUES (?, ?, ?, ?, ?);
                """,
                (raw_file_id, duplicate_of_id, match_type, similarity_score, details),
            )
            conn.execute(
                "UPDATE raw_files SET status = 'quarantined_duplicate' WHERE id = ?;",
                (raw_file_id,),
            )

    def get_stats(self) -> Dict[str, Any]:
        """Retrieve total files, durations, duplicate count, and Kobe speech yield."""
        with self.get_connection() as conn:
            total_sources = conn.execute("SELECT count(*) as c FROM sources;").fetchone()["c"]
            active_files = conn.execute(
                "SELECT count(*) as c, coalesce(sum(file_size_bytes), 0) as s FROM raw_files WHERE status = 'active';"
            ).fetchone()
            duplicate_files = conn.execute(
                "SELECT count(*) as c FROM raw_files WHERE status = 'quarantined_duplicate';"
            ).fetchone()["c"]
            segments_stat = conn.execute(
                "SELECT count(*) as c, coalesce(sum(duration_sec), 0.0) as dur FROM kobe_segments;"
            ).fetchone()

            return {
                "total_sources": total_sources,
                "active_files_count": active_files["c"],
                "active_files_bytes": active_files["s"],
                "duplicates_detected": duplicate_files,
                "kobe_segments_count": segments_stat["c"],
                "kobe_total_hours": segments_stat["dur"] / 3600.0,
            }
