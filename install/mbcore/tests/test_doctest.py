#!/usr/bin/env python3
"""Test file for the doctestable decorator using standard doctest."""

import doctest
import sys
import re
from typing import List, Optional

from mbcore.doctestable import doctestable, run_doctest

try:
    from hypothesis import given, strategies as st
    HYPOTHESIS_AVAILABLE = True
except ImportError:
    HYPOTHESIS_AVAILABLE = False


# Define test functions
def test_basic_transformation():
    """Test basic markdown to doctest transformation."""

    @doctestable
    def example_func():
        """Example function with markdown code block.

        ```python
        1 + 1
        2
        ```
        """
        pass

    print("  Checking basic transformation...")
    assert ">>> 1 + 1" in (example_func.__doc__
                           or ""), "Failed to transform simple code block"
    assert "2" in (example_func.__doc__ or ""), "Failed to include output"


def test_multiline_transformation():
    """Test multiline code block transformation."""

    @doctestable
    def example_func():
        """Example function with multiline markdown code block.

        ```python
        x = 1
        y = 2
        x + y
        3
        ```
        """
        pass

    print("  Checking multiline transformation...")
    assert ">>> x = 1" in (example_func.__doc__
                           or ""), "Failed to transform first line"
    assert ">>> y = 2" in (example_func.__doc__
                           or ""), "Failed to transform second line"
    assert ">>> x + y" in (example_func.__doc__
                           or ""), "Failed to transform third line"
    assert "3" in (example_func.__doc__ or ""), "Failed to include output"


# Define Example class used in tests
class Example:
    """Example class with markdown code block."""

    def __str__(self):
        return "Example instance"

    def method(self):
        """Method with markdown code block."""
        return "method called"


def test_class_transformation():
    """Test class docstring transformation."""

    @doctestable
    class TestExample:
        """Example class with markdown code block.

        ```python
        obj = TestExample()
        str(obj)
        'Example instance'
        ```
        """

        def __str__(self):
            return "Example instance"

    print("  Checking class docstring transformation...")
    assert ">>> obj = TestExample()" in (
        TestExample.__doc__ or ""), "Failed to transform class creation"
    assert ">>> str(obj)" in (TestExample.__doc__
                              or ""), "Failed to transform method call"
    assert "'Example instance'" in (TestExample.__doc__
                                    or ""), "Failed to include output"


def test_method_transformation():
    """Test method docstring transformation."""

    class TestExample:

        @doctestable
        def method(self):
            """Method with markdown code block.

            ```python
            obj = TestExample()
            obj.method()
            'method called'
            ```
            """
            return "method called"

    print("  Checking method docstring transformation...")
    assert ">>> obj = TestExample()" in (
        TestExample.method.__doc__ or ""), "Failed to transform class creation"
    assert ">>> obj.method()" in (TestExample.method.__doc__
                                  or ""), "Failed to transform method call"
    assert "'method called'" in (TestExample.method.__doc__
                                 or ""), "Failed to include output"


def some_func():
    """Function with test.

    >>> some_func()
    42
    """
    return 42


def test_doctest_runs():
    """Test that doctests run correctly after transformation."""

    @doctestable
    def example_func():
        """Function with test.

        ```python
        example_func()
        42
        ```
        """
        return 42

    print("  Checking doctest execution...")
    # Use the helper function that provides the correct globals
    failed_count = run_doctest(example_func)
    assert failed_count == 0


if HYPOTHESIS_AVAILABLE:

    @given(
        # Generate random Python expressions
        expression=st.text(
            alphabet="abcdefghijklmnopqrstuvwxyz0123456789+-*/() ",
            min_size=1,
            max_size=20).filter(lambda s: s.strip() and not re.search(
                r'[^\w\s\+\-\*\/\(\)]', s)),
        # Generate expected result as string
        result=st.text(alphabet="0123456789'\"abcdefghijklmnopqrstuvwxyz",
                       min_size=1,
                       max_size=20),
        # Generate different indentation levels
        indent=st.integers(min_value=0, max_value=8),
    )
    def test_hypothesis_doctestable(expression: str, result: str, indent: int):
        """Test doctestable with hypothesis-generated test cases."""
        # Create indentation
        indent_str = " " * indent

        # Create a docstring with our test code
        docstring = f"""Example with hypothesis-generated test.

        ```python
        {indent_str}{expression}
        {indent_str}{result}
        ```
        """

        # Create a function with this docstring
        def test_func():
            pass

        test_func.__doc__ = docstring

        # Apply decorator
        decorated = doctestable(test_func)

        # Check transformation happened
        transformed_doc = decorated.__doc__
        # Normalize whitespace for comparison
        normalized_doc = re.sub(r'\s+', ' ', transformed_doc)
        normalized_expr = re.sub(r'\s+', ' ', f">>> {expression}")
        assert normalized_expr in normalized_doc, f"Expression not transformed: {expression}"
        assert result in transformed_doc, f"Result not preserved: {result}"


# Add a test that simulates real-world usage with doctest
def test_realistic_doctest_example():
    """Test a more realistic example that would be used in practice."""

    @doctestable
    def calculate_factorial(n):
        """Calculate the factorial of n.
        
        ```python
        calculate_factorial(5)
        120
        ```
        """
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    # Run the doctest with a manual check instead
    import doctest
    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner()

    # Create a globs dictionary with the function
    globs = {'calculate_factorial': calculate_factorial}

    tests = finder.find(calculate_factorial, globs=globs)
    for test in tests:
        test.globs = globs  # Ensure function is available in test
        result = runner.run(test)
        assert result.failed == 0, f"Doctest failed with {result.failed} failures"


# Create a demonstration example
def doctestable_demo():
    """Demonstrate the doctestable decorator.

    ```python
    x = 1 + 1
    x
    2

    y = "hello"
    y.upper()
    'HELLO'
    ```
    """
    pass


if __name__ == "__main__":
    import sys

    import pytest

    pytest.main([__file__, *sys.argv[1:]])
