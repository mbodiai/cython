import asyncio
import re
import sys
from asyncio.tasks import Task
from collections.abc import Callable, Iterable
from contextlib import nullcontext, suppress
from contextvars import Context
from dataclasses import asdict, dataclass, field
from functools import partial
from pathlib import Path
import io
import tempfile
import os
import time


from mbcore.ctx import chdir
import tomlkit
from typing_extensions import (
    TYPE_CHECKING,
    Any,
    Generic,
    Literal,
    NamedTuple,
    NewType,
    Required,
    Self,
    TypedDict,
    TypeVar,
    cast,
)

from mbpy.helpers._env import version_info as version_tuple
from mbcore.import_utils import smart_import

from mbpy.store.py.models.pyproject import PyProject
if TYPE_CHECKING:

    from types import FrameType
    from inspect import Traceback
    from mbcore.collect import compose, getin
    from mbcore.display import Progress, TaskID, safe_print

    from mbcore.traverse import load_file,TOMLDocument

    from mbpy.env import (
        Condition,
        Env,
        SystemSettings,
        UrlPath,
        isgit,
        sync_org_and_repo,
    )
    from mbpy.tools.search import PackageInfo as GitHubPackageInfo
    from pip._internal.commands.install import InstallCommand
    from pip._internal.commands.uninstall import UninstallCommand

class UploadInfo(TypedDict, total=False):
    version: str
    upload_time: str
    requires_python: str


class PyPackageInfo(TypedDict, total=False):
    name: Required[str]
    version: str
    author: str
    summary: str
    description: str
    latest_release: str
    earliest_release: "UploadInfo"
    urls: dict[str, str]
    github_url: str
    requires_python: str
    releases: list[dict[str, UploadInfo]]
    source: str
    extras: dict[str, object]


class CPackageInfo(TypedDict, total=False):
    name: str
    version: str
    spec: str
    conditions: str | None
    path: str | None
    repo: str | None
    manager: Literal["apt", "brew", "yum", "conan"]


class RepoNotFoundError(Exception):
    """Raised when a repository is not found."""

    ...

def get_project(path: Path | str) -> PyProject:
    """Get the project from a path."""
    with chdir(path):
        return PyProject.fromtoml()

class PipOutputCapture(io.StringIO):
    """Capture and process pip command output."""

    def __init__(
        self,
        style: str = "",
        progress_tid: "tuple[Progress, TaskID]|None" = None,
        show: bool = True,
        quiet: bool = False,
    ):
        """
        Initialize output capturer.

        Args:
            style: Rich style string for output formatting
            progress_tid: Tuple of (Progress, TaskID) for progress updates
            show: Whether to print captured output
            quiet: If True, don't write directly to stdout even if show is True
        """
        super().__init__()  # Initialize the StringIO parent
        self.lines: list[str] = []
        self.style = style
        self.prog, self.tid = progress_tid if progress_tid else (None, None)
        self.show = show
        self.quiet = quiet
        self._last_progress_update = time.time()
        self._progress_update_interval = (
            0.1  # Update progress bar at most every 0.1 seconds
        )
        self._in_write = False  # Add flag to prevent recursion

    def write(self, data):
        """Process written data, splitting on newlines."""
        # Prevent recursion by checking if we're already in a write operation
        if self._in_write:
            return super().write(data)

        self._in_write = True
        try:
            # First call the parent's write method to maintain StringIO functionality
            super().write(data)

            # Our custom processing for displaying output
            if "\n" in data:
                lines = data.split("\n")
                # If the last element is empty, remove it (trailing newline)
                if not lines[-1]:
                    lines.pop()

                self.lines.extend(lines)

                if self.show and not self.quiet:
                    # Print the output directly using sys.stdout to avoid recursion
                    for line in lines:
                        if line.strip():  # Only print non-empty lines
                            # Update progress if available
                            current_time = time.time()
                            if (
                                self.prog
                                and self.tid
                                and (
                                    current_time - self._last_progress_update
                                    > self._progress_update_interval
                                )
                            ):
                                # Calculate progress based on pip output indicators
                                if "Installing collected packages:" in line:
                                    self.prog.update(self.tid, completed=25)
                                elif "Successfully installed" in line:
                                    self.prog.update(self.tid, completed=100)
                                elif "Downloading" in line or "Processing" in line:
                                    self.prog.update(
                                        self.tid, advance=1
                                    )  # Small increment for each download
                                self._last_progress_update = current_time

                            if self.prog and self.tid:
                                # Use rich console to print with style
                                self.prog.console.print(line, style=self.style)
                            else:
                                # Fall back to direct print if no progress object
                                import sys

                                sys.stdout.write(line + "\n")
                                sys.stdout.flush()
        finally:
            self._in_write = False

    def get_output(self):
        """Get all captured output as a string."""
        return "\n".join(self.lines)

async def _clone_git(url: str, clone_path: Path|str, ref: str | None = None, progress_tid=None):
    """Clone and install a git repository, checking out a specific ref if provided.

    Args:
        url (str): Git repository URL
        clone_path (Path): Path where to clone the repository
        ref (str | None): Specific ref to check out after cloning

    Returns:
        tuple[str, str]: Base name and pip install command

    """
    from mbcore import ctx
    from mbcore.log import debug, info, warning as warn

    from mbpy.cmd import arun
    from mbpy.env import getws
    from mbpy.git.check import resolve_state, switch_branch
    with ctx.chdir(getws()):

        try:
            # Create clone directory
            clone_path = Path(str(clone_path)).resolve()
            
            debug(f"Clone path: {clone_path} for {url} @ {ref or 'default branch'}")
            
            # Check if directory already exists and has files
            if clone_path.exists() and len(list(clone_path.iterdir())) > 0:
                info(f"{clone_path} exists, attempting update...")
                with ctx.chdir(clone_path):
                    # If a specific ref is requested, check it out first
                    current_branch_or_ref = await arun("git rev-parse --abbrev-ref HEAD", show=False)
                    current_commit = await arun("git rev-parse HEAD", show=False)

                    needs_checkout = False
                    if ref:
                        # Check if ref is a branch name different from current
                        if ref != current_branch_or_ref.strip():
                            # Also check if ref is a commit/tag different from current commit
                            try:
                                ref_commit = await arun(f"git rev-parse {ref}^{{commit}}", show=False) # Get commit for ref
                                if ref_commit.strip() != current_commit.strip():
                                    needs_checkout = True
                            except Exception:
                                # If rev-parse fails, ref likely doesn't exist locally yet or is ambiguous
                                needs_checkout = True # Assume checkout is needed
                        else:
                             # Ref matches current branch, no checkout needed before pull
                             pass

                    if needs_checkout and ref:
                        info(f"Switching to ref: {ref}")
                        await switch_branch(ref)
                        await resolve_state(action="pull --rebase")
                    else:
                        # Already on the correct ref (or no ref specified), just pull
                        await resolve_state(action="pull --rebase")

                base = clone_path.stem
                return base, f"file://{clone_path.resolve()}".removeprefix("-e ")

            # Create directory if it doesn't exist
            clone_path.mkdir(parents=True, exist_ok=True)
            
            # Clone command - clone directly into the target path's parent
            clone_target_dir = clone_path.parent
            clone_target_dir.mkdir(parents=True, exist_ok=True) # Ensure parent exists
            # Strip 'git+' prefix for the actual clone command
            actual_clone_url = url.replace("git+", "")
            clone_cmd = f"git clone {actual_clone_url} {clone_path.name}" # Clone into final dir name within parent
            info(f"Cloning {actual_clone_url} into {clone_path.name} within {clone_target_dir}")

            with ctx.chdir(clone_target_dir): # Change to parent directory for cloning
                result = await arun(clone_cmd, show=True)
                if result and "error" in result.lower():
                     # Check if the error is "destination path exists" - might happen in races
                     if "already exists and is not an empty directory" in result:
                          warn(f"Clone destination {clone_path} already exists, attempting update instead.")
                          # Fallback to the update logic if clone fails due to existence
                          with ctx.chdir(clone_path):
                              if ref:
                                  await switch_branch(ref)
                              await resolve_state(action="pull --rebase")
                              await arun("git submodule update --init --recursive", show=True)
                          return clone_path.stem, f"file://{clone_path.resolve()}".removeprefix("-e ")
                     else:
                          raise RuntimeError(f"Failed to clone repository: {result}")

            # Checkout specific ref if provided AFTER cloning
            if ref:
                with ctx.chdir(clone_path):
                    info(f"Checking out ref: {ref}")
                    # Fetch might be needed if ref is remote and wasn't cloned initially
                    await arun("git fetch origin", show=False)
                    checkout_result = await arun(f"git checkout {ref}", show=True)
                    if checkout_result and "error" in checkout_result.lower():
                        # If checkout fails, maybe it's a remote branch not tracked? Try tracking.
                        if f"pathspec '{ref}' did not match" in checkout_result:
                             track_result = await arun(f"git checkout --track origin/{ref}", show=True)
                             if track_result and "error" in track_result.lower():
                                  warn(f"Failed to checkout ref '{ref}' even after trying to track: {track_result}")
                             else:
                                  info(f"Successfully checked out and tracked remote ref: {ref}")
                        else:
                            warn(f"Failed to checkout ref '{ref}': {checkout_result}") # Warn instead of erroring

            # Update submodules
            with ctx.chdir(clone_path):
                await arun("git submodule update --init --recursive", show=True)

            base = clone_path.stem
            # Return the file path for pip install
            return base, f"file://{clone_path.resolve()}".removeprefix("-e ")

        except Exception as e:
            from mbcore.log import error
            error(f"Error during git operations: {str(e)}")
            raise


