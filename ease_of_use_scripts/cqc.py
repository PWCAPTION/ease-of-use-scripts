import subprocess
import sys

def run_black():
    result = subprocess.run(["black", ".", "--line-length", "255"])
    if result.returncode != 0:
        sys.exit(result.returncode)

def run_ruff():
    result = subprocess.run(["ruff", "check", ".", "--line-length", "255"])
    if result.returncode != 0:
        sys.exit(result.returncode)

if __name__ == "__main__":
    run_black()
    run_ruff()
