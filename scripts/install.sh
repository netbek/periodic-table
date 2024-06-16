#!/bin/bash
set -e

virtualenv --python=python3.8 venv
venv/bin/pip install mendeleev==0.17.0 PyYAML==6.0.1

npm install
