import argparse
import logging
import sys
from pathlib import Path

import yaml

from tasks.cleaner import clean_old_files
from tasks.downloader import download_file
from tasks.reporter import generate_report


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="Python Automation Toolkit")
    parser.add_argument(
        "-c", "--config",
        default="config.yaml",
        help="Path to config file (default: config.yaml)",
    )
    args = parser.parse_args()

    try:
        cfg = load_config(args.config)
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        sys.exit(1)

    logger.info(" Starting automation tasks...")
    print("--------------------------------")

    # Task 1: Clean old files
    print("\n[1/3] Cleaning old files...")
    try:
        clean_old_files(
            directory=cfg.get("clean_dir", ""),
            max_age_days=cfg.get("max_age_days", 7),
        )
    except Exception as e:
        logger.error(f"Clean task failed: {e}")

    # Task 2: Download file
    print("\n[2/3] Downloading file...")
    try:
        download_file(
            url=cfg.get("download_url", ""),
            dest=cfg.get("download_path", ""),
        )
    except Exception as e:
        logger.error(f"Download task failed: {e}")

    # Task 3: Generate report
    print("\n[3/3] Generating report...")
    report = generate_report()
    print(report)

    print("--------------------------------")
    logger.info(" All tasks completed")


if __name__ == "__main__":
    main()
