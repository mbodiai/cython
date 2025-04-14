import logging
import sys
import re

import pytest

from mbcore import log
from mbcore.log import debug, error, fatal, info, warning


@pytest.fixture(autouse=True)
def auto_capture_logs(caplog):
    """Ensure all logs are captured at DEBUG level by default for all tests"""
    # Set a baseline level for default and mbcore loggers
    caplog.set_level(logging.DEBUG, logger="default")
    caplog.set_level(logging.DEBUG, logger="mbcore")  # Add mbcore logger
    return caplog


def test_log_levels():
    # Test different log levels
    assert log.Log["DEBUG"].level == logging.DEBUG
    assert log.Log["INFO"].level == logging.INFO
    assert log.Log["WARNING"].level == logging.WARNING
    assert log.Log["ERROR"].level == logging.ERROR
    assert log.Log["FATAL"].level == logging.CRITICAL  # FATAL maps to CRITICAL


def test_log_bool_check():
    """Test boolean checks for log levels"""
    # Assuming the log level check depends on the currently set level
    log.Log["DEBUG"].set()  # Keep these for this specific test's logic
    assert bool(log.Log["DEBUG"])
    assert bool(log.Log["INFO"]())

    log.Log["INFO"].set()  # Keep these for this specific test's logic
    assert not bool(log.Log["DEBUG"]())
    assert bool(log.Log["INFO"]())


def test_log_set():
    # Test setting log level
    log.Log["DEBUG"].set()
    assert logging.getLogger("default").getEffectiveLevel() == logging.DEBUG

    log.Log["INFO"].set()
    assert logging.getLogger("default").getEffectiveLevel() == logging.INFO


def test_log_call(caplog):
    """Test logging messages by capturing stdout"""
    # Setting level via log object as caplog doesn't seem to affect it
    log.Log["DEBUG"].set()
    logger = log.Log["DEBUG"]

    import io
    from contextlib import redirect_stdout

    stdout_capture = io.StringIO()
    with redirect_stdout(stdout_capture):
        logger("Debug message check")
        logger = log.Log["INFO"]
        logger("Info message check")

    output = stdout_capture.getvalue()
    # Use regex to find messages, ignoring formatting
    assert re.search(r"DEBUG.*Debug message check", output, re.DOTALL)
    assert re.search(r"INFO.*Info message check", output, re.DOTALL)


def test_convenience_functions(caplog):
    """Test convenience logging functions by capturing stdout/stderr"""
    import contextlib
    from io import StringIO

    # Restore the original level setting mechanism for the test
    # And capture stdout/stderr

    # === Test ERROR level ===
    log.Log["ERROR"].set()
    out_err = StringIO()
    with contextlib.redirect_stdout(out_err), contextlib.redirect_stderr(
            out_err):
        debug("Debug message")
        info("Info message")
        warning("Warning message")
        error("Error message")
        fatal("Fatal message")

    output_err = out_err.getvalue()
    out_lines_err = output_err.splitlines()
    # Check if expected LEVEL appears anywhere in the output lines for ERROR level
    assert not any("DEBUG" in line for line in out_lines_err)
    assert not any("INFO" in line for line in out_lines_err)
    assert not any("WARNING" in line for line in out_lines_err)
    assert any("ERROR" in line for line in out_lines_err)
    assert any("FATAL" in line for line in out_lines_err)

    # === Test WARNING level ===
    log.Log["WARNING"].set()
    out_warn = StringIO()
    with contextlib.redirect_stdout(out_warn), contextlib.redirect_stderr(
            out_warn):
        debug("Debug message")
        info("Info message")
        warning("Warning message")
        error("Error message")
        fatal("Fatal message")

    output_warn = out_warn.getvalue()
    out_lines_warn = output_warn.splitlines()
    # Check if expected LEVEL appears anywhere in the output lines for WARNING level
    assert not any("DEBUG" in line for line in out_lines_warn)
    assert not any("INFO" in line for line in out_lines_warn)
    assert any("WARNING" in line for line in out_lines_warn)
    assert any("ERROR" in line for line in out_lines_warn)
    assert any("FATAL" in line for line in out_lines_warn)

    # === Test DEBUG level ===
    log.Log["DEBUG"].set()
    out_debug = StringIO()
    with contextlib.redirect_stdout(out_debug), contextlib.redirect_stderr(
            out_debug):
        debug("Debug message")
        info("Info message")
        warning("Warning message")
        error("Error message")
        fatal("Fatal message")

    output_debug = out_debug.getvalue()
    out_lines_debug = output_debug.splitlines()
    # Check if expected LEVEL appears anywhere in the output lines for DEBUG level
    assert any("DEBUG" in line for line in out_lines_debug)
    assert any("INFO" in line for line in out_lines_debug)
    assert any("WARNING" in line for line in out_lines_debug)
    assert any("ERROR" in line for line in out_lines_debug)
    assert any("FATAL" in line for line in out_lines_debug)


def test_verbose_flags():
    # Test verbose flag detection
    sys.argv = []
    assert not log.isverbose()

    sys.argv = ["-v"]
    assert log.isverbose() == True

    sys.argv = ["--verbose"]
    assert log.isverbose() == True


if __name__ == "__main__":
    pytest.main(["-v", __file__])
