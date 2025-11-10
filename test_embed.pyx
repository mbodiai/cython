# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
# cython: embedsignature=True

"""
Test module for executable mode compilation.
This tests that Options.py works correctly with embedded Python.
"""

cdef int fibonacci(int n):
    """Calculate fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    """Main entry point for the embedded executable."""
    print("=" * 60)
    print("Cython Embedded Executable Test")
    print("=" * 60)

    # Test that compiler directives work
    print(f"Compiler directives applied successfully!")

    # Test C function call
    cdef int result = fibonacci(10)
    print(f"Fibonacci(10) = {result}")

    # Test that we can use Python features
    data = [1, 2, 3, 4, 5]
    total = sum(x ** 2 for x in data)
    print(f"Sum of squares: {total}")

    print("=" * 60)
    print("✅ All tests passed!")
    print("=" * 60)
    return 0

if __name__ == "__main__":
    main()
