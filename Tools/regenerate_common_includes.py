#!/usr/bin/env python3
"""
Regenerate hashed utility headers in ``Cython/Common/Include``.

This drives Cython with ``common_utility_include_dir`` pointing at the target
directory so that utility fragments get written as ``*_impl_<hash>.h`` /
``*_proto_<hash>.h`` files. The script only runs Cython code generation; it
does not compile the resulting C files.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

from Cython.Build import cythonize
from Cython.Compiler import Options as CythonOptions

DEFAULT_BUILD_DIR = Path("generated/common_include_build")
DEFAULT_MODULES = [
    # Core runtime helpers.
    "Cython/Runtime/refnanny.pyx",
    # Parser/lexer utilities that touch many builtins and slots.
    "Cython/Plex/Actions.pyx",
    "Cython/Plex/Scanners.pyx",
    # Fastcall / keyword-only coverage.
    "tests/run/fastargs_kwonly.pyx",
    # TypeName / base validation coverage.
    "tests/run/cpdef_closure.pyx",
]


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Regenerate hashed headers in Cython/Common/Include "
        "via common_utility_include_dir."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(CythonOptions.CYTHON_COMMON_UTILITY_INCLUDE_DIR),
        help="Destination for generated utility headers "
        "(default: Cython/Common/Include)",
    )
    parser.add_argument(
        "--build-dir",
        type=Path,
        default=DEFAULT_BUILD_DIR,
        help="Where to place generated .c/.cpp files (default: %(default)s)",
    )
    parser.add_argument(
        "--module",
        dest="modules",
        action="append",
        help="Module (.pyx/.py) to cythonize. "
        "May be given multiple times. "
        "If omitted, a curated default set is used.",
    )
    parser.add_argument(
        "--nthreads",
        type=int,
        default=0,
        help="Parallel cythonization threads (0 = auto, default: 0)",
    )
    parser.add_argument(
        "--clean-output",
        action="store_true",
        help="Remove the output directory before regenerating.",
    )
    parser.add_argument(
        "--clean-build",
        action="store_true",
        help="Remove the build directory before regenerating.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    modules = args.modules or DEFAULT_MODULES

    if args.clean_output and args.output_dir.exists():
        shutil.rmtree(args.output_dir)
    if args.clean_build and args.build_dir.exists():
        shutil.rmtree(args.build_dir)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.build_dir.mkdir(parents=True, exist_ok=True)

    missing = [m for m in modules if not Path(m).exists()]
    if missing:
        sys.stderr.write(f"Missing modules: {', '.join(missing)}\n")
        return 1

    cythonize(
        modules,
        nthreads=args.nthreads,
        force=True,
        build_dir=str(args.build_dir),
        exclude_failures=False,
        compiler_directives={"language_level": 3},
        common_utility_include_dir=str(args.output_dir),
    )

    print("Utility headers regenerated in", args.output_dir)
    print("Generated C sources are in", args.build_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
