import os
import subprocess
import sys

from dotenv import load_dotenv
from rich.console import Console

console = Console()


def pip_install_uv():
    console.print(":smile: [bold green]Running [italic]pip3 install uv[/italic][/bold green]! :avocado:")
    result = subprocess.run(["pip3", "install", "uv"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def uv_sync():
    console.print(":stuck_out_tongue_winking_eye: [bold green]Running [italic]uv sync[/italic][/bold green]! :broccoli:")

    result = subprocess.run(["uv", "sync"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def main():
    load_dotenv()
    if os.environ.get("UV_EXTRA_INDEX_URL") is None:
        console.print("[bold red]:warning: Missing UV_EXTRA_INDEX_URL env var[/bold red]")
        sys.exit(1)
    if os.environ.get("UV_INDEX_URL") is None:
        console.print("[bold red]:warning: Missing UV_INDEX_URL env var[/bold red]")
        sys.exit(1)

    pip_install_uv()
    uv_sync()
