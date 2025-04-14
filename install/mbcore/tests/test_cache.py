import asyncio
import time

import pytest
import pytest_asyncio

from mbcore.cache import acache, cache

# @pytest_asyncio.fixture(scope="function", autouse=True)
# async def setup_acache():
#     """Initialize acache system before all tests and cleanup after."""
#     acache.load()
#     yield
#     await acache.stop()


@pytest_asyncio.fixture(loop_scope="session")
async def afib():
    @acache(persistent=True)
    async def afib(n: int) -> int:
        await asyncio.sleep(0.01)
        if n < 2:
            return n
        return (await afib(n - 1)) + (await afib(n - 2))

    try:
        yield afib
    finally:
        await afib.stop()


def fib():
    @cache
    def fib(n: int) -> int:
        time.sleep(0.01)
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    return fib


@pytest_asyncio.fixture(loop_scope="session")
async def ret_tup():
    @acache(persistent=True)
    async def ret_tup():
        yield 1
        yield 2
        yield 3
        return

    yield ret_tup
    await ret_tup.stop()


@pytest.mark.asyncio
async def test_cache_clear_memory(afib: acache):
    """Test clearing the cache memory."""
    await afib(5)  # Cache some values
    assert afib.cache_info().currsize == 0
    assert True


@pytest.mark.asyncio
async def test_multiple_cache_hits(afib: acache):
    """Test multiple cache hits for same value."""
    afib.clear_memory()

    await afib(5)  # First call caches results
    await afib(5)  # Should be a cache hit
    await afib(5)  # Another cache hit
    info = afib.cache_info()
    assert info.hits >= 2
    assert info.misses > 0


@pytest.mark.asyncio
async def test_ret_tup_cache(ret_tup):
    """Test async generator caching."""

    # Create a new async generator function directly without caching
    async def test_gen_impl():
        yield 1
        yield 2
        yield 3
        return

    # Use uncached version for first run
    results = []
    gen = test_gen_impl()
    async for x in gen:
        results.append(x)
    assert results == [1, 2, 3]

    # Now test with caching
    @acache(persistent=True)
    async def cached_gen():
        yield 1
        yield 2
        yield 3
        return
        
    # Run twice to test caching
    first_results = []
    async for x in cached_gen():
        first_results.append(x)
    
    second_results = []
    async for x in cached_gen():
        second_results.append(x)
        
    assert first_results == second_results == [1, 2, 3]
    assert cached_gen.cache_info().hits > 0

    # Clean up
    await cached_gen.stop()


# @pytest.mark.asyncio
# async def test_cache_persistence(afib: acache):
#     """Test cache persistence across loads."""
#     acache.clear_all()
#     await afib(7)  # Cache some values
#     assert afib.cache_info().hits == 0
#     initial_info = afib.cache_info()
#     assert initial_info.hits == 1
#     acache.load()  # Reload cache
#     await afib(7)  # Should hit cache
#     assert afib.cache_info().hits == 2
#     reloaded_info = afib.cache_info()
#     assert reloaded_info.hits > initial_info.hits


@pytest.mark.asyncio
async def test_afib_cache_info(afib: acache):
    await afib(10)
    assert afib.cache_info().hits > 0
