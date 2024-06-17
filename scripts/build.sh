#!/bin/bash
set -e

scripts_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="${scripts_dir}/.."
python_dist_dir="${repo_dir}/python/dist"

venv/bin/python python/dump.py
gulp
# find "${python_dist_dir}" -maxdepth 1 ! -name ".gitignore" -type f -exec rm -f {} +
# python3 -m build -o "${python_dist_dir}"
