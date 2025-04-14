# cython: language_level=3
# cython: embed=True

print("This is a simple Cython program with embedding enabled")

def test_function():
    """A test function that we'll call from embedded Python."""
    print("Hello from test_function!")
    return 42

# This will be run when the module is executed as a standalone program
if __name__ == "__main__":
    print("Running as main program")
    result = test_function()
    print(f"Result: {result}") 