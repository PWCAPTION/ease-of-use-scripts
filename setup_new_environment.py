import os
import subprocess
import sys

from dotenv import load_dotenv


def pip_install_uv():
    result = subprocess.run(["pip3", "install", "uv"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def uv_sync():
    result = subprocess.run(["uv", "sync"])
    if result.returncode != 0:
        sys.exit(result.returncode)


def main():
    load_dotenv()
    if os.environ.get("UV_EXTRA_INDEX_URL") is None:
        print("Missing UV_EXTRA_INDEX_URL env var")
        sys.exit(1)
    if os.environ.get("UV_INDEX_URL") is None:
        print("Missing UV_INDEX_URL env var")
        sys.exit(1)

    pip_install_uv()
    uv_sync()
