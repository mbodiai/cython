import sys
import pytest

from mbpy.helpers.autopip import autorun, async_autorun
from mbpy.cmd import arun

@pytest.mark.asyncio
async def test_dependency_installer() -> None:
    try:
        await arun([sys.executable, "-m", "pip", "uninstall","-y", "pandas"])
        assert "WARNING: Package(s) not found: pandas" in await arun([sys.executable, "-m", "pip", "show","pandas"])   
        result = autorun(["python", "-c", "import pandas"])
        assert "pandas" in await arun([sys.executable, "-m", "pip", "show","pandas"]) 
    finally:
        await arun([sys.executable, "-m", "pip", "install","-y", "pandas"])


@pytest.mark.asyncio
async def test_run_command() -> None:
    try:
        await arun([sys.executable, "-m", "pip", "uninstall","-y", "pandas"])
        assert "WARNING: Package(s) not found: pandas" in await arun([sys.executable, "-m", "pip", "show","pandas"])
        result = await async_autorun([sys.executable, "-c", "import pandas"])
        assert "pandas" in await arun([sys.executable, "-m", "pip", "show","pandas"]) 
    finally:
        await arun([sys.executable, "-m", "pip", "install","-y", "pandas"])



if __name__ == "__main__":
    pytest.main(["-v", __file__])
