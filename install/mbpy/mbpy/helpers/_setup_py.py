import atexit
import shlex
import traceback
from pathlib import Path
from subprocess import run
from typing import TYPE_CHECKING, Generator


from mbcore.display import getspinner, safe_print
from typing_extensions import Literal

from mbpy.cli import check_install_prompt
from mbpy.env import getexecutable, load_toml
from mbpy.helpers._show import ainstalled_packages

if not TYPE_CHECKING:
    try:
        from Cython.Compiler.Options import default_options
        from Cython.Build import cythonize as cythonize_cmd
    except ImportError:
        cythonize_cmd = None
        default_options = None

if TYPE_CHECKING:
    from Cython.Build import cythonize as cythonize_cmd
    from Cython.Compiler.Errors import CompileError as CythonBuildError
    from Cython.Compiler.Main import CompilationResult
    from Cython.Compiler.Options import CompilationOptions
from mbcore import log
from mbcore.collect import getin
from mbcore.display import getconsole
from mbcore.log import warning
from rich.progress import BarColumn, Progress, TaskID, TextColumn


def create_progress():
    """Create a rich progress display with dynamic colors and fixed number of bars."""
    return Progress(
        # Overall progress at the top
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=50),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("{task.fields[status]}"),
        console=getconsole(),
        expand=False,
        refresh_per_second=15,
    )


def create_multi_progress():
    """Create a progress display that can show multiple bars."""
    return Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=50),
        "[progress.percentage]{task.percentage:>3.0f}%",
        console=getconsole(),
        expand=True,
        refresh_per_second=10,  # Increase refresh rate
        transient=False,
    )


def compile_cython_files(
    source_dir, install_dir, progress: Progress | None = None
) -> "Generator[TaskID,None,CompilationResult]":
    pyx_files: list[Path] = []
    for ext in ["pyx", "pxc", "py"]:
        pyx_files.extend(list(source_dir.rglob(f"**/*.{ext}")))
    if progress is not None:
        overall_task: TaskID = progress.add_task(
            "[bold cyan]Compiling...[/bold cyan]",
            total=len(pyx_files),
            status="",
        )
        yield overall_task
        print(f"Compiling {len(pyx_files)} files")
    package_name = getin("project.name", load_toml(cwd=source_dir).unwrap())
    extensions = list(
        filter(
            lambda x: Path(x).exists()
            and "site-packages" not in str(x)
            and package_name in str(Path(str(x)).resolve()),
            pyx_files,
        )
    )

    errs = []
    try:
        # Do compilation
        if not cythonize_cmd:
            raise ImportError("Cython not installed")
        if not extensions or not cythonize_cmd or not CompilationOptions:
            return None
        opts = CompilationOptions(
            include_path=[str(source_dir)],
            cplus=True,
            annotate=True,
            generate_pxi=True,
            output_dir=str(install_dir),
            working_path=package_name,
            create_extension=True,
            module_name=package_name,
        )
        errs = cythonize_cmd(
            module_list=[str(pyx_file) for pyx_file in extensions],
            progress=progress,
            compiler_directives=CompileDirectives(embed=True),
            quiet=False,
            output_dir=str(install_dir),
            exclude_failures=True,
            **opts,
        )
        for err in errs:
            yield err
            print(err)

    except CythonBuildError as e:
        if progress:
            progress.update(overall_task, status="fail")
        warning(f"Failed to compile Cython file: {e}")
        return errs

    except Exception:
        traceback.print_exc()


# async def gen_setup(
#     name: str,
#     path: str,
#     verbose: bool = False,
#     build: bool = False
# ) -> CompilationResult:
#     """Generate setup.py and compile Cython files."""
#     pkg_path = Path(path)
#     tmp_dir = pkg_path / "tmp" / name
#     console = getconsole()
#     progress = create_progress()


#     # Generate setup.py content
#     ext_modules = []
#     setup_content = f"""from setuptools import setup, find_namespace_packages
# from setuptools.extension import Extension
# from Cython.Build import cythonize
# import sys
# import platform

# ext_modules = {ext_modules}

# setup(
#     name='{name}',
#     packages=find_namespace_packages(include=['{name}*']),
#     package_dir={{'': '{git_ws.parent.relative_to(pkg_path)}'}},
#     ext_modules=ext_modules,
#     python_requires='>=3.7',
#     zip_safe=False
# )

# # Cleanup after build
# import atexit
# import shutil
# from pathlib import Path

# def cleanup():
#     try:
#         if Path('setup.py').exists():
#             Path('setup.py').unlink()
#         build_dir = Path('build')
#         if build_dir.exists():
#             shutil.rmtree(build_dir)
#     except Exception as e:
#         print(f'Cleanup failed: {{e}}')

# atexit.register(cleanup)
# """
#     compilation_result.setup_content = setup_content
#     return compilation_result


