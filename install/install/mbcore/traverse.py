import asyncio
import json
import logging
import os
from pathlib import Path
from typing import cast

from tomlkit import TOMLDocument
from typing_extensions import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    Generic,
    Literal,
    NamedTuple,
    ParamSpec,
    Protocol,
    TypeIs,
    TypeVar,
    overload,
)

from mbcore.cache import cache

if TYPE_CHECKING:
    import ast
    import json
    from pathlib import Path

    DocumentType = str | TOMLDocument | ast.AST
    from mbcore.types import wraps
else:
    DocumentType = object

    def wraps(*args, **kwargs):
        return lambda f: f


R_co = TypeVar("R_co", covariant=True)


class Value(Protocol):
    __await__: None


P = ParamSpec("P")
R = TypeVar("R", bound=Value | None)
T = TypeVar("T", bound=Any)

E = TypeVar("E", bound=BaseException | None)
LOGLEVEL = 1


def is_coroutine_function(func: Callable[..., R] | Callable[..., Awaitable[R]]) -> TypeIs[Callable[..., Awaitable[R]]]:
    return asyncio.iscoroutinefunction(func)


# Special type that represents: if the second item is None, the first must be non-None and vice versa
class ResultOrErrorType(Protocol[R, E]):
    result: R
    error: E


class NamedResultOr(NamedTuple, Generic[R, E]):
    result: R
    error: E


class NamedResult(NamedResultOr[R, None]): ...


class NamedError(NamedResultOr[None, E]): ...


class Result(ResultOrErrorType[R, None]):
    result: R
    error: None

    def __bool__(self) -> Literal[True]:
        return True

    __iter__ = NamedResult.__iter__


class Error(ResultOrErrorType[None, E]):
    result: None
    error: E


    def __bool__(self) -> Literal[False]:
        return False

    __iter__ = NamedError.__iter__


class DocumentLoadError(Exception):
    def __init__(self, e: Exception | None | str = None):
        if isinstance(e, str):
            self.msg = e
            return
        if e is not None:
            self.__traceback__ = e.__traceback__
            self.__cause__ = e.__cause__


# Type guard functions that tell the type checker about our invariants
def has_result(t: NamedResult[R] | NamedError[E] | Any) -> TypeIs[NamedResult[R]]:
    return t.error is None


def has_error(t: NamedResult[R] | NamedError[E] | Any) -> TypeIs[NamedError[E]]:
    return t.error is not None


@overload
def with_err(
    func: Callable[P, Awaitable[R | T]],
) -> Callable[P, Awaitable[NamedResult[T] | NamedError[DocumentLoadError]]]: ...
@overload
def with_err(func: Callable[P, T]) -> Callable[P, NamedResult[T] | NamedError[DocumentLoadError]]: ...
@overload
def with_err(func: Callable[P, R]) -> Callable[P, NamedResult[R] | NamedError[DocumentLoadError]]: ...
def with_err(func: Callable[P, R] | Callable[P, Awaitable[R]]) -> Any:
    if is_coroutine_function(func):
        f = cast(Callable[P, Awaitable[R]], func)

        @wraps(func, returns=NamedResult[R] | NamedError[DocumentLoadError])
        async def _wrapper(*args: P.args, **kwargs: P.kwargs):
            try:
                result = await f(*args, **kwargs)
                return NamedResult(result, None)
            except Exception as e:
                return NamedError(None, DocumentLoadError(e))

        return _wrapper
    try:

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> NamedResult[R] | NamedError[DocumentLoadError]:
            try:
                return NamedResult(func(*args, **kwargs), None)
            except Exception as e:

                return NamedError(None, DocumentLoadError(e))

        return cast(Callable[P, NamedResult[R] | NamedError[DocumentLoadError]], wrapper)
    except Exception as e:
        return lambda *args, **kwargs: NamedError(None, DocumentLoadError(e))


