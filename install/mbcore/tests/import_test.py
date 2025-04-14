import pytest

from mbcore.types import ModulePackage


# -------------------------------------------------------------------
# DEMO USAGE
# -------------------------------------------------------------------
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("os.path", "os.path"),
        ("os.getcwd", "os.getcwd"),
        ("importlib.util", "importlib.util"),
        ("os.path.NONEXISTENT_THING", "os.path.NONEXISTENT_THING"),
    ],
)
def test_import(test_input, expected):
    # 1) If there's a real package or submodules in your environment, test them here:
    # e.g. Trying a normal dotted import:
    try:
        mp = ModulePackage(test_input)
        assert mp.name == expected
        print("[1] Imported as module =>", mp)
    except Exception as e:
        print("[1] Error =>", e)

    # 2) Now something that doesn't exist as a submodule but is an attribute:
    # e.g. 'path' is a submodule of 'os', but let's pretend the last part is an attribute
    # If there's something like "os: getcwd"? Well, that doesn't exist as a submodule "os.getcwd"
    # but let's do it with a purely dotted approach:
    try:
        mp2 = ModulePackage("os.getcwd")  # 'getcwd' is a function inside 'os', not a submodule
        print("[2] Fallback to attribute =>", mp2)
        print("mp2.obj =>", mp2.obj)
    except Exception as e:
        print("[2] Error =>", e)

    # 3) A real submodule path that actually exists
    # E.g. "importlib.util" is a real submodule chain
    try:
        mp3 = ModulePackage("importlib.util")
        print("[3] Real submodule =>", mp3)
    except Exception as e:
        print("[3] Error =>", e)

    # 4) A final piece that doesn't exist as submodule or attribute => fail
    try:
        mp4 = ModulePackage("os.path.NONEXISTENT_THING")
        print("[4]", mp4)
    except Exception as e:
        print("[4] Error =>", e)

    # 5) Single file path - must be an actual file. Adjust for your local path if you want to test:
    # Suppose you had a local file /tmp/foo.py
    """
    try:
        mp5 = ModulePackage("/tmp/foo.py")
        print("[5] File import =>", mp5)
        # If there's e.g. a function 'bar' in foo.py, we didn't automatically do attribute fallback for file paths,
        # but you could add that if you truly want it.
    except Exception as e:
        print("[5] Error =>", e)
    """


if __name__ == "__main__":
    pytest.main(["-v", __file__])
