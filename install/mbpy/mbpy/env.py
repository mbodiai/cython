# Purpose: Environment detection and management functions.
import json
import logging
import os
import re
from site import getsitepackages
import sys
from collections.abc import Generator
from dataclasses import dataclass, field, asdict
from functools import lru_cache as lru
from pathlib import Path
from mbcore.more import collapse, unique_everseen
from typing_extensions import (
    TYPE_CHECKING,
    Dict,
    List,
    Literal,
    Tuple,
    Union,
    Protocol,
    Any,
)


from mbpy.helpers._env import uname_result, version_info
from mbpy.store.py.models.pyproject import PyProject
from itertools import chain

if TYPE_CHECKING:
    import platform

    from typing_extensions import Callable, Literal, ParamSpec, TypeVar

    from mbpy.pkg.dependency import Dependency

    T = TypeVar("T")
    P = ParamSpec("P")
    Q = ParamSpec("Q")
    R = TypeVar("R")
    ReturnT = TypeVar("ReturnT")

    def lru_cache(
        maxsize: int = 128, typed: bool = False
    ) -> Callable[[Callable[P, R]], Callable[P, R]]:
        def decorator(func: Callable[P, R]) -> Callable[P, R]:
            return func

        return decorator
else:
    lru_cache = lru
    ReturnT = T = P = Q = R = str

# Development directory name
DEV_DIR = ".dev"

# Environment Variables to check for workspace paths
ENV_VARS = [
    "CONDA_DEFAULT_ENV",
    "VIRTUAL_ENV",
    "MB_WS",
    "COLCON_PREFIX",
    "PYTHONPATH",
    "HATCH_ENV_ACTIVE",
]

# Define environment types (keep original naming for compatibility)
EnvType = Literal["system", "conda", "hatch", "venv", "mb", "colcon", "path"]

UrlPath = str | Path


@dataclass(unsafe_hash=True, frozen=False)
class Env:
    """Represents a Python environment with its configuration and paths.

    This maintains the original API while improving the internal logic.
    """

    type: EnvType = field(default="mb")
    name: str = field(default="")
    python: Path = field(default=Path(sys.executable))
    ws: Path = field(default=Path(os.getenv("MB_WS", "")))
    devws: Path = field(default=Path(os.getenv("MB_DEV_WS", "")))
    overlays: "tuple[Env,...]" = field(default_factory=tuple, repr=False, init=False)
    site_packages: list[Path] = field(
        default_factory=lambda: [
            p for d in getsitepackages() for p in Path(d).iterdir()
        ],
        init=False,
        repr=False,
    )

    def __post_init__(self):
        """Improved post-initialization logic with clearer environment detection."""
        env_vars = os.environ

        # Configure based on environment type
        if self.type == "mb":
            self.name = env_vars.get("MB_WS", "")
            # If MB_WS is set, use it for workspace path
            if "MB_WS" in env_vars:
                self.ws = Path(env_vars["MB_WS"])
        elif self.type == "conda":
            self.name = env_vars.get("CONDA_DEFAULT_ENV", "")
            conda_python = detect_conda_env_interpreter()
            if not self.name and not conda_python:
                raise ValueError(
                    "Conda environment not detected. Please activate a conda environment."
                )
            if conda_python:
                self.python = Path(conda_python)
        elif self.type == "system":
            self.python = Path(sys.base_exec_prefix)
        elif self.type == "hatch":
            self.name = env_vars.get("HATCH_ENV_ACTIVE", "unknown")
            self.python = Path(sys.prefix)
        elif self.type == "venv":
            self.name = env_vars.get("VIRTUAL_ENV", "")
            self.python = Path(sys.executable)
        elif self.type == "colcon":
            self.name = env_vars.get("COLCON_PREFIX", "")
            self.python = Path(sys.executable)
        elif self.type == "path":
            self.name = env_vars.get("PYTHONPATH", "")
            self.python = Path(sys.executable)
        else:
            raise ValueError(f"Invalid environment type: {self.type}")

        if not self.ws:
            self.ws = getws()
        # Ensure name is set - use workspace stem if available
        if not self.name and self.ws and self.ws.exists():
            self.name = self.ws.stem

        # If devws is not explicitly set, derive it from ws
        if not self.devws and self.ws:
            self.devws = self.ws / DEV_DIR

    def __str__(self) -> str:
        """Return the environment name."""
        return self.ws.parent.name

    def __truediv__(self, other):
        """Path division support for workspace operations."""
        return self.ws / other

    def __rtruediv__(self, other):
        return other / self.ws

    @classmethod
    def fromenv(cls) -> "Env":
        """Detect the active environment and return an Env object."""
        # Get all relevant environment variables that are set
        env_vars = {key: os.getenv(key, "") for key in ENV_VARS if os.getenv(key)}

        # Sort by priority, putting CONDA_DEFAULT_ENV first if present
        env_keys = sorted(
            env_vars.items(),
            key=lambda x: x[0].startswith("CONDA_DEFAULT_ENV"),
            reverse=True,
        )

        if not env_keys:
            return cls(type="system")

        # Extract the primary and overlay environments
        primary_env_var, primary_env_value = env_keys[0]

        # Determine environment type based on environment variable
        if primary_env_var == "CONDA_DEFAULT_ENV":
            env_type = "conda"
        elif primary_env_var == "VIRTUAL_ENV":
            env_type = "venv"
        elif primary_env_var == "MB_WS":
            env_type = "mb"
        elif primary_env_var == "COLCON_PREFIX":
            env_type = "colcon"
        elif primary_env_var == "PYTHONPATH":
            env_type = "path"
        elif primary_env_var == "HATCH_ENV_ACTIVE":
            env_type = "hatch"
        else:
            env_type = "system"

        # Create the primary environment
        env = cls(type=env_type, name=primary_env_value)

        # Add overlays if there are multiple environments
        if len(env_keys) > 1:
            # Create overlay environments from remaining environment variables
            env.overlays = tuple(
                [
                    cls(
                        type="conda"
                        if key == "CONDA_DEFAULT_ENV"
                        else "venv"
                        if key == "VIRTUAL_ENV"
                        else "mb"
                        if key == "MB_WS"
                        else "system",
                        name=value,
                    )
                    for key, value in env_keys[1:]
                ]
            )

        return env


