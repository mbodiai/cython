# FILE: mbpy/helpers/_git_ctx.py

import asyncio
from dataclasses import dataclass
import os
from datetime import datetime  # Import the correct datetime

from enum import Enum, StrEnum
from pathlib import Path
from typing import List, Any

from mbcore.display import getspinner, getconsole, raw_print, safe_print
from rich.console import Console

from mbcore.log import debug, verbose
from tomlkit import datetime as toml_datetime  # Rename this to avoid conflicts

from mbpy.cmd import arun_command


global _branch, _repo_url, _org, _repo, _upstream, _remotes
_branch = None
_repo_url = None
_org = None
_repo = None
_upstream = None
_remotes = None


@dataclass
class GitState(dict):
    class Local(StrEnum):
        CLEAN = "clean"
        DIRTY = "dirty"
        UNKNOWN = "unknown"
        DIVERGED = "diverged"
        UNTRACKED = "untracked"
        UNCOMMITTED = "uncommited"

    class Remote(StrEnum):
        AHEAD = "ahead"
        BEHIND = "behind"
        DIVERGED = "diverged"
        UP_TO_DATE = "up-to-date"
        NO_UPSTREAM = "no-upstream"
        ERROR = "error"

    msg: str = ""

    local: Local | None = None
    remote: Remote | None = None
    commit_msg: str | None = None
    error: bool | None = None
    branch: str | None = None
    remote_name: str | None = None
    statuses: "dict[str, GitStatus] | None" = None
    repo_url: str | None = None
    org: str | None = None
    repo: str | None = None

    def update(self, **kwargs: "Any") -> "GitState":  # type: ignore
        for k, v in kwargs.items():
            setattr(self, k, v)
        return self

    @classmethod
    def from_msg(cls, msg: "str|GitState") -> "GitState":
        if not msg:
            msg = ""
        if isinstance(msg, GitState):
            return msg
        if isinstance(msg, dict):
            raise ValueError(f"Invalid message: {msg}")
        debug(msg, stacklevel=3)
        msg = msg.lower()
        error = False
        remote = cls.Remote.UP_TO_DATE
        local = cls.Local.CLEAN

        # if "untracked" in msg or "unstaged" in msg or "not staged" in msg or "changes to be committed" in msg:
        if any(
            x in msg for x in ["untracked", "unstaged", "not staged", "to be committed"]
        ):
            local = cls.Local.DIRTY
        if "non-fast-forward" in msg or "rejected" in msg:
            local = cls.Local.DIVERGED

        if "no upstream" in msg or "no tracking" in msg:
            remote = cls.Remote.NO_UPSTREAM
        elif "non-fast-forward" in msg or ("rejected" in msg and "behind" in msg):
            remote = cls.Remote.BEHIND
        elif "ahead" in msg:
            remote = cls.Remote.AHEAD
        elif "behind" in msg:
            remote = cls.Remote.BEHIND
        elif "failed to push" in msg or "error" in msg:
            remote = cls.Remote.ERROR

        for line in msg.splitlines():
            parts = line.split()
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                ahead, behind = map(int, parts)

        error = error or remote in [
            cls.Remote.ERROR,
            cls.Remote.NO_UPSTREAM,
            cls.Remote.DIVERGED,
            cls.Remote.BEHIND,
            cls.Remote.ERROR,
        ]
        return cls(local=local, remote=remote, error=error, msg=msg)

    def __post_init__(self):
        self.error = self.error or self.remote in [
            self.Remote.ERROR,
            self.Remote.NO_UPSTREAM,
            self.Remote.DIVERGED,
            self.Remote.BEHIND,
        ]
        if self.msg and not self.remote and not self.local:
            self.remote = type(self).from_msg(self.msg).remote
            self.local = type(self).from_msg(self.msg).local

        self.branch = self.branch or sync_get_branch()
        self.repo_url = self.repo_url or sync_get_repo_info()[0]
        self.org = self.org or sync_get_repo_info()[1]
        self.repo = self.repo or sync_get_repo_info()[2]


