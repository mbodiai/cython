import logging
import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING


from mbcore.ctx import chdir
from mbcore.display import prompt_ask
from mbcore.cache import cache, acache
from mbcore.traverse import with_err, has_error
from tomlkit import TOMLDocument

if TYPE_CHECKING:
    from pathlib import Path

    from mbpy.env import Env
    from mbpy.pkg.dependency import Dependency


@cache(context_policy="mtime", persistent=True)
def search_parents_for_file(
    file_name: Path | str,
    max_levels=3,
    cwd: "Path | str | None | None" = None,
) -> "Path":
    """Search parent directories for a file."""
    file_name = Path(str(file_name))

    if file_name.exists() and file_name.is_relative_to(Path(str(cwd))):
        return Path(str(file_name))
    logging.getLogger("rich").debug(f"exists ? {Path(file_name).exists()}")
    file_name = file_name.name if file_name.is_absolute() else file_name
    logging.getLogger("rich").debug(
        f"Searching for {file_name} in parent directories of {cwd}"
    )
    seen = set()
    current_dir = Path(cwd) if cwd else Path.cwd()
    it = 0
    target_file = current_dir / file_name
    while it <= max_levels and not target_file.exists():
        seen.add(current_dir)
        logging.getLogger("rich").debug(f"Checking {target_file}")
        current_dir = current_dir.parent
        target_file = current_dir / file_name
        it += 1

    if target_file.exists():
        return target_file
    raise FileNotFoundError(
        f"File '{file_name}' not found in parent directories: {seen}."
    )


async def asearch_parents_for_file(
    file_name: Path | str,
    max_levels=3,
    cwd: "Path| str | None" = None,
) -> "Path":
    """Search parent directories for a file."""
    file_name = Path(str(file_name))
    if Path(str(file_name)).exists():
        return Path(str(file_name))
    file_name = Path(str(file_name))
    file_name = file_name.name if file_name.is_absolute() else file_name
    logging.getLogger("rich").debug(
        f"Searching for {file_name} in parent directories of {cwd}"
    )
    current_dir = Path(cwd) if cwd else Path.cwd()
    it = 0
    target_file = current_dir / file_name
    while it <= max_levels and not target_file.exists():
        logging.getLogger("rich").debug(f"Checking {target_file}")
        current_dir = current_dir.parent
        target_file = current_dir / file_name
        it += 1
        if target_file.exists():
            return target_file
    raise FileNotFoundError(f"File '{file_name}' not found in parent directories.")


async def asearch_children_for_file(
    file_name: "Path",
    max_levels=3,
    cwd: "Path | str| None" = None,
) -> "Path":
    """Search parent directories for a file."""
    if Path(str(file_name)).exists() and Path(str(file_name)).is_relative_to(
        Path(str(cwd))
    ):
        return Path(str(file_name))
    file_name = Path(str(file_name))
    fn = file_name.name if file_name.is_absolute() else file_name

    logging.getLogger("rich").debug(
        f"Searching for {file_name} in child directories of {cwd}"
    )
    current_dir = Path(str(cwd)) if cwd else Path.cwd()
    it = 0
    visited = set()
    target_file = current_dir / fn
    q = [current_dir]
    while it <= max_levels and not target_file.exists() and q:
        current_dir = q.pop(0)
        visited.add(current_dir)
        logging.getLogger("rich").debug(f"Checking {current_dir}")
        for child in current_dir.iterdir():
            if child not in visited:
                if child.is_dir():
                    q.append(child)
                elif child.name == getattr(fn, "name", fn):
                    target_file = child
                    break
        it += 1
    if target_file.exists():
        return target_file
    raise FileNotFoundError(f"File '{file_name}' not found in child directories.")


def search_children_for_file(
    file_name: "Path | str",
    max_levels=2,
    cwd: "Path | str | None" = None,
) -> "Path":
    """Search directories for a file with optimized performance."""
    import os

    # Convert to strings for faster operations
    str_filename = str(file_name)
    base_filename = os.path.basename(str_filename)
    wd = os.path.abspath(str(cwd) if cwd else os.getcwd())

    # Direct check for exact file path first
    if os.path.exists(str_filename) and os.path.isfile(str_filename):
        return Path(str_filename)

    # Prepare a fast check function using strings
    def is_target_file(path):
        return os.path.basename(path) == base_filename and os.path.isfile(path)

    # Use a queue for BFS traversal (more efficient than recursion)
    from collections import deque

    queue = deque([(wd, 0)])  # (path, depth)
    visited = set()

    while queue:
        current_dir, level = queue.popleft()

        # Skip if already visited or exceeding max depth
        if current_dir in visited or level > max_levels:
            continue

        visited.add(current_dir)

        # Check if target file exists directly in current directory
        target_path = os.path.join(current_dir, base_filename)
        if os.path.exists(target_path) and os.path.isfile(target_path):
            return Path(target_path)

        # Only continue traversal if within depth limit
        if level < max_levels:
            try:
                # Use scandir which is more efficient than iterdir
                with os.scandir(current_dir) as entries:
                    for entry in entries:
                        # Only process directories for traversal
                        if entry.is_dir():
                            child_path = entry.path
                            if child_path not in visited:
                                queue.append((child_path, level + 1))
            except (PermissionError, OSError):
                # Skip directories we can't access
                pass

    # File not found after BFS traversal
    raise FileNotFoundError(f"File '{file_name}' not found in child directories.")