@dataclass
class SystemSettings:
    ccompiler: str
    cxxcompiler: str
    cppflags: str
    ld_flags: str
    ldc_flags: str
    ldcxx_flags: str
    arch: str
    build_parallel: int | None
    uname: Union[str, None, "uname_result | platform.uname_result"]
    machine: str
    abi_flag: str
    sizes: Dict[str, int] | None = field(default_factory=dict)

    @classmethod
    def detect(cls) -> "SystemSettings":
        """Detect system settings from the current environment."""
        import os
        import shutil
        from sysconfig import get_config_vars

        try:
            from mbpy.helpers._env import uname
        except ImportError:
            # Fallback if the imports aren't available
            import platform

            uname = platform.uname

        config_vars = get_config_vars()
        sizes = {k: int(v) for k, v in config_vars.items() if k.startswith("SIZEOF_")}

        return cls(
            ccompiler=shutil.which(config_vars.get("CC", ""))
            or config_vars.get("CC", ""),
            cxxcompiler=shutil.which(config_vars.get("CXX", "")),
            cppflags=config_vars.get("CPPFLAGS", ""),
            ld_flags=config_vars.get("LDFLAGS", ""),
            ldc_flags=config_vars.get("LDCFLAGS", ""),
            ldcxx_flags=config_vars.get("LDCXXSHARED", ""),
            arch=config_vars.get("MULTIARCH", ""),
            build_parallel=os.cpu_count(),
            uname=uname(),
            machine=uname().machine,
            sizes=sizes,
            abi_flag=sys.abiflags,
        )


