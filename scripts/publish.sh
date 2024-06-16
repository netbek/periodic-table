#!/bin/bash
set -e

if ([ "$1" == "--help" ] || [ -z "$1" ]); then
    echo "Usage: publish.sh [version]"
    echo ""
    echo "Example: ./publish.sh 0.0.1"
    exit 1
fi

npm publish

python3 -m twine upload --config-file .pypirc --verbose python/dist/*

gh release create $1
