import asyncio
import sys
from collections import defaultdict
from collections.abc import Callable, Coroutine, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import os
import time
import re
import shutil

import tomlkit
from tomlkit.items import Table, Array, String
from mbcore.log import debug, warning, verbose, info  # Ensure info is imported

from mbcore import ctx
from mbcore.types import wraps
from mbcore.display import confirm, getconsole, getspinner, prompt_ask, safe_print
from mbpy.cmd import run_command
from mbpy.git.state import (
    arun,
    get_git_status,
    git_print,
    GitState,
    get_git_state,
    get_branch,
    display_status_summary,
    haserr,
    withstate,
    GitStatus,
    GitContext,
    sync_get_branch,
    sync_get_repo_root,
)
from mbpy.git.changelog import brief_commit_message
from mbpy.helpers._cmd import P
from rich.console import Console
from rich.syntax import Syntax
from typing_extensions import Any, Literal, cast, ParamSpec, Optional
from mbpy.env import getws, getdevws  # Add getws if not already imported

P = ParamSpec("P")
if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from enum import Enum as StrEnum

# Global variable to track seen commit messages across function calls
# This prevents duplicate printing of the same message
_seen_commit_messages = set()


def parse_start_line(diff_text: str) -> int:
    lines = diff_text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("@@"):
            return i + 1
    return 0


async def display_git_diff(diff_text: str, branch=None, remote="origin") -> None:
    """Render Git diff with syntax highlighting using Rich."""
    # Get diff statistics
    lines = diff_text.splitlines()
    total_changes = len([l for l in lines if l.startswith("+") or l.startswith("-")])

    # If more than 50 changes, show summary stats instead of full diff
    if total_changes > 50:
        added = len([l for l in lines if l.startswith("+")])
        getspinner().stop()
        removed = len(
            [l for l in lines if l.startswith("-") and not l.startswith("---")]
        )
        branch = branch or await get_branch()
        remote = remote or "origin"
        getconsole().print(
            await arun(["git", "diff", "--stat", f"{branch}..{remote}/{branch}"])
        )
        getconsole().print(
            f"[yellow]Large diff detected: {added} additions, {removed} deletions. Consider breaking down your changes into smaller commits.[/yellow]"
        )
        return
    # For smaller diffs, show detailed view with syntax highlighting
    for line in lines:
        if line.startswith("+"):
            pass
        elif line.startswith("-") and not line.startswith("---"):
            pass
        else:
            pass
        syntax = Syntax(
            line,
            "diff",
            theme="monokai",
            dedent=True,
            line_numbers=True,
            start_line=parse_start_line(line),
        )
        getspinner().stop()
        getconsole().print(syntax, end="")


class Policy:
    """Policy for handling Git state.

    AHEAD -> PUSH
    BEHIND -> PULL
    DIVERGED -> RESOLVE
    ERROR -> QUIT
    NO_UPSTREAM -> SET_UPSTREAM
    UP_TO_DATE -> NOTHING
    """

    def __init__(self, branch: str | None = None, remote: str = "origin"):
        self.branch = branch
        self.remote = remote
        # Track attempts per branch to allow different branches to set upstream
        self.upstream_attempts = {}

    async def handle_msg(self, msg: str) -> "GitState":
        return await self.handle_state(GitState.from_msg(msg))

    async def handle_state(self, state: "GitState") -> "GitState":
        # Get the branch we're working with - either from state or from init
        current_branch = state.branch or self.branch

        if state.remote == GitState.Remote.UP_TO_DATE:
            safe_print("[green]Branch is up-to-date with remote[/green]")
            return state
        if state.remote == GitState.Remote.NO_UPSTREAM:
            # Only track attempts for the specific branch in the current session
            if (
                current_branch in self.upstream_attempts
                and self.upstream_attempts[current_branch] > 0
            ):
                safe_print(
                    f"[yellow]Already attempted to set upstream for branch '{current_branch}'. Use 'git push -u origin {current_branch}' to try again manually if needed.[/yellow]"
                )
                return state

            # Initialize counter for this branch if not already tracked
            if current_branch not in self.upstream_attempts:
                self.upstream_attempts[current_branch] = 0

            self.upstream_attempts[current_branch] += 1
            safe_print("[yellow]No upstream branch configured[/yellow]")

            if confirm("Would you like to set upstream by pushing the branch?"):
                # Call handle_no_upstream and get the resulting state
                new_state = await handle_no_upstream(state.branch)
                # Return the state returned by handle_no_upstream
                # This prevents immediately calling resolve_state again
                return new_state
            git_print("Operation cancelled")
            return state
        if (
            state.remote == GitState.Remote.DIVERGED
            or state.local == GitState.Local.DIVERGED
        ):
            safe_print("[yellow]Branch has diverged from remote[/yellow]")
            return await resolve_diverging_changes(
                state.branch, state.remote_name or "origin"
            )
        if state.remote == GitState.Remote.BEHIND:
            safe_print("[cyan]Branch is behind remote. Pulling changes...[/cyan]")
            return await handle_pull()
        if state.remote == GitState.Remote.AHEAD:
            return await handle_push(self.branch, self.remote)

        if state.remote == GitState.Remote.ERROR:
            safe_print("[red]Failed to check remote state[/red]")
            return state
        raise ValueError(f"Invalid remote state: {state}")