@dataclass
class Condition:
    """Class for parsing and evaluating dependency conditions."""

    min_version: str | None = None
    max_version: str | None = None
    if_values: List[str] = field(default_factory=list)
    platforms: List[str] = field(default_factory=list)
    env_vars: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def parse(cls, condition_str: str) -> "Condition":
        """Parse a condition string into a Condition object."""
        if_values: List[str] = []
        platforms: List[str] = []
        env_vars: Dict[str, str] = {}
        min_version: str | None = None
        max_version: str | None = None
        versionstr = condition_str

        parts = [p.strip() for p in versionstr.split(";") if p.strip()]
        for part in parts:
            if part.startswith("if "):
                if_values = [v.strip() for v in part[3:].split(",")]
            elif part.startswith("platform "):
                platforms = [p.strip() for p in part[9:].split(",")]
            elif "=" in part:
                key, value = part.split("=", 1)
                env_vars[key.strip()] = value.strip()

        return cls(
            min_version=min_version,
            max_version=max_version,
            if_values=if_values,
            platforms=platforms,
            env_vars=env_vars,
        )

    def evaluate(self, platform: str, env: Dict[str, str], value: str) -> bool:
        """Evaluate if conditions are met."""
        if self.if_values and value not in self.if_values:
            return False

        if self.platforms and platform not in self.platforms:
            return False

        return all(
            env.get(env_key) == env_val for env_key, env_val in self.env_vars.items()
        )


#########################################
# PART 3: ENVIRONMENT DETECTION FUNCTIONS
#########################################


def detect_conda_env_interpreter() -> str | None:
    """Detect the Python interpreter for an active conda environment.

    Returns:
        Path to conda Python interpreter or None if not found

    """
    # Check if conda environment is active
    conda_prefix = os.environ.get("CONDA_PREFIX")
    if not conda_prefix:
        return None

    python_path = (
        Path(conda_prefix) / "python.exe"
        if os.name == "nt"
        else Path(conda_prefix) / "bin" / "python"
    )

    return str(python_path) if python_path.exists() else None


@lru_cache(maxsize=128)
def all_venvs(cwd: Path) -> List[Env]:
    """Get all virtual environments in the current directory.

    Args:
        cwd: Current working directory

    Returns:
        List of Env objects for virtual environments

    """
    venvs = []
    for p in cwd.iterdir():
        if p.is_dir():
            bin_dir = "Scripts" if os.name == "nt" else "bin"
            python_exe = "python.exe" if os.name == "nt" else "python"
            python_path = p / bin_dir / python_exe

            if python_path.exists():
                venvs.append(Env(type="venv", name=p.name, ws=p, python=python_path))
    return venvs


def active_venv() -> Env | None:
    """Get the active virtual environment.

    Returns:
        Env object for the active virtual environment or None

    """
    venv_path = os.environ.get("VIRTUAL_ENV")
    if not venv_path:
        return None

    bin_dir = "Scripts" if os.name == "nt" else "bin"
    python_exe = "python.exe" if os.name == "nt" else "python"

    venv_dir = Path(venv_path)
    python_path = venv_dir / bin_dir / python_exe

    if not python_path.exists():
        return None

    return Env(type="venv", name=venv_dir.name, ws=venv_dir, python=python_path)


@lru_cache(maxsize=128)
def detect_active_interpreter(cwd: Path | None = None) -> List[Path]:
    """Detect active Python interpreters for various environments.

    Args:
        cwd: Current working directory

    Returns:
        List of interpreter paths

    """
    cwd = cwd or Path.cwd()

    # Use a list to collect detection functions and their results
    detection_results = []

    # Check for active virtual environment
    active_env = active_venv()
    if active_env:
        detection_results.append(active_env.python)

    # Check for all virtual environments in the directory
    for env in all_venvs(cwd):
        detection_results.append(env.python)

    # Check for conda environment
    conda_interpreter = detect_conda_env_interpreter()
    if conda_interpreter:
        detection_results.append(Path(conda_interpreter))

    # Flatten the list and remove duplicates while preserving order
    return list(unique_everseen(collapse(filter(None, detection_results))))


