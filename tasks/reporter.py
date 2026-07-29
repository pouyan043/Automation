"""
Generate a simple system report.
"""

import platform
import os
from datetime import datetime, timezone


def generate_report() -> str:
    """Return a formatted system report string."""
    report = f"""
========== Automation Report ==========
Time:       {datetime.now(timezone.utc).isoformat()}
Hostname:   {platform.node()}
OS:         {platform.system()} {platform.release()}
Arch:       {platform.machine()}
Python:     {platform.python_version()}
CPU Count:  {os.cpu_count()}
=======================================
"""
    return report
