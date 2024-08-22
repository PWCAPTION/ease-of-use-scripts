import subprocess
import sys

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


def main():
    run_isort()
    run_black()
    run_ruff()
    console.print("[bold green]Don't forget to eat your veggies. - Anonymous[/bold green] :cucumber: :carrot: :onion: :watermelon:")
