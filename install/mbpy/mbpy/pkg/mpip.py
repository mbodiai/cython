"""Synchronizes requirements and hatch pyproject."""

from itertools import filterfalse
from collections.abc import Iterable
from pathlib import Path

import rich_click as click
import tomlkit
from mbcore.collect import getin
from mbcore.display import safe_print
from mbcore.even.more import find_preferred
from mbcore.log import debug, error
from tomlkit import TOMLDocument, string
from tomlkit.items import Array, Table, Trivia
from typing_extensions import TYPE_CHECKING, Literal

from mbpy.cli import base_args
from mbpy.env import Env
from mbpy.helpers._show import ainstalled_packages
from mbpy.pkg.dependency import Dependency
from mbpy.pkg.requirements import aget_requirements_packages
from mbpy.pkg.toml import afind_toml, aload_toml

if TYPE_CHECKING:
    from typing_extensions import TypeVar

    from mbpy.env import Env

    T = TypeVar("T")


async def write_pyproject(
    data: "TOMLDocument",
    filename: "Path | str" = "pyproject.toml",
    cwd: "Path | str | None" = None,
) -> None:
    """Write the modified pyproject.toml data back to the file."""
    fn = await afind_toml(filename, cwd=cwd)
    original_data = fn.read_text() if Path(filename).exists() else ""
    try:
        fn.write_text(data.as_string())
        check = tomlkit.loads(fn.read_text())
        if check.as_string() != data.as_string():
            from difflib import unified_diff

            safe_print(
                list(
                    unified_diff(
                        list(check.as_string().splitlines()),
                        list(data.as_string().splitlines()),
                    )))
            raise Exception("Data was not written correctly")
    except Exception as e:
        import aiofiles

        error(f"Failed to write to {filename}: {e}")
        async with aiofiles.open(filename, "w") as f:
            await f.write(original_data)
        raise e


@click.command("sync")
@click.option(
    "-p",
    "--pyproject",
    default="pyproject.toml",
    required=False,
    help="Path to the pyproject.toml file.",
)
@click.option(
    "-r",
    "--requirements",
    default="requirements.txt",
    required=False,
    help="Path to the requirements.txt file.",
)
@click.option(
    "-P",
    "--prefer-requirements",
    default=False,
    help="Prefer requirements over project dependencies.",
    is_flag=True,
)
@click.option("-U",
              "--upgrade",
              default=False,
              help="Upgrade all packages.",
              is_flag=True)
@click.option(
    "-o",
    "--only",
    is_flag=True,
    help="Only sync from the source (pyproject.toml or requirements.txt)",
)
@base_args
async def sync(
    pyproject: str | Path = "pyproject.toml",
    requirements: str | Path = "requirements.txt",
    prefer_requirements: bool = False,
    upgrade: bool = False,
    only: bool = False,
    **kwargs,
) -> None:
    """Synchronize the requirements.txt file with the pyproject.toml file."""
    if not requirements:
        return await sync_project(env=kwargs.get("env"),
                                  upgrade=upgrade,
                                  only=only)
    return await sync_requirements_pyproject(pyproject,
                                             requirements,
                                             kwargs.get("env"),
                                             prefer_requirements,
                                             only=only)