async def confirm_dirty(
    action: Literal["commit", "add"], state: GitState | None = None
):
    sum = await display_status_summary()
    if action == "commit":
        return confirm(
            "You have uncommitted changes:\n", *sum, "\n Would you like to commit them?"
        )
    elif action == "add":
        return confirm(
            "You have untracked files:\n", *sum, "\n Would you like to add them?"
        )


def try_debug(
    success_msg: str | None = None,
    error_msg: str | None = None,
    debug_msg: str | None = None,
) -> Callable[
    [Callable[P, Coroutine[Any, Any, Any]]], Callable[P, Coroutine[Any, Any, GitState]]
]:
    def wrapper(
        func: Callable[P, Coroutine[Any, Any, Any]],
    ) -> Callable[P, Coroutine[Any, Any, GitState]]:
        @wraps(func)
        async def wrapped(*args: P.args, **kwargs: P.kwargs) -> GitState:
            out: Any = None
            try:
                out = await func(*args, **kwargs)
                verbose(
                    "cmd: " + str(func.__name__) + " " + str(args) + " " + str(kwargs),
                    "out:",
                    out,
                )

                # Already a GitState - check error flag
                if isinstance(out, GitState):
                    if out.error:
                        if error_msg:
                            git_print(error_msg)
                    # Don't print decorator success_msg if GitState is returned and not an error
                    # Let the function handle its own success messages
                    return out

                # Convert string output to GitState and check for errors
                status = GitState.from_msg(out)

                # Extra error detection on raw output
                error_detected = haserr(out)
                if error_detected and not status.error:
                    status.error = True
                    status.msg = out

                if status.error or error_detected:
                    if error_msg:
                        git_print(error_msg)
                    return status

                # Only print decorator success_msg for string outputs if not "Already up to date"
                if success_msg and "Already up to date." not in str(out):
                    git_print(success_msg)

                return status
            except Exception as e:
                debug(f"Error in {func.__name__}: {e}", stacklevel=3, stack_info=True)
                if debug_msg:
                    debug(debug_msg, stacklevel=3, stack_info=True)
                if error_msg:
                    git_print(error_msg)

                return GitState(error=True, msg=str(e))

        return wrapped

    return wrapper


@try_debug(
    success_msg="Successfully pulled from remote.", error_msg="Failed to pull changes"
)
async def handle_pull(
    branch: str | None = None, remote: str = "origin", flags: Optional[list[str]] = None
) -> str:
    """Pull changes from remote.

    Args:
        branch: Branch to pull from
        remote: Remote to pull from
        flags: Additional git flags to pass through

    Returns:
        Command output
    """
    cmd = ["git", "pull"]

    # Add any extra flags
    if flags:
        cmd.extend(flags)

    # Add remote and branch if provided
    if branch:
        cmd.extend([remote, branch])

    output = await arun(cmd)

    # Extra verification to catch errors that might not be detected automatically
    if haserr(output):
        verbose(f"Pull error detected: {output}")
        return GitState(error=True, msg=output, remote=GitState.Remote.ERROR).msg

    return output


@try_debug(
    success_msg="Successfully pushed and set upstream.",
    error_msg="Failed to push and set upstream.",
)
async def handle_no_upstream(branch: str | None = None) -> GitState | str:
    """Pushes the current branch to origin and sets it as the upstream."""
    if not branch:
        branch = await get_branch()

    remotes = await arun(["git", "remote"])
    if "origin" in remotes:
        # Use git push -u which creates the remote branch if needed and sets tracking
        output = await arun(["git", "push", "--set-upstream", "origin", branch])
        # Reset the upstream cache to ensure we get fresh data next time
        await reset_upstream_cache()

        # Check if there was an error in the push command
        if haserr(output):
            # If push failed, explicitly mark as error and maintain NO_UPSTREAM status
            return GitState.from_msg(output).update(
                branch=branch, remote=GitState.Remote.NO_UPSTREAM, error=True
            )

        # If successful, mark as UP_TO_DATE with the remote name set
        return GitState.from_msg(output).update(
            branch=branch,
            remote=GitState.Remote.UP_TO_DATE,
            remote_name="origin",
            error=False,
        )

    return withstate(
        f"Remote 'origin' not found. Could not set upstream for {branch}.",
        error=True,
        branch=branch,
    )


