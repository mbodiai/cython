import os
import sys

if os.getenv("MB_DEBUG"):
    from mbpy.helpers._show import missing_packages

    if (missing := missing_packages()) and not any("--mb_autorun" in arg
                                                   for arg in sys.argv):
        from mbcore.display import prompt_ask, safe_print

        safe_print(f"\nMissing packages:\n\n {[str(m) for m in missing]}\n")
        y = prompt_ask("Install missing packages?",
                       choices=["y", "n"],
                       default="y")
        if any(str(c) in str(y) for c in "y\n "):
            from mbpy.helpers.autopip import autorun

            autorun(sys.argv + ["--mb_autorun"])

from typing_extensions import TYPE_CHECKING

from mbpy.cli import base_args, cli, click, has_failure

if TYPE_CHECKING:
    from pathlib import Path
    from typing import (
        TYPE_CHECKING,
        AsyncIterator,
        Callable,
        Iterable,
        Literal,
        ParamSpec,
        Tuple,
        TypeVar,
    )

    P = ParamSpec("P")
    R = TypeVar("R")
    from cProfile import Profile

    import rich_click as click
    from mbcore import log
    from rich.progress import TaskID
    from mbpy.pkg.dependency import Dependency
    from mbpy.pkg.pypi import InfoKey


@click.command("install", no_args_is_help=True)
@click.argument("packages", nargs=-1, required=False, default=None)
@base_args
@click.option(
    "-r",
    "--requirements",
    type=click.Path(exists=True),
    help="Install packages from the given requirements file",
)
@click.option("-U", "--upgrade", is_flag=True, help="Upgrade the package(s)")
@click.option(
    "-e",
    "--editable",
    is_flag=True,
    help="Install a package in editable mode",
)
@click.option(
    "-g",
    "--group",
    default="dependencies",
    help="Specify the dependency group to use",
)
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging")
@click.option(
    "-b",
    "--broken",
    type=click.Choice(["skip", "ask", "repair"]),
    default="skip",
    help="Behavior for broken packages",
)
@click.option(
    "-E",
    "--env",
    default=None,
    help="Specify the python, hatch, conda, or mbnix environment",
)
@click.option(
    "-D",
    "--dev",
    is_flag=True,
    help="Install as a development dependency",
)
@click.option(
    "-G",
    "--github",
    is_flag=True,
    help="Install from GitHub",
)
@click.option(
    "--no-deps",
    is_flag=True,
    help="Don't install package dependencies",
)
@click.pass_context
async def install_command(
    ctx: click.RichContext,
    packages=None,
    requirements=None,
    upgrade=False,
    editable=False,
    group=None,
    broken: 'Literal["skip", "ask", "repair"]' = "ask",
    env=None,
    dev=False,
    github=False,
    no_deps=False,
    **_kwargs,
) -> None:
    """Install packages and update requirements.txt and pyproject.toml accordingly.

    Args:
        packages (tuple): Packages to install.
        requirements (str, optional): Requirements file to install packages from. Defaults to None.
        upgrade (bool, optional): Upgrade the package(s). Defaults to False.
        editable (bool, optional): Install a package in editable mode. Defaults to False.
        env (str, optional): The Hatch environment to use. Defaults to "default".
        group (str, optional): The dependency group to use. Defaults to "dependencies".
        debug (bool, optional): Enable debug logging. Defaults to False.
        broken (Literal["skip", "ask", "repair"], optional): Behavior for broken packages. Defaults to "skip".
        env (str, optional): The python, hatch, conda, or mbnix environment. Defaults to None.
        dev (bool, optional): Install as a development dependency. Defaults to False.
        github (bool, optional): Install from GitHub. Defaults to False.
        no_deps (bool, optional): Don't install package dependencies. Defaults to False.

    Examples:
        # Install a package by name
        mb install package_name

        # Install a package in editable mode
        mb install -e ./path/to/package

        # Install from GitHub organization/repository
        mb install -G org/repo

        # Install git URL with specific branch
        mb install "git+https://github.com/org/repo.git@branch"

        # Install from requirements file
        mb install -r requirements.txt

        # Install as development dependency
        mb install -D package_name
    """
    arglist = [a for a in ctx.args if a not in ("-d", "-vv")]
    if no_deps and "--no-deps" not in arglist:
        arglist.append("--no-deps")
    group = group or ("dev" if dev else None)
    async for _ in install_pip(
            packages=packages or [],
            requirements=requirements,
            upgrade=upgrade,
            editable=editable,
            group=group,
            env=env,
            dev=dev,
            broken=broken,
            github=github,
            args=arglist,
    ):
        pass
    return


install_command.allow_extra_args = True


async def install_pip(
    packages: "Iterable[str | Path | Dependency] | None" = None,
    requirements: "str | Path | None" = None,
    upgrade: bool = False,
    editable: bool = False,
    group: str | None = None,
    env: str | None = None,
    dev: bool = False,
    broken: "Literal['skip', 'ask', 'repair']" = "ask",
    github: bool = False,
    args: list[str] | None = None,
    **_kwargs,
) -> "AsyncIterator[tuple[TaskID, Dependency]]":
    """Construct pip install command."""
    from mbcore.import_utils import smart_import

    if not TYPE_CHECKING:
        repair_main = smart_import("mbpy.pkg.repair.main")
    else:
        pass
    from mbcore.display import (
        getprogress,
        getspinner,
        prompt_ask,
        setconsole,
        setprogress,
    )
    from mbcore.execute import process_tasks
    from mbcore.import_utils import smart_import
    from rich.progress import TaskID

    from mbpy.pkg.dependency import Dependency
    from mbpy.pkg.requirements import aget_requirements_packages

    spinner = getspinner()
    if requirements:
        reqs = await aget_requirements_packages(requirements=requirements)
    else:
        reqs = []
    packages = packages or []
    from mbpy.env import getenv
    from itertools import chain

    if group and dev:
        raise ValueError("Cannot specify both --dev and --group")
    group = group or ("dev" if dev else None)
    if not requirements and not packages:
        raise ValueError("No packages or requirements file provided.")
    packages = [
        Dependency(str(pkg),
                   editable=editable,
                   group=group,
                   upgrade=upgrade,
                   env=getenv(env)) for pkg in chain(reqs, packages)
        if pkg is not None
    ]

    spinner.stop()
    with getprogress() as progress:
        setconsole(progress.console)
        setprogress(progress)
        ts = [
            progress.add_task(f"[green]Installing {p.name}...", total=100)
            for p in packages
        ]

        async def install(t: TaskID,
                          p: Dependency) -> tuple[TaskID, Dependency]:
            progress.print(f"Installing {str(p)}...")
            await p.install(
                editable=editable,
                group=group,
                upgrade=upgrade,
                progress_tid=(progress, t),
                github=github,
                args=args,
            )
            progress.update(t, advance=50)
            if p.error:  # noqa: SIM102
                if broken == "ask" and prompt_ask("Repair broken package?",
                                                  choices=["y", "n"],
                                                  default="y"):
                    t = progress.add_task(f"[blue]Repairing {p.name}",
                                          total=None)
                    repair_main = smart_import("mbpy.pkg.repair.main",
                                               debug=True)
                    await repair_main(p.name, console=progress.console)
                    t = progress.add_task(f"[green]Downloading {p.name}",
                                          total=None)
                    return t, p
            return t, p

        while not progress.finished:
            async for t, p in process_tasks(
                [install(t, p) for t, p in zip(ts, packages, strict=False)], ):
                try:
                    if has_failure(p.error or "") or p.error:
                        progress.console.print(f"{p.error}\n",
                                               style="bold red")
                        if broken == "ask" and prompt_ask(
                                "Repair broken package?",
                                choices=["y", "n"],
                                default="y"):
                            t = progress.add_task(f"[blue]Repairing {p.name}",
                                                  total=None)

                            await repair_main(p.name, console=progress.console)
                            t = progress.add_task(
                                f"[green]Downloading {p.name}", total=None)
                            continue

                    progress.update(t, completed=100)
                    yield (t, p)
                except Exception:
                    if broken == "ask" and prompt_ask("Repair broken package?",
                                                      choices=["y", "n"],
                                                      default="y"):
                        t = progress.add_task(f"[blue]Repairing {p.name}",
                                              total=None)
                        repair_main = smart_import("mbpy.pkg.repair.main",
                                                   debug=True)
                        await repair_main(p.name, console=progress.console)
                        t = progress.add_task(f"[green]Downloading {p.name}",
                                              total=None)
                        continue

            return