@lru_cache(maxsize=128)
def detect_active_env(cwd: Path | None = None) -> List[Env]:
    """Detect active environments.

    Args:
        cwd: Current working directory

    Returns:
        List of Env objects

    """
    cwd = cwd or Path.cwd()

    # Use a list to collect detection functions and their results
    detection_results = []

    # Check for active virtual environment
    active_env = active_venv()
    if active_env:
        detection_results.append(active_env)

    # Check for all virtual environments in the directory
    detection_results.extend(all_venvs(cwd))

    # Check for conda environment
    conda_interpreter = detect_conda_env_interpreter()
    if conda_interpreter:
        conda_name = os.environ.get("CONDA_DEFAULT_ENV", "conda-env")
        detection_results.append(
            Env(type="conda", name=conda_name, python=Path(conda_interpreter)),
        )

    # Flatten the list and remove duplicates based on python path
    return list(unique_everseen(detection_results, key=lambda env: str(env.python)))


#########################################
# WORKSPACE MANAGEMENT
#########################################


# Cache dictionaries with simplified implementation
class Hashable(Protocol):
    def __hash__(self) -> int: ...


_ws_cache: Dict[Hashable | Path | str | tuple[Hashable | Path | str, ...], Path] = {}
_exec_cache: Dict[str, str] = {}


# @lru_cache(maxsize=128)
def getenv(env_str: str | Env | None = None) -> Env:
    """Retrieve the correct environment based on the input string or default settings.

    Args:
        env_str: Environment string or Env object

    Returns:
        Env object

    """
    if isinstance(env_str, Env):
        return env_str
    if env_str in (None, "default"):
        return Env.fromenv()
    return Env(type="mb", name=env_str)


def getexecutable(
    env: str | Env | None = None,
    multiple: Literal["auto", "ask", "fail"] = "ask",
) -> str:
    """Determine the appropriate Python interpreter for the environment.

    Args:
        env: Environment string or object
        multiple: How to handle multiple interpreters

    Returns:
        Path to Python interpreter

    """
    env_obj = getenv(env)
    return _getexecutable(env_obj, multiple)


def getexecpath(
    env: str | Env | None = None,
    multiple: Literal["auto", "ask", "fail"] = "ask",
) -> Path:
    """Get the Python interpreter path for an environment.

    Args:
        env: Environment string or object
        multiple: How to handle multiple interpreters

    Returns:
        Path object for the Python interpreter

    """
    return Path(getexecutable(env, multiple))


def _getexecutable(
    env: Env,
    multiple: Literal["auto", "ask", "fail"] = "ask",
) -> str:
    """Determine the appropriate Python interpreter.

    Args:
        env: Environment object
        multiple: How to handle multiple interpreters

    Returns:
        Path to Python interpreter

    """
    from mbpy.pkg.toml import resolve_conflicting

    # Return cached result if available
    if _exec_cache:
        return next(iter(_exec_cache.values()))

    env = getenv(env)
    cwd = Path.cwd()

    # For auto or fail mode, just take the first interpreter
    if multiple in ["auto", "fail"]:
        interpreters = detect_active_interpreter(cwd=cwd)
        if not interpreters:
            raise ValueError("No Python interpreters detected")

        _exec_cache[str(env)] = str(interpreters[0])
        return _exec_cache[str(env)]

    # Get all environments
    envs = detect_active_env(cwd=cwd)

    # Resolve the directory containing pyproject.toml
    cwd = resolve_conflicting("pyproject.toml", cwd)

    # If only one environment is found, use it
    if envs and len(envs) == 1:
        bin_dir = "Scripts" if os.name == "nt" else "bin"
        python_exe = "python.exe" if os.name == "nt" else "python"
        python_path = envs[0].ws / bin_dir / python_exe

        _exec_cache[str(env)] = str(python_path)
        return _exec_cache[str(env)]

    # If multiple environments, ask user to select one
    if len(envs) > 1 and multiple == "ask":
        from mbcore.display import prompt_ask

        options = [f"{env} ({env.ws.parent.stem})" for env in envs]
        res = prompt_ask(
            "Multiple Python interpreters detected. Select one:",
            options,
            default=1,
            enumerate=True,
        )

        selected_env = envs[int(res) - 1]
        bin_dir = "Scripts" if os.name == "nt" else "bin"
        python_exe = "python.exe" if os.name == "nt" else "python"
        python_path = selected_env.ws / bin_dir / python_exe

        if not python_path.exists():
            remaining_envs = [env for env in envs if env != selected_env]
            if not remaining_envs:
                raise ValueError("No valid interpreters available")

            res = prompt_ask(
                "Selected interpreter does not exist. Please select another one:",
                [f"{env} ({env.ws.parent.stem})" for env in remaining_envs],
                default=1,
                enumerate=True,
            )

            selected_env = remaining_envs[int(res) - 1]
            python_path = selected_env.ws / bin_dir / python_exe

        _exec_cache[str(env)] = str(python_path)
        return _exec_cache[str(env)]

    raise ValueError(
        f"Invalid value for 'multiple': {multiple}. Must be 'auto', 'ask', or 'fail'."
    )