@try_debug(success_msg="Successfully rebased", error_msg="Failed to rebase")
async def handle_rebase(
    branch: str | None = None,
    remote: str = "origin",
    state: GitState | None = None,
    autoyes: bool | None = None,
    flags: Optional[list[str]] = None,
    max_depth: int = 1,
) -> str | GitState:
    """Rebase the current branch onto the remote branch.

    Args:
        branch: Branch to rebase
        remote: Remote to rebase onto
        state: GitState object to use for state checking
        autoyes: Whether to automatically confirm actions
        flags: Additional flags to pass to git pull --rebase
        max_depth: Maximum recursion depth to prevent infinite recursion
    """
    # Prevent infinite recursion
    if max_depth <= 0:
        from mbcore.display import safe_print
        from mbcore.log import warning

        warning("Maximum recursion depth exceeded in handle_rebase")
        safe_print(
            "Aborting rebase due to maximum recursion depth reached", style="bold red"
        )
        # Return a GitState that indicates an error occurred
        return GitState.from_msg(
            "Maximum recursion depth exceeded during rebase"
        ).update(error=True)

    state = state or await get_git_state()
    branch = branch or state.branch

    # Filter out invalid flags
    valid_flags = []
    if flags:
        for flag in flags:
            # Check for invalid flags
            if flag == "--abort-on-conflict":
                debug(f"Skipping invalid git flag: {flag}")
                continue
            valid_flags.append(flag)

    if state.local == state.Local.DIRTY and (
        autoyes
        or confirm(
            f"Branch [bold]{branch}[/bold] has [bold green] unstaged changes[/bold green].\n Would you like to commit them before rebasing?"
        )
    ):
        # Directly handle dirty working tree instead of calling Policy
        try:
            from mbcore.display import safe_print

            git_status = await get_git_status()
            out = await commit_changes(git_status)
            if haserr(out):
                safe_print("Failed to commit changes before rebasing", style="bold red")
                return GitState.from_msg(out).update(error=True)
        except Exception as e:
            from mbcore.log import error

            error(f"Error committing changes: {e}")
            return GitState.from_msg(f"Error committing changes: {str(e)}").update(
                error=True
            )

    async with GitContext(autoyes=autoyes) as ctx:
        # Build command with additional flags
        cmd = ["git", "pull", f"{remote}", f"{branch}", "--rebase"]

        # By default, use -X theirs for conflict resolution if not already specified
        if not any(f.startswith("-X") for f in valid_flags):
            cmd.extend(["-X", "theirs"])

        # Add any extra valid flags
        if valid_flags:
            cmd.extend([f for f in valid_flags if f not in cmd])

        debug(f"Running rebase command: {' '.join(cmd)}")
        out = await ctx.run(cmd)
        if "no tracking information" in out:
            if haserr(out):
                # Directly return a state instead of calling Policy().handle_msg
                return GitState.from_msg(out).update(
                    branch=branch, remote=GitState.Remote.NO_UPSTREAM, error=True
                )

            # Try again without specifying branch
            cmd = ["git", "pull", "--rebase"]
            if not any(f.startswith("-X") for f in valid_flags):
                cmd.extend(["-X", "theirs"])
            if valid_flags:
                cmd.extend([f for f in valid_flags if f not in cmd])
            out = await ctx.run(cmd)

        if haserr(out):
            # Directly return a state instead of calling Policy().handle_msg
            return GitState.from_msg(out).update(error=True)

        return out


async def ensure_vendored(modify_main_pyproject=True, remote="origin", force_update=False) -> bool:
    """
    Vendor source packages into the vendored directory.

    Returns True if any packages were actually copied.
    """
    from mbpy.pkg.dependency import Dependency
    from mbpy.pkg.mpip import modify_dependencies
    from mbpy.pkg.toml import load_toml,get_deps
    from mbcore.traverse import setup_workspace
    from mbpy.env import getws
    await commit_changes(await get_git_status(), withdev=False)

    ws = getws()
    if not ws:
        warning("No workspace found for vendoring")
        return False
    pyproject_path = ws / "pyproject.toml"
    if not pyproject_path.exists():
        if not confirm("No pyproject.toml found. Would you like to create one?"):
            return False
        setup_workspace()
    project_deps = get_deps(pyproject_path)
    new_deps = []
    for dep in project_deps:
        if any(c in dep.project_name for c in ["file:","./"]):
            p = Path(str(dep.original_source)).absolute().relative_to(getws().absolute())
            git_url = f"git+https://github.com/{p.parent.name}/{p.name}"
            if dep.version and not "." in dep.version and isinstance(dep.version,str):
                git_url += f"@{dep.version}"
            new_deps.append(Dependency(git_url,git=True))
        else:
            new_deps.append(dep)

    await modify_dependencies(new_deps, "install", cwd=ws)
    await commit_changes(withdev=False, commit_msg="Vendoring dependencies.",autoyes=True)
    safe_print(f"Vendored {list(set(map(lambda x: x.project_name, new_deps)) - set(map(lambda x: x.project_name, project_deps)))}")
    await handle_push(await get_branch(), remote=remote, force=force_update)
    await modify_dependencies(project_deps, "install", cwd=ws)
    await commit_changes(withdev=False, commit_msg="Reversion to local deps.",autoyes=True)
    return True

async def foreach(
    *repos: Path | str,
    action: Callable[[], Coroutine[Any, Any, GitState]],
    **action_kwargs,
):
    for repo in repos:
        path = Path(str(repo))
        with ctx.chdir(path):
            await action(**action_kwargs)