def sync_to_string(dep: "Dependency") -> str:
    """Convert a Dependency object to a string."""
    dep.version = dep.version or dep.installed_version() or ""
    version_str = f">={dep.version_info}" if dep.version_info else ""
    conditions_str = f"; {dep.conditions}" if dep.conditions else ""
    extras = f"[{','.join(map(str, dep.extras))}]" if dep.extras else ""
    install_cmd = f"{dep.name}{version_str}{extras}{conditions_str}"
    return install_cmd.replace("_", "-").lower()


Base = NewType("Base", str)
PipInstallCmd = NewType("PipInstallCmd", str)
RequirementsTxtName = NewType("RequirementsTxtName", str)
ProjectTomlName = NewType("ProjectTomlName", str)
Source = NewType("Source", str)
VersionStr = NewType("VersionStr", str)
Org = NewType("Org", str)
Repo = NewType("Repo", str)



class GitPackageInfo(NamedTuple):
    base: Base
    pip_install_cmd: PipInstallCmd
    source: Source
    requirements_txt_name: RequirementsTxtName
    project_name: ProjectTomlName
    version: VersionStr
    org: Org
    repo: Repo
def isurl(url: str) -> bool:
    """Check if a string is a URL."""
    return url.startswith("http") or url.startswith("file://") or url.startswith("git+")
def parse_git(dep: "Dependency") -> GitPackageInfo:
    """Parse a git dependency and return the base name and install command."""
    from mbpy.env import  git_devws, sync_org_and_repo
    dep.org, dep.repo = sync_org_and_repo(dep.source) if not dep.org or not dep.repo else (dep.org, dep.repo)
    if dep.org and dep.repo and dep._pip_install_cmd:
        return GitPackageInfo(
            base=Base(dep.repo),
            pip_install_cmd=PipInstallCmd(dep._pip_install_cmd),
            source=Source(str(dep.source)),
            requirements_txt_name=RequirementsTxtName(dep._pip_install_cmd),
            project_name=ProjectTomlName(dep.project_name),
            version=VersionStr(str(dep.version_info)),
            org=Org(dep.org),
            repo=Repo(dep.repo),
        )

    src = str(dep.original_source)
    if not isurl(src):
        src = src.replace("file://", "").replace("-","_").lower()


    source = git_devws(dep.org, dep.repo)
    source = str(source)
    source.replace("file://","")
    requirements_name = f"-e {source}" if dep.editable else f"{dep.name} @ file://{source}"
    source = source.replace("file://","")
    project_name = f"{dep.name} @ file://{source}"
    

    return GitPackageInfo(
        base=Base(dep.repo),
        pip_install_cmd=PipInstallCmd(requirements_name.removeprefix("-e ")),
        source=Source(str(source)),
        requirements_txt_name=RequirementsTxtName(requirements_name),
        project_name=ProjectTomlName(project_name),
        version=VersionStr(PyProject.fromtoml().project.version or ""),
        org=Org(dep.org),
        repo=Repo(dep.repo),
    )


def get_requirements_name(dep: "Dependency") -> str:
    """Get the requirements name for a Dependency object."""
    if dep.editable:
        return f"-e {dep.source}"
        
    if dep.git:
        # For git dependencies, use the same @ syntax as project_name but with requirements-specific handling
        # Base URL construction
        if hasattr(dep, 'original_source') and dep.original_source.startswith('git+'):
            # If it's a full git URL with reference
            git_url = dep.original_source
        elif hasattr(dep, 'org') and dep.org and hasattr(dep, 'repo') and dep.repo:
            # If it's org/repo format, always use .git suffix for requirements name
            git_url = f"git+https://github.com/{dep.org}/{dep.repo}.git"
            # Add git reference if available
            if hasattr(dep, 'git_ref') and dep.git_ref:
                git_url += f"@{dep.git_ref}"
        else:
            # Fallback to source
            git_url = str(dep.source)
            
        # Return with @ syntax for Python requirements
        return f"{dep.base} @ {git_url}"
        
    version_str = f">={dep.version_info}" if dep.version_info else ""
    conditions_str = f"; {dep.conditions}" if dep.conditions else ""
    # Use the extras_str property for correct formatting
    extras_formatted_str = dep.extras_str 
    install_cmd = f"{dep.name}{extras_formatted_str}{version_str or ''}{conditions_str}"
    return install_cmd.replace("_", "-").lower()


def get_toml_name(dep: "Dependency") -> str:
    """Get the project name for a Dependency object, including git ref."""
    from pathlib import Path
    import tempfile

    if dep.editable:
        # Editable installs use file paths, ref doesn't apply here
        source_path = str(dep.source).replace("file://", "")
        return f"{dep.base} @ file://{source_path}"

    if dep.git:
        # Check if the source is a local path that exists (a cloned repo)
        try:
            # Check for local clone existence FIRST
            from mbpy.env import git_devws, sync_org_and_repo
            if dep.org and dep.repo:
                local_path = git_devws(dep.org, dep.repo)
                if local_path.exists():
                    return f"{dep.base} @ file://{str(local_path)}"
            # Fallback check: If source itself is a valid existing path
            source_path = Path(str(dep.source))
            if source_path.exists() and not str(dep.source).startswith("git+"):
                 return f"{dep.base} @ file://{str(source_path)}"
        except Exception as e:
             debug(f"Error checking local git path: {e}") # Log error but continue
             pass

        # If it's the original git URL, return it exactly as-is
        if hasattr(dep, 'original_source') and isinstance(dep.original_source, str):
            original = dep.original_source
            if original.startswith('git+'):
                return original
                
        # Fallback: reconstruct the git URL from available properties
        if hasattr(dep, 'org') and dep.org and hasattr(dep, 'repo') and dep.repo:
            # Determine the URL format based on original source
            if hasattr(dep, 'original_source') and dep.original_source == f"{dep.org}/{dep.repo}":
                url = f"git+https://github.com/{dep.org}/{dep.repo}"
            else:
                url = f"git+https://github.com/{dep.org}/{dep.repo}.git"
                
            if dep.git_ref and dep.git_ref != "":
                url += f"@{dep.git_ref}"
            return url
            
        # Last resort: use source directly if it's a git URL
        if str(dep.source).startswith("git+"):
            return str(dep.source)
        
        # Ultimate fallback
        return f"git+{str(dep.source)}"

    # Default handling for regular dependencies
    version_str = f">={dep.version_info}" if dep.version_info else ""
    conditions_str = f"; {dep.conditions}" if dep.conditions else ""
    extras_str = dep.extras_str
    install_cmd = f"{dep.name}{extras_str}{version_str or ''}{conditions_str}"
    return install_cmd.replace("_", "-").lower()


T = TypeVar("T")

def debug(*args, **kwargs) -> bool | None:
    """Print debug information."""
    import logging

    if not args and not kwargs:
        return logging.getLogger("default").getEffectiveLevel() <= logging.DEBUG    

    return logging.getLogger("default").debug(*args, **kwargs)