@lru_cache(maxsize=128)
def version_name(
    name: str, version: str | tuple[int | str] | version_info | None = None
) -> tuple[str, str]:
    """Extract the package name and version from a string."""
    n = (
        name.strip()
        .split("==")[0]
        .split(">=")[0]
        .split("<=")[0]
        .split(">")[0]
        .split("<")[0]
        .split("~=")[0]
        .split("!=")[0]
    )
    if n != name and (not version or version == "0.0.0"):
        version = name[len(n) :].strip()
    return n, str(version) if version and str(version) != "0.0.0" else ""



def getws(source: Path | None = None, env: "Env |None" = None) -> Path:
    """Get the workspace root directory.

    Args:
        source: Starting directory

    Returns:
        Workspace root path

    """
    from mbpy.pkg.toml import find_toml
    from mbpy.env import getenv
    from mbcore.even._internal._trees import make_key

    key = make_key(source, asdict(env or getenv()))
    if key in _ws_cache:
        return _ws_cache[key]

    # 1. Check python path. If it's a virtual environment, use the prefix's grandparent
    # 2. Check the environment variable MB_WS
    # 3. Check for pyproject.toml in the current directory
    # 4. Check for pyproject.toml in the parent directory
    # 5. Check for pyproject.toml in a child's directory
    # 6. Check for pyproject.toml in the grandparent directory
    if env:
        _ws_cache[key] = env.ws
    if source:
        source = Path(source)
        if (
            source.exists()
            and source.parent.name != ".dev"
            and source.parent.parent.name != ".dev"
        ):
            _ws_cache[key] = find_toml("pyproject.toml", source).parent
    elif "MB_WS" in os.environ:
        _ws_cache[key] = Path(os.environ["MB_WS"])
    else:
        _ws_cache[key] = find_toml("pyproject.toml", Path.cwd()).parent
    return _ws_cache[key]


@lru_cache(maxsize=128)
def getdevws(root: Path | None = None, relative: bool = False) -> Path:
    """Get the development workspace directory.

    Args:
        root: Starting directory

    Returns:
        Development workspace path

    """
    # Get the workspace root
    ws_root = getws(root)
    p = (ws_root / DEV_DIR).resolve()
    p.mkdir(parents=True, exist_ok=True)
    if relative:
        return p.absolute().relative_to(ws_root.absolute())
    return p


#########################################
# PART 5: REPOSITORY UTILITIES (PRESERVED API)
#########################################
@lru_cache(maxsize=128)
def isgit(source: Path | str) -> bool:
    """Check if a source is a git repository.

    Args:
        source: Source string, dependency object, or path

    Returns:
        True if source is a git repository

    """
    # Store original path string to preserve case
    original_source = str(source)
    underscored_source = str(source).replace("-", "_")

    def exists_in_devws(source: str) -> bool:
        if Path(source).resolve().exists() and not any(
            getdevws() == p for p in Path(source).resolve().parents
        ):
            return False
        if (getdevws() / Path(source).resolve().parent.name).exists():
            if (
                list((getdevws() / Path(source).resolve().parent.name).iterdir())
                or (getdevws() / Path(source).resolve().parent.name / ".git").exists()
            ):
                return True
        if (getdevws() / Path(source).resolve().name).exists():
            return (
                len(list((getdevws() / Path(source).resolve().name).iterdir())) > 0
                or (getdevws() / Path(source).resolve().name / ".git").exists()
            )
        return True

    if exists_in_devws(original_source) or exists_in_devws(underscored_source):
        return False
    src_str = (
        original_source  # Use original string instead of potentially lowercased version
    )
    return (
        src_str.startswith(("git+", "hg+", "svn+", "bzr+"))
        or (src_str.startswith("http") and "github.com" in src_str)
        or (str(getdevws()) in src_str and Path(src_str).exists())
        or ("/" in src_str and not Path(src_str[:100]).exists())
        and not src_str.startswith("file://")
        and "@" not in src_str
    )