def gensetup(
    name,
    path,
    verbose=False,
    build=False,
    pyproject=None,
    progress=None,
    package_manager="pip",
    cythonize=True,
    install_dir="dist",
):
    pkg_path = Path(path)
    atexit.register(remove_setup, pkg_path)
    install_dir = (
        install_dir if Path(install_dir).is_absolute() else pkg_path / install_dir
    )
    getconsole()
    create_progress()

    # Generate setup.py content
    setup_content = """# setup.py
from setuptools import Extension, setup, find_packages  # Added find_packages
from Cython.Build import cythonize
import glob
from pathlib import Path
import os
import toml  # Added import for reading pyproject.toml

def get_package_name():
    pyproject_path = Path(__file__).parent / "pyproject.toml"
    if pyproject_path.exists():
        pyproject = toml.load(pyproject_path)
        return pyproject.get("project", {{}}).get("name", os.path.basename(os.path.dirname(__file__))) 
    else:
        return Path(__file__).parent.name  # Use directory name as package name

def find_pyx_modules():
    packages = find_packages()  # Dynamically find all packages
    extensions = []
    for package in packages:
        package_dir = package.replace('.', '/')
        for pyx_file in Path(package_dir).rglob("*.pyx"):
            module_name = f"{package}.{pyx_file.stem}"
            extensions.append(
                Extension(
                    module_name,
                    [str(pyx_file)],
                )
            )
    return extensions

extensions = cythonize(
    find_pyx_modules(),  # Removed hardcoded "mbpy/pkg"
    language_level=3,
)

setup(
    name=get_package_name(),  # Replaced hardcoded name with dynamic retrieval
    version="0.1.0",
    packages=find_packages(),  # Automatically find packages
    ext_modules=extensions,
)
"""
    setup_path = pkg_path / "setup.py"
    setup_path.write_text(setup_content)


from dataclasses import dataclass
from typing_extensions import Any


@dataclass
class BuildResults(dict):
    status: str
    message: str
    result: Any


async def managed_install_cmd(package_manager: Literal["pip", "hatch", "uv"]):
    package_manager = package_manager.lower().strip()
    if package_manager == "pip" and await check_install_prompt("build"):
        return "python -m build"
    if package_manager == "hatch" and await check_install_prompt("hatch"):
        return "python -m hatch build"
    if package_manager == "uv" and await check_install_prompt("uv"):
        return f"uv build --python={getexecutable()}"
    raise ValueError(f"Unsupported package manager: {package_manager}")


async def setup_command(
    path, pyproject=None, progress=None, package_manager="pip", cythonize=True
) -> BuildResults:
    try:
        print("Setting up..." + " " + str(package_manager) + " " + str(cythonize))
        path = Path(str(path))
        git_pkgs = list(filter(lambda x: x.git, await ainstalled_packages()))
        if git_pkgs:
            print(f"Found {len(git_pkgs)} : {git_pkgs}")
        else:
            print("No git packages found")
        if cythonize and not cythonize_cmd:
            safe_print(
                "\n\n[bold yellow] Warning: [/bold yellow] Cython not installed.\n Install cython with [bold cyan] `pip install cython` for c-speed. [/bold cyan]\n \n"
            )

            return BuildResults("failed", "Cython not installed", None)
        if not cythonize:
            (path / "dist").mkdir(exist_ok=True)
            if await check_install_prompt("wheel", python=True):
                cmd = f"{await managed_install_cmd(package_manager)} --outdir {path / 'dist'} --no-isolation --wheel"
                safe_print("Installing wheel...")
                getspinner().start()
                out = run(
                    shlex.split(cmd),
                    cwd=path,
                    executable=getexecutable(),
                    capture_output=True,
                )
                getspinner().stop()
            status = (
                "installed"
                if "Successfully built" in (out.stdout + out.stderr).decode()
                else "failed"
            )

            return BuildResults(status, out.stderr, None)
        progress = progress or create_multi_progress()
        with progress:
            hasfail = False
            # Build config phase
            tmp_dir = path / "install" / path.stem
            tmp_dir.mkdir(parents=True, exist_ok=True)
            # Compilation phase
            for tid in compile_cython_files(
                path, install_dir=tmp_dir, progress=progress
            ):
                if progress.tasks[tid].fields.get("status") == "fail":
                    progress.update(tid, visible=True)
                else:
                    safe_print(tid)
                    hasfail = True
            progress.stop()
            if hasfail:
                return BuildResults("failed", "Cython compilation failed", None)

            return BuildResults("succeeded", "", None)

    except Exception as e:
        if progress:
            progress.stop()
        if log.debug():
            traceback.print_exc()

        return BuildResults("failed", str(e), None)


def remove_setup(path):
    path = Path(str(path))
    setup_path = path
    if setup_path.exists():
        setup_path.unlink()
