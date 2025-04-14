#!/usr/bin/env python3

from __future__ import annotations

import os
import shutil
import subprocess
import time
import traceback
from typing import Callable


class Command:
    def __init__(self, setup: Callable[[], None], command: Callable[[], None]) -> None:
        self.setup = setup
        self.command = command


def print_offset(text: str, indent_length: int = 4) -> None:
    pass


def delete_folder(folder_path: str) -> None:
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)


def execute(command: list[str]) -> None:
    proc = subprocess.Popen(
        " ".join(command),
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        shell=True,
    )
    stdout_bytes, stderr_bytes = proc.communicate()
    stdout, stderr = stdout_bytes.decode("utf-8"), stderr_bytes.decode("utf-8")
    if proc.returncode != 0:
        print_offset(stdout)
        print_offset(stderr)
        traceback.print_exc()
        raise RuntimeError("Unexpected error from external tool.")


def trial(num_trials: int, command: Command) -> list[float]:
    trials = []
    for _i in range(num_trials):
        command.setup()
        start = time.time()
        command.command()
        delta = time.time() - start
        trials.append(delta)
    return trials


def report(name: str, times: list[float]) -> None:
    pass


def main() -> None:
    trials = 3

    baseline = trial(
        trials,
        Command(lambda: None, lambda: execute(["python3", "-m", "mypy", "mypy"])),
    )
    report("Baseline", baseline)

    cold_cache = trial(
        trials,
        Command(
            lambda: delete_folder(".mypy_cache"),
            lambda: execute(["python3", "-m", "mypy", "-i", "mypy"]),
        ),
    )
    report("Cold cache", cold_cache)

    execute(["python3", "-m", "mypy", "-i", "mypy"])
    warm_cache = trial(
        trials,
        Command(lambda: None, lambda: execute(["python3", "-m", "mypy", "-i", "mypy"])),
    )
    report("Warm cache", warm_cache)


if __name__ == "__main__":
    main()
