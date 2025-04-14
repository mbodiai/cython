import os
import platform
import shutil
import subprocess
import sys

from mbcore.display import safe_print
import rich_click as click


@click.command()
@click.option(
    "--python-versions",
    default="cp310-* cp311-* cp312-*",
    help="Python versions to build for",
)
@click.option("--output-dir", default="dist", help="Output directory for built wheels")
@click.option("--upload", is_flag=True, help="Upload to PyPI after building")
def build_wheels(python_versions, output_dir, upload) -> None:
    """Builds wheels using cibuildwheel for the detected OS and architecture."""
    system = platform.system()
    arch = platform.machine().lower()

    # Map platform.machine() to cibuildwheel-friendly architectures
    arch_map = {
        "x86_64": "x86_64",
        "amd64": "AMD64",
        "arm64": "arm64",
        "aarch64": "aarch64",
    }

    cibw_arch = arch_map.get(arch)
    if not cibw_arch:
        safe_print(f"[red]Unsupported architecture: {arch}[/red]")
        sys.exit(1)

    # Define architectures per OS
    if system == "Linux":
        cibw_archs = (
            "x86_64 aarch64" if cibw_arch in ["x86_64", "aarch64"] else cibw_arch
        )
    elif system == "Darwin":
        cibw_archs = "x86_64 arm64"
    elif system == "Windows":
        cibw_archs = "AMD64 ARM64"
    else:
        safe_print(f"[red]Unsupported system: {system}[/red]")
        sys.exit(1)

    safe_print(f"[green]Building for {system} ({cibw_archs})[/green]")

    # Set environment variables
    os.environ.update(
        {
            "CIBW_ARCHS": cibw_archs,
            "CIBW_BUILD": python_versions,
            "CFLAGS": "-O3 -march=native -flto",
            "LDFLAGS": "-flto",
        }
    )

    try:
        subprocess.run(["cibuildwheel", "--output-dir", output_dir], check=True)
    except subprocess.CalledProcessError:
        safe_print("[red]Build failed[/red]")
        sys.exit(1)

    # Post-processing
    if system == "Linux":
        if shutil.which("auditwheel"):
            subprocess.run(
                [
                    "find",
                    output_dir,
                    "-name",
                    "*.whl",
                    "-exec",
                    "auditwheel",
                    "show",
                    "{}",
                    ";",
                ],
                check=False,
            )
        else:
            safe_print("[yellow]auditwheel not found; skipping check[/yellow]")

    elif system == "Windows":
        if shutil.which("dumpbin"):
            subprocess.run(
                [
                    "powershell",
                    "-Command",
                    "Get-ChildItem",
                    output_dir,
                    "| ForEach-Object {dumpbin /HEADERS $_.FullName}",
                ],
                check=False,
            )
        else:
            safe_print("[yellow]dumpbin not found; skipping check[/yellow]")

    # Optional: Upload to PyPI
    if upload:
        if shutil.which("mb"):
            subprocess.run(["mb", "-p", "uv", "-B", "-b", "publish"], check=False)
        elif shutil.which("twine"):
            subprocess.run(["twine", "upload", f"{output_dir}/*"], check=False)
        else:
            safe_print("[red]Neither `mb` nor `twine` found. Cannot upload.[/red]")


if __name__ == "__main__":
    build_wheels()