install_command.allow_extra_args = True


def profile_and_run(
    f: "Callable[...,R]",
    argskwargs: tuple[tuple, dict],
    n: int = 50,
    sort: "Literal['cumulative','tottime']" = "tottime",
) -> "Tuple[R|None, float, Profile]":
    """Run a function (sync or async) with cProfile and print stats."""
    import asyncio
    import cProfile
    import pstats
    from inspect import iscoroutinefunction
    from time import time
    from types import ModuleType

    from mbcore.display import safe_print

    args, kwargs = argskwargs
    profiler = cProfile.Profile()
    tic = time()
    profiler.enable()
    globals()["mb_profiler"] = profiler
    safe_print(
        f"Running {f.__name__}... with args: {args} and kwargs: {kwargs}")
    out = None
    if isinstance(f, ModuleType):
        import runpy

        mod = f

        def f():
            runpy.run_module(mod.__name__, run_name="__main__")

        out = f()
    elif iscoroutinefunction(f):
        loop = asyncio.get_event_loop()
        import threading

        thread = threading.Thread(target=loop.run_until_complete,
                                  args=(f(*args, **kwargs), ),
                                  daemon=True)
        thread.start()
        thread.join()
        out = None
    else:
        try:
            out = f(*args, **kwargs)
        except Exception:
            out = f()

    profiler.disable()
    toc = time()
    stats = pstats.Stats(profiler)
    stats.sort_stats(sort).print_stats(n)
    safe_print(f"{f.__name__} took {(toc - tic):.4f} seconds.")
    return out, toc - tic, profiler


def parse_args(args: list[str]) -> tuple[tuple[str], dict[str, str]]:
    """Parse command line arguments of various forms:
    -v=val, val, --v=val, -v val, --v val.

    Returns a dictionary of arguments and their values.
    """  # noqa: D205
    result = {}
    i = 0
    arglist = []
    while i < len(args):
        arg = args[i]

        # Case: --key=value or -key=value
        if arg.startswith("-") and "=" in arg:
            key, value = arg.split("=", 1)
            key = key.lstrip("-")
            result[key] = value
            i += 1

        # Case: --key or -key followed by a value
        elif arg.startswith("-"):
            key = arg.lstrip("-")
            if i + 1 < len(args) and not args[i + 1].startswith("-"):
                result[key] = args[i + 1]
                i += 2
            else:
                # Key with no value is considered a flag
                result[key] = True
                i += 1

        # Case: plain value (positional argument)
        else:
            arg = 0
            while (i < len(args) and not args[i].startswith("-")
                   and not args[i].startswith(" ")):
                arg += 1
                i += 1
            if arg > 0:
                arglist.append(args[i - arg:i])
            i += 1

    return arglist, result


def module_from_file(file_path: str) -> "ModuleType":
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        Path(file_path).stem, file_path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[Path(file_path).stem] = m
    spec.loader.exec_module(m)
    return m


@cli.command("time", no_args_is_help=True)
@click.argument("command", nargs=-1)
@base_args
def time_command(command: str, *args, **kwargs) -> None:
    """Execute a shell command asynchronously and print its execution time."""
    import ast
    import os
    import shlex
    import shutil
    from cProfile import Profile
    from inspect import signature

    from mbcore.display import safe_print
    from mbcore.log import debug, verbose

    cmd = command
    if not command:
        click.echo("Please provide a command to run.")
        return
    try:
        from importlib import import_module

        if isinstance(command, tuple):
            command = " ".join(command)
        outtup = command.rsplit(":", 1)
        pkg, mod = outtup[0], outtup[-1]
        split = mod.rsplit(":")
        if len(split) > 1:
            mod, name = split
        else:
            name = mod
        mod = mod.split()[0].strip()
        name = name.split()[0].strip()
        pkg = pkg.split()[0].strip()
        obj = __import__(pkg, fromlist=[mod])
        obj = getattr(obj, mod)
        if name != mod:
            obj = getattr(obj, name)
        args, kwargs = parse_args(cmd[1:])
        print(args, kwargs)
        profile_and_run(obj, ((*args, ), kwargs))
        return
    except ImportError:
        pass
    if "running_mb_command" in globals():
        safe_print("Command already running.")
        args, kwargs = parse_args(command)
        profile_and_run(os.system, argskwargs=((*args, ), kwargs))
        return
    globals()["running_mb_command"] = True
    command_str = " ".join(command if isinstance(command, list
                                                 | tuple) else [command])
    args = shlex.split(command_str)

    which = shutil.which(args[0])
    if not which:
        safe_print(f"Command {args[0]} not found.")
        return
    if Path(which).is_file():
        for arg in args:
            try:
                try:
                    txt = Path(arg).read_text()
                    verbose(f"Reading text from {arg}")
                except Exception:
                    continue
                if arg.endswith(".py"):
                    mod = module_from_file(arg)

                    args, kwargs = parse_args(args[args.index(arg) + 1:])
                    f = getattr(mod, "main", mod)
                    profile_and_run(f, (args, kwargs))
                    return
                else:
                    nodes = ast.parse(txt)
                    for node in ast.walk(nodes):
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                if alias.name in (
                                        "re",
                                        "os",
                                        "sys",
                                        "time",
                                        "importlib",
                                ):
                                    continue
                                try:
                                    sys.path.append(os.path.dirname(which))
                                    mod = __import__(alias.name)
                                    args, kwargs = parse_args(args[1:])
                                    f = getattr(mod, alias.name)
                                    params = signature(f).parameters
                                    for k, v in kwargs.copy().items():
                                        if k not in params:
                                            from mbcore.log import warning

                                            warning(
                                                f"Invalid argument {k}. Found function: {alias.name} with parameters: {params}"
                                            )
                                            kwargs.pop(k)
                                    profile_and_run(f, (args, kwargs))
                                except ImportError:
                                    import traceback

                                    traceback.print_exc()
                                    print(f"Failed to import {alias.name}")
                                    continue
                        elif isinstance(node, ast.ImportFrom):
                            if node.module in (
                                    "re",
                                    "os",
                                    "sys",
                                    "time",
                                    "importlib",
                                    "__future__",
                            ):
                                continue
                            for alias in node.names:
                                if alias.name in (
                                        "re",
                                        "os",
                                        "sys",
                                        "time",
                                        "importlib",
                                        "__future__",
                                ):
                                    continue
                                try:
                                    sys.path.append(os.path.dirname(which))
                                    mod = __import__(node.module or "",
                                                     fromlist=[alias.name])

                                    verbose(
                                        f"Importing {alias.name} from {node.module or ''}"
                                    )
                                    verbose(f"Args: {args[1:]}")
                                    verbose(f"Kwargs: {kwargs}")
                                    args, kwargs = parse_args(args[1:])
                                    f = getattr(mod, alias.name)
                                    params = signature(f).parameters
                                    for k, v in kwargs.copy().items():
                                        if k not in params:
                                            from mbcore.log import warning

                                            warning(
                                                f"Invalid argument {k}. Found function: {alias.name} with parameters: {params}"
                                            )
                                            kwargs.pop(k)
                                    profile_and_run(f, (args, kwargs))
                                except ImportError:
                                    if debug():
                                        import traceback

                                        traceback.print_exc()
                                        print(f"Failed to import {alias.name}")
                                    continue
                break
            except Exception:
                if debug():
                    import traceback

                    traceback.print_exc()
                pass
    if not globals().get("mb_profiler"):
        from cProfile import Profile
        from pstats import Stats
        from time import time

        tic = time()
        prof = Profile()
        prof.enable()
        os.system(command_str)
        prof.disable()
        toc = time()
        stats = Stats(prof)
        stats.sort_stats("cumulative").print_stats(10)
        safe_print(f"{command_str} took {(toc - tic):.4f} seconds.")