_conflict_cache = {}


def resolve_conflicting(
    primary: "Path | str", alternate: "Path | str | None" = None
) -> Path:
    """Convert conflicting parameters to a canonical path.

    Args:
        primary: Path or string to resolve
        alternate: Optional alternate path, which is used if primary is not compatible

    Returns:
        Path: Resolved path
    """
    from mbcore.log import debug
    import os
    from pathlib import Path

    # If alternate is None, use CWD
    if alternate is None:
        alternate = Path.cwd()

    # Ensure both are Path objects
    primary_path = Path(primary) if primary else Path()
    alternate_path = Path(alternate)

    # For absolute paths, use primary directly
    if isinstance(primary, Path) and primary.is_absolute():
        return primary
    if isinstance(primary, str) and os.path.isabs(primary):
        return Path(primary)

    # Handle path-like strings (file paths, not URLs or package names)
    if isinstance(primary, str) and ("/" in primary or "\\" in primary):
        # If it's a relative path, resolve against alternate
        if not os.path.isabs(primary):
            result = alternate_path / primary
            debug(f"Resolved {primary} with {alternate} to {result}")
            return result
        # If it's an absolute path, use directly
        return Path(primary)

    # Default case: just return alternate path
    return alternate_path


# @cache(context_policy="mtime",persistent=True)

@with_err
def find_toml(
    path: "Path | str" = "pyproject.toml", cwd: "Path | str | None" = Path.cwd()
) -> Path:
    """Find the pyproject.toml file in the current directory or parent directories."""
    import logging

    logging.getLogger("rich").debug(f"Finding {path} in {cwd}", stack_info=True)
    cwd = resolve_conflicting(path, cwd or Path.cwd())
    with chdir(cwd.absolute()):
        from mbcore.traverse import find_file

        file, err = find_file(path, cwd)
        if err:
            raise err
        if not isinstance(file, Path):
            raise ValueError(f"pyproject.toml not found for {cwd}")
        return file


def findall_toml(cwd: "Path | str | None" = Path.cwd()) -> list[Path]:
    """Find the pyproject.toml files with optimized performance.

    Args:
        cwd: Current working directory to start search from

    Returns:
        List of found pyproject.toml files. If none found, prompts to create new workspace.
    """
    import os
    from contextlib import suppress

    # Convert to string for faster path operations
    str_cwd = str(cwd) if cwd is not None else os.getcwd()

    # Check for pyproject.toml in current directory first (fast path)
    if os.path.exists(os.path.join(str_cwd, "pyproject.toml")):
        return [Path(os.path.join(str_cwd, "pyproject.toml"))]

    # Resolve possible conflicts (keep this logic)
    cwd = resolve_conflicting("pyproject.toml", Path(str_cwd))
    str_cwd = str(cwd)

    found = []
    max_results = 10  # Limit results

    # Fast search in the current directory and immediate subdirectories
    with suppress(FileNotFoundError, PermissionError):
        # Check current directory
        toml_path = os.path.join(str_cwd, "pyproject.toml")
        if os.path.exists(toml_path) and os.path.isfile(toml_path):
            found.append(Path(toml_path).absolute())

        # Check immediate subdirectories (depth=1)
        for item in os.scandir(str_cwd):
            if len(found) >= max_results:
                break

            if item.is_dir():
                toml_path = os.path.join(item.path, "pyproject.toml")
                if os.path.exists(toml_path) and os.path.isfile(toml_path):
                    found.append(Path(toml_path).absolute())

    # If still not found, try one more level of directories
    if not found:
        with suppress(FileNotFoundError, PermissionError):
            for root_item in os.scandir(str_cwd):
                if not root_item.is_dir():
                    continue

                with suppress(PermissionError, OSError):
                    for sub_item in os.scandir(root_item.path):
                        if len(found) >= max_results:
                            break

                        if sub_item.is_dir():
                            continue

                        if sub_item.name == "pyproject.toml":
                            found.append(Path(sub_item.path).absolute())

    # If no files found, prompt to create new workspace
    if not found:
        if (
            prompt_ask(
                "No pyproject.toml file found. Would you like to create a new workspace?",
                choices=["y", "n"],
                default="n",
            )
            == "y"
        ):
            new_workspace = create_new_workspace()
            return [new_workspace / "pyproject.toml"]

    # Convert to relative paths and return
    return [Path(f) for f in found] if found else []