def haserr(output: str | GitState) -> bool:
    if isinstance(output, GitState):
        return bool(output.error)
    debug(f"Checking for errors in output: {output}")
    if not isinstance(output, str):
        return False

    # Specific git error patterns
    if any(
        error_msg in output.lower()
        for error_msg in [
            "error",
            "fatal",
            "rejected",
            "cannot",
            "diverging branches can't be fast-forwarded",
            "couldn't find remote ref",
            "couldn't find remote branch",
            "couldn't find",
        ]
    ):
        return True

    # Check for git hints about required manual actions
    if "hint:" in output.lower() and any(
        action in output.lower()
        for action in ["git merge", "merge the remote", "rebase", "cannot fast-forward"]
    ):
        return True

    # Don't flag as error if it's just a commit message with common keywords
    commit_keywords = ["feat", "update", "fix"]
    if any(keyword in output.lower() for keyword in commit_keywords):
        # Only consider it a non-error if there are no explicit error messages
        return any(x in output.lower() for x in ["error", "fatal", "rejected"])

    # Catch specific upstream/branch existence errors
    if (
        any(
            err in output.lower()
            for err in [
                "does not exist",
                "no upstream configured",
                "couldn't find remote ref",
                "couldn't find remote branch",
            ]
        )
        and "set upstream" not in output.lower()
    ):  # Avoid matching hints about how *to* set upstream
        return True

    return False


def withstate(msg: str, state: GitState | None = None, **kwargs) -> GitState:
    if state:
        state.msg = msg
        state.update(**kwargs)
        return state
    return GitState(msg=msg, **kwargs)


async def get_status_summary(
    file_status: "dict[str, GitStatus]|None" = None,
) -> "dict[GitStatus, list[str]]":
    """Group files by status type for display and structured reporting."""
    file_status = file_status or await get_git_status()
    summary: dict[GitStatus, list[str]] = {
        GitStatus.ADD: [],
        GitStatus.MODIFY: [],
        GitStatus.REMOVE: [],
        GitStatus.RENAME: [],
        GitStatus.UNTRACKED: [],
        GitStatus.STAGED: [],
        GitStatus.STAGED_DELETE: [],
    }

    for filepath, status in file_status.items():
        summary[status].append(str(filepath))

    return {k: v for k, v in summary.items() if v}