def error(*args, **kwargs) -> bool | None:
    """Print error information."""
    import logging

    if not args and not kwargs:
        return logging.getLogger("default").getEffectiveLevel() <= logging.ERROR
    return logging.getLogger("default").error(*args, **kwargs)

def warn(*args, **kwargs) -> bool | None:
    """Print warning information."""
    import logging

    if not args and not kwargs:
        return logging.getLogger("default").getEffectiveLevel() <= logging.WARNING
    return logging.getLogger("default").warning(*args, **kwargs)

def caller(mode: str = "function") -> "FrameType| Traceback | str":
    """Get the caller of a function."""
    import inspect

    current = inspect.currentframe()
    frame = current.f_back if current else None
    if frame is None:
        return ""
    if mode == "file":
        return inspect.getframeinfo(frame).filename
    if mode == "function":
        return inspect.getframeinfo(frame).function
    return inspect.getframeinfo(frame)
class AsyncTreeNode(TypedDict, Generic[T]):
    name: str
    value: T
    children: "dict[str, AsyncTreeNode[T]] | None"
    context: Context | None


if TYPE_CHECKING:
    from typing import Coroutine

    from typing_extensions import Any, Callable, Concatenate, ParamSpec, TypeVar

    P = ParamSpec("P")
    CoroT = Coroutine[Any, Any, T]
    T = TypeVar("T")




def with_async_init(
    async_init: "Callable[Concatenate[Dependency, ...], Coroutine[Any,Any,Any]]",
) -> "Callable[[Callable[Concatenate[Dependency, P], Coroutine[Any,Any,T]]], Callable[Concatenate[Dependency, P], Coroutine[Any,Any,T]]]":
    def decorator(
        func: "Callable[Concatenate[Dependency, P], Coroutine[T, Any, Any]]",
    ) -> "Callable[Concatenate[Dependency, P], Coroutine[Any,Any,T]]":
        if func is None:
            raise ValueError(f"Function is None: {func}")

        async def wrapper(self: "Dependency", *args: "P.args", **kwargs: "P.kwargs") -> "Coroutine[Any,Any,T]":
            cond: asyncio.Condition = self._async_init_condition
            if not self._async_initialized and (not cond.locked() or await cond.acquire()):
                await async_init(self,*args,**kwargs)
            if self._tasks and not self.isdone() and (not cond.locked() or await cond.acquire()):
                async with cond:
                    # Create a copy of the tasks to avoid dictionary modification during iteration
                    tasks_copy = list(self._tasks.values())
                    for task in tasks_copy:
                        try:
                            await task
                        except KeyboardInterrupt:
                            task.cancel()
                            raise
                        except Exception as e:
                            error("Failed to initialize ",caller(mode='file'),f" {self}: {e}")

            if self.isdone():
                try:
                    return await func(self, *args, **kwargs)
                except Exception as e:
                    debug("Failed to initialize ",caller(mode='file'),f" {self}: {e}")
                    if self._tasks:
                        # Create a copy of the tasks to avoid dictionary modification during iteration
                        tasks_copy = list(self._tasks.values())
                        for task in tasks_copy:
                            task.cancel()
                    if debug():
                        import traceback

                        traceback.print_exc()
                        error("Failed to initialize ",caller(mode='file'),f" {self}: {e}")
                        raise RuntimeError(f"Failed to initialize {caller()} {self}") from e
            return await func(self, *args, **kwargs)

        return wrapper # type: ignore

    return decorator


SOURCE_KEYS = ["install_cmd", "source", "pip_install_cmd", "project_name"]


def capture_text(*args, **kwargs) -> str:
    import sys
    from contextlib import redirect_stderr, redirect_stdout
    from io import StringIO

    from rich.console import Console

    console = Console(record=True)
    output = StringIO()
    with redirect_stdout(output), redirect_stderr(output):
        console.print(*args, **kwargs)
        sys.stdout.flush()
        sys.stderr.flush()
    return output.getvalue()


def intorstr(value: int | str) -> int:
    """Convert a value to an integer."""
    if isinstance(value, int):
        return value
    try:
        return int(value)
    except ValueError:
        return 0


def notnone(d: dict) -> dict:
    """Remove None values from a dictionary."""
    return {k: notnone(v) if isinstance(v, dict) else v for k, v in d.items() if v is not None}


@dataclass
class CDependency:
    source_paths: "list[UrlPath]" = field(default_factory=list)
    abi_version: int | None = field(default=None)
    c_standard: int | None = field(default=None)
    cxx_standard: int | None = field(default=None)
    shared_libs: list[str] | None = field(default=None)
    name: str | None = field(default=None)
    git: bool = False

    def __str__(self):
        from mbcore.collect import pluckattr
        return self.name or f"CDep({','.join(pluckattr('name', self.source_paths))})"

    def __post_init__(self):
        self.source_paths = []
        self.abi_version = self.abi_version or 0
        self.c_standard = self.c_standard or 11
        self.shared_libs = self.shared_libs or []
        self.git = any("git+" in path.name or isgit(path) for path in map(compose(Path, str), self.source_paths))

    @classmethod
    async def afrom_toml(cls, name: str, toml_path: "Path | str" = "pyproject.toml") -> "CDependency":
        from mbpy.pkg.toml import aload_toml
        deps = await aload_toml(toml_path)

        content = deps.unwrap().setdefault("dependencies", {}).get(name)
        if not content:
            raise ValueError(f"Dependency {name} not found in pyproject.toml")

        specs = cls()
        for key, value in content.items():
            if key == "source_paths":
                specs.source_paths = value
            elif key == "abi_version":
                specs.abi_version = value
            elif key == "c_standard":
                specs.c_standard = value
            elif key == "shared_libs":
                specs.shared_libs = value

        return specs

    def __hash__(self):
        """Hash implementation for CDependency."""
        return hash((self.name, self.abi_version, self.c_standard, tuple(sorted(self.shared_libs or []))))

    @classmethod
    def from_cmake(cls, cmake_path: "Path | str" = "CMakeLists.txt") -> "CDependency":

        content,err = load_file(cmake_path, cwd=Path.cwd())
        if err:
            content,err = load_file("CMakeLists.txt", cwd=Path.cwd())
            if err:
                logging.warning("CMakeLists.txt not found in current or parent directories.")
                raise err

        specs = cls()
        if not isinstance(content, TOMLDocument):
            raise ValueError(f"CMakeLists.txt is not a valid document: {content}")
        for line in content.as_string().splitlines():
            if "TREE_SITTER_ABI_VERSION" in line and "set(" in line.lower():
                with suppress(ValueError):
                    specs.abi_version = int(line.split()[-1].rstrip(")"))
        return specs

    @classmethod
    async def afrom_cmake(cls, cmake_path: "Path | str" = "CMakeLists.txt") -> "CDependency":
        from mbcore.traverse import aload_file


        content,err = await aload_file(cmake_path, cwd=Path.cwd())
        if err:
            content, err = await aload_file("CMakeLists.txt", cwd=Path.cwd())
            if err:
                logging.warning("CMakeLists.txt not found in current or parent directories.")
                raise err

        specs = cls()
        if not isinstance(content, TOMLDocument):
            raise ValueError(f"CMakeLists.txt is not a valid document: {content}")
        for line in content.as_string().splitlines():
            if "TREE_SITTER_ABI_VERSION" in line and "set(" in line.lower():
                with suppress(ValueError):
                    specs.abi_version = int(line.split()[-1].rstrip(")"))
        return specs


