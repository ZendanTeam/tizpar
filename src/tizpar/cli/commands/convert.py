"""
Convert Commands — ابزارهای تبدیل و جابه‌جایی
"""

import click
from tizpar import console
from tizpar.utils.converters import (
    json_to_yaml,
    yaml_to_json,
    text_to_base64,
    base64_to_text,
)


@click.group(name="convert", help="ابزارهای تبدیل فرمت‌ها")
def convert_group() -> None:
    """ابزارهای تبدیل بین فرمت‌های مختلف"""
    pass


@convert_group.command(name="json2yaml")
@click.argument("json_string", type=str, required=True)
def json_to_yaml_cmd(json_string: str) -> None:
    """تبدیل JSON به YAML"""
    try:
        result = json_to_yaml(json_string)
        console.print("[bold green]✅ نتیجه (YAML):[/bold green]")
        console.print(result)
    except Exception as e:
        console.print(f"[error]خطا: {e}[/error]")


@convert_group.command(name="yaml2json")
@click.argument("yaml_string", type=str, required=True)
def yaml_to_json_cmd(yaml_string: str) -> None:
    """تبدیل YAML به JSON"""
    try:
        result = yaml_to_json(yaml_string)
        console.print("[bold green]✅ نتیجه (JSON):[/bold green]")
        console.print(result)
    except Exception as e:
        console.print(f"[error]خطا: {e}[/error]")


@convert_group.command(name="to-base64")
@click.argument("text", type=str, required=True)
@click.option("--encoding", default="utf-8", help="نوع encoding")
def to_base64(text: str, encoding: str) -> None:
    """تبدیل متن به Base64"""
    try:
        result = text_to_base64(text, encoding=encoding)
        console.print(f"[bold]ورودی:[/bold] {text}")
        console.print(f"[bold green]Base64:[/bold green] {result}")
    except Exception as e:
        console.print(f"[error]خطا: {e}[/error]")


@convert_group.command(name="from-base64")
@click.argument("base64_string", type=str, required=True)
@click.option("--encoding", default="utf-8", help="نوع encoding")
def from_base64(base64_string: str, encoding: str) -> None:
    """تبدیل Base64 به متن"""
    try:
        result = base64_to_text(base64_string, encoding=encoding)
        console.print(f"[bold]Base64:[/bold] {base64_string}")
        console.print(f"[bold green]متن:[/bold green] {result}")
    except Exception as e:
        console.print(f"[error]خطا: {e}[/error]")
