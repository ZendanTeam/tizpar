"""
System Commands — اطلاعات و مانیتورینگ سیستم
"""

import click
from tizpar import console
from tizpar.utils.system import (
    get_system_info,
    cpu_usage,
    memory_usage,
    disk_usage,
    uptime,
)
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn


@click.group(name="system", help="اطلاعات و مانیتورینگ سیستم")
def system_group() -> None:
    """ابزارهای مانیتورینگ سیستم"""
    pass


@system_group.command(name="info", help="نمایش اطلاعات کامل سیستم")
def sys_info() -> None:
    """نمایش اطلاعات کامل سیستم عامل"""
    info = get_system_info()
    table = Table(title="💻 اطلاعات سیستم", border_style="green")
    table.add_column("کلید", style="bold yellow")
    table.add_column("مقدار", style="white")
    for key, value in info.items():
        table.add_row(key.replace("_", " ").title(), str(value))
    console.print(table)


@system_group.command(name="cpu", help="نمایش وضعیت CPU")
def cpu() -> None:
    """نمایش میزان استفاده از CPU"""
    usage = cpu_usage()
    console.print(f"[bold]استفاده از CPU:[/bold] {usage}%")
    
    # نمایش نوار پیشرفت
    from rich.progress import Progress, BarColumn, TextColumn
    
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]CPU Usage", total=100)
        progress.update(task, completed=usage)


@system_group.command(name="memory", help="نمایش وضعیت حافظه")
def memory() -> None:
    """نمایش میزان استفاده از RAM"""
    mem = memory_usage()
    table = Table(title="🧠 حافظه سیستم (RAM)", border_style="magenta")
    table.add_column("کلید", style="bold yellow")
    table.add_column("مقدار", style="white")
    for key, value in mem.items():
        table.add_row(key.replace("_", " ").title(), str(value))
    console.print(table)


@system_group.command(name="disk", help="نمایش وضعیت دیسک")
@click.option("--path", default="/", help="مسیر مورد نظر برای بررسی")
def disk(path: str) -> None:
    """نمایش میزان استفاده از دیسک"""
    usage = disk_usage(path)
    table = Table(title=f"💾 وضعیت دیسک — {path}", border_style="blue")
    table.add_column("کلید", style="bold yellow")
    table.add_column("مقدار", style="white")
    for key, value in usage.items():
        table.add_row(key.replace("_", " ").title(), str(value))
    console.print(table)


@system_group.command(name="uptime", help="نمایش زمان روشن بودن سیستم")
def sys_uptime() -> None:
    """نمایش مدت زمان روشن بودن سیستم"""
    up = uptime()
    console.print(f"⏱  زمان روشن بودن سیستم: [bold green]{up}[/bold green]")