@dataclass
class Project:
    from mbpy.env import SystemSettings
    system: "SystemSettings" = field(default_factory=SystemSettings.detect)
    c: list[CDependency] | None = field(default_factory=list)
    python: "list[Dependency] | None" = field(default_factory=list)

    def getcflags(self) -> str:
        return f"{self.system.cppflags} {self.system.arch}"

    def getenv(self) -> dict[str, str]:
        return asdict(self.system)

    @classmethod
    def fromlist(cls, python: "Iterable[Dependency | str]", c: "Iterable[CDependency | str]") -> "Project":
        try:
            c_ = [CDependency([dep]) if isinstance(dep, str) else dep for dep in c]

        except Exception as e:
            safe_print(f"Failed to parse C dependencies: {e}")
            c_ = []

        try:
            py = [Dependency(dep) if isinstance(dep, str) else dep for dep in python]
        except Exception:
            py = []
        return cls(c=c_, python=py)

    @classmethod
    def fromtoml(cls, toml_path: "Path | str" = "pyproject.toml") -> "Project":
        from mbpy.pkg.toml import load_toml

        toml = load_toml(toml_path).unwrap()
        return cls.fromlist(getin(toml, "project.dependencies", []), getin(toml, "tools.mb.dependencies.c", []))

    def __post_init__(self):
        from mbpy.pkg.toml import load_toml

        self.system = self.system or SystemSettings.detect()
        self.python = (
            self.python
            if self.python == []
            else [Dependency(dep) for dep in load_toml("pyproject.toml").unwrap().get("dependencies", [])]
        )
        self.c = (
            self.c if self.c == [] else [CDependency.from_cmake(cmake) for cmake in Path.cwd().rglob("CMakeLists.txt")]
        )

def strip_operators(name: str, ind=0) -> str:
    return (name.strip()
        .split("==")[ind]
        .split(">=")[ind]
        .split("<=")[ind]
        .split(">")[ind]
        .split("<")[ind]
        .split("~=")[ind]
        .split("!=")[ind]
    )
def version_name(name: str, version: str | tuple[int | str] | version_tuple | None = None) -> tuple[str, version_tuple | None]:
    """Extract the package name and version from a string."""
    n = strip_operators(name)
    if n != name and (not version or version == "0.0.0"):
        version = strip_operators(name[len(n) :], ind=-1)

    out = n,version_tuple(*map(intorstr,version.split("."))) if isinstance(version, str) and version else None
    return out

def extras_name(
    name: str, extras: "str | list[str] | list[Dependency] | None" = None
) -> "tuple[str, None | str | list[str] | list[Dependency]]":
    """Extract the package name and extras from a string."""

    n = name.strip().split("[")[0]
    if extras is None and "[" in name and "]" in name:
        ex = name[len(n) :].strip().removeprefix("[").removesuffix("]").split(",")
    elif extras is not None:
        ex = extras
    else:
        ex = []
    return n, ex


def quote(value: str) -> str:
    """Quote a string."""
    v = value.removeprefix('"').removesuffix('"').removeprefix("'").removesuffix("'")
    return f"'{v}'"

# @cache(context_policy="site_packages", persistent=True)


def get_installed_version(name: str) -> str:
    from importlib.metadata import version, PackageNotFoundError
    from mbpy.cmd import run

    try:
        out = version(name)
        if not out:
            raise PackageNotFoundError
    except PackageNotFoundError:
        out = run(f"pip show {name} | grep Version", show=False).split(":",maxsplit=1)[-1].split(" ")[0]
    if name == "mrender":
        debug(f"Installed version of {name}: {out}")

    if out.strip() == name.strip():
        out = ""
    return out

async def aget_installed_version(name: str) -> str | None:
    from importlib.metadata import version, PackageNotFoundError
    from mbpy.cmd import arun

    try:
        out = version(name)
        if not out:
            raise PackageNotFoundError
    except PackageNotFoundError:
        out = await arun(f"pip show {name} | grep Version", show=False)
        out = out.split(":",maxsplit=1)[-1].split(" ")[0]
    if name == "mrender":
        debug(f"Installed version of {name}: {out}")
    
    if out.strip() == name.strip():
        out = ""
    return out



# Assume version_tuple is defined elsewhere
# And intorstr is a helper function that converts to int if possible

def maybe_parse_version(
    q: str,
    line: str,
) -> tuple[str, str, str] | tuple[Literal[-1], str, dict[str, str]] | tuple[str, str, dict[str, str]]:
    """Parse a version from a dependency line.
    
    Args:
        q: dependency name
        line: line to parse
        
    Returns:
        tuple[str, str, str] | tuple[Literal[-1], str, dict[str, str]]: (version, line, {})
    """
    if "==" in line:
        version_str = line.split("==")[1].split()[0]
        # Remove or comment out this print statement
        # print(f"Found version for {q} in {line}: {version_str}")
        return version_str, line, {}

    if q.lower() not in line.lower():
        # Remove or comment out this print statement
        # print(f"Could not find version for {q} in {line}")
        return -1, line, {}
        
    # Find the version string in the line
    # First, check for a standard version pattern after the package name
    version_pattern = re.compile(r'{}\s+([\d\.]+)'.format(re.escape(q)), re.IGNORECASE)
    match = version_pattern.search(line)
    
    if match:
        version_str = match.group(1)
        # Remove or comment out this print statement
        # print(f"Found version for {q} in {line}: {version_str}")
        return version_str, line, {}
        
    # If not found with the first pattern, try another common pattern in pip output
    version_pattern = re.compile(r'{}-([0-9\.]+)'.format(re.escape(q)), re.IGNORECASE)
    match = version_pattern.search(line)
    
    if match:
        version_str = match.group(1)
        # Remove or comment out this print statement
        # print(f"Found version for {q} in {line}: {version_str}")
        return version_str, line, {}
    
    # Try to find version in parentheses
    version_pattern = re.compile(r'{}.+?\(([0-9\.]+)\)'.format(re.escape(q)), re.IGNORECASE)
    match = version_pattern.search(line)
    
    if match:
        version_str = match.group(1)
        # Remove or comment out this print statement
        # print(f"Found version for {q} in {line}: {version_str}")
        return version_str, line, {}

    # Remove or comment out this print statement
    # print(f"Could not find version for {q} in {line}")
    return -1, str(line), {}
  
async def run_pip_command(command_class: "type[InstallCommand] | type[UninstallCommand]", command_args, progress_tid=None, show=True, style=""):
    """Run a pip command and capture its output using pip's internal API.
    
    Args:
        command_class: The pip command class to instantiate (e.g., InstallCommand)
        command_args: List of arguments to pass to the command
        style: Rich style to apply to output lines
        progress_tid: Optional tuple of (Progress, TaskID) for progress updates
        show: Whether to display output in real-time
        
    Returns:
        tuple: (exit_code, output_text, parsed_results)
    """
    from pip._internal.cli.status_codes import SUCCESS
    from contextlib import redirect_stdout, redirect_stderr
    from mbcore.log import debug

    # Create output capturer
    capturer = PipOutputCapture(style, progress_tid=progress_tid, show=show, quiet=False)
    parsed_results = {}
    if not progress_tid:
        from mbcore.display import getprogress
        progress_tid = (getprogress(), getprogress().add_task(f"[green]Running pip {command_class.__name__.replace('Command', '').lower()}...", total=100))
    
    try:
        # Get the command name from the class name
        cmd_name = command_class.__name__.replace('Command', '').lower()
        cmd_description = f"{cmd_name.capitalize()} packages."
        
        # Create the command instance
        cmd = command_class(cmd_name, cmd_description)
        
        # Add verbose flag if not already present
        if '-v' not in command_args and '--verbose' not in command_args and show:
            command_args = ['--verbose'] + list(command_args)
        
        # Disable progress bar in pip itself since we're showing our own
        if '--progress-bar' not in command_args and '--no-progress-bar' not in command_args:
            command_args = ['--progress-bar', 'off'] + list(command_args)
            
        # Run command with output redirection
        ctx = redirect_stdout(capturer), redirect_stderr(capturer)
            
        with ctx[0], ctx[1]:
            exit_code = cmd.main(command_args)
            
            # Try to extract useful information based on command type
            if exit_code == SUCCESS:
                try:
                    # For install commands, extract package names from command args
                    # This is a safer approach than trying to use internal APIs
                    # that might change across different pip versions
                    if cmd_name == 'install':
                        # Simple extraction of package names from command args
                        parsed_results['requirements'] = [
                            arg.split('==')[0].split('>=')[0].split('<=')[0].split('>')[0].split('<')[0].split('@')[0].strip()
                            for arg in command_args 
                            if not arg.startswith('-') and not arg.startswith('--')
                        ]
                
                except Exception as e:
                    debug(f"Error extracting pip command results: {str(e)}")
 
        # Make sure to complete the progress bar when done
        if progress_tid and progress_tid[0] and progress_tid[1]:
            progress_tid[0].update(progress_tid[1], completed=100)
        
        return exit_code, capturer.get_output(), parsed_results
    except Exception as e:
        import traceback
        error_tb = traceback.format_exc()
        debug(f"Error running pip command: {str(e)}\n{error_tb}")
        
        # Make sure progress bar shows error state
        if progress_tid and progress_tid[0] and progress_tid[1]:
            progress_tid[0].update(progress_tid[1], description=f"[red]Error: {str(e)[:30]}...[/red]", completed=100)
            
        return -1, str(e), {}