@cli.command("uninstall", no_args_is_help=True)
@click.argument("packages", nargs=-1)
@click.option(
    "-g",
    "--group",
    default="dependencies",
    help="Specify the dependency group to use",
)
@base_args
@click.pass_context
async def uninstall_command(ctx, packages, group, **kwargs) -> None:
    """Uninstall packages and update requirements.txt and pyproject.toml accordingly.

    Args:
        packages (tuple): Packages to uninstall.
        group (str, optional): The dependency group to use. Defaults to "dependencies".
        **kwargs: Additional arguments from base_args (env, debug, etc.)

    """
    await _uninstall_command(packages,
                             kwargs.get("env"),
                             group,
                             debug=kwargs.get("debug", False),
                             ctx=ctx)


uninstall_command.allow_extra_args = True


async def _uninstall_command(packages,
                             env,
                             group,
                             *,
                             debug=False,
                             ctx=None) -> None:
    """Uninstall packages and update requirements.txt and pyproject.toml accordingly."""
    from mbcore import log
    from mbcore.display import safe_print
    from mbpy.pkg.dependency import Dependency
    from mbpy.pkg.mpip import modify_dependencies

    packages = [
        Dependency(pkg) if not isinstance(pkg, Dependency) else pkg
        for pkg in packages
    ]

    for package in packages:
        package_name = package.name

        # First update pyproject.toml and requirements.txt regardless of installation status
        try:
            await modify_dependencies(incoming=[package],
                                      action="uninstall",
                                      group=group)
            safe_print(
                f"Removed {package_name} from project dependencies",
                style="bold light_goldenrod2",
            )
        except Exception as e:
            safe_print(
                f"Error: Failed to remove {package_name} from dependencies: {str(e)}",
                style="bold red",
            )
            if debug:
                import traceback

                traceback.print_exc()

        # Now try to uninstall if it's actually installed
        try:
            # Get any extra args that might be present
            extra_args = None
            if ctx and hasattr(ctx, "args"):
                extra_args = [a for a in ctx.args if a not in ("-d", "-vv")]

            # Check if package is actually installed before trying to uninstall
            if await package.ainstalled_version():
                await package.uninstall(env=env, args=extra_args)
            else:
                safe_print(
                    f"Package {package_name} not installed, skipping uninstall",
                    style="bold yellow",
                )
        except Exception as e:
            safe_print(f"Error: Failed to uninstall {package_name}.",
                       style="bold red")
            if debug:
                import traceback

                traceback.print_exc()
            log.error(f"Error: {e}")
            # Continue to the next package instead of returning


@cli.command("show", no_args_is_help=False)
@click.argument("package", type=str, default=None, required=False)
@base_args
async def show_command(package=None, **kwargs) -> None:
    """Show the dependencies from the pyproject.toml file.

    Args:
        package (str, optional): The package to show information about. Defaults to None.
        env (str, optional): The Hatch environment to use. Defaults to "default".
        debug (bool, optional): Enable debug logging. Defaults to False.

    """
    from mbpy.helpers._show import show_command

    env = kwargs.get("env")
    await show_command(package, env=env, debug=kwargs.get("debug", False))


INFO_KEYS = [
    "author",
    "author_email",
    "bugtrack_url",
    "classifiers",
    "description",
    "description_content_type",
    "docs_url",
    "download_url",
    "downloads",
    "dynamic",
    "home_page",
    "keywords",
    "license",
    "maintainer",
    "maintainer_email",
    "name",
    "package_url",
    "platform",
    "project_url",
    "project_urls",
    "provides_extra",
    "release_url",
    "requires_dist",
    "requires_python",
    "summary",
    "version",
    "yanked",
    "yanked_reason",
]
ADDITONAL_KEYS = ["last_serial", "releases", "urls", "vulnerabilities"]
from mbpy.cli import get_help_config


@cli.command("search",
             no_args_is_help=True,
             help="Search for a package on PyPI.")
@click.argument("query", type=str, nargs=-1, required=False)
@click.option("-l", "--limit", default=10, help="Limit the number of results")
@click.option(
    "-i",
    "--include",
    multiple=True,
    type=click.Choice(["all"] + INFO_KEYS + ADDITONAL_KEYS),
    default=None,
    help="Include additional information",
)
@click.option(
    "-p",
    "--provider",
    type=click.Choice(["pypi", "github", "google", "huggingface"]),
    default=["pypi"],
    help="Provider to use",
    multiple=True,
)
@click.option("-r", "--release", default=None, help="Release version to use")
@click.option("-D",
              "--describe",
              is_flag=True,
              help="Show package description")