async def display_status_summary(file_status: "dict[str, GitStatus]|None" = None):
    from rich.table import Table
    from mbcore.display import NO_BOX
    from mbpy.cmd import arun

    # Get branch name
    branch = await get_branch()

    # Get ahead/behind status
    tracking_info = ""
    ahead_files = []
    try:
        # Check if branch has upstream
        upstream_check = await get_upstream(branch)
        if upstream_check is None:
            raise ValueError(f"No upstream for branch {branch}")
        upstream_check = upstream_check.strip()
        if "fatal: no upstream" not in upstream_check:
            # Get ahead/behind counts
            counts = await arun(
                [
                    "git",
                    "rev-list",
                    "--left-right",
                    "--count",
                    f"{branch}...{upstream_check}",
                ],
                show=False,
            )
            if counts and len(counts.strip().split()) == 2:
                ahead, behind = counts.strip().split()
                if int(ahead) > 0:
                    tracking_info += f"[gold1]ahead of '{upstream_check}' by {ahead} commit{'s' if int(ahead) > 1 else ''}[/gold1]"

                    # Get files changed in ahead commits
                    try:
                        diff_files = await arun(
                            [
                                "git",
                                "diff",
                                "--name-only",
                                f"{upstream_check}..{branch}",
                            ],
                            show=False,
                        )
                        if diff_files:
                            ahead_files = [
                                f for f in diff_files.strip().split("\n") if f
                            ]
                    except Exception:
                        pass

                if int(behind) > 0:
                    if tracking_info:
                        tracking_info += "\n"
                    tracking_info += f"[bold red]behind '{upstream_check}' by {behind} commit{'s' if int(behind) > 1 else ''}[/bold red]"
    except Exception as e:
        from mbcore.log import debug

        debug(f"Error getting tracking info: {e}", stacklevel=3, stack_info=True)

    # Get file statuses
    local_changes = await get_status_summary(await get_git_status())

    # Build title with branch name
    title = f"\n[bold white]ON BRANCH [bold green]{branch}[/bold green][/bold white]"
    if tracking_info:
        title += f"\n\n{tracking_info}"
    console_width = getconsole().width // 2
    # Create main table
    title_table = Table(
        title=title,
        show_header=True,
        header_style="bold white",
        box=NO_BOX,
        border_style="",
        show_lines=False,
        width=console_width,
        padding=0,
        pad_edge=False,
    )

    # Add columns
    title_table.add_column("Status", header_style="bold blue", width=console_width)
    title_table.add_column("File", header_style="bold green", width=console_width)
    header = [title_table]
    tables = []
    # Add files section if local changes exist
    if local_changes:
        # Add section header
        local_table = Table(
            title="[bold green]since[/bold green] [bold white]LAST COMMIT[/bold white]",
            box=NO_BOX,
            border_style="",
            show_lines=False,
            width=console_width,
            padding=0,
            pad_edge=False,
        )
        # Combine STAGED and STAGED_DELETE for unified display
        staged_files = local_changes.pop(GitStatus.STAGED, [])
        staged_delete_files = local_changes.pop(GitStatus.STAGED_DELETE, [])
        # Store as (status_enum, filename_string) tuples
        combined_staged = [(GitStatus.STAGED, f) for f in staged_files] + [
            (GitStatus.STAGED_DELETE, f) for f in staged_delete_files
        ]

        # Keep track if we add any rows to the table
        table_has_rows = False

        if combined_staged:
            table_has_rows = True
            # Add combined staged files first
            for i, (status_type, filename) in enumerate(combined_staged):
                local_table.add_row(
                    "staged" if i == 0 else "",  # Use single "staged" label
                    *status_type.withstyle(
                        str(filename), fp=str(filename)
                    ),  # Apply correct color
                )

        # Add remaining non-staged local changes
        for (
            k,
            v,
        ) in (
            local_changes.items()
        ):  # Now iterates through MODIFY, REMOVE, UNTRACKED, etc.
            table_has_rows = True
            for i, filename in enumerate(v):
                local_table.add_row(
                    str(k) if i == 0 else "",  # Use original labels for others
                    *k.withstyle(str(filename), fp=str(filename)),
                )

        # Only add the table if it has rows (either combined staged or others)
        if table_has_rows:
            tables.append(local_table)

    # Add ahead files section if any exist
    if ahead_files:
        # Add section header
        ahead_table = Table(
            title="\n[bold green]since[/bold green] [bold white]LAST PUSH[/bold white]",
            box=NO_BOX,
            border_style="",
            show_lines=False,
            width=console_width,
            padding=0,
            pad_edge=False,
        )

        ahead_table.add_column("Status", header_style="bold blue")
        ahead_table.add_column("File", header_style="bold green", justify="left")

        # Get commit information for ahead files
        try:
            for i, file in enumerate(ahead_files[:5]):
                # For ahead files, just show the commit hash without GitHub links
                # since these commits haven't been pushed yet
                if i == 0:
                    # Get commit info for the first row only
                    commit_info = await arun(
                        ["git", "log", "--format=%h:%s", "--max-count=1", "--", file],
                        show=False,
                    )
                    if commit_info and ":" in commit_info:
                        hash_part, msg_part = commit_info.split(":", 1)
                        status_text = f"[bold blue]{hash_part}[/bold blue]: [gold1]{msg_part.strip()[:20]}{'...' if len(msg_part) > 20 else ''}[/gold1]"
                    else:
                        status_text = "[bold blue]unpushed[/bold blue]"
                else:
                    status_text = ""  # Empty status for rows after the first

                # Style filename in gold to indicate it's ahead of remote
                file_text = f"[dim gold1]{file}[/dim gold1]"
                ahead_table.add_row(status_text, file_text)

            # Show count if more than 10 files
            if len(ahead_files) > 10:
                ahead_table.add_row(
                    "", f"[dim]...and {len(ahead_files) - 5} more files[/dim]"
                )
        except Exception as e:
            debug(f"Error displaying ahead files: {e}")
            ahead_table.add_row(
                "[bold red]Error[/bold red]",
                f"[red]Failed to get commit info: {str(e)}[/red]",
            )

        tables.append(ahead_table)

    return header + tables if tables else []


