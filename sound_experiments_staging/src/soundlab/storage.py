"""
Storage Manager: disk space guarding, spillover between E: and D:,
atomic file writing, checksumming, and non-destructive quarantine.
"""

from __future__ import annotations

import hashlib
import os
import shutil
from pathlib import Path
from typing import Optional, Tuple
from soundlab.config import config


def get_free_space_gb(path: Path) -> float:
    """Return free space in gigabytes for the volume containing path."""
    try:
        usage = shutil.disk_usage(path.anchor if path.anchor else str(path))
        return usage.free / (1024.0 ** 3)
    except Exception:
        return 0.0


def compute_sha256(file_path: Path, chunk_size: int = 65536) -> str:
    """Compute standard SHA-256 checksum of a file."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()


class StorageManager:
    """Manages raw audio storage tiers, disk boundaries, and quarantines."""

    def __init__(self):
        config.ensure_directories()
        self.raw_dir = config.raw_dir
        self.overflow_dir = config.raw_overflow_dir
        self.quarantine_dir = config.quarantine_dir
        self.disk_floor_gb = config.disk_floor_gb

    def resolve_destination(self, platform: str, platform_id: str, filename: str) -> Path:
        """
        Determine target file path based on drive free space.
        Prefers E:\ (primary raw archive) unless free space < disk_floor_gb.
        Spills gracefully to D:\ when primary is near full.
        """
        free_e = get_free_space_gb(self.raw_dir)
        
        rel_subpath = Path("sources") / platform / platform_id / filename
        if free_e > self.disk_floor_gb:
            target = self.raw_dir / rel_subpath
        else:
            target = self.overflow_dir / rel_subpath
            
        target.parent.mkdir(parents=True, exist_ok=True)
        return target

    def atomic_move(self, src: Path, dest: Path) -> Path:
        """Atomically place a file at destination (using temporary file if crossing devices)."""
        dest.parent.mkdir(parents=True, exist_ok=True)
        temp_dest = dest.with_suffix(dest.suffix + ".tmp")
        try:
            shutil.copy2(src, temp_dest)
            os.replace(temp_dest, dest)
            if src.exists() and src != dest:
                src.unlink(missing_ok=True)
        finally:
            if temp_dest.exists():
                temp_dest.unlink(missing_ok=True)
        return dest

    def quarantine(self, file_path: Path, duplicate_of_id: str) -> Path:
        """
        Move a duplicate audio file to quarantine.
        Never permanently deletes raw data.
        """
        target = self.quarantine_dir / f"dup_of_{duplicate_of_id}" / file_path.name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file_path), str(target))
        return target
