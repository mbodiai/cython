import pytest

from mbcore.even._internal._trees import atreemap, treemap


# Async tests
@pytest.mark.asyncio
async def test_atreemap_with_flat_dict():
    async def double(x):
        return x * 2

    data = {"a": 1, "b": 2, "c": 3}
    result = await atreemap(double, data)
    assert result == {"a": 2, "b": 4, "c": 6}


@pytest.mark.asyncio
async def test_atreemap_with_nested_dict():
    async def double(x):
        return x * 2

    data = {"a": 1, "b": {"c": 2, "d": 3}, "e": 4}
    result = await atreemap(double, data)
    assert result == {"a": 2, "b": {"c": 4, "d": 6}, "e": 8}


@pytest.mark.asyncio
async def test_atreemap_with_list():
    async def double(x):
        return x * 2

    data = [1, 2, 3]
    result = await atreemap(double, data)
    assert result == {0: 2, 1: 4, 2: 6}


@pytest.mark.asyncio
async def test_atreemap_with_empty_input():
    async def double(x):
        return x * 2

    result = await atreemap(double, {})
    assert result == {}


@pytest.mark.asyncio
async def test_atreemap_with_string():
    async def double(x):
        return x + x

    result = await atreemap(double, "test")
    assert result == "testtest"


@pytest.mark.asyncio
async def test_atreemap_with_none():
    async def func(x):
        return x

    result = await atreemap(func, None)
    assert result is None


# Sync tests
def test_treemap_with_flat_dict():
    def double(x):
        return x * 2

    data = {"a": 1, "b": 2, "c": 3}
    result = treemap(double, data)
    assert result == {"a": 2, "b": 4, "c": 6}


def test_treemap_with_nested_dict():
    def double(x):
        return x * 2

    data = {"a": 1, "b": {"c": 2, "d": 3}, "e": 4}
    result = treemap(double, data)
    assert result == {"a": 2, "b": {"c": 4, "d": 6}, "e": 8}


def test_treemap_with_list():
    def double(x):
        return x * 2

    data = [1, 2, 3]
    result = treemap(double, data)
    assert result == {0: 2, 1: 4, 2: 6}


def test_treemap_with_empty_input():
    def double(x):
        return x * 2

    result = treemap(double, {})
    assert result == {}


def test_treemap_with_string():
    def double(x):
        return x * 2

    result = treemap(double, "test")
    assert result == "testtest"


def test_treemap_with_none():
    def func(x):
        return x

    result = treemap(func, None)
    assert result is None


def test_cachekey_mtime():
    from pathlib import Path
    from time import time
    from typing import Literal

    from mbcore.even._internal._trees import CacheKey

    t = time()

    def func(a, b, c=1, d=Path()):
        return a + b + c

    # Create a test file we can modify
    test_file = Path("test1.txt")
    if not test_file.exists():
        test_file.touch()

    # Create keys with the test file as a parameter - use literal strings for policy type
    policy_type: Literal["mtime"] = "mtime"
    ttl: int = 1
    keyfactory = CacheKey[(policy_type, ttl)](func)
    key1 = keyfactory(func, 1, 2, c=3, d=test_file)
    assert key1 is not None, f"{key1} should not be None"

    # Create a second key with the same parameters
    key2 = keyfactory(func, 1, 2, c=3, d=test_file)
    assert key1 & key2, f"{key1} & {key2} should be True"

    # Modify the file to change its mtime

    test_file.touch()

    # Create a new key after modification
    key3 = keyfactory(func, 1, 2, c=3, d=test_file)
    assert not key1 & key3, f"{key1} & {key3} should be False"

    # Clean up
    if test_file.exists():
        test_file.unlink()

    print("All tests passed!")
    t = time() - t
    print(key1)
    print(key2)
    print(key3)
    print(f"Time taken: {t} seconds")


if __name__ == "__main__":
    pytest.main(["-v", __file__])