def iseditable(source: Union[str, "Dependency"]) -> bool:
    """Check if a source is an editable install.

    Args:
        source: Source string or dependency object

    Returns:
        True if source is editable

    """
    src = source.original_source if hasattr(source, "original_source") else source  # type: ignore
    return src.startswith("-e") or "/" in src or "-e" in src  # type: ignore


def exists(source: str) -> bool:
    """Check if a source exists as a file or directory.

    Args:
        source: Source string

    Returns:
        True if source exists

    """
    try:
        return Path(source[:250]).exists()
    except (ValueError, TypeError, OSError):
        return False


def isatformat(source: Union[str, "Dependency"]) -> bool:
    """Check if string is in package @ location format.

    Args:
        source: Source string or dependency object

    Returns:
        True if source is in @ format

    """
    if hasattr(source, "name"):
        source = source.name  # type: ignore

    try:
        return bool(re.match(r"^[a-zA-Z0-9_\-]+ @ [a-zA-Z0-9_\-:/\.]+$", source))  # type: ignore
    except (TypeError, AttributeError):
        return False


def get_url(source: str) -> str:
    """Get the URL from a source string.

    Args:
        source: Source string

    Returns:
        URL from source

    """
    if "/" not in str(source):
        raise ValueError(f"Invalid source: {source}")
    if source.split("github.com")[1].count("/") > 1:
        source, rest = source.split("github.com")
        parts = rest.split("/")
        org, repo = parts[1], parts[2]

        source = f"{source}github.com/{org}/{repo}"
    if "#" in source and "@" not in source and "egg=" not in source:
        source = source.split("#")[0]
    if source.startswith("git+"):
        source = source.split("git+")[1]

    if ".git" in source and "@" not in source and "egg=" not in source:
        source = source.split(".git")[0]
    if "@" in source:
        source = "".join(source.split("@")[1:]).strip()

    return source


def get_vcs(source: str) -> str:
    """Get the version control system type from a source string.

    Args:
        source: Source string

    Returns:
        VCS prefix and URL

    """
    if source.startswith("git+"):
        return "git+" + source.split("git+")[1].split("@")[0]
    if source.startswith("http") and "github.com" in source:
        return (
            "git+https://github.com"
            + source.split("https://github.com")[1].split("@")[0]
        )
    raise ValueError(f"VCS type not supported in source: {source}")


_cache = {}