@try_debug()
async def handle_push(
    branch_or_args: str | tuple[str] | list[str] | None = None,
    remote: str = "origin",
    force=False,
    flags: Optional[list[str]] = None,
) -> GitState | str:
    """Vendors dependencies (modifying pyproject.toml) before pushing."""
    from mbpy.git.state import arun, git_print, GitState  # Ensure GitState is imported
    from mbpy.env import getws  # Import getws

    # Use the global _seen_commit_messages instead of creating a new local set
    global _seen_commit_messages

    branch = None
    args = []
    if isinstance(branch_or_args, str):
        branch = branch_or_args
    elif isinstance(branch_or_args, (list, tuple)):
        args = list(branch_or_args)
        branch = args[0] if args else None
    # Get branch before potential chdir or mocks affect it
    if not branch:
        branch = await get_branch()  # Assuming get_branch is async
    if branch is None:
        raise ValueError("No branch found or specified")

    # Get workspace root using getws() and construct path
    ws_root = getws()
    if not ws_root:
        return GitState(error=True, msg="Workspace root not found.")
    # --- DEBUG ---
    print(f"[DEBUG handle_push] ws_root = {ws_root} (exists: {ws_root.exists()})")
    # -------------
    pyproject_path = ws_root / "pyproject.toml"
    # --- DEBUG ---
    print(
        f"[DEBUG handle_push] pyproject_path = {pyproject_path} (exists: {pyproject_path.exists()})"
    )
    # -------------

    try:
        # 1. Commit current state first
        git_status = await get_git_status()
        if git_status:  # If there are changes to commit
            pre_vendor_commit = await commit_changes(
                git_status, withdev=False, commit_msg="chore: Pre-vendoring commit"
            )
            if hasattr(pre_vendor_commit, "commit_msg"):
                print_once(pre_vendor_commit.commit_msg)

        # 2. Vendor dependencies and modify pyproject.toml
        try:
            # --- DEBUG ---
            print(
                f"[DEBUG handle_push] Calling ensure_vendored with modify_main_pyproject=True"
            )
            # -------------
            vendoring_result = await ensure_vendored(
                modify_main_pyproject=True, force_update=True
            )
            print(f"[DEBUG handle_push] Vendoring result: {vendoring_result}")
        except Exception as e:
            import traceback
            traceback.print_exc()
            debug(f"Vendoring error: {e}")
            print(f"[DEBUG handle_push] Vendoring exception: {e}")
            debug(f"Vendoring traceback: {traceback.format_exc()}")

        # Check if pyproject.toml was modified and stage it
        if pyproject_path.exists():
            # --- DEBUG ---
            print(
                f"[DEBUG handle_push] Adding pyproject.toml: git add {str(pyproject_path)}"
            )
            # -------------
            add_result = await arun(["git", "add", str(pyproject_path)])
            print(f"[DEBUG handle_push] git add result: {add_result}")

        # Stage any changes within the vendored directory itself
        if ws_root:
            vendored_path_abs = ws_root / "vendored"
            # --- DEBUG ---
            print(
                f"[DEBUG handle_push] Staging vendored dir: {vendored_path_abs} (exists: {vendored_path_abs.exists()})"
            )
            # -------------
            if vendored_path_abs.exists():  # Check if it exists before adding
                # --- DEBUG ---
                print(f"[DEBUG handle_push] Running: git add {str(vendored_path_abs)}")
                # -------------
                add_vendored_result = await arun(["git", "add", str(vendored_path_abs)])
                print(
                    f"[DEBUG handle_push] git add vendored result: {add_vendored_result}"
                )

        # 3. Commit the vendored changes
        vendor_commit = await commit_changes(
            None,
            withdev=False,
            autoyes=True,
            commit_msg="chore: Vendoring dependencies for distribution",
        )
        if hasattr(vendor_commit, "commit_msg"):
            print_once(vendor_commit.commit_msg)

        # 4. Push both commits
        push_cmd = ["git", "push"]
        if flags:
            push_cmd.extend([f for f in flags if f not in push_cmd])
        if args:
            extra_flags = [
                arg for arg in args if arg != branch and arg not in (flags or [])
            ]
            push_cmd.extend(extra_flags)
        push_cmd.extend([remote, branch])
        if force and "--force" not in push_cmd:
            push_cmd.append("--force")

        debug(f"Running push command: {' '.join(push_cmd)}")
        push_output = await arun(push_cmd)
        push_state = GitState.from_msg(push_output)
        push_error = haserr(push_output)

        # --- Push Result Handling ---
        if push_error:
            git_print(f"Push failed: {push_output}")
            # Attempt policy handling, but return the state from Policy
            return await Policy(branch=branch, remote=remote).handle_msg(push_output)
        else:
            # Simplified success message
            if "Everything up-to-date" in push_output:
                safe_print("Everything up-to-date")
                push_state = GitState(
                    local=GitState.Local.CLEAN, remote=GitState.Remote.UP_TO_DATE
                )
            else:
                safe_print(f"Successfully pushed to {remote}/{branch}")
                push_state.remote = GitState.Remote.UP_TO_DATE
                push_state.error = False

        return push_state

    except Exception as e:
        debug(f"Error in handle_push: {e}")
        import traceback

        debug(f"Traceback: {traceback.format_exc()}")

        return GitState(error=True, msg=f"Push failed: {e}")


@try_debug(
    success_msg="Successfully created new branch",
    error_msg="Failed to create new branch",
)
async def handle_new_branch(branch: str) -> str:
    # First handle any uncommitted changes
    status = await get_git_status()
    if status:
        # Auto add and commit changes
        await add_untracked()
        # Commit should NOT modify pyproject.toml
        state = await commit_changes(
            status, withdev=False
        )  # Assuming commit doesn't trigger vendoring mod
        if haserr(state):
            return state.msg

    return await arun(["git", "checkout", "-b", branch])