async def sync_requirements_pyproject(
    pyproject: str | Path = "pyproject.toml",
    requirements: str | Path = "requirements.txt",
    env: str | Env | None = None,
    prefer_requirements: bool = False,
    upgrade: bool = False,
    only=False,
) -> None:
    proj = await aload_toml(pyproject)
    if env:
        grp = env.name if isinstance(env, Env) else env
        deps = getin(proj.unwrap(),
                     f"tools.mb.envs.{grp}.dependencies",
                     default=[])
    else:
        deps = getin(proj.unwrap(), "project.dependencies", default=[])

    projdeps = [Dependency(dep) for dep in deps]
    reqs = await aget_requirements_packages("deps", requirements)

    def preference(a: Dependency, b: Dependency) -> bool:
        nonlocal reqs, projdeps
        # Only consider one dependency preferred over another if they're the same package
        if not (
                a & b
        ):  # Using the __and__ operator that checks if they're the same package
            return False

        # For the same package, prefer:
        # 1. Installed versions
        # 2. Versions from the preferred source (reqs or projdeps)
        # 3. Higher versions
        return ((a.isinstalled() and not b.isinstalled())
                or (a in (reqs if prefer_requirements else projdeps)
                    and b not in (reqs if prefer_requirements else projdeps))
                or (a > b))

    prefered = find_preferred(projdeps, reqs, is_preferred=preference)

    await sync_project(env=env, upgrade=upgrade, packages=prefered, only=only)


async def sync_project(env=None,
                       upgrade=False,
                       packages=None,
                       only=False) -> None:
    """Synchronize the requirements.txt file with the pyproject.toml file."""
    deps = await ainstalled_packages() if not only else packages

    from mbpy.main import install_pip

    async for _ in install_pip(deps, env=env, upgrade=upgrade):
        pass


async def modify_pyproject(
    packages: "Iterable[Dependency | str]",
    action: Literal["install", "uninstall", "upgrade"] = "install",
    env: Env | str | None = None,
    group: Literal["dependencies", "optional-dependencies", "all"] | str
    | None = None,
    pyproject_path: "Path | str" = "pyproject.toml",
    cwd: "Path | str | None" = None,
) -> TOMLDocument:
    """Modify the pyproject.toml file to update dependencies based on action.

    Args:
        packages (str): Name of the package to modify.
        action (str): Action to perform, either 'install' or 'uninstall'.
        env (Optional[str]): Environment to modify (if applicable).
        group (str): Dependency group to modify (default is 'dependencies').
        pyproject_path (str): Path to the pyproject.toml file.
        cwd: Working directory to use (defaults to current dir)

    Raises:
        FileNotFoundError: If pyproject.toml is not found.
        ValueError: If Hatch environment is specified but not found in pyproject.toml.

    """
    from mbcore.log import debug

    group = group.strip("-").strip(
        ".").strip() if group is not None else "dependencies"
    pyproject = await aload_toml(pyproject_path, cwd=cwd)
    is_optional = group is not None and group != "dependencies"
    if env:
        base_project: Table = pyproject.setdefault("project", {})

    else:
        base_project: Table = pyproject.setdefault("project", {})

    if isinstance(packages, str):
        packages = [packages]
    if is_optional:
        existing = base_project.setdefault("optional-dependencies",
                                           {}).setdefault(group, [])
    else:
        existing = base_project.setdefault("dependencies", [])

    modified = await modify_dependency_list(existing, packages, action)
    debug(
        f"is optional:{is_optional}",
        "existing",
        existing,
        "modified",
        [dep.project_name for dep in modified],
    )
    all_modified = await modify_dependency_list(
        base_project.get("optional-dependencies", {}).get("all", []), packages,
        action)
    if is_optional:
        pyproject.setdefault("project", {}).setdefault(
            "optional-dependencies", {})[group] = Array(
                [string(dep.project_name) for dep in modified],
                Trivia(),
                multiline=True,
            )
    else:
        pyproject.setdefault("project", {})["dependencies"] = Array(
            [string(dep.project_name) for dep in modified],
            Trivia(),
            multiline=True,
        )

    pyproject.setdefault("project", {}).setdefault(
        "optional-dependencies", {})["all"] = Array(
            [string(dep.project_name) for dep in all_modified],
            Trivia(),
            multiline=True,
        )
    return pyproject


async def commit(
    snapshot: "Iterable[Dependency]",
    tomldata: "TOMLDocument",
    cwd: "Path | str | None" = None,
):
    """Commit the changes to the pyproject.toml file and the requirements.txt file."""
    from mbpy.pkg.requirements import awrite_requirements

    await write_pyproject(tomldata, cwd=cwd)
    await awrite_requirements(snapshot, cwd=cwd)