@lru_cache(maxsize=128)
def _org_and_repo(
    source: str | Path,
) -> Generator[Path | str | None, PyProject | None, tuple[str, str]]:
    """Async function to get (org, repo) from a source string or path.

    1) If it contains 'github.com', parse directly.
    2) If local path or dev workspace path has pyproject info, extract from that.
    3) If 'org/repo' string, parse that.
    4) Otherwise raise ValueError.
    """
    key = str(Path(str(source).strip()).resolve())
    if key in _cache:
        return _cache[key]
    from mbcore.log import verbose
    from mbcore.more import first_true

    source_str = str(source).strip()
    verbose(f"source_str: {source_str}")
    # Strip editable prefix
    if source_str.startswith("-e "):
        source_str = source_str[3:].strip()

    # Case 1: GitHub direct
    lower = source_str.lower()
    if "github.com" in lower:
        parts = source_str.split("github.com/", 1)[-1].split("/")
        verbose(f"parts: {parts},len: {len(parts)}")
        if len(parts) >= 2:
            org_ = parts[0]
            repo_ = parts[1].split(".git")[0] if ".git" in parts[1] else parts[1]
            repo_ = repo_.split("#")[0]  # strip #branch if any
            _cache[key] = org_, repo_
            return org_, repo_

    # Case 2: local path or dev workspace
    p = Path(source_str)
    if p.exists():
        # First try to get from TOML

        project = yield p
        if project and project.repository:
            project = project.repository
            return project.org, project.repo
        # If that fails, try to extract from path
        if len(p.parts) >= 2:
            # Try to extract org/repo from path structure
            verbose(f"parts: {p.parts}")
            parts = p.parts[-2:]
            if len(parts) == 2 and "/" not in parts[0] and "/" not in parts[1]:
                _cache[key] = parts[0], parts[1]

                return parts[0], parts[1]

    try:
        candidate = first_true(
            lambda x: Path(source_str).stem in str(x.resolve()),
            chain(*(c.iterdir() for c in getdevws().iterdir()), getws().iterdir()),
        )
    except Exception as e:
        verbose(f"error: {e}")
        candidate = None
    if candidate and candidate.exists():
        # First try TOML
        project = yield candidate.parent
        project = project.repository
        if project and project.org and project.repo:
            return project.org, project.repo

        # If that fails, try path extraction
        return candidate.parent, candidate.stem

    # Case 3: 'org/repo' fallback
    if "/" in source_str and not p.exists():
        parts = (
            str(p.resolve()).rsplit("/", maxsplit=1)
            if "/" in str(p.resolve())
            else (str(p.resolve()), "")
        )
        verbose(f"case3 parts: {parts}")
        if len(parts) >= 2:
            *org_, repo_ = parts
            verbose(f"case3 org: {org_}, repo: {repo_}, parts: {parts}")
            org_ = "/".join(org_)
            org_ = Path(org_).stem

            repo_ = repo_.split(".git")[0] if ".git" in parts[1] else parts[1]
            repo_ = repo_.split("#")[0]
            verbose(f"case3 org: {org_}, repo: {repo_}")
            _cache[key] = org_, repo_
            return org_, repo_

    return None, None


def consume(gen: Generator[Any | None, Any | None, ReturnT]) -> ReturnT:
    while True:
        try:
            next(gen)
        except StopIteration as e:
            return e.value


# Just use the fixed aserve client and serve client functions


async def org_and_repo(source: Union[str, Path]) -> Tuple[str, str]:
    if not isgit(source):
        return "", ""
    gen = _org_and_repo(source)
    if isinstance(gen, tuple):
        return gen
    from mbpy.serve import serve

    try:
        return consume((serve(gen, PyProject.fromtoml)))
    except StopIteration as e:
        return e.value


@lru_cache(maxsize=128)
def sync_org_and_repo(source: Union[str, Path]) -> Tuple[str, str]:
    if not isgit(source):
        try:
            org, repo = _org_and_repo(source)
            if org and repo:
                return org, repo
        except Exception as e:
            from mbcore.log import error

            error(f"Failed to get org and repo for {source}: {e}")
            return None, None

    gen = _org_and_repo(source)
    if isinstance(gen, tuple):
        return gen
    from mbpy.serve import serve

    return serve(gen, PyProject.fromtoml)


@lru_cache(maxsize=128)
def git_devws(org: str, repo: str) -> Path:
    """Get the development workspace path for a git repository.

    Args:
        project_root: Project root directory
        org: Organization name
        repo: Repository name

    Returns:
        Path to development workspace for the repository

    """
    if repo is None:
        raise ValueError(f"Repository name is required for {org}")
    out = getdevws()
    out = out / f"{org}/{repo}"
    if not out.exists() and (getws() / repo).exists():
        out = getws() / repo
    return out


#########################################
# PART 6: IDE INTEGRATION (PRESERVED API)
#########################################


