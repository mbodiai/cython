import re
import subprocess
import sys
import time
from asyncio import sleep
from pathlib import Path

from mbcore.display import safe_print
from mbpy.cmd import arun, run_command


def install_cmd(mod):
    if Path(mod).exists():
        return f"pip install -e {mod}/"

    return f"pip install {mod}"


def print(*args, **kwargs):
    """Print function that flushes the output."""
    safe_print(*args, **kwargs)


def autorun(command: list[str], max_retries=5, delay=1, enable_gpt=False):
    retries = 0
    modules_installed = set()
    command_stack = [" ".join(command)]
    print(f"command_stack: {command_stack}")
    while retries < max_retries and command_stack:
        current_command = command_stack.pop()
        try:
            if isinstance(current_command, list):
                raise ValueError("Command must be a string, not a list")
            result = ""
            for line in run_command(current_command, show=True, cwd=Path.cwd()):
                result += line
            if "No module named" in result:
                match = re.search(r"No module named ['\"]?(\S+)['\"]?", result)
                if match:
                    missing_module = match.group(1).split(".")[0]
                    if missing_module not in modules_installed:
                        try:
                            result = ""
                            for line in run_command(
                                install_cmd(missing_module.strip("'")),
                                show=True,
                                cwd=Path.cwd(),
                            ):
                                result += line
                            if "No module named" not in result:
                                modules_installed.add(missing_module)
                                command_stack.append(
                                    current_command
                                )  # Retry the original command
                                time.sleep(delay)
                        except subprocess.CalledProcessError:
                            retries += 1
                else:
                    print(f"Error: {result}")
                    return 1
        except subprocess.CalledProcessError as e:
            out = (e.stderr or "") + (e.stdout or "")
            match = re.search(r"No module named ['\"]?(\S+)['\"]?", out)
            if match:
                missing_module = match.group(1).split(".")[0]
                if missing_module not in modules_installed:
                    safe_print(f"Installing {missing_module}...")
                    result = ""
                    for line in run_command(install_cmd(missing_module.strip("'"))):
                        print(line)
                        result += line
                    if "No module named" not in result:
                        modules_installed.add(missing_module)
                        command_stack.append(current_command)
    return None


async def async_autorun(
    command: list[str] | str, max_retries=5, delay=2, enable_gpt=False
):
    retries = 0
    modules_installed = set()
    import shlex

    command = (
        command
        if isinstance(command, list)
        else shlex.split(command if isinstance(command, str) else " ".join(command))
    )
    command_stack = [" ".join(command)]
    while retries < max_retries and command_stack:
        current_command = command_stack.pop()
        try:
            if isinstance(current_command, list):
                raise ValueError("Command must be a string, not a list")
            result = await arun(current_command, cwd=Path.cwd())
            print(result)
            if "No module named" in result:
                match = re.search(r"No module named ['\"]?(\S+)['\"]?", result)
                if match:
                    missing_module = match.group(1).split(".")[0]
                    if missing_module not in modules_installed:
                        try:
                            print(f"Installing {missing_module}...")
                            result = await arun(
                                install_cmd(missing_module.strip("'")),
                                show=True,
                                cwd=Path.cwd(),
                            )
                            print(result)
                            if "No module named" not in result:
                                modules_installed.add(missing_module)
                                command_stack.append(
                                    current_command
                                )  # Retry the original command
                                await sleep(delay)
                        except subprocess.CalledProcessError:
                            retries += 1
                else:
                    print(f"Error: {result}")
                    return 1

        except subprocess.CalledProcessError as e:
            out = (e.stderr or "") + (e.stdout or "")
            match = re.search(r"No module named ['\"]?(\S+)['\"]?", out)

            if match:
                missing_module = match.group(1).split(".")[0]
                if missing_module not in modules_installed:
                    print(f"Installing {missing_module}...")
                    result = await arun(
                        install_cmd(missing_module.strip("'")),
                        show=True,
                        cwd=Path.cwd(),
                    )
                    if "No module named" not in result:
                        modules_installed.add(missing_module)
                        command_stack.append(
                            current_command
                        )  # Retry the original command
                        time.sleep(delay)
                    else:
                        retries += 1
            else:
                print(f"Error: {out}")
                return e.returncode

    return 1


if __name__ == "__main__":
    import asyncio

    if len(sys.argv) < 2:
        print("Usage: python3 auto_pip_install.py <command> [args...]")
        sys.exit(1)

    # Extract the command and its arguments from the script arguments
    command = sys.argv[1:]
    exit_code = asyncio.run(async_autorun(command))
    sys.exit(exit_code)