@with_err
def search_parents_for_file(
    file_name: Path | str,
    max_levels=3,
    cwd: "Path | str | None | None" = None,
) -> "Path":
    """Search parent directories for a file."""
    file_name = Path(str(file_name))
    if file_name.exists() and file_name.is_relative_to(Path(str(cwd))):
        return Path(str(file_name))
    logging.getLogger("default").log(LOGLEVEL, f"exists ? {Path(file_name).exists()}")
    file_name = file_name.name if file_name.is_absolute() else file_name

    seen = set()
    current_dir = Path(cwd) if cwd else Path.cwd()
    logging.getLogger("default").log(LOGLEVEL, f"Searching for {file_name} in parent directories of {current_dir}")
    it = 0
    target_file = current_dir / file_name
    while it <= max_levels and not target_file.exists():
        seen.add(current_dir)
        logging.getLogger("default").log(LOGLEVEL, f"Checking {target_file}")
        current_dir = current_dir.parent
        target_file = current_dir / file_name
        it += 1
    if target_file.exists():
        logging.getLogger("default").log(LOGLEVEL, f"Found {target_file}")

    if target_file.exists():
        return target_file
    raise FileNotFoundError(f"File '{file_name}' not found in parent directories.")


@with_err
async def asearch_parents_for_file(
    file_name: Path | str,
    max_levels=3,
    cwd: "Path| str | None" = None,
) -> Path:
    """Search parent directories for a file."""
    try:
        print(f">>> DEBUG 1: file_name={file_name} (type: {type(file_name)})")

        # Convert to Path object
        original_file_name = file_name  # Save for error messages
        file_name_str = str(file_name)
        print(
            f">>> DEBUG 2: file_name_str={file_name_str}, has_slash={'/' in file_name_str}, exists={os.path.exists(file_name_str)}",
        )

        # For paths like "cython/cython", extract just the last component
        if "/" in file_name_str and not os.path.exists(file_name_str):
            # Extract the last part after the last slash
            search_name = file_name_str.split("/")[-1]
            print(f">>> DEBUG 3A: search_name={search_name} (from slash-based extraction)")
        else:
            # Convert to Path and get name
            file_name = Path(file_name_str)
            print(f">>> DEBUG 3B: file_name Path={file_name}")

            # If the file exists as an absolute path, return it immediately
            if file_name.is_absolute() and file_name.exists():
                print(f">>> DEBUG 4: Returning absolute path that exists: {file_name}")
                return file_name

            # Extract just the filename part
            search_name = file_name.name
            print(f">>> DEBUG 5: search_name={search_name} (from Path.name)")

        # Always use resolved absolute paths
        current_dir = Path(cwd).resolve() if cwd else Path.cwd().resolve()
        print(f">>> DEBUG 6: current_dir={current_dir}")

        it = 0
        target_file = current_dir / search_name
        print(f">>> DEBUG 7: target_file={target_file}, exists={target_file.exists()}")

        # Check if the file exists in the current directory before entering the loop
        if target_file.exists():
            print(f">>> DEBUG 8: Found file in current directory, returning: {target_file.resolve()}")
            return target_file.resolve()

        logging.getLogger("default").log(
            LOGLEVEL, f"Searching for {search_name} in parent directories of {current_dir}",
        )
        while it <= max_levels and not target_file.exists():
            logging.getLogger("default").log(LOGLEVEL, f"Checking {target_file}")
            print(f">>> DEBUG LOOP {it}: Checking {target_file}, exists={target_file.exists()}")
            current_dir = current_dir.parent
            target_file = current_dir / search_name
            it += 1
            if target_file.exists():
                print(f">>> DEBUG 9: Found file in parent directory, returning: {target_file.resolve()}")
                # Always return an absolute path
                return target_file.resolve()

        print(f">>> DEBUG 10: File not found after searching {it} levels, max_levels={max_levels}")
        # When search fails, raise the error to ensure correct error handling
        raise FileNotFoundError(f"File '{original_file_name}' not found in parent directories.")
    except Exception as e:
        print(f">>> DEBUG ERROR: {type(e).__name__}: {str(e)}")
        # Re-raise to ensure @with_err catches it properly
        raise FileNotFoundError(f"Error searching for {original_file_name}: {str(e)}")