class GitContext:
    def __init__(
        self,
        cwd: str | Path | None = None,
        repo: str | None = None,
        branch: str | None = None,
        console: Console | None = None,
        autoyes: bool | None = None,
    ):
        self.cwd = Path(str(cwd)) if cwd else Path.cwd()
        self.repo = repo or sync_get_repo_root()
        # Ensure we get a valid branch name
        self.branch = branch or sync_get_branch()
        self.console = console or getconsole()
        self.tmp_branch = f"{self.branch}-tmp-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.autoyes = autoyes

    async def __aenter__(self, autoyes=False) -> "GitContext":
        from mbpy.git.check import handle_new_branch

        self.console = self.console or getconsole()
        self.cwd = self.cwd or Path.cwd()
        self.out = await handle_new_branch(self.tmp_branch)
        self.autoyes = autoyes
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if exc:
            import traceback

            traceback.print_exc()
            safe_print(f"An error occurred: {str(exc)}")

        if haserr(self.out):
            from mbpy.git.check import handle_clean_up, handle_checkout_merge

            return await handle_clean_up(
                tmp_branch=self.tmp_branch, branch=self.branch, err=self.out.msg
            )
        from mbpy.git.check import handle_checkout_merge

        out = await handle_checkout_merge(
            self.branch, self.tmp_branch, confirm=bool(self.autoyes)
        )

        if haserr(out):
            safe_print(out)
            return False
        return None

    async def run(self, cmd: list[str] | str, show=False) -> str:
        return await arun(cmd, cwd=self.cwd, show=show, console=self.console)


def git_print(output: str) -> None:
    ansi = "\x1b["
    bold = "1;37m"
    red_code = "31m"
    green_code = "32m"
    yellow_code = "33m"
    cyan_code = "36m"
    blue_code = "34m"
    unset = "0m"
    state = GitState.Local.UNKNOWN
    getspinner().stop()
    for line in output.splitlines():
        if "Untracked files" in line:
            raw_print(f"{ansi}{bold}{line}{ansi}{unset}")

            state = GitState.Local.UNTRACKED
            continue
        if "failed" in line.lower():
            raw_print(f"{ansi}{red_code}{line}{ansi}{unset}")
        if "Changes not staged for commit" in line:
            raw_print(f"{ansi}{bold}{line}{ansi}{unset}")
            state = GitState.Local.DIRTY

            continue
        if "Changes to be committed" in line:
            state = GitState.Local.DIRTY
            raw_print(f"{ansi}{bold}{line}{ansi}{unset}")
            continue
        if "Your branch is ahead of" in line:
            state = GitState.Remote.AHEAD
            raw_print(f"{ansi}{bold}{line}{ansi}{unset}")
            continue
        if "Your branch is behind" in line:
            state = GitState.Remote.BEHIND
            raw_print(f"{ansi}{bold}{line}{ansi}{unset}")
            continue
        if state == GitState.Local.UNTRACKED:
            raw_print(f"{ansi}{red_code}{line}{ansi}{unset}")
        elif state == GitState.Local.DIRTY:
            raw_print(f"{ansi}{green_code}{line}{ansi}{unset}")
        elif state == GitState.Remote.AHEAD:
            raw_print(f"{ansi}{cyan_code}{line}{ansi}{unset}")
        elif state == GitState.Remote.BEHIND:
            raw_print(f"{ansi}{blue_code}{line}{ansi}{unset}")
        else:
            raw_print(f"{ansi}{unset}{line}")


_repo_root = None


async def get_repo_root(path: str | Path | None = None):
    path = path or Path.cwd()
    global _repo_root
    if not _repo_root:
        # Import arun locally to avoid circular imports
        from mbpy.cmd import arun as local_arun

        result = await local_arun(["git", "rev-parse", "--show-toplevel"], show=False)
        _repo_root = result.strip()
    return _repo_root


def haserror(output: str) -> bool:
    return any(c in output.lower() for c in ["error", "fatal", "rejected"])


def sync_get_repo_root() -> str:
    global _repo_root
    if not _repo_root:
        from mbpy.cmd import run

        result = run(["git", "rev-parse", "--show-toplevel"], show=False)
        _repo_root = result.strip()
    return _repo_root


