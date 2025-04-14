import os
from pathlib import Path

from typing_extensions import TYPE_CHECKING, Literal, TypedDict, TypeVar

if TYPE_CHECKING:
    from mbcore.log import LevelStr
else:
    LevelStr = str

ONE_WEEK = 60 * 60 * 24 * 7
MB = 1024 * 1024

T = TypeVar("T")


def getenv(env_key: str, default: T) -> T:
    """Return the environment variable if it exists, otherwise return the default value."""
    return type(default)(os.getenv(env_key) or default)  # type: ignore


class CacheConfig(TypedDict):
    """Cache configuration."""

    pathdir: Path
    ttl: int
    maxsize: int
    context_policy: Literal["mtime", "site_packages", "ttl", "all"]
    """Additional rules for cache invalidation.

    - mtime: Invalidate cache if any Path argument has changed for the decorated function.
    - site_packages: Invalidate cache if any site-packages module has changed.
    - ttl: Invalidate cache after a certain time.
    - all: All of the above.
    """
    persistent: bool
    """Save cache to disk."""
    enabled: bool


class LogConfig(TypedDict):
    """Workspace logging configuration."""

    level: LevelStr
    handlers: dict[str, list[str]]
    pathdir: "Path"
    """Root path for log files."""
    show_locals: bool
    """Show local variables in stack traces."""
    show_stack: bool
    """Show stack traces. In log files."""
    exclude_modules: list[str]
    """Modules to exclude from logging."""
    ignore_third_party: bool
    """Whether to ignore third-party modules in error stack traces."""
    full_trace: bool
    """Whether to trace every function call in the stack trace."""
    log_off: bool
    """Whether to disable logging."""


class MBConfig(TypedDict):
    """mbodi.ai configuration."""

    openai_api_key: str
    anthropic_api_key: str
    """OpenAI API key."""
    base_url: str
    logs: LogConfig
    cache: CacheConfig


CACHE_CONFIG: CacheConfig = {
    "enabled": getenv("MB_CACHE_ENABLED", True),
    "pathdir": Path.home() / ".mb" / "cache",
    "ttl": getenv("MB_CACHE_TTL", ONE_WEEK),
    "context_policy": getenv("MB_CACHE_CONTEXT_POLICY", "ttl"),
    "persistent": getenv("MB_CACHE_PERSISTENT", False),
    "maxsize": getenv("MB_CACHE_MAXSIZE", 100 * MB),
}


LOG_CONFIG: LogConfig = {
    "level": getenv("MB_LOG_LEVEL", "info"),
    "handlers": {
        "default": ["rich"],
        "file": ["file"],
    },
    "pathdir": Path.home() / ".mb" / "logs",
    "show_locals": getenv("MB_LOG_SHOW_LOCALS", False),
    "show_stack": getenv("MB_LOG_SHOW_STACK", False),
    "exclude_modules": getenv("MB_LOG_EXCLUDE_MODULES", ["markdown_it"]),
    "ignore_third_party": getenv("MB_LOG_IGNORE_THIRD_PARTY", False),
    "full_trace": getenv("MB_LOG_FULL_TRACE", False),
    "log_off": getenv("MB_LOG_OFF", False),
}


config: MBConfig = {
    "openai_api_key": getenv("OPENAI_API_KEY", ""),
    "anthropic_api_key": getenv("ANTHROPIC_API_KEY", ""),
    "base_url": getenv("MB_BASE_URL", "https://api.mbodi.ai/test"),
    "logs": LOG_CONFIG,
    "cache": CACHE_CONFIG,
}