# @acache(context_policy="mtime",persistent=True)
async def afind_toml(
    path: "Path | str" = "pyproject.toml", cwd: "Path | str | None" = None
) -> Path:
    """Find the pyproject.toml file in the current directory or parent directories."""
    if has_error(ok:= find_toml(path, cwd)):
        raise ok.error
    return ok.result


# @cache(context_policy="mtime",persistent=True)
def load_toml(
    path: "Path | str" = "pyproject.toml", cwd: "Path | str |None" = Path.cwd()
) -> "TOMLDocument":
    """Get the data from the pyproject.toml file."""
    from tomlkit import loads

    cwd = resolve_conflicting(path, cwd or Path.cwd())
    if has_error(ok:= find_toml(path, cwd)):
        raise ok.error
    with Path(ok.result).open() as f:
        return loads(f.read())


async def aload_toml(
    path: "Path | str | Env" = "pyproject.toml", cwd: "Path | str | None" = Path.cwd()
) -> "TOMLDocument":
    """Get the data from the pyproject.toml file.

    Args:
        path: Path to the TOML file
        cwd: Working directory to use (defaults to current dir)
    """
    import logging

    logging.getLogger("rich").debug(f"Finding {path} in {cwd}", stack_info=True)
    from mbpy.env import Env

    if isinstance(path, Env):
        path = path.python.parent.parent.parent / "pyproject.toml"

    path = Path(str(path)) if path is not None else Path("pyproject.toml")
    import aiofiles
    from tomlkit import loads

    p = Path(str(path))
    cwd = resolve_conflicting(path, cwd or Path.cwd())
    async with aiofiles.open(await afind_toml(p, cwd)) as f:
        return loads(await f.read())


@cache(context_policy="site_packages", persistent=True)
def get_deps(
    toml: "TOMLDocument | Path | str | None" = None, cwd: "Path | str" = Path.cwd()
) -> "list[Dependency]":
    """Get the dependencies from the pyproject.toml file."""
    if isinstance(toml, TOMLDocument):
        from mbpy.pkg.dependency import Dependency

        deps: list[str] = toml.get("project", {}).get("dependencies", [])
        return [Dependency(dep) for dep in deps]
    toml = load_toml(toml or "pyproject.toml", cwd)
    from mbpy.pkg.dependency import Dependency

    deps: list[str] = toml.get("project", {}).get("dependencies", [])
    return [Dependency(dep) for dep in deps]


@acache(context_policy="site_packages", persistent=True)
async def aget_deps(
    toml: "TOMLDocument | Path | str | None" = None,
    cwd: "Path | str| None" = Path.cwd(),
) -> "list[Dependency]":
    """Get the dependencies from the pyproject.toml file."""
    if isinstance(toml, TOMLDocument):
        from mbpy.pkg.dependency import Dependency

        deps: list[str] = toml.get("project", {}).get("dependencies", [])
        return [Dependency(dep) for dep in deps]
    toml = await aload_toml(toml or "pyproject.toml", cwd)
    from mbpy.pkg.dependency import Dependency

    deps: list[str] = toml.get("project", {}).get("dependencies", [])
    return [Dependency(dep) for dep in deps]


def create_new_workspace() -> "Path":
    """Create a new workspace."""
    from pathlib import Path
    from mbcore.collect import setdefault as setin
    from mbcore.display import safe_print, prompt_ask
    from tomlkit import TOMLDocument

    toml = TOMLDocument()
    name = prompt_ask("Enter the name of the new workspace: ")
    setin(toml, "project.name", name)
    setin(toml, "project.version", "0.1.0")
    setin(toml, "project.description", "A new workspace")
    setin(toml, "project.authors", "A happy mb user")
    setin(toml, "project.license", "MIT")
    safe_print(f"Created new workspace: {name}.")
    Path("pyproject.toml").write_text(toml.as_string())
    return Path.cwd()