def include_pyright_vscode(source: str | Path) -> None:
    """Include the Pyright settings in VSCode settings and pyproject.toml.

    Args:
        source: Source path to include

    """
    from mbcore.more import unique_everseen

    source = Path(str(source))
    # Determine paths to include based on source type
    if isgit(source) and str(getdevws()) not in str(source):
        source = getdevws() / source

    if (source / "src").exists():
        ps = [source / "src"]
    elif (source / "pyproject.toml").exists():
        ps = [source]
    elif (source / source.stem).exists() and (
        source / source.stem / "pyproject.toml"
    ).exists():
        ps = [source / source.stem]
    else:
        ps = [source]

    # Update pyproject.toml if it exists
    pyproject_path = Path(getws() / "pyproject.toml")
    if pyproject_path.exists():
        from mbpy.pkg.toml import load_toml

        try:
            # Load current pyproject.toml
            pyproj = load_toml(pyproject_path)
            if not pyproj:
                logging.getLogger("default").debug(
                    "Failed to load pyproject.toml. Skipping Pyright settings."
                )
                return
            # Get current extraPaths or initialize empty list
            extra_paths = (
                pyproj.get("tool", {}).get("pyright", {}).get("extraPaths", [])
            )
            extra_paths = [
                Path(p).absolute().relative_to(getws().absolute())
                for p in extra_paths
                if Path(p).exists()
                and Path(p).absolute().is_relative_to(getws().absolute())
            ]
            logging.getLogger("default").debug(f"extra_paths: {extra_paths}")

            pyproj.setdefault("tool", {}).setdefault("pyright", {})["extraPaths"] = (
                list(unique_everseen(map(str, extra_paths + ps)))
            )

            with open(pyproject_path, "w") as f:
                f.write(pyproj.as_string())
        except Exception as e:
            import traceback

            traceback.print_exc()
            logging.getLogger("default").debug(f"Failed to update pyproject.toml: {e}")

    # Update VSCode settings.json if it exists
    vscode_settings = Path(getws() / ".vscode/settings.json")
    if vscode_settings.exists():
        try:
            # Load current settings
            with Path(vscode_settings).open("r") as f:
                settings = json.load(f)

            # Get current extraPaths or initialize empty list
            extra_paths = (
                settings.get("python", {}).get("analysis", {}).get("extraPaths", [])
            )

            # Skip if source doesn't exist and isn't a git repo
            if not Path(source).exists() and not isgit(source):
                logging.getLogger("default").debug(
                    f"Path {source} does not exist. Skipping Pyright settings."
                )
                return

            # Update settings with new paths
            if "python" not in settings:
                settings["python"] = {}
            if "analysis" not in settings["python"]:
                settings["python"]["analysis"] = {}

            # Combine paths, removing duplicates while preserving order
            settings["python"]["analysis"]["extraPaths"] = list(
                unique_everseen(extra_paths + ps)
            )

            # Write updated settings
            with open(vscode_settings, "w") as f:
                json.dump(settings, f, indent=4)
        except (OSError, json.JSONDecodeError):
            logging.getLogger("default").debug(
                f"Failed to update VSCode settings: {vscode_settings}"
            )


def get_simple_org_repo(source: Union[str, Path] = None) -> Tuple[str, str]:
    """Get organization and repository name directly from git remote URL.

    A simpler alternative to sync_org_and_repo that just gets the info from git.
    """
    from mbpy.cmd import run
    import re

    try:
        # If source is provided and exists as a path, use that directory
        cwd = None
        if source and Path(str(source)).exists() and Path(str(source)).is_dir():
            cwd = str(Path(str(source)))

        # Get the remote URL directly from git
        cmd = "git remote get-url origin"
        if cwd:
            cmd = f"cd {cwd} && {cmd}"

        remote_url = run(cmd).strip()

        # Parse GitHub URL formats
        if "github.com" in remote_url:
            # Handle HTTPS format
            if remote_url.startswith(("http://", "https://")):
                path = remote_url.split("github.com/")[-1]
                org, repo = path.split("/", 1)
                repo = repo.replace(".git", "")
                return org, repo
            # Handle SSH format
            elif remote_url.startswith("git@"):
                match = re.match(
                    r"git@github\.com:([^/]+)/([^.]+)(?:\.git)?", remote_url
                )
                if match:
                    return match.groups()

        # Fallback to existing method if URL parsing fails
        return sync_org_and_repo(source or Path.cwd())

    except Exception as e:
        from mbcore.log import verbose

        verbose(f"Failed to get org and repo from git: {e}")
        # Fallback to existing method
        return sync_org_and_repo(source or Path.cwd())


if __name__ == "__main__":
    from mbcore.log import info

    info(getdevws(relative=True))