async def arun(
    cmd_args: List[str] | str,
    cwd: "str |Path| None" = None,
    show=False,
    console=None,
    columns=False,
) -> str:
    """Runs a command asynchronously. If it fails, we raise RuntimeError.

    Returns combined stdout+stderr as a string.
    """  # noqa: D401
    import shlex

    # Convert cwd to Path if it's a string
    if cwd and not isinstance(cwd, Path):
        cwd = Path(str(cwd))

    # Get repo root only if cwd is None
    if cwd is None:
        try:
            cwd = Path(await get_repo_root())
        except Exception as e:
            debug(f"Error getting repo root: {e}")
            cwd = Path.cwd()  # Fall back to current directory

    console = console or getconsole()
    cmd_args = cmd_args if isinstance(cmd_args, list) else shlex.split(cmd_args)

    if columns:
        cmd_args += ["|", "column", "-x"] if "column" not in cmd_args else []

    try:
        if verbose():
            safe_print(f"[dim]$ {' '.join(cmd_args)}[/dim]")

        # Only check if cwd exists if it's not None
        if cwd and not cwd.exists():
            debug(f"Directory not found: {cwd}")
            raise FileNotFoundError(f"Directory not found: {cwd}")

        # Convert Path to string for arun_command
        cwd_str = str(cwd) if cwd else None
        debug(f"Running command in directory: {cwd_str}")

        async with await arun_command(cmd_args, cwd=cwd_str) as process:
            output = await process.areadtext()

        return output

    except Exception as e:
        getspinner().stop()
        safe_print(f"[red]Error:[/red] {str(e)}")
        raise


async def get_branch() -> str:
    global _branch
    if _branch is None:
        _branch = (
            await arun(["git", "rev-parse", "--abbrev-ref", "HEAD"], show=False)
        ).strip()

    return _branch


def sync_get_branch() -> str:
    global _branch
    if _branch is None:
        from mbpy.cmd import run

        _branch = (
            run(["git", "rev-parse", "--abbrev-ref", "HEAD"], show=False)
        ).strip()
    return _branch


def sync_get_upstream(branch: str | None = None) -> str | None:
    global _upstream
    if _upstream is None:
        from mbpy.cmd import run

        _upstream = (
            run(
                ["git", "rev-parse", "--abbrev-ref", f"{branch}@{{upstream}}"],
                show=False,
            )
        ).strip()
    return _upstream


async def get_upstream(branch: str | None = None) -> str | None:
    global _upstream
    if _upstream is None:
        if branch is None:
            branch = await get_branch()
        if branch is None:
            raise ValueError("No branch found")
        _upstream = (
            await arun(
                ["git", "rev-parse", "--abbrev-ref", f"{branch}@{{upstream}}"],
                show=False,
            )
        ).strip()
    return _upstream


async def get_remotes() -> list[str]:
    global _remotes
    if _remotes is None:
        _remotes = (await arun(["git", "remote"])).strip().splitlines()
    return _remotes


def sync_get_remotes() -> list[str]:
    global _remotes
    if _remotes is None:
        from mbpy.cmd import run

        _remotes = run(["git", "remote"]).strip().splitlines()
    return _remotes


def sync_get_repo_info() -> tuple[str | None, str | None, str | None]:
    global _repo_url, _org, _repo
    if _repo_url is None:
        from mbpy.cmd import run

        try:
            repo_info = run(["git", "remote", "get-url", "origin"], show=False)
            if not repo_info.strip():
                # No output means no remote origin is configured
                from mbcore.log import warning

                warning(
                    "No remote origin configured - using default values", stacklevel=2
                )
                _owner = "mbodiai"
                _repo = "mbcore"
                _repo_url = f"https://github.com/{_owner}/{_repo}"
                return _repo_url, _owner, _repo

            if "github.com" in repo_info:
                if repo_info.startswith("git@"):
                    parts = (
                        repo_info.replace("git@github.com:", "")
                        .replace(".git", "")
                        .strip()
                        .split("/")
                    )
                else:
                    parts = (
                        repo_info.replace("https://github.com/", "")
                        .replace(".git", "")
                        .strip()
                        .split("/")
                    )

                if len(parts) >= 2:
                    _owner = parts[0]
                    _repo = parts[1]
                    _repo_url = f"https://github.com/{_owner}/{_repo}"

            # If we couldn't extract info from the remote URL, fall back to defaults
            if _repo_url is None:
                # Look at the directory name as a fallback
                import os
                from pathlib import Path

                current_dir = Path(os.getcwd()).name
                if current_dir:
                    _repo = current_dir
                    _owner = "mbodiai"  # Default owner
                    _repo_url = f"https://github.com/{_owner}/{_repo}"
                else:
                    from mbcore.log import error

                    error(
                        f"Failed to get repository info: {repo_info}",
                        stacklevel=2,
                        stack_info=True,
                    )
                    raise ValueError(f"Failed to get repository info: {repo_info}")
        except Exception as e:
            from mbcore.log import error

            error(
                f"Error in sync_get_repo_info: {str(e)}", stacklevel=2, stack_info=True
            )
            # Fallback to default values
            _owner = "mbodiai"
            _repo = "mbcore"
            _repo_url = f"https://github.com/{_owner}/{_repo}"

    return _repo_url, _org, _repo


