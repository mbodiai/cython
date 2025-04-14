from __future__ import annotations


from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

from mbcore.cache import cache, acache
from mbcore.collect import attrgetter, compose, equals
from mbcore.more import first_true
from mbcore.display import list_or_dict_table
from mbcore._traceback import link_fp
from mbcore.resolve import resolve_name

if TYPE_CHECKING:
    from rich.console import RenderableType as Renderable
    from typing_extensions import TypeVar

    from mbpy.env import Env
    from mbpy.pkg.dependency import Dependency

    from mbcore.collect import identity

    from collections.abc import Callable, Iterable

    T = TypeVar("T", bound=Iterable)
else:
    identity = None


def stylemap(
    installed_packages: "list[Dependency]",
) -> "Callable[[Dependency],dict[str,str]]":
    def stylmap(item):
        if item in installed_packages:
            return {"Status": "bold green"}
        return {"Status": "bold red"}

    return stylmap


def valuemap(installed_packages: "list[Dependency]") -> "Callable[[Dependency],str]":
    def valmap(item):
        if item in installed_packages:
            return "✓ Installed"
        return "✗ Not Installed"

    return valmap


def pathmap(
    installed_packages: "list[Dependency]",
) -> "Callable[[Dependency],str|Text]":
    from pathlib import Path

    def pm(item: "Dependency"):
        if item in installed_packages:
            p = resolve_name(item.name)
            p = getattr(p, "__file__", p) or item.name
            if "__init__" in str(Path(str(p))):
                path = Path(str(p)).parent
            else:
                path = Path(str(p))
            return link_fp(
                str(Path(path).relative_to(Path(path).parent.parent)),
                first_true(path.iterdir(), compose(equals(".py"), attrgetter("suffix")))
                if path.is_dir()
                else path,
                lineno=1,
                style="bold cyan",
                showpath=False,
            )

        return "Not Found"

    return pm


@cache(persistent=True, ttl=10, context_policy="site_packages")
def pip_packages(env: "Env|str|None" = None) -> "list[dict[str,str]]":
    """Get a list of installed packages."""
    lines = ""
    from mbpy.cmd import run_command
    from mbpy.env import getexecutable
    import json

    for line in run_command(
        f"{getexecutable(env)} -m pip list --format=json", show=False
    ):
        lines += line
    return json.loads(lines)


def installed_packages(env: "Env|str|None" = None) -> "list[Dependency]":
    """Get a list of installed packages."""
    from mbpy.pkg.dependency import Dependency

    pkgs = pip_packages(env)
    return [Dependency(**cast(dict[str, Any], item)) for item in pkgs]


async def apip_packages(env: "Env|str|None" = None) -> "list[dict[str,str]]":
    """Get a list of installed packages using pip's internal API."""
    # Import pip's internal list command
    from pip._internal.commands.list import ListCommand
    from contextlib import redirect_stdout
    import io
    import json

    # Create output capturer
    output = io.StringIO()

    try:
        # Setup command with JSON format
        list_cmd = ListCommand("list", "List installed packages.")

        # Run pip command with output redirection
        with redirect_stdout(output):
            list_cmd.main(["--format=json"])

        # Process output
        result = output.getvalue()
        return json.loads(result)
    except Exception as e:
        from mbcore.log import error

        error(f"Error listing packages: {e}")
        return []


# @acache(persistent=True, ttl=10, context_policy="site_packages")
async def ainstalled_packages(env: "Env|str|None" = None) -> "list[Dependency]":
    """Get a list of installed packages."""
    pkgs = await apip_packages(env)
    from mbpy.pkg.dependency import Dependency

    return [Dependency(**item) for item in pkgs]


_installed_packages = installed_packages


@cache(persistent=True, ttl=10, context_policy="site_packages")
def missing_packages(env: "Env|str|None" = None) -> "list[Dependency]":
    """Get a list of missing packages."""
    from mbpy.pkg.toml import get_deps
    from mbpy.pkg.dependency import Dependency

    dependencies = get_deps()
    return list(filter(lambda x: not cast(Dependency, x).isinstalled(), dependencies))