@click.option(
    "-s",
    "--sort",
    type=click.Choice(["downloads", "relevance", "name", "version"]),
    default="downloads",
    help="Sort key to use",
)
@click.option(
    "-V",
    "--verbosity",
    type=click.Choice(["0", "1", "2"]),
    default="0",
    help="Verbosity level",
)
@base_args
@click.rich_config(get_help_config())
async def search_command(
    query: list[str] | None = None,
    limit: int = 5,
    include: "list[InfoKey] | None" = None,
    provider: list[str] = ["pypi"],
    release: str | None = None,
    describe: bool = False,
    sort: str = "downloads",
    verbosity: "Literal[0,1,2,3]" = 0,
    **kwargs,
) -> None:
    """Find a package on PyPI and optionally sort the results.

    Args:
        package (str): The package to search for.s
        limit (int, optional): Limit the number of results. Defaults to 5.
        sort (str, optional): Sort key to use. Defaults to "downloads".
        include (str, optional): Include pre-release versions. Defaults to None.
        release (str, optional): Release type to use. Defaults to None.
        debug (bool, optional): Enable debug logging. Defaults to False.

    """
    import traceback

    from mbcore.display import getspinner, safe_print
    from mbcore.log import verbose
    from mrender.md import Markdown

    from mbpy.pkg.pypi import find_and_sort

    include = list(include or [])
    if describe:
        include.append("description")

    if not isinstance(query, str):
        q = " ".join(
            map(str,
                [query] if not isinstance(query, list | tuple) else query))
    try:
        getspinner().start()
        if "google" in provider:
            from mbpy.tools.google import agoogle

            out = await agoogle(q, **kwargs)
            getspinner().stop()
            md = Markdown(out)
            md.stream()

            return

        async for pkg in find_and_sort(
                q,
                limit=limit,
                verbosity=verbosity,
                include=include or [],
                release=release,
                github="github" in provider,
                pypi="pypi" in provider,
        ):
            md = Markdown(pkg)
            verbose(pkg)
            getspinner().stop()
            md.stream()
    except KeyboardInterrupt:
        safe_print("Search cancelled.", style="bold red")
    except Exception:
        traceback.print_exc()


search_command.allow_extra_args = True


@cli.command("info", no_args_is_help=False)
@click.argument("package_or_path", required=False)
@click.option("-p",
              "--path",
              is_flag=True,
              help="Show the path to the package")
@click.option("--deps",
              is_flag=True,
              help="Show the dependencies of the package")
@click.option("-v", "--verbose", is_flag=True, help="Show verbose information")
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging")
async def info_command(package_or_path=None,
                       verbose=False,
                       path=False,
                       deps=False,
                       **kwargs) -> None:
    """Get information about a package from PyPI."""
    await _info_command(package_or_path,
                        verbose=verbose,
                        path=path,
                        deps=deps,
                        **kwargs)


async def _info_command(
    package_or_path: str | None = None,
    verbose: bool = False,
    path: bool = False,
    deps: bool = False,
    **kwargs,
) -> str | None:
    """Get information about a package.\
    
    Attempts to get info from the local installation using pip show first.
    If not found locally, falls back to querying PyPI.
    """
    from pathlib import Path
    from mbcore.display import safe_print
    from mrender.md import Markdown
    from mbpy.cmd import arun_cached
    from mbpy.pkg.dependency import Dependency
    from mbpy.pkg.pypi import get_package_info
    from mbcore.log import error, debug
    import traceback

    if not package_or_path:
        try:
            package = Dependency.fromtoml()
        except Exception as e:
            error(
                f"No package specified and couldn't find one in pyproject.toml: {e}"
            )
            return None
    else:
        package = Dependency(package_or_path)

    # --- Attempt to get info from local installation using pip show ---
    pip_show_failed = False
    data = ""  # Initialize data
    try:
        debug(
            f"Running 'pip show {package.base}' (cached) to check local installation."
        )
        data = await arun_cached(f"pip show {package.base}", show=False)

        if not data or "WARNING: Package(s) not found" in data:
            debug(
                f"'pip show {package.base}' (cached) indicated package not found."
            )
            pip_show_failed = True
        else:
            debug(f"'pip show {package.base}' (cached) successful.")
            # --- Pip show succeeded, package is installed locally ---
            if path:
                location = ""
                if "Editable Location:" in data:
                    location = (data.split("Editable Location:")[1].split("\n")
                                [0].strip())
                elif "Location:" in data:
                    install_loc = data.split("Location:")[1].split(
                        "\n")[0].strip()
                    potential_path = Path(install_loc) / package.base
                    potential_init = Path(
                        install_loc) / package.base / "__init__.py"
                    if potential_init.exists():
                        location = str(potential_path)
                    else:
                        potential_py_file = Path(
                            install_loc) / f"{package.base}.py"
                        if potential_py_file.exists():
                            location = str(potential_py_file)
                        else:
                            location = install_loc
                if location:
                    safe_print(location)
                    return location
                else:
                    error(
                        f"Could not parse Location or Editable Location from 'pip show {package.base}' output."
                    )
                    pip_show_failed = True

            elif deps:
                if "Requires:" in data:
                    deps_list = (data.split("Requires:")[1].split("\n")
                                 [0].strip().split(", "))
                    safe_print(deps_list)
                    return ", ".join(deps_list)
                else:
                    safe_print([])
                    return ""
            else:
                safe_print(data)
                return data

    except Exception as e:
        error(
            f"Unexpected error processing 'pip show {package.base}' (cached): {e}"
        )
        traceback.print_exc()
        pip_show_failed = True

    # --- If pip show failed, try getting info from PyPI ---
    if pip_show_failed:
        debug(f"Falling back to PyPI query for {package.base}.")
        try:
            package_info = await get_package_info(
                package.base,
                include="description" if verbose else None,
                once=True)
            if not package_info:
                safe_print(
                    f"Package '{package.base}' not found locally or on PyPI.")
                return None

            md = Markdown(package_info)
            md.stream()
            return str(package_info)

        except Exception as e:
            error(f"Error getting package info from PyPI: {e}")
            traceback.print_exc()
            return None


@cli.command("create", no_args_is_help=True)
@click.argument("project_name")
@click.argument("author")
@click.option("-n", "--new", is_flag=True)
@click.option("--description", default="", help="Project description")
@click.option("--deps", default=None, help="Dependencies separated by commas")
@click.option("--python", default="3.11", help="Python version to use")
@click.option("--no-cli", is_flag=True, help="Do not add a CLI")
@click.option(
    "--autodoc",
    type=click.Choice(["sphinx", "mkdocs"]),
    default="sphinx",
    help="Documentation type to use",
)
async def create_command(
    project_name,
    author,
    new,
    description,
    deps: str,
    python="3.11",
    no_cli=False,
    autodoc="sphinx",
) -> None:
    """Create a new Python project. Optionally add dependencies and a CLI."""
    if not TYPE_CHECKING:
        from mbcore.import_utils import smart_import

        create_project = smart_import("mbpy.create.create_project")
        safe_print = smart_import("mbcore.display.safe_print")
    else:
        from mbcore.display import safe_print

        from mbpy.create import create_project
    python_version = python

    try:
        dep = deps.split(",") if deps else []
        out = await create_project(
            project_name=project_name,
            author=author,
            new=new,
            description=description,
            python_version=python_version,
            dependencies=dep,
            add_cli=not no_cli,
            autodoc=autodoc,
        )
        if out:
            safe_print(
                f"Project {project_name} created successfully.",
                style="bold light_goldenrod2",
            )
    except Exception:
        import traceback

        traceback.print_exc()


