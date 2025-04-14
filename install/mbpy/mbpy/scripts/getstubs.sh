#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: getstubs.sh <module>"
    exit 1
else
    ARG="$1"
    shift
fi
if [ -z "$1" ]; then
    P="."
else
    P="$1"
    shift
fi
mypy --show-error-codes --pretty
stubgen -o typings $ARG --ignore-errors --export-less --include-docstrings -v --no-import --search-path "$P" "$@"