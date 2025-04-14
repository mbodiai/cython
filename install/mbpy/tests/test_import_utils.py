from pathlib import Path
import platform
import sys
from typing import Any, cast
import pytest

from mbpy.utils import smart_import
import pytest


def test_smart_import():
    # Test importing a module that exists
    result = smart_import("os", "eager")
    assert result is not None
    assert result.__name__ == "os"


def test_lazy_import():
    result = smart_import("os", "lazy")
    assert result is not None
    assert result.__name__ == "os"
    assert getattr(result, "path", None) is not None
