from Cython.Compiler import Main
import os

# Create options to match expected arguments
options = Main.CompilationOptions(
    language_level=3,
    output_dir=os.curdir,
    cplus=True,
)

# Use proper Context instantiation with options
result = Main.compile('test_stdlib.pyx', options) 