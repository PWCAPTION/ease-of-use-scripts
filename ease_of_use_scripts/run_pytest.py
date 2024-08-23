import subprocess
import sys

from dotenv import load_dotenv
from rich.console import Console

console = Console()


def run_pytest():
    console.print(":information_desk_person: [bold green]Running [italic]python3 -m pytest . -s --disable-warnings[/italic][/bold green]! :raised_hands:")
    result = subprocess.run(["python3", "-m", "pytest", ".", "-s", "--disable-warnings"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def main():
    load_dotenv()
    run_pytest()
