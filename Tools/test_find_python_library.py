from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from Cython.Build import BuildExecutable as build_exec_mod
from Cython.Compiler import build_executable as compiler_build_exec_mod


def _run_builder(module, tmpdir: Path, tag: str) -> None:
    """Build and run a tiny script using the given build_executable module."""
    print(f"=== {tag} ===")

    finder = getattr(module, "find_python_library", None)
    lib = finder() if callable(finder) else None
    print(f"{tag}: find_python_library() -> {lib!r}")

    script = tmpdir / f"hello_{tag.replace('.', '_')}.py"
    script.write_text(
        "import sys\n"
        "print('hello from', %r, 'on', sys.version.split()[0])\n"
        % tag,
        encoding="utf-8",
    )

    exe = module.build(str(script), compiler_args=(), force=True)
    print(f"{tag}: built executable {exe!r}")

    proc = subprocess.run(
        [exe],
        text=True,
        capture_output=True,
        check=False,
    )
    print(f"{tag}: returncode={proc.returncode}")
    print(f"{tag}: stdout:\n{proc.stdout}")
    print(f"{tag}: stderr:\n{proc.stderr}", file=sys.stderr)
    proc.check_returncode()


def main(argv: list[str] | None = None) -> int:
    """Compare the behaviour of the two find_python_library implementations."""
    del argv  # currently unused

    with TemporaryDirectory() as td:
        tmpdir = Path(td)
        _run_builder(
            compiler_build_exec_mod,
            tmpdir,
            "Cython.Compiler.build_executable",
        )
        _run_builder(
            build_exec_mod,
            tmpdir,
            "Cython.Build.BuildExecutable",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



