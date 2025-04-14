import tempfile
import contextlib
from mbcore.log import verbose
import rich_click as click
from httpx import Client

from mbpy.cli import base_args, get_help_config


@contextlib.contextmanager
def temp_url(url: str):
    with tempfile.NamedTemporaryFile(delete=True) as f:
        content = Client().get(url, follow_redirects=True).content
        f.write(content)
        f.seek(0)
        yield f.name, content.decode()


@click.command("tempcat")
@click.argument("url")
@click.rich_config(get_help_config())
@base_args
def main(url, **kwargs):
    with temp_url(url) as (filename, content):
        import os

        term_size = os.get_terminal_size()
        from html2text import html2text
        from mrender.md import Markdown

        c = html2text(content, bodywidth=term_size.columns).splitlines()
        verbose(c)
        Markdown(c).stream()
