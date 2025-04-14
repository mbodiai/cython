import asyncio
import atexit
import logging
import time
from collections.abc import AsyncIterator
from pathlib import Path

from typing_extensions import Callable, TypeAlias

from mbcore.config import CACHE_CONFIG, CacheConfig
from mbcore.even._internal._cache import _cache as _cache_dict  # Import the actual cache dictionary
from mbcore.even._internal._cache_impl import acache as _acache
from mbcore.even._internal._cache_impl import cache as _cache
from mbcore.even._internal._cache_impl import safe_print
from mbcore.types import wraps

_handlers_registered = False

cache: TypeAlias = _cache
acache: TypeAlias = _acache


def get_cache_size() -> int:
    """Helper function to get the cache size"""
    return len(_cache_dict)


def _register_handlers():
    global _handlers_registered
    if not _handlers_registered:

        @atexit.register
        def save_cache_on_exit():
            """Ensure cache is saved when program exits."""
            try:
                import asyncio

                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(cache.save())
                loop.close()
            except Exception as e:
                safe_print(
                    f"[red][ERROR][/red] Failed to save cache on exit: {e}")


def ensure_handlers(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        _register_handlers()
        return func(*args, **kwargs)

    return wrapper


@ensure_handlers
def init_cache(cfg: CacheConfig = CACHE_CONFIG) -> None:
    import os

    if os.getenv("MB_CACHE_OFF", not cfg["enabled"]):
        return
    cache.load(cfg["pathdir"])
    if logging.getLogger("default").getEffectiveLevel() <= logging.DEBUG:
        safe_print(f"Cache loaded with {get_cache_size()} entries")


init_cache()


@cache(persistent=True)
def fib(n: int) -> int:
    print("fib ran")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@cache(persistent=True)
def pret_tup(p: Path):
    print("pret_tup ran")
    time.sleep(1)
    yield 1
    yield 2
    yield 3
    return


@acache(persistent=True)
async def afib(n: int) -> int:
    if n < 2:
        return n
    return (await afib(n - 1)) + (await afib(n - 2))


def example():
    """Run an example cache test with async generators and functions."""

    @acache(persistent=True)
    async def ret_tup() -> AsyncIterator[int]:
        print("This should only run once")
        await asyncio.sleep(1)
        yield 1
        yield 2
        yield 3
        return

    async def main():
        # First run
        print("First run:")
        first_results = []
        async for i in ret_tup():
            print(f"  Item: {i}")
            first_results.append(i)

        # Second run - should use cache
        print("\nSecond run (should use cache):")
        second_results = []
        # Collect all values first to avoid consumption issues
        values = [i async for i in ret_tup()]
        for i in values:
            print(f"  Item: {i}")
            second_results.append(i)

        # Verify caching works
        results_match = first_results == second_results == [1, 2, 3]
        print(f"Results match: {results_match}")
        print(f"Cache hits: {ret_tup.cache_info().hits}\n")

        # Test another function (Fibonacci)
        await afib(13)
        print(f"Cache entries: {get_cache_size()}")

        # Explicitly save cache to ensure persistence
        await cache.save()

    asyncio.run(main(), debug=False)  # Set debug to False to reduce output

    # Display function cache stats using the mb command format
    from rich.console import Console

    console = Console()
    console.print(f"Total cache entries: {get_cache_size()}")

    # Display detailed cache info
    info = acache.cache_info()
    console.print(f"[bold]Cache Statistics:[/bold]")
    console.print(f"Hits: {info.hits}, Misses: {info.misses}")

    # Show top functions
    if info.by_function:
        console.print("\n[bold]Top Functions:[/bold]")
        for func_name, func_info in sorted(info.by_function.items(),
                                           key=lambda x: x[1].hits,
                                           reverse=True)[:3]:
            console.print(
                f"  {func_name}: hits={func_info.hits}, misses={func_info.misses}"
            )


if __name__ == "__main__":
    example()