@cli.command("bump")
@click.option("--major", is_flag=True, help="Bump the major version")
@click.option("--minor", is_flag=True, help="Bump the minor version")
@click.option("--patch", is_flag=True, help="Bump the patch version")
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging")
async def bump_command(major=False,
                       minor=False,
                       patch=True,
                       debug=False) -> None:
    """Bump the version of a package."""
    from mbcore.import_utils import smart_import

    smart_import("mbpy")

    if debug:
        log.debug.set()
    bump_pkg = smart_import("mbpy.pkg.bump.bump")
    try:
        await bump_pkg(major=major, minor=minor, patch=patch)
    except Exception:
        import traceback

        traceback.print_exc()


@cli.command("build", no_args_is_help=True)
@click.argument("path", default=".", required=False)
@click.option("-c", "--cythonize", is_flag=True, help="Cythonize the package")
@click.option(
    "-p",
    "--package-manager",
    type=click.Choice(["gh", "hatch", "uv", "pip"]),
    default="pip",
    help="Package manager to use",
)
@base_args
async def build_command(path: "str | Path" = ".",
                        cythonize: bool = False,
                        package_manager="pip",
                        **kwargs) -> None:
    """Cythonize and build a package."""
    await _build_command(
        path,
        env=kwargs.get("env"),
        cythonize=cythonize,
        package_manager=package_manager,
    )


async def _build_command(
    path: "Path | str" = ".",
    env: str | None = None,
    cythonize: bool = False,
    package_manager="pip",
) -> None:
    """Cythonize and build a package."""
    from pathlib import Path

    import tomlkit
    from mbcore.display import getprogress, getspinner, prompt_ask, safe_print
    from mbcore.more import unique_everseen

    from mbpy.env import getexecutable
    from mbpy.helpers._setup_py import setup_command

    try:
        path = Path(str(path))
        getspinner().stop()
        with getprogress() as progress:
            # Setup task
            setup_task = progress.add_task(
                "[cyan]Setting up build environment...", total=100)

            # Initialize build environment
            out = path / "dist" / path.stem
            out.mkdir(parents=True, exist_ok=True)

            # Configure build settings
            progress.update(setup_task,
                            description="[cyan]Configuring build settings...")
            pyproject = tomlkit.loads((path / "pyproject.toml").read_text())

            # Update build requirements
            progress.update(setup_task,
                            description="[cyan]Updating build requirements...")
            bsr = (pyproject.unwrap().setdefault("build-system",
                                                 {}).setdefault(
                                                     "requires", []))
            bsr = unique_everseen(bsr + ["setuptools", "wheel"])
            pyproject.unwrap()["build-system"]["requires"] = list(bsr)

            # Verify and update build backend
            progress.update(
                setup_task,
                advance=20,
                description="[cyan]Verifying build configuration...",
            )
            if (pyproject.setdefault("build-system", {}).get("build-backend")
                    != "setuptools.build_meta"):
                progress.stop()
                y = prompt_ask(
                    "Build backend not set to setuptools. Configure it now?",
                    choices=["y", "n", "explain"],
                    default="y",
                )
                if y == "explain":
                    safe_print(
                        "\n".join([
                            f"Current build backend: {pyproject.setdefault('build-system', {}).get('build-backend', 'None')}",
                            "",
                            "Setuptools is the recommended build backend for Cython projects because:",
                            "1. It has mature Cython support built-in",
                            "2. It handles extension modules reliably across platforms",
                            "3. It's well-tested with most Python packaging tools",
                            "",
                            "A temporary setup.py will be created to ensure proper Cython compilation.",
                        ]), )

                if prompt_ask("Continue?", choices=["y", "n"],
                              default="y") == "y":
                    pyproject.setdefault(
                        "build-system",
                        {})["build-backend"] = ("setuptools.build_meta")

                    pkg_section = (pyproject["tool"].setdefault(
                        "setuptools", {}).setdefault("packages", {}))
                    if not pkg_section:
                        pkg_section["find"] = {
                            "where": ["."],
                            "include": ["*"],
                            "exclude": ["tests", "docs", "tmp"],
                        }
                    else:
                        safe_print(
                            "[bold yellow]Package section already exists. Consider removing `tool.setuptools.packages` from pyproject.toml if you encounter issues.[\bold yellow]"
                        )
                    (path / "pyproject.toml").write_text(pyproject.as_string())
                else:
                    safe_print("Build cancelled.", style="bold cyan")
                    return

        build_result = await setup_command(
            path,
            pyproject=pyproject,
            package_manager=package_manager,
            cythonize=cythonize,
        )
        status = build_result.status
        if status != "succeeded":
            safe_print(f"[red]Build failed:[/red]\n{build_result}")
        if status == "succeeded":
            safe_print("[green]Build succeeded.[/green]")
            return

        if not cythonize:
            out = await arun(
                f"{getexecutable(env)} -m pip install -e {str(path)}",
                show=True)
            status = "installed" if "Successfully installed" in out else "failed"
        safe_print(f"Package {status} successfully.")

    except Exception as e:
        safe_print(f"[red]Build failed:[/red] {str(e)}")
        if log.debug():
            log.error(e)
            import traceback

            traceback.print_exc()


@cli.command("undo")
async def undo_command() -> None:
    """Undo the last commit."""
    from mbcore.import_utils import smart_import

    undo_commit = smart_import("mbpy.git.git.undo_last_commit")
    try:
        await undo_commit()
    except Exception:
        import traceback

        traceback.print_exc()


@cli.command("publish", no_args_is_help=True)
@click.option("--bump",
              "-b",
              is_flag=True,
              help="Bump the version before publishing")
@click.option("--build",
              "-B",
              is_flag=True,
              help="Build the package before publishing")
@click.option(
    "--package-manager",
    "-p",
    type=click.Choice([
        "gh",
        "hatch",
        "uv",
        "nix",
    ], ),
    default="github",
    help="Package manager to use",
)
@click.option(
    "--auth",
    "-a",
    help=
    "PyPI or GitHub authentication token. Defaults to PYPI_TOKEN or GIT_TOKEN environment variable.",
)
@click.rich_config(get_help_config())
@click.option("-G",
              "--gh-release",
              is_flag=True,
              help="Create a GitHub release")
