"""
Network Commands — ابزارهای شبکه
"""

import click
from tizpar import console
from tizpar.utils.network import check_url, get_public_ip, ping_host
from rich.table import Table


@click.group(name="network", help="ابزارهای شبکه و اینترنت")
def network_group() -> None:
    """ابزارهای بررسی شبکه"""
    pass


@network_group.command(name="ip", help="نمایش IP عمومی")
def public_ip() -> None:
    """نمایش آدرس IP عمومی"""
    try:
        ip = get_public_ip()
        console.print(f"🌐 آدرس IP عمومی شما: [bold green]{ip}[/bold green]")
    except Exception as e:
        console.print(f"[error]خطا در دریافت IP: {e}[/error]")


@network_group.command(name="check")
@click.argument("url", type=str, required=True)
@click.option("--timeout", default=10, help="تایم‌اوت به ثانیه")
def check(url: str, timeout: int) -> None:
    """بررسی وضعیت یک URL"""
    console.print(f"🔍 در حال بررسی [bold]{url}[/bold] ...")
    try:
        result = check_url(url, timeout=timeout)
        table = Table(title=f"📡 وضعیت {url}", border_style="cyan")
        table.add_column("کلید", style="bold yellow")
        table.add_column("مقدار", style="white")
        for key, value in result.items():
            table.add_row(key.replace("_", " ").title(), str(value))
        console.print(table)
    except Exception as e:
        console.print(f"[error]خطا: {e}[/error]")


@network_group.command(name="ping")
@click.argument("host", type=str, required=True)
@click.option("--count", default=4, help="تعداد پینگ‌ها")
def ping(host: str, count: int) -> None:
    """پینگ یک هاست"""
    console.print(f"🏓 در حال پینگ [bold]{host}[/bold] ...")
    try:
        result = ping_host(host, count=count)
        if result["success"]:
            console.print(f"[success]✓ {host} در دسترس است[/success]")
            table = Table(title=f"📊 آمار پینگ {host}", border_style="green")
            table.add_column("کلید", style="bold yellow")
            table.add_column("مقدار", style="white")
            for key, value in result.items():
                if key != "success":
                    table.add_row(key.replace("_", " ").title(), str(value))
            console.print(table)
        else:
            console.print(f"[error]✗ {host} در دسترس نیست[/error]")
            console.print(f"دلیل: {result.get('error', 'نامشخص')}")
    except Exception as e:
        console.print(f"[error]خطا: {e}[/error]")