@try_debug(
    success_msg="Successfully forked and checked out new branch",
    error_msg="Failed to fork and check out new branch",
)
async def handle_new_fork(
    repo: str, branch: str, remote: str = "origin"
) -> str | GitState:
    if (status := await get_git_state()).local == GitState.Local.DIRTY:
        y = await confirm_dirty("commit", status)
        if y:
            # Commit should NOT modify pyproject.toml
            await commit_changes(
                status, withdev=False
            )  # Assuming commit doesn't trigger vendoring mod
        else:
            return "Uncommitted changes. Aborting."
    return withstate(
        repo=repo,
        branch=branch,
        remote=remote,
        msg=await arun(
            [
                "gh",
                "repo",
                "fork",
                repo,
                "--clone",
                "--remote",
                remote,
                "--branch",
                branch,
            ]
        ),
    )


@try_debug(
    success_msg="Successfully added untracked files",
    error_msg="Failed to add untracked files",
)
async def add_untracked(
    dry_run: bool = False, skip_submodules: bool = False
) -> GitState:
    file_status = {}
    cmd = ["git", "status", "--porcelain"]
    output = await arun(cmd)

    has_submodule_changes = False

    for line in output.splitlines():
        if not line:
            continue
        status, filepath = line[0:2], line[3:].strip()

        # Check for submodule changes
        if "(untracked content)" in filepath or "(modified content)" in filepath:
            has_submodule_changes = True
            if skip_submodules:
                continue

        if " -> " in filepath:
            _, filepath = filepath.split(" -> ")
        filepath = filepath.strip('"')
        if not Path(filepath).exists() and status[0] != "D":
            continue

        if status[0] == "M" or status[1] == "M":
            file_status[filepath] = "modified"
        elif status[0] == "A":
            file_status[filepath] = "added"
        elif status[0] == "D":
            file_status[filepath] = "removed"
        elif status[0] == "?" and not dry_run:
            file_status[filepath] = "added"

    state = await get_git_state()
    for line in state.msg.splitlines():
        f = line.split(":")[-1].strip()
        if f in file_status:
            continue
        if "untracked" in line.lower() or "not staged" in line.lower():
            file_status[f] = "added"
        if "deleted" in line.lower():
            file_status[f] = "removed"
        if "modified" in line.lower():
            file_status[f] = "modified"
        if "new file" in line.lower():
            file_status[f] = "added"
        if "renamed" in line.lower():
            file_status[f] = "renamed"

    if not dry_run:
        out = await arun(["git", "add", "."])

        # If there are submodule changes, warn the user
        if has_submodule_changes and skip_submodules:
            safe_print(
                "[yellow]Note: Submodule changes were detected but skipped.[/yellow]"
            )
        elif has_submodule_changes:
            safe_print(
                "[yellow]Note: Submodule changes detected. You may need to commit changes inside the submodule first.[/yellow]"
            )

        return GitState.from_msg(out).update(statuses=file_status)
    return GitState(statuses=file_status)


global yes
yes = None


@try_debug(error_msg="Failed to commit changes")
async def commit_changes(
    status: dict[str, GitStatus] | None = None,
    dry_run: bool = False,
    autoyes: bool = False,
    withdev=True,
    branch: str | None = None,
    commit_msg: str | None = None,
    skip_submodules: bool = False,
) -> GitState:
    from mbpy.env import getdevws
    from mbcore.traverse import find_file

    doc, err = find_file(".gitignore")
    status = status or await get_git_status()
    state = await get_git_state()

    # Check if there's anything to commit first
    if not status and state.local == GitState.Local.CLEAN:
        debug("No changes found to commit")
        return GitState(
            local=GitState.Local.CLEAN,
            remote=state.remote,
            commit_msg="No changes to commit",
        )

    if state.local == GitState.Local.DIRTY:
        state = await get_git_state()
        if state.local == GitState.Local.DIRTY:
            global yes
            if yes is None and not autoyes:
                yes = await confirm_dirty("add")
            if yes:
                await add_untracked(skip_submodules=skip_submodules)
                status = await get_git_status()  # Update status after adding

    if withdev:
        devws = getdevws(relative=True)
        if doc and devws.exists() and str(devws) not in doc.read_text():
            debug(
                f"Development workspace {getdevws(relative=True)=}{getdevws()=}, {Path.cwd().absolute()=},{devws.absolute()=}"
            )
            warning(
                f"Development workspace {getdevws(relative=True)} has not been not added to git ignore. Run `mbgit ignore {getdevws().absolute().relative_to(Path.cwd().absolute())}` to add it"
            )
            if prompt_ask("Would you like to add it to git ignore?") == "y":
                # Simplified adding to .gitignore
                with Path(str(doc)).open("a") as f:
                    f.write(f"\n{getdevws(relative=True)}")

        # Ensure vendored directory is up-to-date, but DO NOT modify pyproject.toml
        try:
            await ensure_vendored(modify_main_pyproject=False)
        except Exception as e:
            debug(f"Vendoring error (silencing): {e}")

        # Add the vendored directory contents if they changed
        # Use an absolute path constructed from ws_root
        ws_root = getws()  # Need ws_root here too
        if ws_root:
            vendored_path_abs = ws_root / "vendored"
            if vendored_path_abs.exists():  # Check if it exists before adding
                await arun(["git", "add", str(vendored_path_abs)])

        # Re-fetch status in case vendoring added files to be committed
        status = await get_git_status()

    else:
        devws = None

    if dry_run:
        # (Dry run logic remains the same)
        by_status = defaultdict(list)
        # Ensure status is a dict here
        current_status = status if isinstance(status, dict) else await get_git_status()
        for file, st in current_status.items():
            by_status[st].append(str(file))
        for st, files in by_status.items():
            color = f"{'green' if st == GitStatus.ADD or st == GitStatus.STAGED else 'red' if st == GitStatus.REMOVE or st == GitStatus.STAGED_DELETE else 'magenta' if st == GitStatus.MODIFY else 'cyan' if st == GitStatus.UNTRACKED else 'white'} bold"
            safe_print(
                f"[blue]Files that would be [/blue][{color}]{st}[/{color}][blue] in a commit:[/blue]"
            )
            for f in files:
                safe_print(f"  - {f}")
        cl = commit_msg or await brief_commit_message()
        safe_print(f"[Bold blue]Dry run commit message:[/blue]]\n\n {cl}")
        return GitState(local=GitState.Local.CLEAN, remote=state.remote, commit_msg=cl)

    # Generate commit message
    cl = commit_msg or await brief_commit_message()

    # Use a simple string command with explicit quotes around the message
    from mbpy.cmd import arun as cmd_arun

    cmd_str = f'git commit -m "{cl}"'
    debug(f"Running commit with shell command: {cmd_str}", stacklevel=3)

    # Use the cmd module's arun which supports shell=True
    out = await cmd_arun(cmd_str, shell=True, show=verbose())

    gs = GitState.from_msg(out)  # Assume success initially
    if haserr(out):
        # Handle commit errors
        policy_handled_state = await Policy(branch=branch).handle_state(
            GitState.from_msg(out)
        )
        # Check if policy resolved the error or if it persists
        return policy_handled_state
    elif "nothing to commit" not in out and "no changes" not in out:
        gs.commit_msg = cl  # Set commit message only if something was committed
        # Don't print the message here - handled by caller
    else:
        debug("Nothing to commit, working tree clean.")
        gs.commit_msg = "No changes to commit"

    return gs