@dataclass
class Dependency:
    """Handles Python package dependencies with smart version handling and installation.

    Usage:
        Create dependencies in various ways:
        >>> # From version requirement
        >>> requests = Dependency("requests>=2.24.0")
        >>> pandas = Dependency("pandas[excel,parquet]>=1.5.0")
        >>> tensorflow = Dependency("tensorflow; platform_system=='Linux'")

        >>> # From git repositories
        >>> dep = Dependency("git+https://github.com/user/repo.git")
        >>> dep = Dependency("user/repo")  # Short GitHub format

        >>> # From local paths
        >>> local = Dependency(".", editable=True)  # Current directory
        >>> path = Dependency("../mypackage", editable=True)

        Compare dependencies:
        >>> requests1 = Dependency("requests>=2.24.0")
        >>> requests2 = Dependency("requests>=2.25.0")
        >>> requests1 == requests2  # Exact version match
        False
        >>> requests1 & requests2  # Same package check
        True

        Install dependencies:
        >>> await requests.install()  # Normal install
        >>> await local.install(editable=True)  # Editable install
        >>> await dep.install(upgrade=True)  # Upgrade existing

        Version checking:
        >>> requests.require_version(min_version="2.0.0", max_version="3.0.0")
        >>> requests.warn_if_mismatch_version(min_version="2.24.0")
        >>> requests.require("for making HTTP requests")

        Get dependency info:
        >>> print(requests.base)  # Base package name
        'requests'
        >>> print(requests.version)  # Version info
        '2.24.0'
        >>> print(requests.extras)  # Optional features
        ['excel', 'parquet']

        Format for different contexts:
        >>> await requests.project_name  # For pyproject.toml
        'requests>=2.24.0'
        >>> await requests.requirements_name  # For requirements.txt
        'requests>=2.24.0'
        >>> print(requests)  # String representation
        'Dependency(name=requests, version=>=2.24.0)'

    Features:
        - Smart version parsing and comparison
        - Git repository support with auto-cloning
        - Local package installation with editable mode
        - Platform-specific conditions
        - Extras handling
        - Version requirement checking
        - Multiple output formats
        - Async installation support
    """

    name: str = field()
    version: str | tuple[int | str] | version_tuple = field(default="")
    extra: "str | list[str] | list[Dependency] | None" = field(default=None)
    conditions: "list[Condition]" = field(default_factory=list, repr=False)
    pypi_info: "PyPackageInfo" = field(default_factory=partial(PyPackageInfo, name=""))
    editable: bool = False
    upgrade: bool = False
    dependencies: "list[Dependency]" = field(default_factory=list)
    group: str | None = None
    git: bool | None = None
    _at: bool = False  # Changed from at to _at to avoid property name collision
    env: "Env | None" = None
    author: str = ""
    source: str | Path = ""
    org: str | None = None
    repo: str | None = None
    error: str | None = field(default=None, init=False, repr=False)
    editable_project_location: Path | None = field(default=None, repr=False)
    git_ref: str | None = field(default=None, init=False)
    dev_root: Path | None = None # Add optional root for development path checks

    _project_dir: Path | None = field(default=None, init=False, repr=False)
    _requirements_name: str | None = field(default=None, init=False, repr=False)
    _pyproject_name: str | None = field(default=None, init=False, repr=False)
    _project_name: str | None = field(default=None, init=False, repr=False)
    _base: str | None = field(default=None, init=False, repr=False)
    _pip_install_cmd: str | None = field(default=None, init=False, repr=False)
    _to_string: str | None = field(default=None, init=False, repr=False)
    _version: version_tuple | None = field(default=None, init=False, repr=False)
    _installed_version: str | None = field(default=None, init=False, repr=False)


    _async_initialized: bool = field(default=False, init=False, repr=False)
    _pypi_info: "PyPackageInfo| GitHubPackageInfo| None" = field(init=False, default=None, repr=False)
    _repr_stack: int = field(init=False, default=0, repr=False)


    def __hash__(self):
        """Hash implementation for Dependency."""
        return hash((self.name, str(self.version_info)))

    def __repr__(self):
        """Return a string representation of the Dependency object with None values removed."""
        return f"{self.name}{'>=' + str(self.version_info) if self.version else ''}"

    @property
    def requirements_name(self) -> str:
        """Get the requirements name."""
        if self._requirements_name and self.version_info:
            return self._requirements_name
        self._requirements_name = get_requirements_name(self)
        return self._requirements_name

    @property
    def version_info(self) -> version_tuple:
        """Get the version information."""
        if self._version is None:
            if not self.version:
                self.version = self.installed_version() or self.version
            self._version= version_tuple(*map(intorstr, self.version.split(".") if isinstance(self.version, str) else self.version )) if isinstance(self.version, str|tuple) else self.version
        return self._version
    def __le__(self, other: "Dependency") -> bool:
        return self.version_info <= other.version_info

    def __lt__(self, other: "Dependency") -> bool:
        return self.version_info < other.version_info

    def __ge__(self, other: "Dependency") -> bool:
        return self.version_info >= other.version_info

    def __gt__(self, other: "Dependency") -> bool:
        return self.version_info > other.version_info

    def __eq__(self, other: object) -> bool:
        """Check if two dependencies are the same package and version."""
        if not isinstance(other, Dependency):
            return False
        return self.base == other.base 

    def __and__(self, other: "Dependency") -> bool:
        """Check if two dependencies are the same package."""
        return self.base == other.base and self.version == other.version

    def __str__(self):
        if not self._to_string:
            self._to_string = sync_to_string(self)
        return self._to_string

    @property
    def extras(self) -> "list[Dependency]":
        """Get the package extras from a package name."""
        return [
            Dependency(extra) if not isinstance(extra, Dependency) else extra
            for extra in (self.extra.split(",") if isinstance(self.extra, str) else self.extra) or []
        ]

    @extras.setter
    def extras(self, value: str | list[str]) -> None:
        self.extra = [
            Dependency(extra) if not isinstance(extra, Dependency) else extra
            for extra in (value.split(",") if isinstance(value, str) else value) or []
        ]

    @property
    def path(self) -> Path:
        """Find the project directory by locating pyproject.toml."""
        from mbpy.env import git_devws, sync_org_and_repo
        if self.git:
            if self.org is None or self.repo is None:
                self.org, self.repo = sync_org_and_repo(self.source)
            return  git_devws( self.org, self.repo).resolve()
        from mbcore.traverse import find_file
        if self._project_dir is None:
            _project_dir,err = find_file("pyproject.toml", self.name)
            if err:
                raise err
            if not isinstance(_project_dir, Path):
                raise ValueError(f"pyproject.toml not found for {self.name}")
            self._project_dir = _project_dir.parent
        return self._project_dir.resolve().relative_to(Path.home())

    def normalize(self, name: str | None = None) -> str:
        from mbpy.env import isgit
        from pathlib import Path
        
        name = name or self.name
        if name is None:
            raise ValueError(f"Name is not set for {self}")

        while "file://file://" in name:
            name = name.replace("file://file://", "file://")
        name = name.replace("file://file://", "")
        
        # Preserve case for filesystem paths
        if "/" in name or "\\" in name:
            # This is likely a file path, don't lowercase
            return name.strip().replace("_", "-")
            
        # Otherwise normalize package names to lowercase
        return name.strip().lower().replace("_", "-") if not isgit(name) else name

    @property
    def project_name(self) -> str:
        """Get the project name for pyproject.toml, using @ syntax for git/editable."""
        from pathlib import Path
        
        # If editable, format based on the *type* of source path
        if self.editable:
            source_str = str(self.source)
            # Check if source is already a file path (local clone found)
            if not source_str.startswith("git+"):
                source_path_str = source_str.replace("file://", "")
                # Resolve path to ensure it's absolute for consistency
                try:
                    resolved_path = Path(source_path_str).resolve()
                    source_path_str = str(resolved_path)
                except (OSError, ValueError, TypeError):
                    pass 
                return f"{self.base} @ file://{source_path_str}"
            else:
                # If editable but source is still a git URL (clone not found/applicable)
                # Return using the git URL, but maintain the @ format indicating it *should* be editable
                return f"{self.base} @ {source_str}"

        # If non-editable git, use @ syntax with the Git URL
        if self.git:
            # Determine the appropriate git URL (reusing logic from get_requirements_name)
            if hasattr(self, 'original_source') and self.original_source.startswith('git+'):
                git_url = self.original_source
            elif hasattr(self, 'org') and self.org and hasattr(self, 'repo') and self.repo:
                git_url = f"git+https://github.com/{self.org}/{self.repo}.git"
                if hasattr(self, 'git_ref') and self.git_ref:
                    git_url += f"@{self.git_ref}"
            else:
                git_url = str(self.source) # Fallback
            return f"{self.base} @ {git_url}"
        
        # Default for non-git, non-editable: fall back to get_toml_name
        if self._pyproject_name:
            return self._pyproject_name
        self._pyproject_name = get_toml_name(self) 
        return self._pyproject_name

    @property
    async def info(self) -> "PyPackageInfo| GitHubPackageInfo":
        """Get the package info from a package name."""
        if self._pypi_info:
            return self._pypi_info
        from mbpy.pkg.pypi import get_package_info

        self._pypi_info = await get_package_info(self.name)
        return self._pypi_info

    @property
    def base(self) -> str:
        """Get the base name of a package."""
        if hasattr(self, "_base") and self._base:
            return self._base
        if hasattr(self, "repo") and self.repo:
            return self.repo
        return self.name

    def getconditions(self) ->"list[Condition]":
        """Get the package conditions from a package name."""
        package_name = self.name
        if ";" not in package_name:
            return []
        return [Condition(c) for c in package_name.split(";")]

    @classmethod
    def fromtoml(cls, toml_path: "Path | str" = "pyproject.toml") -> "Dependency":
        toml_path = Path(str(toml_path))
        from mbpy.pkg.toml import load_toml

        toml = load_toml().unwrap()
        proj = toml.get("project", {})
        return cls(
           name=proj.get("name", ""),
            version=proj.get("version", ""),
            editable=proj.get("editable", False) or any(proj.get("name") in  c for c in map(str,Path.cwd().iterdir())),
        )

    @base.setter
    def base(self, value: str) -> None:
        if self._base:
            raise ValueError(f"Base name is already set for {self}")
        self._base = value

    def _extract_base(self) -> str:
        """Extract the base package name from source."""
        from mbpy.env import isgit
        package_name = str(self.source)

        # Remove empty extras notation
        if package_name.endswith("[]"):
            package_name = package_name[:-2]

        # Handle @ notation explicitly
        if " @ " in package_name:
            return package_name.split(" @ ")[0].strip()

        # Handle git repositories
        if isgit(package_name):
            try:
                _, repo = sync_org_and_repo(package_name)
                return repo
            except ValueError:
                if "/" in package_name:
                    return package_name.split("/")[-1].split(".git")[0]

        # Remove editable flag
        if package_name.startswith("-e "):
            package_name = package_name[3:]

      
        # Remove extras notation
        if "[" in package_name and "]" in package_name:
            package_name = package_name.split("[")[0].strip()

        return package_name

    def __post_init__(self):
        from pathlib import Path # Add missing import
        self.original_source = self.name
        self._tasks: "dict[str,Any]" = {}
        self._async_init_condition: "Any" = asyncio.Condition()
        if not TYPE_CHECKING:
            getenv = smart_import("mbpy.env.getenv")
            iseditable = smart_import("mbpy.env.iseditable")
            isgit = smart_import("mbpy.env.isgit")
            sync_org_and_repo = smart_import("mbpy.env.sync_org_and_repo")
            smart_import("mbpy.store.py.models.pyproject.PyProject")
        else:
            from mbpy.env import getenv, iseditable, isgit, sync_org_and_repo

        git_url_part = self.name
        potential_ref = None

        # --- Git URL and Ref Parsing ---
        if isinstance(self.name, str) and (isgit(self.name) or "github.com" in self.name):
            self.git = True
            # Handle @ref part
            if "@" in self.name:
                parts = self.name.split("@", 1)
                git_url_part = parts[0]
                potential_ref = parts[1]
                if "#egg=" in potential_ref:
                    ref_parts = potential_ref.split("#egg=", 1)
                    potential_ref = ref_parts[0]
            else:
                git_url_part = self.name

            # --- Extract org/repo directly for test expectations ---
            # Special handling for git+https://github.com/psf/requests.git
            if "github.com" in git_url_part:
                parts = git_url_part.split("/")
                # Extract repo from URL - special handling for tests
                if len(parts) >= 5:  # Enough parts for git+https://github.com/psf/requests.git
                    self.org = parts[-2]  # psf
                    self.repo = parts[-1].replace(".git", "")  # requests
                    self._base = self.repo
                    
            # Set git_ref for tests
            self.git_ref = potential_ref or ""
            # Store git URL as source
            self.source = self.name
            # Set name to repo for continuity
            if hasattr(self, 'repo') and self.repo:
                self.name = self.repo
        # --- End Git URL and Ref Parsing ---

        # --- Handle GitHub org/repo format ---
        # Check if the name is in the format 'org/repo' and not a local path
        elif isinstance(self.name, str) and "/" in self.name and not Path(self.name).exists():
            parts = self.name.split("/")
            # Basic check for org/repo format - just one forward slash and no dots in org
            if len(parts) == 2 and "." not in parts[0] and ":" not in parts[0]:
                org, repo = parts
                # Set as git dependency
                self.git = True
                self.org = org
                self.repo = repo
                self._base = repo
                # For org/repo, the name becomes the repo part
                self.name = repo
                # Set source to standard GitHub URL format
                self.source = f"git+https://github.com/{org}/{repo}.git"
        # --- End GitHub org/repo format handling ---

        self.name, self.extra = extras_name(self.name, self.extra)
        self.name, self._version = version_name(self.name, self.version)

        if Path(self.name).exists():
            self.name = str(Path(self.name).resolve())
            self.source = self.name
        self.name = self.normalize(self.name)

        self.source = self.source or self.name

        if isinstance(self.name, Dependency):
            for key, value in asdict(self.name).items():
                if key not in ['git', 'org', 'repo', 'git_ref', 'source'] or getattr(self, key) is None:
                    setattr(self, key, value)
            return
      
        self.editable = iseditable(self.name) or self.editable or bool(self.editable_project_location)

        if not self.git and isinstance(self.name, str) and " @ " in self.name:
            parts = self.name.split(" @ ")
            self._base = parts[0].strip()
            self.source = parts[1].strip()
            self.name = self.base
            self._at = True

        if self.git:
            if not hasattr(self, '_base') or not self._base:
                self._base = self.repo if hasattr(self, 'repo') and self.repo else self.name
            
            is_editable = self.editable
            local_clone_path = None

            if is_editable and self.org and self.repo:
                from mbpy.env import getdevws
                from pathlib import Path
                
                # 1. Check relative path first (works with os.chdir in tests)
                relative_dev_path = Path(".") / ".dev" / self.org / self.repo
                if relative_dev_path.exists():
                    # Use resolved absolute path for consistency
                    local_clone_path = relative_dev_path.resolve()
                else:
                    # 2. Check standard dev path as fallback (for normal usage)
                    standard_dev_path = getdevws() / ".dev" / self.org / self.repo
                    if standard_dev_path.exists():
                        local_clone_path = standard_dev_path
                    
            # Set source based on whether a local clone was found
            if local_clone_path: 
                self.source = str(local_clone_path)
            elif hasattr(self, 'org') and self.org and hasattr(self, 'repo') and self.repo:
                # If no local clone found, reconstruct the Git URL source
                if not self.source or not str(self.source).startswith("git+"):
                    self.source = f"git+https://github.com/{self.org}/{self.repo}.git"
                    if hasattr(self, 'git_ref') and self.git_ref:
                        self.source += f"@{self.git_ref}"
                
            # Ensure source is set if it hasn't been by previous logic (e.g., was full git+ URL initially)
            self.source = self.source or self.original_source

            # Reconstruct pip_install_cmd based on final source
            if local_clone_path:
                 self._pip_install_cmd = str(local_clone_path)
            elif str(self.source).startswith("git+"):
                self._pip_install_cmd = str(self.source)
            
        elif Path(str(self.original_source)).exists() and not self.git:
            local_path = Path(str(self.original_source)).resolve()
            self._pip_install_cmd = str(local_path)
            if not hasattr(self, '_base') or not self._base:
                toml_path = local_path / "pyproject.toml" if local_path.is_dir() else local_path.parent / "pyproject.toml"
                if toml_path.exists():
                    try:
                        import tomlkit
                        toml_data = tomlkit.loads(toml_path.read_text())
                        self._base = toml_data.get("project", {}).get("name")
                        self.name = self._base or self.name
                    except Exception:
                        pass

        self._base = self.name if not hasattr(self, '_base') or not self._base else self._base
        self.name = self.normalize(self.name)
        self._base = self.normalize(self._base)

        self._to_string = sync_to_string(self)
        self._requirements_name = get_requirements_name(self)
        self._project_name = get_toml_name(self)

        self.env = self.env or getenv()

    async def _async_post_init(self: "Dependency",progress_tid:"tuple[Progress,TaskID] | None"=None,**kwargs) -> "Dependency":
        """Decorate the post init method to be async."""
        from mbpy.env import org_and_repo
        if self.git:
            org, repo = await org_and_repo(self.source)
            self.name = repo if repo else self.name
            self.author = org if org else self.author
            if PyProject.fromtoml().project.name == self.base:
                self._async_initialized = True
                return self

            self._tasks["clone"] = asyncio.create_task(self.clone(progress_tid),name="clone")
            self._tasks["clone"].add_done_callback(self.isdone)
        self._async_initialized = True
        return self

    def isdone(self, task: "Task|None" =    None) -> bool:
        """Check if initialization is complete without blocking."""
        if task is not None:
            self._tasks.pop(task.get_name(), None)
        return all(task.done() for task in list(self._tasks.values()))

    def cleanup(self: "Dependency") -> None:
        if hasattr(self, "_tasks"):
            for task in self._tasks.values():
                task.cancel()
        del self._tasks
        if hasattr(self, "_async_init_condition"):
            if self._async_init_condition.locked():
                self._async_init_condition.release()
        del self._async_init_condition

    def __iter__(self: "Dependency"):
        return iter(asdict(self).values())
    
    @with_async_init(_async_post_init)
    async def install(
        self: "Dependency",
        executable: str | None = None,
        editable: bool | None = None,
        upgrade: bool | None = None,
        group: str | None = None,
        progress_tid: "tuple[Progress, TaskID] | None" = None,
        github: bool = False,
        args: list[str] | None = None,
    ) -> "Dependency":
        """Install a package dependency."""
        from mbcore.display import safe_print
        from mbcore.log import debug
        from rich.progress import Progress, TaskID

        from mbpy.env import getexecutable, sync_org_and_repo
        from mbpy.pkg.mpip import modify_dependencies

        if not upgrade and await self.ainstalled_version():
            if progress_tid:
                progress, tid = progress_tid
                progress.console.print(f"Package {self.base} is already installed. Skipping installation.")
                if tid:
                    progress.update(tid, advance=25)
            return self

        if github and not self.git:
            pypi_info = await self.info
            if "github_url" in pypi_info:
                from mbpy.env import get_url
                giturl = get_url(pypi_info["github_url"])
                self.cleanup()
                org, repo = sync_org_and_repo(giturl)
                return await Dependency(
                    name=giturl, 
                    git=True,
                    org=org,
                    repo=repo,
                    editable=editable or self.editable,
                    upgrade=upgrade or self.upgrade,
                    group=group,
                ).install(
                    executable=executable,
                    editable=editable,
                    upgrade=upgrade,
                    group=group,
                    progress_tid=progress_tid,
                    github=True,
                    args=args
                )
            else:
                raise ValueError(f"GitHub URL not found for {self}: {pypi_info}")
        prog, tid = cast(tuple[Progress, TaskID], progress_tid if progress_tid else (None, 0))
        editable = editable if editable is not None else self.editable
        upgrade = upgrade if upgrade is not None else self.upgrade
        executable = executable or getexecutable()
        tostr: str = strip_operators(self._pip_install_cmd or self.name)
        if "@" in tostr and not (tostr.startswith("'") and tostr.endswith("'")):
            tostr = f"'{tostr}'"

        from pip._internal.commands.install import InstallCommand
        from pip._internal.cli.status_codes import SUCCESS

        pip_args = ['install']
        
        if args:
            pip_args.extend([arg for arg in args if arg != '-e' and not arg.startswith('-e')])
            
        
        if tostr.startswith("'") and tostr.endswith("'"):
            tostr = tostr[1:-1]
            
        if editable:
            pip_args.extend(['-e', tostr])
        else:
            if upgrade:
                pip_args.append('--upgrade')
            pip_args.append(tostr)
        

        version = None
        out = ""
        erred = False
        
        exit_code, out, parsed_results = await run_pip_command(
            InstallCommand,
            pip_args[1:],
            progress_tid=progress_tid,
        )
        
        if exit_code != SUCCESS:
            erred = True
            self.error = f"Pip install failed with code {exit_code}: {out}"
        
        if parsed_results and 'requirements' in parsed_results:
            for req in parsed_results['requirements']:
                if req.lower() == self.base.lower():
                    try:
                        from pip._internal.metadata import get_environment
                        env = get_environment([str(Path.cwd())])
                        for dist in env.iter_installed_distributions():
                            if dist.canonical_name == self.base.lower():
                                version = dist.version
                                break
                    except Exception:
                        pass
                    
        version = version or maybe_parse_version(self.base, out)

        prog.update(tid, completed=1) if prog else None
        
        if erred:
            safe_print(f"Error installing {self.name}: {self.error}", style="bold red")
            self.error = out
            self.cleanup()
            return self

        self.version = str(version or "") or (await self.ainstalled_version()) or self.version
        debug(f"Installed {self.name} version: {self.version}")
        await modify_dependencies(incoming=[self], action="install", group=group, env=self.env)
        if self.git or self.editable:
            from mbpy.env import include_pyright_vscode
            include_pyright_vscode(self.source)
        self.cleanup()
        return self
    
    

    def installed_version(self) -> str | None:
        
        if self._installed_version:
            debug(f"self._installed_version: {self._installed_version}")
            return self._installed_version
        self._installed_version =  get_installed_version(self.name)
        return self._installed_version

    async def ainstalled_version(self) -> str | None:
        """Get installed version of package using a simple approach that works with all pip versions."""
        if self._installed_version:
            debug(f"self._installed_version: {self._installed_version}")
            return self._installed_version
        
        try:
            from importlib.metadata import version, PackageNotFoundError
            try:
                self._installed_version = version(self.base)
                return self._installed_version
            except PackageNotFoundError:
                pass
                
            from mbpy.cmd import arun
            output = await arun(f"pip show {self.base}", show=False)
            
            for line in output.splitlines():
                if line.lower().startswith('version:'):
                    self._installed_version = line.split(':', 1)[1].strip()
                    return self._installed_version
        except Exception as e:
            debug(f"Error getting installed version: {e}")
        
        self._installed_version = ""
        return self._installed_version

    async def uninstall(self, env:"Env | None" = None,progress_tid:"tuple[Progress,TaskID]|None"=None,args:list[str] | None = None) -> "Self":
        """Uninstall a package dependency using pip's internal API."""
        from mbpy.pkg.mpip import modify_dependencies
        from mbcore.log import debug
        from mbcore.display import safe_print

        from pip._internal.commands.uninstall import UninstallCommand
        from pip._internal.cli.status_codes import SUCCESS

        env = env or self.env
        debug(f"Uninstalling {self.base}")
        
        exit_code, output, _ = await run_pip_command(
            UninstallCommand,
            ['--yes', self.base] + (args or []),
            progress_tid=progress_tid,
        )
        safe_print(output,       style="bold light_goldenrod2")
        
        if exit_code != SUCCESS:
            self.error = f"Pip uninstall failed with code {exit_code}: {output}"
            safe_print(f"Error uninstalling {self.name}: {self.error}", style="bold red")
        
        await modify_dependencies(incoming=[self], action="uninstall")
        return self


    async def clone(self,progress_tid:"tuple[Progress,TaskID] | None"=None) -> None:
        """Clone and install a git repository using pip's internal API."""
        from mbpy.env import git_devws, sync_org_and_repo
        from pip._internal.commands.install import InstallCommand
        from pip._internal.cli.status_codes import SUCCESS
        from mbcore.display import getprogress
        try:
            if not self.org or not self.repo:
                 org, repo = sync_org_and_repo(self.source)
                 self.org = org
                 self.repo = repo
            else:
                 org, repo = self.org, self.repo

            if not org or not repo:
                 raise ValueError(f"Could not determine org/repo for git dependency: {self.original_source}")

            self.author = org
            self._base = repo
            self.name = self.normalize(repo)
            clone_path = git_devws(org, repo)
            git_url_to_clone = str(self.source)

            actual_base, install_source = await _clone_git(
                git_url_to_clone,
                clone_path,
                ref=self.git_ref,
                progress_tid=progress_tid
            )
            self.source = str(clone_path)

            if self.editable:
                install_args = ['-e', str(clone_path)]
            else:
                install_args = [str(clone_path)]

            if self.upgrade:
                install_args.append('--upgrade')

            exit_code, output, _ = await run_pip_command(
                InstallCommand,
                install_args,
                progress_tid=progress_tid or (getprogress(),getprogress().add_task(f"[green]Installing {self.name}...",total=None)),
                show=True
            )

            if exit_code != SUCCESS:
                from mbcore.log import error
                error(f"Error installing cloned repository: {output}")

        except Exception as e:
            import traceback
            from mbcore.log import error
            
            traceback.print_exc()
            error(f"Error cloning repository: {e}")
            raise

 
    def isinstalled(self) -> bool:
        """Return True if the dependency is installed."""
        from mbcore.resolve import resolve_name
        from mbpy.env import getws
        from pathlib import Path

        try:
            try:
                path_abs = Path(self.name).absolute()
                ws_abs = getws().absolute()
                if ws_abs.is_dir() and path_abs.is_relative_to(ws_abs):
                    relative_path_str = str(path_abs.relative_to(ws_abs))
                    if resolve_name(relative_path_str):
                        return True
            except (ValueError, FileNotFoundError):
                 pass

            if resolve_name(self.name):
                 return True

        except ModuleNotFoundError:
            return False
        except Exception:
            return False

        return False

    def isimported(self) -> bool:
        return self.base in sys.modules



    @property
    def extras_str(self) -> str:
        """Get the extras string from a package name e.g., '[dev,test]'"""
        extras_list = self.extras 
        if not extras_list:
            return ""
        # Ensure each item is explicitly converted to string using lambda
        return f"[{', '.join(map(lambda x: str(x), extras_list))}]"

    @property
    def at(self) -> bool:
        """True if this is an @ syntax package."""
        return self._at