# @acache
@with_err
async def asearch_children_for_file(
    file_name: "Path",
    max_levels=3,
    cwd: "Path | str| None" = None,
) -> Path:
    """Search parent directories for a file."""
    # Prevent None directory searches
    if cwd is None:
        cwd = Path.cwd()

    # Use resolved path to prevent redundant searches
    current_dir = Path(str(cwd)).resolve()
    file_name = Path(str(file_name))

    if file_name.exists() and file_name.is_relative_to(current_dir):
        return file_name
    logging.getLogger("default").log(LOGLEVEL, f"Searching for {file_name} in child directories of {current_dir}")
    fn = file_name.name if file_name.is_absolute() else file_name
    visited = set()
    target_file = current_dir / fn

    target_file = current_dir / fn
    q = [current_dir]
    it = 0
    while it <= max_levels and not target_file.exists() and q:
        current_dir = q.pop(0)
        visited.add(current_dir)
        logging.getLogger("default").log(LOGLEVEL, f"Checking {current_dir}")
        for child in current_dir.iterdir():
            if child not in visited:
                if child.is_dir():
                    q.append(child)
                elif child.name == getattr(fn, "name", fn):
                    target_file = child
                    break
        it += 1
    if not target_file.exists():
        raise DocumentLoadError(f"File '{file_name}' not found in child directories.")
    return target_file


# @cache
@with_err
def search_children_for_file(
    file_name: "Path | str",
    max_levels=3,
    cwd: "Path | str | None" = None,
) -> Path:
    """Search parent directories for a file."""
    file_name = Path(str(file_name))
    target_file = Path(str(file_name))
    visited = set()

    file_name = Path(str(file_name))
    if file_name.is_absolute() and cwd is not None:
        raise DocumentLoadError("Cannot search for absolute paths with a cwd.")
    wd = Path(cwd) if cwd else Path.cwd()
    if (wd / file_name).exists():
        return wd / file_name
    fn = (file_name.name if file_name.is_absolute() else file_name) if not file_name.exists() else file_name
    logging.getLogger("default").log(LOGLEVEL, f"Searching for {file_name} in child directories of {wd}")
    it = 0

    target_file = wd / fn
    q = [wd]
    while it <= max_levels and not target_file.exists() and q:
        current_dir = q.pop(0)
        visited.add(current_dir)
        logging.getLogger("default").log(LOGLEVEL, f"Checking {current_dir}")
        if current_dir.is_dir():
            for child in current_dir.iterdir():
                if child not in visited:
                    if child.is_dir():
                        q.append(child)
                    elif child.name == getattr(fn, "name", fn):
                        target_file = child
                        break
        it += 1
    if not target_file.exists():
        raise DocumentLoadError(f"File '{file_name}' not found in child directories: {visited}")
    return target_file


_find_cache = {}


# @acache
@with_err
async def afind_file(file_name: "Path | str", cwd: "Path |str | None" = None, max_levels=3) -> Path:
    """Find a file in parent or child directories."""
    from pathlib import Path

    from mbcore.log import verbose

    wd = Path(cwd) if cwd else Path.cwd()
    if (wd / file_name).exists():
        return wd / file_name

    fn = Path(str(file_name))
    verbose(f"finding in {fn}")

    if fn.exists() and fn.is_relative_to(wd):
        return fn
    try:
        # Try to find in children directories
        result = await asearch_children_for_file(fn, max_levels=max_levels, cwd=cwd)
        if has_result(result):
            return result.result

        # Try to find in parent directories
        result = await asearch_parents_for_file(fn, max_levels=max_levels, cwd=cwd)
        if has_result(result):
            return result.result
        if has_error(result):
            raise result.error
    except BaseException as e:
        raise DocumentLoadError(e)


def path_to_uri(path: str) -> str:
    if os.sep == "/":
        return f"file://{os.path.abspath(path).replace(' ', '%20')}"

    return f"file:///{os.path.abspath(path).replace(' ', '%20').replace(os.sep, '/')}"


def setup_workspace() -> Path:
    """Setup the workspace."""
    from pathlib import Path

    return Path.home() / ".mb" / "workspaces" / "default"


@cache(persistent=True)
def find_workspace(cwd: "Path | str | None" = None) -> str:
    """Find the workspace name."""
    wd = find_file("pyproject.toml", cwd=cwd, workspace=False)
    if has_result(wd):
        return wd.result.parent.name
    if ws := setup_workspace():
        return ws.name
    raise DocumentLoadError("Could not find workspace")


