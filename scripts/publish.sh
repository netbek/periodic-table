#!/bin/bash
set -e

npm publish

python3 -m twine upload --config-file .pypirc --verbose dist/*

gh release create [VERSION]
