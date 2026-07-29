"""
Download a file from a URL and save it locally.
"""

import logging
from pathlib import Path

import requests

logger = logging.getLogger(__name__)


def download_file(url: str, dest: str, timeout: int = 30) -> int:
    """
    Download file from url and save to dest.
    Returns the number of bytes written.
    """
    if not url:
        print("  No download_url configured, skipping...")
        return 0

    dest_path = Path(dest)
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        response = requests.get(url, timeout=timeout, stream=True)
        response.raise_for_status()

        total_bytes = 0
        with open(dest_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    total_bytes += len(chunk)

        print(f"  Downloaded {url} → {dest} ({total_bytes} bytes)")
        return total_bytes

    except requests.RequestException as e:
        raise RuntimeError(f"Download failed: {e}") from e