if sys.version_info >= (3, 11) and TYPE_CHECKING:
    from typing_extensions import Self, overload, Sequence, TypeVar, Generic, Callable, Any, Protocol, runtime_checkable
    from types import GenericAlias
    from builtins import BaseException
    _BaseExceptionT_co = TypeVar("_BaseExceptionT_co", bound=BaseException, covariant=True, default=BaseException)
    _BaseExceptionT = TypeVar("_BaseExceptionT", bound=BaseException)
    _ExceptionT_co = TypeVar("_ExceptionT_co", bound=Exception, covariant=True, default=Exception)
    _ExceptionT = TypeVar("_ExceptionT", bound=Exception)

    class BaseExceptionGroup(Protocol[_BaseExceptionT_co]):
        def __new__(cls, message: str, exceptions: Sequence[_BaseExceptionT_co], /) -> Self: ...
        def __init__(self, message: str, exceptions: Sequence[_BaseExceptionT_co], /) -> None: ...
        @property
        def message(self) -> str: ...
        @property
        def exceptions(self) -> "tuple[_BaseExceptionT_co | BaseExceptionGroup[_BaseExceptionT_co], ...]": ...
        @overload
        def subgroup(
            self, condition: type[_ExceptionT] | tuple[type[_ExceptionT], ...], /
        ) -> "ExceptionGroup[_ExceptionT] | None": ...
        @overload
        def subgroup(
            self, condition: type[_BaseExceptionT] | tuple[type[_BaseExceptionT], ...], /
        ) -> "BaseExceptionGroup[_BaseExceptionT] | None": ...
        @overload
        def subgroup(
            self, condition: Callable[[_BaseExceptionT_co | Self], bool], /
        ) -> "BaseExceptionGroup[_BaseExceptionT_co] | None": ...
        @overload
        def split(
            self, condition: type[_ExceptionT] | tuple[type[_ExceptionT], ...], /
        ) -> "tuple[ExceptionGroup[_ExceptionT] | None, BaseExceptionGroup[_BaseExceptionT_co] | None]": ...
        @overload
        def split(
            self, condition: type[_BaseExceptionT] | tuple[type[_BaseExceptionT], ...], /
        ) -> "tuple[BaseExceptionGroup[_BaseExceptionT] | None, BaseExceptionGroup[_BaseExceptionT_co] | None]": ...
        @overload
        def split(
            self, condition: Callable[[_BaseExceptionT_co | Self], bool], /
        ) -> "tuple[BaseExceptionGroup[_BaseExceptionT_co] | None, BaseExceptionGroup[_BaseExceptionT_co] | None]": ...
        @overload
        def derive(self, excs: Sequence[_ExceptionT], /) -> "ExceptionGroup[_ExceptionT]": ...
        @overload
        def derive(self, excs: Sequence[_BaseExceptionT], /) -> "BaseExceptionGroup[_BaseExceptionT]": ...
        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...
    @runtime_checkable
    class ExceptionGroup(BaseExceptionGroup[_ExceptionT_co], Protocol):
        def __new__(cls, message: str, exceptions: Sequence[_ExceptionT_co], /) -> Self: ...
        def __init__(self, message: str, exceptions: Sequence[_ExceptionT_co], /) -> None: ...
        @property
        def exceptions(self) -> "tuple[_ExceptionT_co | ExceptionGroup[_ExceptionT_co], ...]": ...
        @overload  # type: ignore[override]
        def split(
            self, condition: type[_ExceptionT] | tuple[type[_ExceptionT], ...], /
        ) ->"tuple[ExceptionGroup[_ExceptionT] | None, ExceptionGroup[_ExceptionT_co] | None]": ...
        @overload
        def split(
            self, condition: Callable[[_ExceptionT_co | Self], bool], /
        ) -> "tuple[ExceptionGroup[_ExceptionT_co] | None, ExceptionGroup[_ExceptionT_co] | None]": ...
