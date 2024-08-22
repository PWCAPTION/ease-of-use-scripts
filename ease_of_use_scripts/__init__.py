import os
import subprocess
import sys

from dotenv import load_dotenv
from rich.console import Console

console = Console()


def run_isort():
    console.print("[bold green]Running isort[/bold green]! :avocado:")
    result = subprocess.run(["isort", ".", "--line-length", "255"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def run_black():
    console.print("[bold green]Running black[/bold green]! :broccoli:")
    result = subprocess.run(["black", ".", "--line-length", "255"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def run_ruff():
    console.print("[bold green]Running ruff[/bold green]! :green_apple:")
    result = subprocess.run(["ruff", "check", ".", "--line-length", "255"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def cqc():
    run_isort()
    run_black()
    run_ruff()
    console.print("[bold green]Don't forget to eat your veggies. - Anonymous[/bold green] :cucumber: :carrot: :onion: :watermelon:")


def pip_install_uv():
    result = subprocess.run(["pip3", "install", "uv"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def uv_sync():
    result = subprocess.run(["uv", "sync"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def setup():
    load_dotenv()
    if os.environ.get("UV_EXTRA_INDEX_URL") is None:
        print("Missing UV_EXTRA_INDEX_URL env var")
        sys.exit(1)
    if os.environ.get("UV_INDEX_URL") is None:
        print("Missing UV_INDEX_URL env var")
        sys.exit(1)

    pip_install_uv()
    uv_sync()
