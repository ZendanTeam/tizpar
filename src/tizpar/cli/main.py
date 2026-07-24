"""
تیزپر Command-Line Interface (CLI)
==================================
Usage: tizpar [OPTIONS] COMMAND [ARGS]...
"""

import click
from tizpar import __version__, console
from tizpar.cli.commands import (
    info,
    persian,
    system,
    network,
    convert,
)


@click.group(
    name="tizpar",
    invoke_without_command=True,
    help="تیزپر - Swift Persian Developer Toolkit",
)
@click.version_option(
    version=__version__,
    prog_name="tizpar",
    message="تیزپر (Tizpar) v%(version)s — Swift Persian Developer Toolkit",
)
@click.pass_context
def cli(ctx: click.Context) -> None:
    """تیزپر - ابزارک سریع و کامل توسعه‌دهندگان فارسی زبان"""
    if ctx.invoked_subcommand is None:
        # Show banner and help
        _show_banner()
        click.echo(ctx.get_help())
        click.echo()
        console.print("[info]➡  از `tizpar --help` برای راهنمایی کامل استفاده کنید[/info]")


def _show_banner() -> None:
    """نمایش بنر تیزپر"""
    banner = """
[title]  ⚡ تیزپر (Tizpar) v{}  [/title]
[highlight]  Swift Persian Developer Toolkit  [/highlight]
[persian]  ابزارک توسعه‌دهنده فارسی — سریع و کامل  [/persian]
""".format(__version__)
    console.print(banner)


# Register commands
cli.add_command(info.info)
cli.add_command(persian.persian_group, name="persian")
cli.add_command(system.system_group, name="system")
cli.add_command(network.network_group, name="network")
cli.add_command(convert.convert_group, name="convert")


def main() -> None:
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
