from __future__ import annotations

from dataclasses import dataclass
import os
import shutil
from collections.abc import Sequence
from pathlib import Path
from subprocess import run
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

from mbcore import log


class BuildScriptsHook(BuildHookInterface):
    PLUGIN_NAME = "build-scripts"

    def initialize(
        self,
        version: str,  # noqa: ARG002
        build_data: dict[str, Any],
    ) -> None:
        created: set[Path] = set()

        all_scripts = [
            BuildConfig(
                commands=["echo", "Hello, World!"],
                build_dir="build",
                install_dir="/usr/local/lib/mb/",
            )
        ]

        for script in all_scripts:
            if script.build_dir:
                out_dir = Path(self.root, script.build_dir)
                log.debug(f"Cleaning {out_dir}")
                shutil.rmtree(out_dir, ignore_errors=True)
            elif script.clean:
                for out_file in script.out_files(self.root):
                    log.debug(f"Cleaning {out_file}")
                    out_file.unlink(missing_ok=True)

        for script in all_scripts:
            log.debug(f"Script config: {asdict(script)}")
            work_dir = Path(self.root, script.work_dir)
            out_dir = Path(self.root, script.build_dir)
            out_dir.mkdir(parents=True, exist_ok=True)

            for cmd in script.commands:
                log.info(f"Running command: {cmd}")
                run(cmd, cwd=str(work_dir), check=True, shell=True)  # noqa: S602

            log.info(f"Copying artifacts to {out_dir}")
            for work_file in script.out_files():
                src_file = work_dir / work_file
                out_file = out_dir / work_file
                log.debug(f"Copying {src_file} to {out_file}")
                if src_file not in created:
                    out_file.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(src_file, out_file)
                    created.add(out_file)
                else:
                    log.debug(f"Skipping {src_file} - already exists")

            build_data["artifacts"].append(str(out_dir.relative_to(self.root)))


@dataclass
class BuildConfig:
    """A configuration for a single build script."""

    commands: Sequence[str]
    """The commands to run"""

    work_dir: str = "."
    """The directory to run the commands in"""

    build_dir: str = "build"
    """Git file patterns relative to the work_dir to save as build artifacts"""

    install_dir: str = "/usr/local/lib/mb/"
    """The path where build artifacts will be saved"""

    clean: bool = False
    """If true, clean the build directory before building"""

    prefix: str = "/usr/local/bin/mb"
    """The prefix to install the build artifacts to"""

    def __post_init__(self) -> None:
        self.install_dir = conv_path(self.install_dir)

    def out_files(self) -> Sequence[Path]:
        """Get files in the output directory that match the artifacts spec."""
        d = Path(self.build_dir)
        return list(d.glob("*")) if d.exists() else []


def conv_path(path: str) -> str:
    """Convert a unix path to a platform-specific path."""
    return path.replace("/", os.sep)
