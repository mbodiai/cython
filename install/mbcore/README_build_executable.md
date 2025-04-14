# Python to Executable Builder

This tool compiles Python files into standalone executables using Cython.

## Requirements

- Python (3.3+)
- Cython
- C compiler (clang/gcc)

## Usage

```bash
python build_executable.py [cython_options] input_file [runtime_args]
```

### Examples

Basic usage:
```bash
python build_executable.py hello.py
```

With Cython options:
```bash
python build_executable.py -a -v hello.py
```

Compile and run with arguments:
```bash
python build_executable.py hello.py arg1 arg2
```

### How it works

1. Converts your Python code to C/C++ using Cython
2. Compiles the C/C++ code with your system compiler
3. Links with Python libraries to create a standalone executable
4. Optionally runs the executable with any provided arguments

### Options

Most Cython command-line options are supported. Common ones include:

- `-a`: Generate an HTML annotation file
- `-v`: Verbose mode
- `-X language_level=3`: Set Python language level

Run without arguments to see the current configuration:
```bash
python build_executable.py
```

## Troubleshooting

If you encounter issues with Python library paths, run the script with no arguments to see the detected configuration. 