class GitStatus(StrEnum):
    ADD = "add"
    MODIFY = "modify"
    REMOVE = "remove"
    RENAME = "rename"
    UNTRACKED = "untracked"
    STAGED = "staged"
    STAGED_DELETE = "staged_delete"
    UNMERGED = "unmerged"
    PUSHED = "pushed"
    STASHED = "stashed"
    IGNORED = "ignored"
    CLEAN = "clean"

    def __str__(self) -> str:
        if self == GitStatus.ADD:
            return "added"
        if self == GitStatus.MODIFY:
            return "modified"
        if self == GitStatus.REMOVE:
            return "removed"
        if self == GitStatus.RENAME:
            return "renamed"
        if self == GitStatus.UNTRACKED:
            return "untracked"
        if self == GitStatus.STAGED:
            return "staged"
        if self == GitStatus.STAGED_DELETE:
            return "staged"
        return "unknown"

    def withstyle(self, line: str, fp: str | Path | None = None) -> list[str]:
        """Apply git-like color styling to status entries."""
        if self == GitStatus.MODIFY:
            # User requested magenta for modified
            style = "magenta"
        elif self == GitStatus.RENAME:
            style = "bright_blue"  # Git uses blue for renames
        elif self == GitStatus.UNTRACKED:
            # User requested cyan for untracked
            style = "cyan"
        elif self == GitStatus.REMOVE:
            style = "bright_red"  # Git uses red for deleted
        elif self == GitStatus.ADD:
            style = "bright_green"  # Git uses green for added
        elif self == GitStatus.STAGED:
            style = "bright_green"  # Git uses green for staged
        elif self == GitStatus.STAGED_DELETE:
            style = "bright_red"  # Color staged deletes red

        style = f"bold {style}" if line.endswith("...") else style
        if fp:
            fp = Path(str(fp))
            from mbcore._traceback import link_fp

            # Handle path without replacing 'M', and preserve quotes for paths with spaces
            file_parts = []
            # Keep the line intact, just strip whitespace
            cleaned_line = line.strip()
            # If the line is quoted, handle it as a single entity
            if cleaned_line.startswith('"') and cleaned_line.endswith('"'):
                file_parts = [cleaned_line]
            else:
                file_parts = cleaned_line.split(" ")

            return [
                link_fp(m, m.removesuffix("..."), lineno=1, showpath=False, style=style)
                for m in file_parts
            ]  # type: ignore
        return [f"[{style}]{line}[/{style}]"]


async def get_git_state() -> GitState:
    from mbpy.cmd import run

    state = GitState.from_msg(run(["git", "status"], show=False))
    return state

_git_status = None

