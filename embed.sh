#!/bin/bash
PYTHON=$( python3-config --prefix)
PYVERSION=$( python3-config --libs | cut -d' ' -f1 | cut -d'-' -f2)
CC="gcc"
MOD=""
PKG=""
if [ -n "$1" ]; then
    MOD="$1"
    shift
fi
if [ -n "$1" ]; then
    PKG="$1"
    shift
else
    PKG="$MOD"
fi
if [ -z "$MOD" ]; then
    echo "Usage: $0 <module> [<package>]"
    printf "%s\n" "$(cython -h)"
    exit 1
fi
cython  --embed "$MOD.py" -o "$MOD".c 
$CC -I$PYTHON "$MOD".c -lpython$PYVERSION -o "$PKG" $@