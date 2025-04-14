# import sys
# import traceback


# class Debugger:
#     def __init__(self):
#         self.breakpoints = set()

#     def caller(self, depth: int | tuple | slice = 1):
#         """Retrieve the name of the calling module while avoiding debugging interference."""
#         frame = sys._getframe()
#         stack = []

#         while frame:
#             module = frame.f_globals.get("__name__", None)
#             if module and module not in ("importlib", "sys", "mbcore.import_utils"):
#                 stack.append(module)
#             frame = frame.f_back

#         return stack[depth] if isinstance(depth, int) else stack[depth]

#     def log(self, message: str, **variables):
#         """Log debugging info with caller context."""
#         caller_info = self.caller(2)  # Get function that called the log
#         print(f"[DEBUG] {caller_info}: {message} | Vars: {variables}")

#     def trace(self, exception: Exception):
#         """Trace where an exception originated."""
#         tb = traceback.extract_tb(exception.__traceback__)
#         print("[TRACE] Exception Traceback:")
#         for i, frame in enumerate(tb):
#             print(f"  {i}: File {frame.filename}, line {frame.lineno}, in {frame.name}")
#             print(f"     Code: {frame.line}")

#     def search_breakpoint(self, func, *args, **kwargs):
#         """Perform a binary search to locate where execution fails."""
#         try:
#             return func(*args, **kwargs)  # Run normally
#         except Exception as e:
#             self.trace(e)
#             stack = self.caller()
#             left, right = 0, len(stack) - 1

#             while left <= right:
#                 mid = (left + right) // 2
#                 print(f"[BINARY SEARCH] Testing {stack[mid]}")

#                 try:
#                     # Rerun with modified context
#                     return func(*args, **kwargs)
#                 except Exception:
#                     right = mid - 1  # Narrow down where it fails
#                 else:
#                     left = mid + 1

#             print(f"[FAILED] Error localized at {stack[right + 1]}")
#     async def asearch_breakpoint(self, func, *args, **kwargs):
#         """Perform a binary search to locate where execution fails."""
#         try:
#             return await func(*args, **kwargs)  # Run normally
#         except Exception as e:
#             self.trace(e)
#             stack = self.caller()
#             left, right = 0, len(stack) - 1

#             while left <= right:
#                 mid = (left + right) // 2
#                 print(f"[BINARY SEARCH] Testing {stack[mid]}")

#                 try:
#                     # Rerun with modified context
#                     return await func(*args, **kwargs)
#                 except Exception:
#                     right = mid - 1
# debugger = Debugger()


# from mbpy.pkg.dependency import Dependency

# async def main():
#     await debugger.asearch_breakpoint(Dependency("pipelearn").install)
#     await debugger.asearch_breakpoint(Dependency("pipelearn").uninstall)

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())


import traceback
import hypothesis.strategies as st
from hypothesis import given


def parse_stack_trace(exc):
    """Extracts structured stack trace information."""
    tb = traceback.extract_tb(exc.__traceback__)
    return [
        {
            "filename": frame.filename,
            "lineno": frame.lineno,
            "name": frame.name,
            "line": frame.line,
        }
        for frame in tb
    ]


def extract_failing_function(exc):
    """Extracts the function name from the first failing frame."""
    tb = traceback.extract_tb(exc.__traceback__)
    for frame in reversed(tb):  # Iterate backward to find the first real failure
        if "(" in frame.line and ")" in frame.line:  # Likely a function call
            func_name = frame.line.split("(")[0].strip()
            return func_name
    return None


def binary_search_stack(frames, test_hypothesis):
    """Perform binary search over stack trace to find the first failing assumption."""
    left, right = 0, len(frames) - 1

    while left < right:
        mid = (left + right) // 2
        frame = frames[mid]

        if test_hypothesis(frame):
            left = mid + 1  # Move forward if hypothesis holds
        else:
            right = mid  # Narrow down the failure

    return frames[right]  # First failing frame


def test_hypothesis(frame):
    """Test if execution should reach this point without failure."""
    return True  # Assume frame is valid unless proven otherwise


def test_failing_function(func, input_strategy):
    """Automatically test a function using Hypothesis-generated inputs."""

    @given(input_strategy)
    def run_test(x):
        try:
            result = func(x)
            assert result is not None, "Function returned None unexpectedly."
        except Exception as e:
            print(f"❌ Function {func.__name__} failed with input {x}: {e}")
            raise e  # Let Hypothesis record the failure

    run_test()


# Simulated failing function
def buggy_function(x):
    if x > 5:
        raise ValueError("Something broke")
    return x


# RUN THE SYSTEM
try:
    buggy_function(10)  # Simulating failure

except Exception as e:
    trace = parse_stack_trace(e)
    failing_func_name = extract_failing_function(e)

    if failing_func_name:
        print(f"🚨 Found failing function: {failing_func_name}")

        failing_func = globals().get(failing_func_name)
        if failing_func:
            print("🔍 Retesting function with Hypothesis...")
            test_failing_function(failing_func, st.integers())  # Use integer inputs
