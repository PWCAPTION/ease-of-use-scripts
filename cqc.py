import subprocess
import sys


def run_isort():
    result = subprocess.run(["isort", ".", "--line-length", "255"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def run_black():
    result = subprocess.run(["black", ".", "--line-length", "255"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def run_ruff():
    result = subprocess.run(["ruff", "check", ".", "--line-length", "255"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def main():
    run_isort()
    run_black()
    run_ruff()
