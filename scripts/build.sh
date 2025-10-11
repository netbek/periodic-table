#!/bin/bash
set -e

scripts_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="${scripts_dir}/.."

cd "${repo_dir}"
.venv/bin/python python/dump.py
gulp
find python/dist -maxdepth 1 ! -name ".gitignore" -type f -exec rm -f {} +
uv build -o python/dist --sdist
uv build -o python/dist --wheel
.venv/bin/twine check python/dist/*
