"""
Configuration and Path Management for Sound Experiments.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any, Dict, Optional
import yaml

# Base project paths
WORKSPACE_DIR = Path(r"E:\Sound Experiments")
RAW_DATABASE_DIR = WORKSPACE_DIR / "Kobe bryant Database raw"
CATALOG_DB_PATH = RAW_DATABASE_DIR / "_catalog" / "catalog.sqlite"
RAW_SOURCES_DIR = RAW_DATABASE_DIR / "sources"
QUARANTINE_DIR = RAW_DATABASE_DIR / "_quarantine" / "duplicates"
INBOX_DIR = RAW_DATABASE_DIR / "inbox"
MANIFESTS_DIR = RAW_DATABASE_DIR / "_manifests"

# Overflow & Scratch paths on D: drive
OVERFLOW_DIR = Path(r"D:\SoundExperiments")
RAW_OVERFLOW_DIR = OVERFLOW_DIR / "raw_overflow"
DERIVED_DIR = OVERFLOW_DIR / "derived"
MODELS_CACHE_DIR = OVERFLOW_DIR / "models"
LOGS_DIR = OVERFLOW_DIR / "logs"

# Hardware thresholds
DEFAULT_DISK_FLOOR_GB = 12.0  # Keep at least 12 GB free on E:
DEFAULT_RAW_BUDGET_GB = 60.0  # Cap on E: before spilling to D:
GPU_VRAM_CEILING_MIB = 7000   # For 8 GB RTX 4060 laptop
RAM_HEADROOM_GB = 2.0         # Keep 2 GB RAM free for system


class SoundlabConfig:
    """Central configuration object."""

    def __init__(self, hardware_yaml_path: Optional[Path] = None):
        self.raw_dir = RAW_DATABASE_DIR
        self.raw_overflow_dir = RAW_OVERFLOW_DIR
        self.catalog_path = CATALOG_DB_PATH
        self.quarantine_dir = QUARANTINE_DIR
        self.inbox_dir = INBOX_DIR
        self.manifests_dir = MANIFESTS_DIR
        self.derived_dir = DERIVED_DIR
        self.models_dir = MODELS_CACHE_DIR
        self.logs_dir = LOGS_DIR

        self.disk_floor_gb = DEFAULT_DISK_FLOOR_GB
        self.raw_budget_gb = DEFAULT_RAW_BUDGET_GB
        self.gpu_vram_ceiling_mib = GPU_VRAM_CEILING_MIB

        self.hardware_profile: Dict[str, Any] = {}
        if hardware_yaml_path and hardware_yaml_path.exists():
            try:
                with open(hardware_yaml_path, "r", encoding="utf-8") as f:
                    self.hardware_profile = yaml.safe_load(f) or {}
            except Exception:
                pass

    def ensure_directories(self) -> None:
        """Create all required project directories."""
        for d in [
            self.raw_dir,
            self.raw_dir / "sources",
            self.raw_dir / "_catalog",
            self.quarantine_dir,
            self.inbox_dir,
            self.manifests_dir,
            self.raw_overflow_dir,
            self.derived_dir,
            self.models_dir,
            self.logs_dir,
        ]:
            d.mkdir(parents=True, exist_ok=True)


config = SoundlabConfig(WORKSPACE_DIR / "configs" / "hardware_profile.yaml")