@with_err
def find_file(file_name: "Path | str", cwd: "Path | str | None" = None, max_levels=3, workspace: bool = False) -> Path:
    """Find a file in parent or child directories."""

    def verbose(*args):
        logging.getLogger("default").log(LOGLEVEL, *args)

    wd = Path(cwd).resolve() if cwd else Path.cwd().resolve()
    if workspace:
        wd = Path.home() / ".mb" / "workspaces" / find_workspace(cwd)
    fn = Path(str(file_name))
    if fn.exists() and fn.is_relative_to(wd):
        return fn

    result = search_children_for_file(file_name, max_levels=max_levels, cwd=cwd)

    if has_result(result):
        return result.result
    result = search_parents_for_file(file_name, max_levels=max_levels, cwd=cwd)
    if has_result(result):
        return result.result
    raise DocumentLoadError(f"File '{file_name}' not found in parent or child directories.")

@with_err
async def aload_file(file_name: "Path | str", cwd: "Path | str | None" = None) -> "DocumentType":
    """Load a file."""
    import aiofiles

    # First check if the file exists directly
    file_path = Path(str(file_name))
    if cwd and file_path.exists() and file_path.is_relative_to(Path(str(cwd))) or not cwd and file_path.exists():
        fn = file_path
    else:
        # Try to find the file
        result = await afind_file(file_name, cwd=cwd)
        if not has_result(result):
            raise result.error
        fn = result.result

    # At this point, fn is guaranteed to be a valid Path
    async with aiofiles.open(fn) as f:
        content = await f.read()
        if fn.suffix == ".json":
            return json.loads(content)
        if fn.suffix == ".toml":
            import tomlkit

            return tomlkit.loads(content)
        if fn.suffix == ".py":
            import ast

            return ast.parse(content)
        return content


# @cache
@with_err
def load_file(file_name: "Path | str", cwd: "Path | str | None" = None) -> DocumentType:
    """Load a file."""
    import json

    fn, err = find_file(file_name, cwd=cwd)
    if err:
        raise err
    assert fn is not None  # Help type checker understand our invariant

    # At this point, fn is guaranteed to be valid (not None)
    with fn.open() as f:
        if fn.suffix == ".json":
            return json.load(f)
        if fn.suffix == ".yaml":
            import yaml

            return yaml.load(fn.read_bytes(), yaml.SafeLoader)
        if fn.suffix == ".toml":
            import tomlkit

            return tomlkit.loads(f.read())
        if fn.suffix == ".py":
            import ast

            return ast.parse(f.read())
        return f.read()


@with_err
def find_mb(cwd: "Path | None" = None) -> Path:
    """Find the mb directory."""
    from pathlib import Path

    cwd = Path(str(cwd)) if cwd else Path.cwd()
    if (cwd / ".mb").exists():
        return cwd / ".mb"

    # Try to find in parent directories
    result = search_parents_for_file(".mb", cwd=cwd)
    if has_result(result):
        return result.result

    # Try to find in child directories
    result = search_children_for_file(".mb", cwd=cwd)
    if has_result(result):
        return result.result

    # Create a default .mb directory if not found
    p = Path.home() / ".mb"
    p.mkdir(exist_ok=True, parents=True)
    return p


@with_err
def find_mb_toml(cwd: "Path | str | None" = None) -> "TOMLDocument":
    """Find the mb.toml file."""
    import tomlkit

    # Try mb.toml first
    mb_toml = find_mb_toml_path(cwd)
    if has_result(mb_toml):
        try:
            return tomlkit.loads(mb_toml.result.read_text())
        except Exception as e:
            raise DocumentLoadError(f"Error loading mb.toml: {e}")
    raise DocumentLoadError("mb.toml not found")


@with_err
def find_mb_toml_path(cwd: "Path | str | None" = None) -> Path:
    """Find the mb.toml file."""
    result = find_file("pyproject.toml")
    if has_error(result):
        raise result.error
    project = result.result
    mb_toml = project.parent / "mb.toml"
    if not mb_toml.exists():
        raise FileNotFoundError(f"mb.toml not found in {project.parent}")
    return mb_toml