@try_debug(success_msg="Successfully cleaned up", error_msg="Failed to clean up")
async def handle_clean_up(tmp_branch: str, branch: str, err: str | None = None) -> str:
    if not ismidcleanup(tmp_branch):
        raise ValueError(
            f"Invalid branch name: {tmp_branch}. Expected format: <branch>-tmp-<timestamp>"
        )

    # First, checkout the original branch
    checkout_result = await arun(["git", "checkout", branch])
    if haserr(checkout_result):
        return f"Failed to checkout original branch: {checkout_result}"

    # Check if fully merged before deletion
    merge_check = await arun(["git", "branch", "--merged"])
    if tmp_branch in merge_check:
        delete_result = await arun(["git", "branch", "-D", tmp_branch])
        return f"{delete_result} {err or ''}".strip()

    return f"Branch {tmp_branch} is not fully merged. Manual cleanup may be required."


@try_debug(
    success_msg="Successfully checked out and merged",
    error_msg="Failed to check out and merge",
)
async def handle_checkout_merge(
    origin_branch: str, tmp_branch: str, confirm=False
) -> GitState:
    out = await add_untracked()
    if haserr(out):
        return out
    status = await get_git_status()
    # Use await get_git_state() to ensure out is a GitState object
    commit_state = await commit_changes(status)
    if haserr(commit_state):
        # Pass commit_state.msg if it exists
        err_msg = (
            commit_state.msg if hasattr(commit_state, "msg") else str(commit_state)
        )
        return await handle_clean_up(tmp_branch, origin_branch, err_msg)
    else:
        # Safely check commit_msg attribute
        commit_msg = getattr(commit_state, "commit_msg", None)
        if commit_msg and "No changes to commit" not in commit_msg:
            safe_print(commit_msg)
    out_checkout = await arun(["git", "checkout", origin_branch])
    if haserr(out_checkout):
        # Pass checkout output string directly
        return await handle_clean_up(tmp_branch, origin_branch, out_checkout)
    if not confirm or prompt_ask("Would you like to merge the changes?") == "y":
        merge_out = await arun(["git", "merge", tmp_branch, "-X", "theirs"])
        if haserr(merge_out):
            return await handle_clean_up(tmp_branch, origin_branch, merge_out)
        # Check if the merge output says "Already up to date"
        if "Already up to date." in merge_out:
            # If up to date, still clean up but return a state reflecting this
            cleanup_state = await handle_clean_up(tmp_branch, origin_branch)
            if isinstance(cleanup_state, GitState) and not cleanup_state.error:
                return GitState.from_msg(merge_out).update(
                    error=False
                )  # Return merge output state
            return cleanup_state  # Return potential cleanup error state
        else:
            # If merge happened, proceed with cleanup normally
            return await handle_clean_up(tmp_branch, origin_branch)
    else:
        # User chose not to merge, clean up the temp branch
        return await handle_clean_up(tmp_branch, origin_branch)


