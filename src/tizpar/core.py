"""
تیزپر Core Module — Rich Console & Shared Utilities
"""

from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print as rprint

# تِم اختصاصی تیزپر با رنگ‌های ایرانی
tizpar_theme = Theme(
    {
        "info": "bold cyan",
        "warning": "bold yellow",
        "error": "bold red",
        "success": "bold green",
        "highlight": "bold magenta",
        "title": "bold white on blue",
        "persian": "bold cyan",
    }
)

console = Console(theme=tizpar_theme, width=100)

__all__ = [
    "console",
    "tizpar_theme",
    "Table",
    "Panel",
    "Progress",
    "SpinnerColumn",
    "TextColumn",
    "rprint",
]
