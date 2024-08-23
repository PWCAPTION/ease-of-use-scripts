import subprocess
import sys

# import requests
from rich.console import Console

console = Console()


# def print_joke():
#     response = requests.get("https://v2.jokeapi.dev/joke/Any", params={"blacklistFlags": "nsfw,religious,political,racist,sexist,explicit"})
#     json_response = response.json()
#     setup = json_response["setup"]
#     delivery = json_response["delivery"]
#     console.print(f"[bold magenta]{setup}[/bold magenta]")
#     console.print(f"[bold magenta]{delivery}[/bold magenta]")


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
    # try:
    #     print_joke()
    # except Exception:
    #     pass
    console.print("[bold green]Don't forget to eat your veggies. - Anonymous[/bold green] :cucumber: :carrot: :onion: :watermelon:")
