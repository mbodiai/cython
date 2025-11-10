#!/usr/bin/env python3
"""Compile test_embed.pyx in executable mode."""

import sys
from Cython.Compiler.Main import compile, CompilationOptions
from Cython.Compiler import Options

# Set up compilation options for embedded executable
Options.embed = "main"  # Set embed option at module level

# Create compilation options
options = CompilationOptions()
options.embed = "main"
options.output_file = "test_embed.c"
options.module_name = "test_embed"  # Set module name
options.compiler_directives = Options.get_directive_defaults()

print("Compiling test_embed.pyx with embed mode...")
print(f"Embed option: {Options.embed}")
print(f"Module name: {options.module_name}")
print(f"Compiler directives: {len(options.compiler_directives)} directives loaded")

# Compile the file with full module name
result = compile("test_embed.pyx", options, full_module_name="test_embed")

if result and result.num_errors == 0:
    print("✓ Compilation successful!")
    print(f"✓ Generated: test_embed.c")
    sys.exit(0)
else:
    print(f"✗ Compilation failed with {result.num_errors if result else 'unknown'} errors")
    sys.exit(1)