_commit = commit


async def modify_dependencies(
    incoming: "list[Dependency]",
    action: Literal["install", "uninstall", "upgrade"],
    group: Literal["dependencies", "optional-dependencies", "all"]
    | str
    | None = "dependencies",
    env: "str | Env | None" = None,
    commit: bool = True,
    cwd: "Path | str | None" = None,
) -> "tuple[Iterable[Dependency], TOMLDocument]":
    """Modify dependencies in pyproject.toml and requirements.txt.

    Args:
        incoming: List of dependencies to modify
        action: Action to perform (install/uninstall/upgrade)
        group: Dependency group to modify
        env: Environment to use
        commit: Whether to commit changes to disk
        cwd: Working directory to use (defaults to current dir)
    """
    req_out = await modify_requirements(incoming, action, cwd=cwd)
    project_out = await modify_pyproject(packages=incoming,
                                         action=action,
                                         group=group,
                                         env=env,
                                         cwd=cwd)
    if commit:
        await _commit(req_out, project_out, cwd=cwd)
    return req_out, project_out


async def modify_dependency_list(
    existing: "Iterable[Dependency|str] | Iterable[str]",
    incoming: "Iterable[Dependency|str] | Iterable[str]",
    action: Literal["install", "uninstall", "upgrade"],
) -> "Iterable[Dependency]":
    """Modify a list of dependencies based on the specified action."""
    from mbpy.pkg.dependency import Dependency

    # Normalize all items to Dependency objects
    incs = [
        Dependency(inc) if isinstance(inc, str) else inc for inc in incoming
    ]
    deps = [
        Dependency(dep) if isinstance(dep, str) else dep for dep in existing
    ]

    debug(
        f"modify_dependency_list action={action}, incoming={[getattr(d, 'project_name', str(d)) for d in incs]}, existing={[getattr(d, 'project_name', str(d)) for d in deps]}"
    )

    if action in ("uninstall", "upgrade"):
        return list(
            filterfalse(lambda dep: any(dep == inc for inc in incs), deps))

    if action in ("install", "upgrade"):
        # Check if any dependency has no name attribute or it's None
        if any(
                getattr(dep, 'project_name', None) is None
                for dep in incs + deps):
            raise ValueError(
                f"Cannot install or upgrade packages with no name: {incs + deps}"
            )
        # Filter out existing deps that match any incoming deps
        filtered_deps = list(
            filterfalse(lambda dep: any(dep == inc for inc in incs), deps))
        return incs + filtered_deps

    raise ValueError(
        f"Invalid action: {action}. Must be one of 'install', 'uninstall', or 'upgrade'."
    )


def get_project_deps(
    path: "Path | str" = "pyproject.toml",
    cwd=None,
    type: Literal["dep", "name"] = "name",
) -> "list[Dependency] | list[str]":
    from mbpy.pkg.dependency import Dependency
    from mbpy.pkg.toml import load_toml

    toml = load_toml(path, cwd)
    deps = [
        Dependency(name)
        for name in getin(toml.unwrap(), "project.dependencies", default=[])
    ]
    return [d.name for d in deps] if type == "name" else deps


async def modify_requirements(
    incoming: "list[Dependency]",
    action: Literal["install", "uninstall", "upgrade"],
    cwd: "Path | str | None" = None,
):
    """Modify the requirements.txt file to install or uninstall a package.

    Args:
        incoming: List of dependencies to modify
        action: Action to perform
        cwd: Working directory to use (defaults to current dir)
    """
    from mbpy.pkg.requirements import aget_requirements_packages

    deps = await aget_requirements_packages(astype="deps", cwd=cwd)
    return await modify_dependency_list(deps, incoming, action)