def create_portable_pyproject(output_path=None):
    """Create a portable version of pyproject.toml with vendored paths.

    This function generates a copy of the project's pyproject.toml with all
    local development paths (.dev directories) replaced with vendored paths
    and ensures all paths are relative to the project root.
    It's meant to be used for distribution, not during development.

    Args:
        output_path: Path where to save the portable pyproject.toml.
                     Defaults to workspace/vendored/pyproject.toml

    Returns:
        Path to the generated file
    """
    import re

    from mbpy.env import getws

    # Get workspace root
    ws = getws()
    if not ws:
        from mbcore.log import warning

        warning("No workspace detected. Cannot create portable pyproject.toml")
        return None

    # Source pyproject.toml
    pyproject_path = ws / "pyproject.toml"
    if not pyproject_path.exists():
        from mbcore.log import warning

        warning(f"Pyproject file not found at {pyproject_path}")
        return None

    # Default output path
    if not output_path:
        vendored_dir = ws / "vendored"
        vendored_dir.mkdir(exist_ok=True, parents=True)
        output_path = "pyproject.toml"

    # Load the pyproject.toml
    pyproject = load_toml(pyproject_path)
    if not pyproject:
        from mbcore.log import warning

        warning(f"Failed to load {pyproject_path}")
        return None

    # Convert the TOML to a string
    toml_string = pyproject.as_string()

    # Regular expressions to find different types of paths
    patterns = [
        # Match file:/// paths (both .dev and any other absolute paths)
        (r'file:///[^\s,"\']*', "file"),
        # Match absolute paths starting with /
        (r'"/[^\s,"\']*"', "abs_path"),
        # Match absolute paths in tool.pyright.extraPaths or similar sections
        (r'"\$\{.*?\}/[^\s,"\']*"', "placeholder"),
    ]

    for pattern, path_type in patterns:
        # Apply the replacements for each pattern type
        if path_type == "file":
            toml_string = re.sub(
                pattern, lambda match: replace_file_path(match, ws), toml_string
            )
        elif path_type == "abs_path":
            toml_string = re.sub(
                pattern, lambda match: replace_abs_path(match, ws), toml_string
            )
        elif path_type == "placeholder":
            toml_string = re.sub(
                pattern, lambda match: replace_placeholder_path(match, ws), toml_string
            )

    # Write the portable TOML
    with open(output_path, "w") as f:
        f.write(toml_string)

    from mbcore.log import info

    info(f"Created portable pyproject.toml at {output_path}")
    return Path(output_path).absolute()


def replace_file_path(match, ws):
    """Replace file:/// paths with git URLs for proper distribution."""
    from mbpy.env import getws, get_simple_org_repo

    abs_path = match.group(0)
    path = Path(abs_path.replace("file:///", "/"))

    # Get workspace root
    workspace = ws or getws()
    repo_org, repo_name = get_simple_org_repo(workspace)

    try:
        # Make the path relative to the workspace
        rel_path = path.absolute().relative_to(workspace.absolute())

        # For paths already in vendored directory
        if "vendored" in rel_path.parts:
            vendored_index = rel_path.parts.index("vendored")
            if len(rel_path.parts) > vendored_index + 1:
                # Use the full vendored path as the subdirectory
                subdir = "/".join(rel_path.parts[vendored_index:])
                return f"git+https://github.com/{repo_org}/{repo_name}.git#subdirectory={subdir}"

        # For .dev paths
        if ".dev" in rel_path.parts:
            dev_index = rel_path.parts.index(".dev")
            if len(rel_path.parts) > dev_index + 2:
                org = rel_path.parts[dev_index + 1]
                pkg = rel_path.parts[dev_index + 2]
                return f"git+https://github.com/{repo_org}/{repo_name}.git#subdirectory=vendored/{org}/{pkg}"

        # For other paths in the workspace
        workspace_relative = f"vendored/{rel_path.parts[0] if rel_path.parts else 'misc'}/{rel_path.parts[1] if len(rel_path.parts) > 1 else rel_path.name}"
        return f"git+https://github.com/{repo_org}/{repo_name}.git#subdirectory={workspace_relative}"

    except (ValueError, IndexError):
        # If we can't make it relative, return original
        return abs_path


def replace_abs_path(match, ws):
    """Replace absolute paths with relative paths."""
    abs_path = match.group(0).strip('"')
    path = Path(abs_path)

    try:
        # Try to make the path relative to the workspace
        rel_path = path.absolute().relative_to(ws.absolute())
        return f'"./{rel_path}"'
    except (ValueError, IndexError):
        # Can't make it relative, return the original
        return f'"{abs_path}"'


def replace_placeholder_path(match, ws):
    """Replace paths with placeholders with relative paths where possible."""
    original = match.group(0)

    # Extract the path part after the placeholder
    parts = original.split("/")
    if len(parts) <= 1:
        return original

    # Keep the placeholder but make the rest relative
    placeholder = parts[0].rstrip('"')
    path_parts = parts[1:]

    return f'{placeholder}/"{"".join(path_parts)}'