@base_args
async def publish_command(
    bump=False,
    build=False,
    package_manager: "Literal['gh', 'hatch', 'uv']" = "gh",
    auth=None,
    gh_release=False,
    **kwargs,
) -> None:
    r"""Publish a package to PyPI or GitHub.

    Note: Git features require the GitHub CLI to be installed. See https://cli.github.com/ for more information.
    """
    from datetime import datetime

    from mbcore.display import safe_print

    from mbpy.cmd import arun
    from mbpy.pkg.bump import bump as bump_pkg

    today = datetime.today
    import os

    from rich.text import Text

    if not await arun("which gh", show=False) and (package_manager == "github"
                                                   or gh_release):
        platform_install_cmd = ("`brew install gh`" if arun("which brew") else
                                "`sudo snap install gh --classic`")
        safe_print(
            f"GitHub CLI not found. Please install it to use this feature by running {platform_install_cmd}.",
            style="bold red",
        )
        return
    if not auth:
        auth = (os.getenv("GIT_TOKEN", os.getenv("GITHUB_TOKEN", None))
                if package_manager == "github" else os.getenv("PYPI_TOKEN"))
    if auth is None:
        safe_print(
            "No authentication token found. Please provide one with the --auth flag or set `GIT_TOKEN` or `PYPI_TOKEN` environment variables.",
            style="bold red",
        )
        return
    version = None

    try:
        if bump:
            version = await bump_pkg()
        out = []
        if build:
            await _clean_command(all=True)
            await _build_command(package_manager=package_manager)
        if package_manager in ("gh", "github"):
            from mbpy.git.changelog import generate_changelog
            from mbpy.git.check import resolve_state

            gc = await generate_changelog()
            out.append(await resolve_state(version,
                                           "push",
                                           args=["--changelog", gc]))
            outs = ""
            for o in out:
                outs += getattr(o, "commit_msg", getattr(o, "msg", o)) or ""
                if "error" in outs.lower():
                    from mbcore.log import error

                    error("Error occurred while creating release: " + o)

            out = [outs] or ["Pull request created successfully."]
        elif package_manager == "uv":
            if not await arun("which twine"):
                safe_print(
                    "Twine is not installed. Installing...",
                    style="bold light_goldenrod2",
                )
                await arun("pip install twine", show=True)
            out.append(await arun(
                ["twine", "upload", "'dist/*'", "-u", "__token__", "-p", auth],
                show=False,
            ))
            safe_print(Text.from_ansi(out))
        elif package_manager == "hatch":
            out.append(
                await arun(["hatch", "publish", "-u", "__token__", "-a", auth],
                           show=True))
        else:
            safe_print("Invalid package manager specified.", style="bold red")

        if "error" in out[-1].lower():
            safe_print("Error occurred while publishing package.",
                       style="bold red")
        else:
            safe_print(
                f"Package published successfully with {('version ' + version) if version else 'current version.'}",
                style="bold light_goldenrod2",
            )

        if gh_release:
            out = await arun(
                [
                    "gh",
                    "release",
                    "create",
                    version or f"{today().strftime('%d-%m-%Y')}",
                ],
                show=True,
            )
        if "error" in out[-1].lower():
            safe_print("Error occurred while creating release.",
                       style="bold red")
        else:
            safe_print(
                f"Release created successfully for version {version}.",
                style="bold light_goldenrod2",
            )

    except Exception:
        import traceback

        traceback.print_exc()


@cli.command("help", no_args_is_help=True)
@click.argument("command", default=None, required=False)
async def help_command(command) -> None:
    """Display help for a command."""
    from mbcore.display import safe_print
    from mbcore.import_utils import smart_import

    arun = smart_import("mbpy.cmd.arun")
    await arun(f"python -m pydoc {command}", show=True)
    command = smart_import(f"{command}")
    from pydoc import getdoc

    safe_print(getdoc(command))
    from pyclbr import readmodule_ex

    safe_print(readmodule_ex("mbpy"))


@cli.command("remove", no_args_is_help=True)
@click.argument("packages", nargs=-1)
@click.option("--dev", is_flag=True, help="Remove as a development dependency")
@click.option("--env",
              default=None,
              help="Specify the python, hatch, conda, or mbnix environment")
@click.option("-g",
              "--group",
              default=None,
              help="Specify the dependency group to use")
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging")
@click.pass_context
async def remove_command(ctx, packages, dev, env, group, debug) -> None:
    """Remove a package from the project using uv or pip."""
    if dev and group:
        if group != "dev":
            msg = "Cannot specify both --dev and --group"
            raise click.UsageError(msg)
        group = None

    return await _uninstall_command(packages, env, group, debug=debug, ctx=ctx)


remove_command.allow_extra_args = True


@cli.command("run",
             no_args_is_help=True,
             context_settings={"ignore_unknown_options": True})
@click.argument("command", nargs=-1)
@click.option(
    "-a",
    "--auto/--no-auto",
    is_flag=True,
    default=True,
    help="Auto repair broken imports",
)
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging")
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose logging")
@click.option("-t", "--timed", is_flag=True, help="Time the command")
@click.pass_context
async def run_cli_command(
    ctx: click.RichContext,
    command: list[str],
    auto: bool = True,
    debug: bool = False,
    verbose: bool = False,
    timed: bool = False,
    *args,
) -> None:
    from time import time

    from mbcore.display import safe_print

    from mbpy.cmd import arun
    from mbpy.env import getexecutable
    from mbpy.helpers.autopip import async_autorun

    command = list(command) or sys.argv[1:]
    if any(c.endswith("py") for c in command) and not any(
            c.startswith("python") for c in command):
        command = ([getexecutable()] + list(command)
                   if not isinstance(command, str) else command.split())
    try:
        tic = time()
        if auto:
            from mbpy.helpers.autopip import async_autorun

            await async_autorun(command, max_retries=3)
        else:
            from mbpy.cmd import arun

            await arun(command, show=True)
    except Exception:
        import traceback

        traceback.print_exc()
    finally:
        if timed:
            toc = time()
            safe_print(f"Command executed in {toc - tic:.2f} seconds.")


@cli.command("add", no_args_is_help=True)
@base_args
@click.argument("packages", nargs=-1, required=False)
@click.option("-e",
              "--editable",
              is_flag=True,
              help="Add as an optional dependency")
@click.option("-g",
              "--group",
              default=None,
              help="Specify the dependency group to use")
@click.option("-U", "--upgrade", is_flag=True, help="Upgrade the package(s)")
@click.option(
    "-r",
    "--requirements",
    type=click.Path(exists=True),
    help="Requirements file to install packages from",
)
@click.option(
    "-b",
    "--broken",
    type=click.Choice(["skip", "ask", "repair"]),
    default="skip",
    help="Behavior for broken packages",
)
@click.option("-D",
              "--dev",
              is_flag=True,
              help="Add as a development dependency")
@click.option("-G", "--github", is_flag=True, help="Install from GitHub")
@click.option("--no-deps",
              is_flag=True,
              help="Don't install package dependencies")
@click.pass_context
async def add_command(
    ctx,
    packages: list[str] | None = None,
    editable: bool = False,
    group: str | None = None,
    upgrade: bool = False,
    requirements: str | None = None,
    broken: "Literal['skip', 'ask', 'repair']" = "ask",
    dev: bool = False,
    github: bool = False,
    no_deps=False,
    **_kwargs,
) -> None:
    """Add packages as dependencies and update requirements.txt and pyproject.toml.

    Args:
        packages: Packages to add as dependencies.
        editable: Add as an editable dependency.
        group: Dependency group to use.
        upgrade: Upgrade the package if already installed.
        requirements: Requirements file to install from.
        broken: Behavior for broken packages.
        dev: Add as a development dependency.
        github: Install from GitHub.
        no_deps: Don't install package dependencies.

    Examples:
        # Add a regular package
        mb add package_name

        # Add a package with version constraint
        mb add "package_name>=1.0.0"

        # Add a package in editable mode
        mb add -e /path/to/local/package

        # Add from GitHub repository
        mb add -G org/repo

        # Add git repository with specific branch
        mb add "git+https://github.com/org/repo.git@branch"

        # Add package with specific extras
        mb add "package_name[extra1,extra2]"

        # Add as development dependency
        mb add -D package_name
    """
    group = group or ("dev" if dev else None)
    arglist = [a for a in ctx.args if a not in ("-d", "-vv")]
    if no_deps and "--no-deps" not in arglist:
        arglist.append("--no-deps")
    async for _ in install_pip(
            packages=packages or [],
            requirements=requirements,
            upgrade=upgrade,
            editable=editable,
            group=group or "dev" if dev else "dependencies",
            broken=broken,
            github=github,
            args=arglist,
    ):
        pass