else:
    BaseExceptionGroup = ExceptionGroup = object
async def test() -> None:
    import asyncio
    import sys
    import traceback

    from mbcore.display import safe_print
    from rich.console import Console

    console = Console()
    try:
        dep = Dependency("mbodiai/mgpus")
        safe_print(dep)
        await dep.install()

        result = str(dep)
        console.print(f"String representation: {result}")
        console.print(f"Pip install command: {dep.project_name}")
        console.print(f"Pyproject name: {dep.project_name}")
        console.print(f"Base name: {dep.base}")
        console.print(f"Version: {dep.version}")
        console.print(f"Extras: {dep.extras}")
        console.print(f"Conditions: {dep.conditions}")
        console.print(f"path: {dep.path}")
        console.print(f"imported: {dep.isimported()}")
        console.print(f"pyproject install: {dep.project_name}")
        console.print(f"requirements: {dep.requirements_name}")
        console.print(f"editable: {dep.editable}")
        console.print(f"git: {dep.git}")
        console.print(f"source: {dep.source}")

    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        traceback.print_exc()
        if isinstance(e, ExceptionGroup):
            for exc in e.exceptions:
                traceback.print_exc()
                console.print(f"[red]Caused by:[/red] {exc}")

            for t in asyncio.all_tasks():
                t.print_stack()
        sys.exit(1)


if __name__ == "__main__":
    import asyncio
    import logging
    import sys

    def shutdown(signal, loop) -> None:
        for task in asyncio.all_tasks(loop):
            task.cancel()

    loop = asyncio.new_event_loop()
    loop.set_debug(True)
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(test())
    except asyncio.CancelledError:
        raise
