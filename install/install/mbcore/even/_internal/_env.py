# Purpose: Environment detection and management functions.
import os
import sys
from dataclasses import dataclass, field
from functools import lru_cache as lru
from pathlib import Path
from site import getsitepackages

from typing_extensions import TYPE_CHECKING, Dict, List, Literal

from mbcore.more import collapse, unique_everseen

if TYPE_CHECKING:

    from typing_extensions import Callable, Literal, ParamSpec, TypeVar

    T = TypeVar("T")
    P = ParamSpec("P")
    Q = ParamSpec("Q")
    R = TypeVar("R")

    def lru_cache(maxsize: int = 128, typed: bool = False) -> Callable[[Callable[P, R]], Callable[P, R]]:
        def decorator(func: Callable[P, R]) -> Callable[P, R]:
            return func

        return decorator
else:
    lru_cache = lru

# Development directory name
DEV_DIR = ".dev"

# Environment Variables to check for workspace paths
ENV_VARS = ["CONDA_DEFAULT_ENV", "VIRTUAL_ENV", "MB_WS", "COLCON_PREFIX", "PYTHONPATH", "HATCH_ENV_ACTIVE"]

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
        default_factory=lambda: [p for d in getsitepackages() for p in Path(d).iterdir()], init=False, repr=False,
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
                raise ValueError("Conda environment not detected. Please activate a conda environment.")
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
            self.ws = Path.cwd()
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
                ],
            )

        return env


def detect_conda_env_interpreter() -> str | None:
    """Detect the Python interpreter for an active conda environment.

    Returns:
        Path to conda Python interpreter or None if not found

    """
    # Check if conda environment is active
    conda_prefix = os.environ.get("CONDA_PREFIX")
    if not conda_prefix:
        return None

    python_path = Path(conda_prefix) / "python.exe" if os.name == "nt" else Path(conda_prefix) / "bin" / "python"

    return str(python_path) if python_path.exists() else None


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
_ws_cache: Dict[str, Path] = {}
_exec_cache: Dict[str, str] = {}


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

    raise ValueError(f"Invalid value for 'multiple': {multiple}. Must be 'auto', 'ask', or 'fail'.")
