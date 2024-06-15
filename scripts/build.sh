#!/bin/bash
set -e

scripts_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="${scripts_dir}/.."

find "${repo_dir}/dist" -maxdepth 1 ! -name ".gitignore" -type f -exec rm -f {} +
python3 -m build