async def get_diff(
    branch: str | None = None, remote: str = "origin", show=False
) -> str:
    # Get current branch name if not provided
    from mbpy.cmd import run
    from mbcore.log import verbose

    branch = branch or sync_get_branch()
    # Fetch latest from remote
    out = run(["git", "fetch", remote])
    verbose(out)
    # Verify remote branch exists
    branches = run(["git", "branch", "-a"]).splitlines()
    if branch in branches:
        other = branch
    elif f"{remote}/{branch}" in branches:
        other = f"{remote}/{branch}"

    else:
        safe_print(
            f"Remote branch {remote}/{branch} not found. Comparing to origin/main instead."
        )
        other = f"{remote}/main"

    # Get diff between local and remote branch

    diff = run(["git", "diff", f"{branch}..{other}"])
    return diff


@try_debug(
    success_msg="Successfully resolved diverging changes",
    error_msg="Failed to resolve diverging changes",
)
async def resolve_diverging_changes(
    branch: str | None = None, remote: str = "origin", dry_run: bool = False
) -> GitState | str:
    safe_print("\nYou have several options:")
    safe_print("1. Pull and rebase (recommended)")
    safe_print("2. Create a new branch")
    safe_print("3. Force push (not recommended)")
    safe_print("4. Manually resolve conflicts")
    safe_print("5. Cancel")

    choice = prompt_ask(
        "How would you like to proceed?",
        choices=["1", "2", "3", "4", "5"],
        default="1",
    )
    if dry_run:
        return await get_git_state()

    match choice:
        case "1":
            out = await handle_rebase(branch, remote)
            out = await handle_push(branch, remote=remote)
            if haserr(out):
                out = await Policy(branch, remote).handle_state(out)
                return await handle_push(branch, remote=remote)
            return out
        case "2":
            new_branch = cast(
                str, prompt_ask("Enter new branch name", default="tmp-branch")
            )
            await handle_new_branch(new_branch)
            out = await handle_push(new_branch, remote=remote)
            if haserr(out):
                return await resolve_state(branch)
            return out
        case "3":
            if not confirm(
                "[red]WARNING: Force push will overwrite remote changes. Continue?[/red]"
            ):
                return GitState(error=True)
            return await handle_push(remote=remote, force=True)
        case "4":
            return await arun(["git", "mergetool"])
        case _:
            git_print("Operation cancelled")
            return GitState(error=True)


async def check_state(branch: str | None = None) -> GitState:
    """Check if local branch has diverged from remote."""
    if not branch:
        branch = await get_branch()

    try:
        # Refresh index to prevent stale state detection
        await arun(["git", "update-index", "--refresh"])

        # Reset upstream cache before checking to ensure fresh data
        await reset_upstream_cache()

        # Check if we have upstream configured
        upstream = await arun(
            ["git", "rev-parse", "--abbrev-ref", f"{branch}@{{upstream}}"]
        )
        upstream = upstream.strip()

        if "fatal: no upstream" in upstream:
            return GitState(
                local=GitState.Local.CLEAN, remote=GitState.Remote.NO_UPSTREAM
            )
        return GitState.from_msg(upstream)

    except Exception:
        if debug():
            import traceback

            traceback.print_exc()
        return GitState(local=GitState.Local.UNKNOWN, remote=GitState.Remote.ERROR)


def ismidcleanup(branch: str | None = None) -> bool:
    if not branch:
        branch = sync_get_branch()
    return (
        branch.count("-") >= 2
        and branch.split("-")[-2] == "tmp"
        and branch.split("-")[-1].isdigit()
    )


def original_from_tmp(branch: str) -> str:
    if not ismidcleanup(branch):
        raise ValueError(
            f"Invalid branch name: {branch}. Expected format: <branch>-tmp-<timestamp>"
        )
    orig = "-".join(branch.split("-")[:-2])
    if orig == "None":
        # Default to main if we can't determine original branch
        return "main"
    return orig


async def resolve_state(
    branch: str | None = None,
    action: str | None = None,
    dry_run: bool = False,
    autoyes: bool = False,
    args=None,
    skip_submodules: bool = False,
) -> GitState:
    # Get the actual branch name first
    branch = branch or await get_branch()

    if ismidcleanup(branch):
        y = confirm(
            f"Your branch {branch} is in the middle of a cleanup. Would you like to continue?"
        )
        if y:
            original_branch = original_from_tmp(branch)
            cleanup_result = await handle_clean_up(branch, original_branch)
            if haserr(cleanup_result):
                return GitState(error=True, branch=branch)
            # Exit immediately after cleanup to prevent recursion
            return GitState(branch=original_branch)
        return GitState(error=True, branch=branch)

    state = await check_state(branch)
    if haserr(state):
        state = await Policy(branch).handle_state(state)

    if action:
        # Parse the action and any flags
        action_parts = action.split() if isinstance(action, str) else [action]
        primary_action = action_parts[0].lower() if action_parts else None
        action_flags = action_parts[1:] if len(action_parts) > 1 else []

        debug(f"Processing action: {primary_action} with flags: {action_flags}")

        match primary_action:
            case "pull":
                if "--rebase" in action_flags:
                    # Remove --rebase from flags as it's handled specially
                    other_flags = [f for f in action_flags if f != "--rebase"]
                    state = await handle_rebase(
                        branch=branch, flags=cast(list[str], other_flags)
                    )
                else:
                    state = await handle_pull(
                        branch=branch, flags=cast(list[str], action_flags)
                    )
            case "push":
                state = await get_git_state()
                if state.local == GitState.Local.DIRTY:
                    state = await commit_changes(
                        state,
                        dry_run=dry_run,
                        skip_submodules=skip_submodules,
                        autoyes=autoyes,
                    )
                    if state.commit_msg:
                        git_print(state.commit_msg)
                if state.remote == GitState.Remote.DIVERGED:
                    state = await resolve_diverging_changes(branch, dry_run=dry_run)

                # Pass through all flags to handle_push
                force = "--force" in action_flags or "-f" in action_flags
                other_flags = [f for f in action_flags if f not in ["--force", "-f"]]
                state = await handle_push(
                    branch_or_args=args, force=force, flags=cast(list[str], other_flags)
                )
                if not state.error:
                    return state
            case "rebase":
                state = await handle_rebase(
                    branch=branch, flags=cast(list[str], action_flags)
                )
                if not state.error:
                    return state
            case "commit":
                status = await get_git_status()
                commit_msg = (
                    args[0]
                    if args and isinstance(args, (list, tuple)) and len(args) > 0
                    else None
                )
                autoyes = "--yes" in action_flags or "-y" in action_flags
                return await commit_changes(
                    status, dry_run=dry_run, commit_msg=commit_msg, autoyes=autoyes
                )
            case _:
                git_print(f"Invalid action: {action}")

    # Return the final state
    return state


