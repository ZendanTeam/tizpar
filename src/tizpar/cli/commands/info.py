"""
Info Commands — نمایش اطلاعات تیزپر و سیستم
"""

import click
from tizpar import __version__, __author__, __license__, console
from tizpar.utils.system import get_system_info, get_python_info
from rich.table import Table


@click.command(name="info", help="نمایش اطلاعات تیزپر و سیستم")
def info() -> None:
    """نمایش اطلاعات کامل تیزپر و وضعیت سیستم"""
    sys_info = get_system_info()
    py_info = get_python_info()

    # Project info table
    table = Table(title="⚡ تیزپر — اطلاعات پروژه", border_style="cyan")
    table.add_column("کلید", style="bold yellow")
    table.add_column("مقدار", style="white")
    table.add_row("نسخه", __version__)
    table.add_row("نویسنده", __author__)
    table.add_row("مجوز", __license__)
    table.add_row("Python", py_info["version"])
    table.add_row("مسیر Python", py_info["executable"])

    console.print(table)

    # System info table
    sys_table = Table(title="💻 اطلاعات سیستم", border_style="green")
    sys_table.add_column("کلید", style="bold yellow")
    sys_table.add_column("مقدار", style="white")
    for key, value in sys_info.items():
        sys_table.add_row(key.replace("_", " ").title(), str(value))

    console.print(sys_table)