add_command.allow_extra_args = True


def clean_cython(path: "Path | str") -> bool:
    from pathlib import Path
    from itertools import chain

    from mbcore.display import safe_print

    rm = False
    path = Path(str(path)).resolve()
    c_files = path.rglob("**/*.c")
    cpp_files = path.rglob("**/*.cpp")
    for cfile in chain.from_iterable([c_files, cpp_files]):
        c_file = str(cfile)
        py_file = cfile.with_suffix(".py")
        pyxd_file = cfile.with_suffix(".pyxd")
        pyx_file = cfile.with_suffix(".pyx")
        cf = Path(str(c_file)).relative_to(path)
        if py_file.exists() or pyxd_file.exists() or pyx_file.exists():
            try:
                cfile.unlink()
                safe_print(f"Removed: {cf}")
                rm = True
            except OSError as e:
                safe_print(f"Error removing {cf}: {e}")
                return False
    return rm


async def _clean_command(
    path: "str | Path" = ".",
    env: str | None = None,
    all: bool = False,
    logs=False,
    force=False,
    cython=False,
    patterns: list[str] | None = None,
    **_kwargs,
) -> None:
    """Remove build artifacts and optionally, generated c,cpp,so files."""
    from mbcore.display import prompt_ask, safe_print
    from mbcore.import_utils import smart_import
    from mbcore.log import debug

    arun = smart_import("mbpy.cmd.arun")
    files = smart_import("importlib.resources.files")
    logs = "-p '*.log'" if logs else ""
    force_clean = "-f" if force else ""
    if cython:
        clean_cython(path)

    try:
        clean_script = files("mbpy") / "scripts" / "clean.sh"
        cmd = f"bash {clean_script} {force_clean} {env or ''} {'--all' if all else ''} {logs}"

        if patterns:
            cmd += " ".join([f"-p {p}" for p in patterns])

        cmd += f" {str(path)}"
        if debug():
            cmd += " --dry-run"

        out = await arun(cmd, show=True)
        if (debug() and prompt_ask(
                "Clean project?", choices=["y", "n"], default="y") == "y"):
            out = await arun(cmd.replace("--dry-run", ""), show=True)
            safe_print(out)

    except Exception as e:
        if debug():
            import traceback

            traceback.print_exc()
        else:
            safe_print(f"Error: Failed to clean project: {str(e)}",
                       style="bold red")


@cli.command("clean")
@base_args
@click.argument("path", default=".", required=False)
@click.option("-a", "--all", is_flag=True, help="Clean all files")
@click.option("-l", "--logs", is_flag=True, help="Clean log files")
@click.option("-c",
              "--cython_compiled",
              is_flag=True,
              help="Clean Cython compiled files")
@click.option("-f", "--force", is_flag=True, help="Force clean")
@click.option("-p", "--patterns", multiple=True, help="Patterns to clean")
async def clean_command(
    path: str,
    all: bool = False,
    logs=False,
    cython_compiled=False,
    force=False,
    patterns=None,
    **_kwargs,
) -> None:
    """Remove build artifacts and optionally, logs and generated c,cpp,so files.

    Args:
        path (str): Path to clean
        all (bool): Clean all files
        logs (bool): Clean log files
        force (bool): Force clean
        cython_compiled (bool): Clean Cython compiled files
        patterns (list): Patterns to clean (using find pattern **not glob pattern**)

    """
    return await _clean_command(
        path=path,
        all=all,
        logs=logs,
        force=force,
        cython_compiled=cython_compiled,
        patterns=patterns,
    )


@cli.command("docs", no_args_is_help=True)
@base_args
@click.argument("name", type=str)
@click.argument("author", type=str)
@click.argument("kind",
                type=click.Choice(["sphinx", "mkdocs"]),
                default="sphinx")
@click.option("--theme", default="furo", help="Documentation theme to use")
async def docs_command(name: str,
                       author: str,
                       kind: str = "sphinx",
                       theme: str = "furo") -> None:
    """Generate documentation for a project."""
    # Import locally to avoid circular imports
    from mbpy.create import setup_documentation
    from mbpy.pkg.toml import afind_toml

    # Find project root using the toml file location
    project_root = (await afind_toml()).parent
    readme = project_root / "README.md"
    description = readme.read_text() if readme.exists() else ""

    await setup_documentation(
        project_name=name,
        author=author,
        description=description,
        autodoc=kind,
        theme=theme,
        project_root=project_root,
    )


@cli.command("repair", no_args_is_help=True)
@click.argument("path", default=".")
@click.option("-d", "--dry-run", is_flag=True, help="Dry run")
async def repair_command(path, dry_run) -> None:
    """Repair broken imports."""
    from mbcore.import_utils import smart_import

    traceback = smart_import("traceback")
    repair_main = smart_import("mbpy.pkg.repair.main", debug=True)
    try:
        await repair_main(path, dry_run)
    except Exception:
        import traceback

        traceback.print_exc()


# from mbcore.main import log as log_command  # noqa: E402

from mbcore.main import cache as cache_command  # noqa: E402
from mbcore.main import log as log_command  # noqa: E402

from mbpy.cmd import arun  # noqa: E402
from mbpy.git.gcliff import main as git  # noqa: E402
from mbpy.pkg.graph import generate, who_imports  # noqa: E402
from mbpy.pkg.mpip import sync  # noqa: E402
from mbpy.tools.tempcat import main as tempcat  # noqa: E402
from mbpy.tools.google import google, google_cli as google_command
from mbpy.tools.diff import main as diff_command  # noqa: E402
from mbpy.tools.search import search_repos as search_repos_command  # noqa: E402
from mbpy.tools.ns import main as ns_command  # no
from mbpy.tools.ns import whoami_command as whoami_command  # no

# from mbcore.even._internal.diff import main as diff_command  # noqa: E402
cli.add_command(who_imports, name="who-imports")
cli.add_command(generate, name="graph")
cli.add_command(git, name="git")
cli.add_command(sync, name="sync")
cli.add_command(tempcat, name="tempcat")
cli.add_command(log_command, name="log")
cli.add_command(cache_command, name="cache")
cli.add_command(info_command, name="info")
cli.add_command(diff_command, name="diff")
cli.add_command(search_repos_command, name="search_repos")
cli.add_command(ns_command, name="login")
cli.add_command(whoami_command, name="whoami")
cli.add_command(google_command, name="google")

# cli.add_command(diff_command, name="diff")
# cli.no_args_is_help = True
from pathlib import Path  # noqa: E402

from mbpy.git.gcliff import main as git  # noqa: E402
from mbpy.pkg.toml import findall_toml as _findall_toml  # noqa: E402


