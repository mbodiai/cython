from typing import TYPE_CHECKING, Literal, overload

from mbcore.import_utils import smart_import
from mbcore.traverse import with_err, has_error
from mbpy.pkg.toml import resolve_conflicting

if TYPE_CHECKING:
    from pathlib import Path
    from typing_extensions import Literal, Iterable

    from mbpy.pkg.dependency import Dependency

@with_err
async def aget_requirements_file(
    requirements: "Path | str" = "requirements.txt", cwd: "Path | None" = None
) -> "Path":
    """Get the requirements file path, creating one if it doesn't exist.

    We do a multi-step process:
    1. If requirements is "requirements.txt", search in parent directories up to max_levels=3
    2. If not found (or requirements is a different filename), create it in the current directory

    Args:
        requirements: Name of the requirements file, defaults to "requirements.txt"
        cwd: Directory to search from, defaults to current directory

    Returns:
        Path to the requirements file
    """
    from pathlib import Path
    from mbcore.display import safe_print
    from mbcore.traverse import asearch_parents_for_file
    from mbcore.log import debug

    # Store original cwd before it's potentially modified by resolve_conflicting
    original_cwd = Path(cwd).resolve() if cwd else Path.cwd().resolve()

    resolved_cwd = resolve_conflicting(requirements, original_cwd)  # Pass original_cwd
    debug(
        f"original_cwd: {original_cwd}, resolved_cwd: {resolved_cwd}, requirements: {requirements}"
    )

    # Determine how to handle the requirements parameter:
    # 1. If it's a directory Path object, use "requirements.txt" as the filename and create IN that directory
    # 2. Otherwise use "requirements.txt" as the default filename
    requirements_filename = "requirements.txt"
    create_in_directory = None

    if isinstance(requirements, Path) and requirements.is_dir():
        safe_print(
            f"Warning: 'requirements' argument was a directory ({requirements}). Using default filename 'requirements.txt'."
        )
        # If explicit directory is provided, create requirements.txt IN that directory if not found
        create_in_directory = requirements

    debug(
        f"Using filename: {requirements_filename}, create_in_directory: {create_in_directory}"
    )

    try:
        # Always search for requirements.txt file in parent directories
        requirements_path, err = await asearch_parents_for_file(
            requirements_filename, max_levels=3, cwd=resolved_cwd.absolute()
        )

        debug(f"After search: requirements_path={requirements_path}, err={err}")

        if err:
            # If search failed, create the file in the original current directory
            # (unless an explicit directory was provided)
            target_dir = create_in_directory if create_in_directory else original_cwd
            requirements_path = target_dir / requirements_filename
            debug(f"Search failed (err={err}). Creating at: {requirements_path}")

            if not requirements_path.exists():
                safe_print(
                    f"Creating requirements file at {requirements_path}", style="yellow"
                )
                requirements_path.parent.mkdir(parents=True, exist_ok=True)
                requirements_path.touch()
    except Exception as e:
        safe_print(f"Error accessing requirements file: {e}", style="red")
        # Use the original cwd as fallback for creating the file
        target_dir = create_in_directory if create_in_directory else original_cwd
        requirements_path = target_dir / requirements_filename
        if not requirements_path.exists():
            safe_print(
                f"Creating requirements file at {requirements_path}", style="yellow"
            )
            requirements_path.parent.mkdir(parents=True, exist_ok=True)
            requirements_path.touch()

    return requirements_path


@overload
@with_err
async def aget_requirements_packages(
    astype: Literal["list"] = "list",
    requirements: "Path | str" = "requirements.txt",
) -> list[str]: ...
@overload
@with_err
async def aget_requirements_packages(
    astype: Literal["set"] = "set",
    requirements: "Path | str" = "requirements.txt",
) -> set[str]: ...
@overload
@with_err
async def aget_requirements_packages(
    astype: Literal["deps"] = "deps",
    requirements: "Path | str" = "requirements.txt",
    cwd: "Path | str | None" = None,
) -> "list[Dependency]": ...

