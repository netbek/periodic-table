#!/bin/bash
set -e

virtualenv --python=python3.8 venv
venv/bin/pip install -r requirements_dev.txt

npm ci