@cache(persistent=True, ttl=10, context_policy="site_packages")
def _sync_show_command(
    package: str | None = None,
    *,
    env: "Env|str|None" = None,
    **_kwargs,
) -> "tuple[Renderable|None, Renderable|None]":
    """Show the dependencies from the pyproject.toml file."""
    import traceback

    from mbcore.display import safe_print

    from mbpy.pkg.toml import load_toml

    installed_packages = []
    dependencies = []

    if package is not None and package.strip():
        try:
            # Use pip's internal API instead of shell commands
            from pip._internal.commands.show import ShowCommand
            import io
            from contextlib import redirect_stdout

            # Create output capturer
            output = io.StringIO()

            # Run pip show command
            cmd = ShowCommand("show", "Show information about installed packages")
            with redirect_stdout(output):
                exit_code = cmd.main([package])

            result = output.getvalue()

            if exit_code == 0:
                # Limit output to first 20 and last 20 lines
                lines = result.strip().split("\n")
                if len(lines) > 40:
                    result = "\n".join(lines[:20] + ["..."] + lines[-20:])
                return result, None
            else:
                # For packages not found, we'll return a formatted error
                return f"Package(s) not found: {package}", None
        except Exception:
            traceback.print_exc()

    try:
        # Create a prettier table for installed packages
        from mbpy.helpers._show import installed_packages as get_installed_packages

        installed_packages = get_installed_packages(env)
        from mbpy.pkg.toml import get_deps

        dependencies = get_deps(load_toml("pyproject.toml"))

        return list_or_dict_table(
            installed_packages,
            title="Installed Packages",
            title_style="bold green",
            columns={"Name": "cyan", "Version": "magenta"},
            column_width=25,
        ), list_or_dict_table(
            dependencies,
            title="Required Packages",
            title_style="bold cyan",
            columns={
                "Name": None,
                "Version": None,
                "Status": valuemap,
                "Path": pathmap,
            },
            stylemap=stylemap,
        )
    except FileNotFoundError:
        import traceback

        traceback.print_exc()
        safe_print("No pyproject.toml file found.", style="bold red")
    return None, None


@acache(persistent=True, context_policy="mtime", ttl=3600)
async def _show_command(
    package: str | None = None,
    *,
    env: "Env|str|None" = None,
    cwd: Path | None = None,
    **_kwargs,
) -> "tuple[Renderable|None, Renderable|None]":
    """Show the dependencies from the pyproject.toml file."""
    import traceback
    from mbcore.log import verbose

    verbose("Running show command")

    from mbcore.display import safe_print
    from mbpy.pkg.toml import aload_toml

    installed_packages = []
    dependencies = []

    if package is not None and package.strip():
        try:
            # Use pip's internal API instead of shell commands
            from pip._internal.commands.show import ShowCommand
            from mbpy.pkg.dependency import run_pip_command

            # Run pip show command with our helper function to prevent duplicate outputs
            exit_code, output, metadata = await run_pip_command(
                ShowCommand, [package], show=False
            )

            if exit_code == 0:
                # Limit output to first 20 and last 20 lines
                lines = output.strip().split("\n")
                if len(lines) > 40:
                    result = "\n".join(lines[:20] + ["..."] + lines[-20:])
                else:
                    result = output
                return result, None
            else:
                # For packages not found, we'll return a formatted error
                return f"Package(s) not found: {package}", None
        except Exception:
            traceback.print_exc()

    try:
        # Create a prettier table for installed packages
        installed_packages = await ainstalled_packages(env)
        from mbpy.pkg.toml import aget_deps

        dependencies = await aget_deps(await aload_toml("pyproject.toml"))

        return list_or_dict_table(
            installed_packages,
            title="Installed Packages",
            title_style="bold green",
            columns={"Name": "cyan", "Version": "magenta"},
            column_width=25,
        ), list_or_dict_table(
            dependencies,
            title="Required Packages",
            title_style="bold cyan",
            columns={
                "Name": None,
                "Version": None,
                "Status": valuemap(installed_packages),
                "Path": pathmap(installed_packages),
            },
            stylemap=stylemap(installed_packages),
        )

    except FileNotFoundError:
        import traceback

        traceback.print_exc()
        safe_print("No pyproject.toml file found.", style="bold red")
    except Exception as e:
        safe_print(f"Error: {e}", style="bold red")
        traceback.print_exc()

    return None, None


def sync_show_command(
    package: str | None = None,
    *,
    env: "Env|str|None" = None,
    **_kwargs,
) -> "None":
    """Show the dependencies from the pyproject.toml file."""
    from mbcore.display import safe_print

    installed, required = _sync_show_command(package, env=env, **_kwargs)
    if installed:
        safe_print(installed)
    if required:
        safe_print(required)


async def show_command(
    package: str | None = None,
    *,
    env: "Env|str|None" = None,
    **_kwargs,
) -> "None":
    """Show the dependencies from the pyproject.toml file."""
    from mbcore.display import safe_print

    installed, required = await _show_command(package, env=env, **_kwargs)

    if installed:
        safe_print(installed)
    if required:
        safe_print(required)
