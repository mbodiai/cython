#!/bin/bash
# Compile test_embed.c to executable

echo "Compiling test_embed.c to executable..."

cc -o test_embed test_embed.c \
   -I/opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14 \
   -L/opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/lib/python3.14/config-3.14-darwin \
   -lpython3.14 -ldl -framework CoreFoundation

if [ $? -eq 0 ]; then
    echo "✓ Executable created successfully!"
    ls -lh test_embed
else
    echo "✗ Compilation failed"
    exit 1
fi
