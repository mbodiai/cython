#!/bin/bash
# Robust script to embed a Cython module into a standalone executable
# Works across platforms and different Python environments

set -e  # Exit immediately if a command exits with a non-zero status

# Display usage information
usage() {
    echo "Usage: $0 <input.pyx>"
    echo "Compiles a Cython .pyx file into a standalone executable"
    echo ""
    echo "Example: $0 example.pyx"
    exit 1
}

# Check if we have enough arguments
if [ $# -lt 1 ]; then
    usage
fi

INPUT_FILE="$1"
BASE_NAME=$(basename "${INPUT_FILE}" .pyx)
DIR_NAME=$(dirname "${INPUT_FILE}")
C_FILE="${DIR_NAME}/${BASE_NAME}.c"
EXE_FILE="${BASE_NAME}"

echo "=== Embedding Python in ${INPUT_FILE} ==="

# Detect OS
case "$(uname -s)" in
    Linux*)     OS="Linux";;
    Darwin*)    OS="MacOS";;
    CYGWIN*)    OS="Windows";;
    MINGW*)     OS="Windows";;
    MSYS*)      OS="Windows";;
    *)          OS="Unknown";;
esac

echo "Detected OS: ${OS}"

# Find Python
PYTHON="$(command -v python3 2>/dev/null || command -v python 2>/dev/null)"

if [ -z "$PYTHON" ]; then
    echo "Error: Python not found. Please install Python 3."
    exit 1
fi

echo "Using Python: $PYTHON"
echo "Python version: $($PYTHON --version)"

# Check if Cython is installed
if ! $PYTHON -c "import Cython" &>/dev/null; then
    echo "Error: Cython not installed. Please install Cython (pip install Cython)."
    exit 1
fi

# Get Cython version
CYTHON_VERSION=$($PYTHON -c "import Cython; print(Cython.__version__)")
echo "Cython version: ${CYTHON_VERSION}"

# Step 1: Generate C code with embedded Python interpreter
echo "Compiling ${INPUT_FILE} to C with embedded Python..."
$PYTHON -m Cython.Compiler.Main --embed "${INPUT_FILE}" -o "${C_FILE}"

if [ ! -f "${C_FILE}" ]; then
    echo "Error: Failed to generate C file ${C_FILE}"
    exit 1
fi

# Step 2: Compile the C file to an executable
echo "Compiling C code to executable..."

# Check if python3-config exists
PYTHON_CONFIG="$(command -v python3-config 2>/dev/null || command -v python-config 2>/dev/null)"

if [ -z "$PYTHON_CONFIG" ]; then
    # No python-config, try to use the Python we found to locate it
    PYTHON_CONFIG="${PYTHON}-config"
    if ! command -v "$PYTHON_CONFIG" &>/dev/null; then
        # Still not found, try to get from sys.prefix
        PYTHON_PREFIX=$($PYTHON -c "import sys; print(sys.prefix)")
        PYTHON_CONFIG="${PYTHON_PREFIX}/bin/python3-config"
        if [ ! -f "$PYTHON_CONFIG" ]; then
            echo "Warning: python-config not found. Will attempt to use sysconfig module."
            # Get compile and link flags directly from Python
            PYTHON_CFLAGS=$($PYTHON -c "import sysconfig; print(' '.join(f'-I{sysconfig.get_path(\"include\")}' for p in ['include', 'platinclude'] if sysconfig.get_path(p)))")
            PYTHON_LDFLAGS=$($PYTHON -c "import sysconfig; print(f'-L{sysconfig.get_config_var(\"LIBDIR\")} -lpython{sysconfig.get_config_var(\"VERSION\")}' if sysconfig.get_config_var('LIBDIR') else '')")
        else
            echo "Found python-config at $PYTHON_CONFIG"
        fi
    fi
fi

# Get compiler flags for Python
if [ -n "$PYTHON_CONFIG" ] && [ -x "$PYTHON_CONFIG" ]; then
    echo "Using $PYTHON_CONFIG to get compilation flags"
    if $PYTHON_CONFIG --help | grep -q -- "--embed"; then
        # Newer Python versions support --embed
        PYTHON_CFLAGS=$($PYTHON_CONFIG --cflags --embed)
        PYTHON_LDFLAGS=$($PYTHON_CONFIG --ldflags --embed)
    else
        # Older Python versions
        PYTHON_CFLAGS=$($PYTHON_CONFIG --cflags)
        PYTHON_LDFLAGS=$($PYTHON_CONFIG --ldflags)
    fi
fi

echo "Python CFLAGS: ${PYTHON_CFLAGS}"
echo "Python LDFLAGS: ${PYTHON_LDFLAGS}"

# Find C compiler
if [ "${OS}" = "Windows" ]; then
    CC="$(command -v cl 2>/dev/null || command -v gcc 2>/dev/null || command -v clang 2>/dev/null)"
else
    CC="$(command -v clang 2>/dev/null || command -v gcc 2>/dev/null || command -v cc 2>/dev/null)"
fi

if [ -z "$CC" ]; then
    echo "Error: No C compiler found. Please install GCC, Clang, or Microsoft Visual C++."
    exit 1
fi

echo "Using compiler: $CC"

# Add file extension for Windows
if [ "${OS}" = "Windows" ]; then
    EXE_FILE="${EXE_FILE}.exe"
fi

# Platform-specific compilation commands
if [ "${OS}" = "Windows" ]; then
    if [[ "$CC" == *"cl"* ]]; then
        # MSVC compilation
        COMPILE_CMD="$CC ${C_FILE} /Fe${EXE_FILE} ${PYTHON_CFLAGS} /link ${PYTHON_LDFLAGS}"
    else
        # MinGW compilation
        COMPILE_CMD="$CC -o ${EXE_FILE} ${C_FILE} ${PYTHON_CFLAGS} ${PYTHON_LDFLAGS}"
    fi
elif [ "${OS}" = "MacOS" ]; then
    # Add CoreFoundation framework for macOS
    COMPILE_CMD="$CC -o ${EXE_FILE} ${C_FILE} ${PYTHON_CFLAGS} ${PYTHON_LDFLAGS} -framework CoreFoundation"
else
    # Linux and other systems
    COMPILE_CMD="$CC -o ${EXE_FILE} ${C_FILE} ${PYTHON_CFLAGS} ${PYTHON_LDFLAGS} -lm -ldl -lutil"
fi

echo "Running: ${COMPILE_CMD}"
eval "${COMPILE_CMD}"

# Check if the executable was created successfully
if [ ! -f "${EXE_FILE}" ]; then
    echo "Error: Failed to build executable ${EXE_FILE}"
    exit 1
fi

# Make the file executable on Unix-like systems
if [ "${OS}" != "Windows" ]; then
    chmod +x "${EXE_FILE}"
fi

echo "=== Build successful ==="
echo "Created executable: ${EXE_FILE}"
echo "Run with: ./${EXE_FILE}"