def findall_toml():
    if not Path("pyproject.toml").exists() and not Path("mb.toml").exists():
        _findall_toml()


findall_toml()


@cli.command("parse", no_args_is_help=True)
@click.argument("dependency", required=False)
@click.option("-f",
              "--file",
              type=click.Path(exists=True),
              help="Parse dependencies from a file")
@click.option("--json", is_flag=True, help="Output in JSON format")
@click.option("-t",
              "--type",
              type=click.Choice(["list", "deps", "set"]),
              default="list",
              help="Output format type")
@click.option("--online",
              is_flag=True,
              help="Use the online parser for hierarchical text parsing")
@click.pass_context
async def parse_command(ctx,
                        dependency=None,
                        file=None,
                        json=False,
                        type="list",
                        online=False):
    """Parse dependency strings in various formats.
    
    Parses a single dependency string or a file containing multiple dependencies.
    
    Examples:
        # Parse a single dependency string
        mb parse "pandas[excel,parquet]>=1.0.0"
        
        # Parse dependencies from a requirements file
        mb parse -f requirements.txt
        
        # Parse a GitHub repo reference
        mb parse "org/repo"
        
        # Parse a git URL with branch
        mb parse "git+https://github.com/org/repo.git@branch"
        
        # Parse hierarchical text using the online parser
        mb parse -f document.txt --online
    """
    from mbpy.pkg.dependency import Dependency
    from mbpy.pkg.requirements import aget_requirements_packages
    from mbcore.traverse import has_error
    from mbcore.display import safe_print
    import json as json_lib

    # If online flag is set, use the text hierarchy parser
    if online:
        if file:
            from mbpy.parse.online import build_text_hierarchy, tree_nodes
            from io import StringIO

            try:
                with open(file, "r") as f:
                    content = f.read()
                    hierarchy = build_text_hierarchy(StringIO(content))

                if json:
                    # Convert hierarchy to a simpler format for JSON
                    result = []
                    for node in hierarchy:
                        node_dict = {
                            "tag": node["tag"].value,
                            "content": node["content"],
                            "children": [
                            ]  # simplified, would need recursion for full tree
                        }
                        result.append(node_dict)
                    safe_print(json_lib.dumps(result, indent=2))
                else:
                    # Display the hierarchical structure
                    safe_print("Text Hierarchy:")
                    nodes = list(tree_nodes(hierarchy))
                    for i, node in enumerate(nodes):
                        if isinstance(node, dict):
                            content = " ".join(node["content"])
                            tag = node["tag"].value if hasattr(
                                node["tag"], "value") else str(node["tag"])
                            safe_print(
                                f"Node {i+1} [{tag}]: {content[:50]}{'...' if len(content) > 50 else ''}"
                            )
                        else:
                            safe_print(f"Item {i+1}: {node}")
            except Exception as e:
                safe_print(f"Error parsing file with online parser: {str(e)}",
                           style="bold red")
            return
        else:
            safe_print("Please provide a file to parse with the online parser",
                       style="bold red")
            return

    # Regular dependency parsing
    result = None

    if dependency:
        # Parse a single dependency
        dep = Dependency(dependency)
        if json:
            output = {
                "name": dep.name,
                "base": dep.base,
                "editable": dep.editable,
                "git": dep.git,
                "extras": dep.extras,
                "version": dep.version,
            }
            if hasattr(dep, "org"):
                output["org"] = dep.org
            if hasattr(dep, "repo"):
                output["repo"] = dep.repo
            if hasattr(dep, "git_ref") and dep.git_ref:
                output["git_ref"] = dep.git_ref
            safe_print(json_lib.dumps(output, indent=2))
        else:
            safe_print(f"Dependency: {dep}")
            safe_print(f"Base name: {dep.base}")
            if dep.extras:
                safe_print(f"Extras: {dep.extras}")
            if dep.version:
                safe_print(f"Version: {dep.version}")
            if dep.editable:
                safe_print(f"Editable: {dep.editable}")
            if dep.git:
                safe_print(f"Git: {dep.git}")
                if hasattr(dep, "org") and dep.org:
                    safe_print(f"Organization: {dep.org}")
                if hasattr(dep, "repo") and dep.repo:
                    safe_print(f"Repository: {dep.repo}")
                if hasattr(dep, "git_ref") and dep.git_ref:
                    safe_print(f"Git ref: {dep.git_ref}")
    elif file:
        # Parse dependencies from a file
        result = await aget_requirements_packages(type, file)
        if has_error(result):
            safe_print(f"Error: {result.error}", style="bold red")
            return

        deps_list = result.result

        if json:
            if type == "deps":
                # Convert Dependency objects to dicts
                output = []
                for dep in deps_list:
                    dep_dict = {
                        "name": dep.name,
                        "base": dep.base,
                        "editable": dep.editable,
                        "git": dep.git,
                        "extras": dep.extras,
                        "version": dep.version
                    }
                    if hasattr(dep, "org") and dep.org:
                        dep_dict["org"] = dep.org
                    if hasattr(dep, "repo") and dep.repo:
                        dep_dict["repo"] = dep.repo
                    if hasattr(dep, "git_ref") and dep.git_ref:
                        dep_dict["git_ref"] = dep.git_ref
                    output.append(dep_dict)
                safe_print(json_lib.dumps(output, indent=2))
            else:
                # For list and set types, just output the strings
                safe_print(json_lib.dumps(list(deps_list), indent=2))
        else:
            if type == "deps":
                for idx, dep in enumerate(deps_list):
                    safe_print(f"Dependency {idx+1}: {dep}")
                    safe_print(f"  Base name: {dep.base}")
                    if dep.extras:
                        safe_print(f"  Extras: {dep.extras}")
                    if dep.version:
                        safe_print(f"  Version: {dep.version}")
                    if dep.editable:
                        safe_print(f"  Editable: {dep.editable}")
                    if dep.git:
                        safe_print(f"  Git: {dep.git}")
                        if hasattr(dep, "org") and dep.org:
                            safe_print(f"  Organization: {dep.org}")
                        if hasattr(dep, "repo") and dep.repo:
                            safe_print(f"  Repository: {dep.repo}")
                        if hasattr(dep, "git_ref") and dep.git_ref:
                            safe_print(f"  Git ref: {dep.git_ref}")
                    safe_print("")
            else:
                # For list and set types, format nicely
                if type == "list":
                    safe_print("Dependencies:")
                    for idx, dep in enumerate(deps_list):
                        safe_print(f"  {idx+1}. {dep}")
                else:  # set
                    safe_print("Unique dependencies:")
                    for idx, dep in enumerate(deps_list):
                        safe_print(f"  - {dep}")
    else:
        safe_print(
            "Please provide either a dependency string or a file to parse.")


def main():
    # Check for shell completion request
    if "_MB_COMPLETE" in os.environ:
        from mbpy.helpers.completion import shell_complete

        sys.exit(shell_complete(cli, {}, "mb", "_MB_COMPLETE"))

    try:
        import uvloop

        uvloop.install()
    except ImportError:
        pass

    cli(prog_name="mb")


if __name__ == "__main__":
    main()
