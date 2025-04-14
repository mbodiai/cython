import asyncio
from pathlib import Path
from time import sleep

import pytest
import pytest_asyncio

from mbcore.cache import acache, cache
from mbcore.even._internal._cache import CacheEntry
from mbcore.even._internal._trees import CacheKey


@pytest.fixture
def test_func():
    """Create a simple test function for key creation."""

    def func(arg1: Path):
        return arg1

    return func


@pytest.fixture
def mtime_keyfactory(test_func):
    """Create a key factory with mtime policy."""
    policy_type = "mtime"
    ttl = 3600
    return CacheKey[(policy_type, ttl)](test_func)


@pytest.fixture
def test_keys(mtime_keyfactory):
    """Create test keys for comparisons."""
    key1 = mtime_keyfactory.make("arg1", "value1")
    key2 = mtime_keyfactory.make("arg1", "value1")
    key3 = mtime_keyfactory.make("arg1", "value2")
    return key1, key2, key3


def test_cachekey_comparison(test_keys):
    """Test that CacheKey's & operator works properly."""
    key1, key2, key3 = test_keys

    # Keys with the same args should match
    assert key1 & key2, "key1 & key2 should be True"

    # Keys with different args should not match
    assert not (key1 & key3), "key1 & key3 should be False"


def test_cachekey_in_dict(test_keys):
    """Test direct lookup in a dict with CacheKey."""
    key1, key2, _ = test_keys

    # Create test cache
    test_cache = {}

    # Store value
    test_cache[key1] = CacheEntry(key=key1, value="test value")

    # Check lookup with identical key works
    assert key2 in test_cache, "key2 should be found in test_cache"


@pytest.mark.asyncio
async def test_sync_cache_with_cachekey():
    """Test synchronous cache with CacheKey."""

    # Define a synchronous test function
    async def sync_test_fn(x):
        return f"Processed: {x}"

    # Create cache instance with the test function
    sync_cache = acache(sync_test_fn)

    # Store directly using CacheKey system
    test_key = sync_cache._mkey(sync_cache.func, "test_arg")
    from mbcore.even._internal._cache import _cache

    _cache[test_key] = CacheEntry(key=test_key, value="cached_result")

    # Key should be found in cache
    assert test_key in sync_cache.entries

    # Function should return the cached value
    result = await sync_cache("test_arg")
    assert result == "cached_result"


def test_mtime_changes(test_func):
    """Test that CacheKey detects file modification time changes."""
    # Create a test file
    try:
        try:
            test_file = Path("test_mtime.txt")
            test_file.unlink()
        except Exception as e:
            print(f"Error: {e}")
        test_file.touch()

        # Create keys with the test file as a parameter
        keyfactory = CacheKey["mtime", 1](test_func)
        key1 = keyfactory.make("arg1", test_file)

        # Wait briefly to ensure timestamp changes
        sleep(0.01)

        # Modify the file to change its mtime
        test_file.touch()

        # Create a new key after modification
        key2 = keyfactory.make("arg1", test_file)

        # Keys should not match due to mtime change
        assert not (key1
                    & key2), "keys should not match after file modification"

    finally:
        # Clean up
        test_file.unlink()


@pytest.mark.asyncio
async def test_async_cache_with_cachekey():
    """Test async cache with CacheKey."""

    # Create an async function
    async def async_test_fn(x):
        await asyncio.sleep(0.01)
        return f"Async: {x}"

    # Create async cache instance
    async_cache = acache(async_test_fn)

    # Store directly
    async_key = async_cache._mkey(async_cache.func, "async_arg")
    from mbcore.even._internal._cache import _cache

    _cache[async_key] = CacheEntry(key=async_key, value="async_result")

    # Key should be found in cache
    assert async_key in async_cache.entries

    # Function should return the cached value via coroutine
    result = await async_cache("async_arg")
    assert result == "async_result"

    # Clean up
    await async_cache.stop()
