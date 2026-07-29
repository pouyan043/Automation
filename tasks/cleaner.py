"""
Clean old files from a directory based on age.
"""

import logging
from datetime import datetime, timedelta
from pathlib import Path

logger = logging.getLogger(__name__)


def clean_old_files(directory: str, max_age_days: int = 7) -> int:
    """
    Remove files older than max_age_days from the given directory.
    Returns the number of deleted files.
    """
    if not directory:
        print("  No clean_dir configured, skipping...")
        return 0

    path = Path(directory)
    if not path.exists():
        print(f"  Directory {directory} does not exist, creating it...")
        path.mkdir(parents=True, exist_ok=True)
        return 0

    cutoff = datetime.now() - timedelta(days=max_age_days)
    deleted = 0

    for file_path in path.rglob("*"):
        if not file_path.is_file():
            continue

        mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
        if mtime < cutoff:
            try:
                file_path.unlink()
                deleted += 1
                print(f"  Deleted: {file_path}")
            except OSError as e:
                logger.error(f"Failed to delete {file_path}: {e}")

    print(f"  Cleaned {deleted} old file(s) from {directory}")
    return deleted
