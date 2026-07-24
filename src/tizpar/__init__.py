"""
تیزپر (Tizpar) — A Swift & Full Persian Developer Toolkit
==========================================================

یک ابزارک توسعه‌دهنده فارسی برای انجام سریع کارهای روزمره
A Persian developer toolkit for getting things done swiftly.

Version: 0.0.1
Author: ZendanTeam
"""

__version__ = "0.0.1"
__author__ = "ZendanTeam"
__license__ = "MIT"
__description__ = "تیزپر - Swift Persian Developer Toolkit"

from tizpar.core import console
from tizpar.utils.persian import (
    to_persian_digits,
    to_english_digits,
    is_persian_text,
    remove_diacritics,
)
from tizpar.utils.system import (
    get_system_info,
    get_python_info,
    disk_usage,
    memory_usage,
)
from tizpar.utils.network import (
    check_url,
    get_public_ip,
    ping_host,
)

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "__description__",
    # Core
    "console",
    # Persian utils
    "to_persian_digits",
    "to_english_digits",
    "is_persian_text",
    "remove_diacritics",
    # System utils
    "get_system_info",
    "get_python_info",
    "disk_usage",
    "memory_usage",
    # Network utils
    "check_url",
    "get_public_ip",
    "ping_host",
]