@with_err
async def aget_requirements_packages(
    *_args, **_kwargs
) -> "set[Dependency] | list[Dependency] | list[str] | set[str]":
    """Get the list of packages from the requirements.txt file.

    Args:
        astype (str): Whether to return the result as "deps", "list", or "set". Defaults to "deps".
        requirements (str): Path to the requirements file. Defaults to "requirements.txt".
        cwd: Working directory to use (defaults to current dir)

    Returns:
        Union[set[str], list[str], list[Dependency]]: Packages listed in the requirements file.
        
    Note:
        When astype="deps", returns a list of Dependency objects.
        When astype="list", returns a list of strings (paths or package names).
        When astype="set", returns a set of strings (paths or package names).
    """
    arglist = list(_args)
    requirements = arglist.pop() if len(arglist) > 0 and arglist[-1] not in ("set", "list", "deps") else "requirements.txt"
    astype = arglist.pop() if len(arglist) > 0 and arglist[-1] in ("set", "list", "deps") else "deps"
    cwd = arglist.pop() if len(arglist) > 0 else None

    # Pass cwd to aget_requirements_file
    result = await aget_requirements_file(requirements, cwd=cwd)
    if has_error(result):
        raise result.error
    requirements_path = result.result
    if not TYPE_CHECKING:
        Dependency = smart_import("mbpy.pkg.dependency.Dependency")  # noqa
    if not requirements_path:
        return set() if astype == "set" else [] if astype == "list" else []

    try:
        lines = requirements_path.read_text().splitlines()
        # Filter out comments and empty lines
        lines = [
            line.strip()
            for line in lines
            if line.strip() and not line.strip().startswith("#")
        ]

        # Create Dependency objects for all cases - we might need them to convert to strings
        deps = [Dependency(l) for l in lines]
        
        # Handle different return types according to function signature
        if astype == "set":
            # For set type, return set of strings
            return set(str(d) for d in deps)
        if astype == "list":
            # For list type, return list of strings
            return [str(d) for d in deps]

        # For deps type, return list of Dependency objects
        return deps

    except Exception as e:
        from mbcore.log import debug, error
        import traceback

        traceback.print_exc()
        error(f"Error reading requirements file: {e}", stack_info=True)
        return set() if astype == "set" else [] if astype == "list" else []


@with_err
async def awrite_requirements(
    packages: "Iterable[Dependency]",
    requirements: "Path | str" = "requirements.txt",
    cwd: "Path | str | None" = None,  # Add cwd parameter
) -> None:
    """Write the list of packages to the requirements.txt file.

    Args:
        packages (set): Set of packages to write to the requirements file.
        requirements (str): Path to the requirements file. Defaults to "requirements.txt".
        cwd: Working directory to use (defaults to current dir)
    """
    from pathlib import Path

    from aiofiles import open
    from mbcore.display import safe_print

    try:
        # Pass cwd to aget_requirements_file
        requirements_path = await aget_requirements_file(requirements, cwd=cwd)

        # Make sure requirements_path is a Path object
        if not isinstance(requirements_path, Path):
            requirements_path = Path(cwd) / str(requirements)
            safe_print(
                f"Creating requirements file at {requirements_path}", style="yellow"
            )
            requirements_path.touch()

        # Make sure the path exists
        if not requirements_path.exists():
            requirements_path.touch()

        # Write the requirements file
        async with open(requirements_path, "w") as f:
            await f.write("\n".join([p.requirements_name for p in packages]))

    except Exception as e:
        # Handle any errors during writing
        safe_print(f"Error writing requirements file: {e}", style="bold red")
        # Create the file at the specified location as a fallback
        try:
            fallback_path = (
                Path(cwd) / str(requirements) if cwd else Path(requirements).absolute()
            )
            async with open(fallback_path, "w") as f:
                await f.write("\n".join([p.requirements_name for p in packages]))
            safe_print(
                f"Requirements written to fallback location: {fallback_path}",
                style="yellow",
            )
        except Exception as inner_e:
            safe_print(
                f"Failed to write requirements to fallback location: {inner_e}",
                style="bold red",
            )
