"""Module for converting markdown code blocks to doctest format."""

import re
import sys
import inspect
from typing import TypeVar, List, Dict, Any, Optional, Tuple

T = TypeVar("T")


def doctestable(obj: T) -> T:
    """Decorator that converts markdown code blocks to doctest format.

    Transforms:
    ```python
    code example
    output
    ```

    Into proper doctest format with >>> and ... prefixes.

    Example usage:

    ```python
    @doctestable
    def example():
        \"\"\"Example with code block:

        ```python
        1 + 2
        3
        ```
        \"\"\"
        return 1 + 2
    ```

    The docstring will be transformed to:

    Example with code block:

    >>> 1 + 2
    3
    """
    if not hasattr(obj, "__doc__") or not obj.__doc__:
        return obj

    doc = obj.__doc__

    # Find code blocks
    code_blocks = re.findall(r"```python\n(.*?)```", doc, re.DOTALL)

    for block in code_blocks:
        # Use rstrip to handle trailing whitespace correctly but preserve leading
        lines = block.rstrip().split('\n')
        parsed_lines = parse_code_and_output(lines)
        doctest_block = "\n".join(parsed_lines)
        # Ensure replacement occurs with original block content
        doc = doc.replace(f"```python\n{block}```", doctest_block)

    obj.__doc__ = doc

    # Add doctestable support
    if hasattr(obj, "__name__"):
        # Create a wrapper to make the function available for doctests
        def _doctest_wrapper(obj_with_doctests=obj):
            # Add the function itself to the globals
            import doctest
            import types

            # Store the original function's globals dictionary
            if not hasattr(obj_with_doctests, "__doc_test_globs__"):
                if hasattr(obj_with_doctests, "__dict__"):
                    obj_with_doctests.__doc_test_globs__ = {
                        obj_with_doctests.__name__: obj_with_doctests
                    }

            return obj_with_doctests

        # Add a __wrapped__ to maintain the original object's identity for introspection
        _doctest_wrapper.__wrapped__ = obj

        # Apply the wrapper to set up doctest globals
        obj = _doctest_wrapper(obj)

    return obj


def parse_code_and_output(original_lines: List[str]) -> List[str]:
    """Parse lines of a code block into doctest format.
    
    Distinguishes code vs output and preserves original output indentation.
    """
    if not original_lines:
        return []

    # Find minimum indentation of the block, ignoring empty lines
    indent_levels = [
        len(line) - len(line.lstrip()) for line in original_lines
        if line.strip()
    ]
    min_indent = min(indent_levels) if indent_levels else 0

    # Create normalized lines (common indent removed) for code checking
    normalized_lines = [(line[min_indent:] if line.strip() else "")
                        for line in original_lines]

    doctest_lines = []
    last_line_was_code = False
    for i, norm_line in enumerate(normalized_lines):
        stripped = norm_line.strip()
        original_line = original_lines[
            i]  # Keep original for output indentation

        if not stripped:
            # Keep empty lines, reset code flag
            doctest_lines.append("")
            last_line_was_code = False
            continue

        if is_likely_code(stripped):
            # It's code
            doctest_lines.append(
                f">>> {norm_line}")  # Use normalized line with >>>
            last_line_was_code = True
        elif last_line_was_code:
            # It's not code, and previous was code -> likely output
            # Use the ORIGINAL line to preserve indentation relative to docstring
            doctest_lines.append(original_line)
            last_line_was_code = False  # Output doesn't trigger next output
        else:
            # Not code, and previous wasn't code (or start) -> treat as code to be safe
            # This might happen for multiline strings or data structures not caught by is_likely_code
            doctest_lines.append(f">>> {norm_line}")
            last_line_was_code = True

    return doctest_lines


def is_likely_code(line: str) -> bool:
    """Determine if a line is likely code rather than output.
    More restrictive than the opposite check.
    """
    line = line.strip()  # Check content, ignore indentation here
    if not line:
        return False

    # Common keywords or patterns indicating code
    code_indicators = [
        '=',  # Assignment
        'def ',
        'class ',
        'if ',
        'elif',
        'else:',
        'for ',
        'while ',
        'import ',
        'from ',
        'with ',
        'try:',
        'except',
        'finally:',
        'return ',
        'yield ',
        'raise ',
        'assert ',
        '@'  # Decorators
    ]
    if any(indicator in line for indicator in code_indicators):
        return True

    # Function or method calls (check for balanced parentheses)
    if re.search(r"\w+\s*\(.*\)", line) and line.count('(') == line.count(')'):
        return True

    # Lines ending in a colon are usually code
    if line.endswith(':'):
        return True

    # Expressions involving operators, but not just a literal number/string
    if any(op in line for op in [
            '+', '-', '*', '/', '%', '**', '//', '<=', '>=', '==', '!=', '< ',
            '> '
    ]):
        try:
            # Avoid classifying simple literals like '-5' or '+10' as code here
            compile(line, '<string>', 'eval')  # Check if it evaluates
            if not re.match(r'^\s*[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?\s*$',
                            line):  # Not just a number
                if not ((line.startswith("'") and line.endswith("'")) or
                        (line.startswith('"') and line.endswith('"'))
                        ):  # Not just a simple string literal
                    return True
        except:  # If it doesn't compile as eval, it might still be code (part of multi-line) or complex expr
            pass  # Let other checks decide or default to False

    # Attribute access might be code
    if '.' in line and not line.startswith('.') and re.match(
            r'^[a-zA-Z_]\w*\.', line):
        return True

    # Default: If none of the above, assume it might be output or continuation
    return False


def run_doctest(obj: Any, verbose: bool = False) -> int:
    """Run doctest on an object with proper globals setting."""
    import doctest
    globs = {}
    if hasattr(obj, "__name__"):
        globs[obj.__name__] = obj
    if hasattr(obj, "__doc_test_globs__"):
        globs.update(obj.__doc_test_globs__)

    # Ensure module is correctly found even when run as script
    module = sys.modules.get(obj.__module__)
    if module is None:
        try:
            __import__(obj.__module__)
            module = sys.modules[obj.__module__]
        except ImportError:
            print(f"Warning: Could not import module {obj.__module__}",
                  file=sys.stderr)
            module = sys.modules.get("__main__")

    if module:
        test_finder = doctest.DocTestFinder()
        test_runner = doctest.DocTestRunner(verbose=verbose)

        tests = test_finder.find(obj,
                                 name=obj.__name__,
                                 module=module,
                                 globs=globs)
        for test in tests:
            # Ensure the function is available in test globals
            test.globs[obj.__name__] = obj
            failures, _ = test_runner.run(test)
        return failures
    else:
        print("Error: Could not determine module for doctest.",
              file=sys.stderr)
        return 1  # Indicate failure


if __name__ == "__main__":

    @doctestable
    def example_func():
        """Example function with code block:

        ```python
        x = 1
        y = 2
        x + y
        3
        
        # This should also work:
        example_func()
        3
        ```
        """
        x = 1
        y = 2
        return x + y

    # print("Final docstring:")
    # print(repr(example_func.__doc__))

    import doctest
    failed = run_doctest(example_func)
    sys.exit(failed)