@try_debug(
    success_msg="Successfully switched branch", error_msg="Failed to switch branch"
)
async def switch_branch(branch: str, force: bool = False) -> GitState | str:
    """Switch to a branch, creating it if it doesn't exist."""
    from mbpy.git.state import arun, git_print

    try:
        # First check if we're in a git repository
        git_dir_check = await arun("git rev-parse --git-dir", show=False)
        if not git_dir_check or git_dir_check.strip() == "":
            return GitState(error=True, msg=f"Not a git repository")

        # Check if the branch exists locally
        branches = await arun(["git", "branch"], show=False)
        branch_exists = any(
            b.strip().replace("* ", "") == branch for b in branches.splitlines()
        )

        if branch_exists:
            # Branch exists locally, just check it out
            cmd = ["git", "checkout"]
            if force:
                cmd.append("-f")
            cmd.append(branch)
            output = await arun(cmd, show=True)
        else:
            # Check if branch exists remotely
            try:
                remote_check = await arun(
                    ["git", "ls-remote", "--heads", "origin", branch], show=False
                )
                branch_exists_remotely = branch in remote_check

                if branch_exists_remotely:
                    # Branch exists remotely, create tracking branch
                    git_print(
                        f"Branch '{branch}' exists remotely but not locally. Creating tracking branch..."
                    )
                    cmd = ["git", "checkout", "-b", branch, f"origin/{branch}"]
                    output = await arun(cmd, show=True)
                else:
                    # Branch doesn't exist anywhere, create new branch
                    git_print(f"Creating new branch '{branch}'...")
                    cmd = ["git", "checkout", "-b", branch]
                    output = await arun(cmd, show=True)
            except Exception as e:
                # Handle error during remote check
                warning(f"Error checking remote branches: {e}")
                # Fall back to creating a new local branch
                git_print(f"Creating new branch '{branch}'...")
                cmd = ["git", "checkout", "-b", branch]
                output = await arun(cmd, show=True)

        return output
    except Exception as e:
        # Catch any exceptions and return as a GitState error
        warning(f"Error in switch_branch: {e}")
        return GitState(error=True, msg=f"Failed to switch branch: {e}")


@try_debug(
    success_msg="Successfully merged and cleaned up",
    error_msg="Failed to merge and cleanup",
)
async def quick_merge(branch: str) -> str:
    """Quick merge a branch and delete it both locally and remotely."""
    if not confirm(f"Merge and delete {branch}?"):
        return "Cancelled"

    out = await arun(["git", "merge", branch])
    if haserr(out):
        return out

    # Delete remote first
    await arun(["git", "push", "origin", "--delete", branch])
    # Then delete local
    return await arun(["git", "branch", "-D", branch])


if __name__ == "__main__":
    import asyncio

    async def main():
        print(await resolve_state(dry_run=True))

    asyncio.run(main())


# Add this function to reset the upstream cache
async def reset_upstream_cache() -> None:
    """Reset the cached upstream value to force re-checking."""
    global _upstream
    _upstream = None


# Helper function to print commit message only once
def print_once(msg):
    global _seen_commit_messages
    if not msg or "No changes to commit" in msg:
        return
    # Normalize message by removing any leading/trailing whitespace
    msg = msg.strip()
    if msg not in _seen_commit_messages:
        safe_print(msg)
        _seen_commit_messages.add(msg)


def count_files_with_limit(path, limit=1000):
    """Count files up to limit then stop, skipping vendored directories."""
    try:
        count = 0
        for root, dirs, files in os.walk(str(path)):
            # Skip vendored directories to avoid counting nested vendored dependencies
            if "vendored" in dirs:
                dirs.remove("vendored")

            count += len(files)
            if count > limit:
                return limit + 1  # Just return over the limit
    except Exception as e:
        debug(f"Error counting files: {e}")
        return 0
    return count