async def get_git_status() -> dict[str, GitStatus]:
    """Parses git status --porcelain output and returns a dictionary of file statuses."""
    global _git_status
    if _git_status:
        return _git_status
    status: dict[Path, GitStatus] = {}

    from mbcore.log import debug, warning  # Import warning

    try:
        cmd = ["git", "status", "--porcelain=v1", "-uall"]
        lines = (await arun(cmd)).splitlines()

        status: dict[Path, GitStatus] = {}
        for line in lines:
            if not line.strip():
                continue
            status_code = line[:2]
            filepath_part = line[3:]
            if len(status_code) != 2 or not line[2:3] == " ":
                continue
            final_status: GitStatus | None = None
            if status_code in [" M", "MM"]:
                final_status = GitStatus.MODIFY
            elif status_code == " D":
                final_status = GitStatus.REMOVE
            elif status_code == "??":
                final_status = GitStatus.UNTRACKED
            elif status_code == "A ":
                final_status = GitStatus.STAGED
            elif status_code == "R ":
                final_status = GitStatus.RENAME
            elif status_code == "C ":
                final_status = GitStatus.STAGED
            elif status_code == "D ":  # Handle Staged Deletes
                final_status = GitStatus.STAGED_DELETE
            elif status_code == "U":
                final_status = GitStatus.UNMERGED
            elif status_code == "P":
                final_status = GitStatus.PUSHED
            elif status_code == "S":
                final_status = GitStatus.STASHED
            elif status_code == "!":
                final_status = GitStatus.IGNORED
            elif status_code == " ":
                final_status = GitStatus.CLEAN
            elif status_code == "DD":
                final_status = GitStatus.REMOVE

            if final_status:
                filepath = filepath_part  # Needs rename handling
                if "\0" in filepath_part and status_code[0] in ("R", "C"):
                    _orig, filepath = filepath_part.split("\0", 1)
                filepath = filepath.strip()
                # Remove any surrounding quotes from filepath
                if filepath.startswith('"') and filepath.endswith('"'):
                    filepath = filepath[1:-1]
                if filepath:
                    status[Path(filepath)] = final_status

        # --- Start Chunking and Post-Processing ---
        from collections import defaultdict
        import os  # For path manipulation

        # 1. Build a tree structure of files and their statuses
        file_tree = {}
        # Sort paths to ensure parent directories are processed before children
        for file_path, file_status in sorted(status.items(), key=lambda x: str(x[0])):
            path_parts = str(file_path).split(os.sep)
            current = file_tree
            # Build tree structure
            for i, part in enumerate(path_parts):
                if i == len(path_parts) - 1:  # Leaf node (actual file)
                    current[part] = file_status
                else:
                    if part not in current:
                        current[part] = {}
                    current = current[part]

        # 2. Function to check if a subtree has all identical statuses
        def check_uniform_status(subtree, min_files=5):
            """Check if all files in subtree have identical status and count them."""
            if not isinstance(subtree, dict):
                return True, 1, subtree  # Leaf node (file)

            files_count = 0
            status_set = set()

            for _, value in subtree.items():
                is_uniform, count, status_value = check_uniform_status(value, min_files)
                if not is_uniform:
                    return False, 0, None  # Non-uniform child
                files_count += count
                status_set.add(status_value)

            # Return if ALL files have the same status
            if len(status_set) == 1:
                return True, files_count, next(iter(status_set))
            return False, 0, None

        # 3. Function to build final status dict with collapsing
        def build_status_dict(subtree, path="", min_files=20):
            """Build the status dictionary with directory collapsing."""
            result = {}

            is_uniform, files_count, uniform_status = check_uniform_status(
                subtree, min_files
            )

            # If uniform with enough files, collapse
            if is_uniform and files_count >= min_files and path:
                collapsed_path = f"{path}/..."
                result[collapsed_path] = uniform_status
                return result

            # Otherwise process individually
            if isinstance(subtree, dict):
                for name, value in subtree.items():
                    child_path = f"{path}/{name}" if path else name
                    if not isinstance(value, dict):  # Leaf node
                        result[child_path] = value
                    else:  # Directory
                        child_result = build_status_dict(value, child_path, min_files)
                        result.update(child_result)

            return result

        # 4. Build final status dict with appropriate collapsing
        processed_status = build_status_dict(
            file_tree, "", 20
        )  # Adjust the threshold as needed

        # 5. Format result properly (handle quotes for spaces, etc.)
        final_status_dict = {}
        for path_str, file_status in processed_status.items():
            # Handle files with spaces by adding quotes
            if " " in path_str:
                path_str = f'"{path_str}"'
            final_status_dict[path_str] = file_status

        merged = final_status_dict
        # --- End Chunking and Post-Processing ---

    except Exception as e:
        # Ensure debug import is available if needed
        from mbcore.log import debug, warning  # Use warning

        if debug():
            import traceback

            traceback.print_exc()
        warning(f"Failed to get git status: {str(e)}")  # Use warning log
        merged = {}  # Return empty on error

    # Final result uses string keys
    return merged
