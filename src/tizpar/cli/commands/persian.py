"""
Persian Commands — ابزارهای کار با متن فارسی
"""

import click
from tizpar import console
from tizpar.utils.persian import (
    to_persian_digits,
    to_english_digits,
    is_persian_text,
    remove_diacritics,
    get_persian_chars_count,
)


@click.group(name="persian", help="ابزارهای کار با متن و اعداد فارسی")
def persian_group() -> None:
    """ابزارهای پردازش متن فارسی"""
    pass


@persian_group.command(name="to-persian")
@click.argument("text", type=str, required=True)
@click.option("--keep-non-digits/--no-keep-non-digits", default=True, help="نگهداری کاراکترهای غیرعددی")
def to_persian(text: str, keep_non_digits: bool) -> None:
    """تبدیل اعداد انگلیسی به فارسی
    
    مثال:
        tizpar persian to-persian "Hello 123 World 456"
    """
    result = to_persian_digits(text, keep_non_digits=keep_non_digits)
    console.print(f"[bold]ورودی:[/bold] {text}")
    console.print(f"[bold green]خروجی:[/bold green] {result}")


@persian_group.command(name="to-english")
@click.argument("text", type=str, required=True)
@click.option("--keep-non-digits/--no-keep-non-digits", default=True, help="نگهداری کاراکترهای غیرعددی")
def to_english(text: str, keep_non_digits: bool) -> None:
    """تبدیل اعداد فارسی به انگلیسی
    
    مثال:
        tizpar persian to-english "سلام ۱۲۳ دنیا ۴۵۶"
    """
    result = to_english_digits(text, keep_non_digits=keep_non_digits)
    console.print(f"[bold]ورودی:[/bold] {text}")
    console.print(f"[bold green]خروجی:[/bold green] {result}")


@persian_group.command(name="detect")
@click.argument("text", type=str, required=True)
def detect(text: str) -> None:
    """تشخیص فارسی بودن متن"""
    is_persian = is_persian_text(text)
    persian_count = get_persian_chars_count(text)
    total = len(text.replace(" ", ""))
    
    if is_persian:
        console.print(f"[success]✓ این متن فارسی است[/success]")
    else:
        console.print(f"[warning]⚠ این متن فارسی نیست[/warning]")
    
    console.print(f"تعداد کاراکترهای فارسی: [highlight]{persian_count}[/highlight]")
    console.print(f"تعداد کل کاراکترها (بدون فاصله): [highlight]{total}[/highlight]")
    if total > 0:
        ratio = (persian_count / total) * 100
        console.print(f"درصد کاراکترهای فارسی: [bold]{ratio:.1f}%[/bold]")


@persian_group.command(name="clean")
@click.argument("text", type=str, required=True)
def clean(text: str) -> None:
    """حذف اعراب و کاراکترهای خاص از متن فارسی"""
    result = remove_diacritics(text)
    console.print(f"[bold]ورودی:[/bold] {text}")
    console.print(f"[bold green]خروجی (بدون اعراب):[/bold green] {result}")
