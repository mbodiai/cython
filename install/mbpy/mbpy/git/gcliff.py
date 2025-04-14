from mbcore.display import getspinner
from mbcore.more import unique_everseen
from mbpy import PINK
from mbpy.cli import get_help_config
from mbpy.cmd import arun_command
from mbpy.expect.asyncspawn import AsyncSpawn
from mbpy.git.state import get_repo_root
from mbpy.git.check import (
    GitState,
    GitStatus,
    add_untracked,
    display_status_summary,
    get_branch,
    get_git_status,
)
from rich.text import Text
from mbcore.log import error, debug
from mbpy.cmd import arun


try:
    from typing_extensions import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False

if TYPE_CHECKING:
    from typing import Any

    import rich_click as click
    from mbcore.display import safe_print
    from mbpy.cli import base_args
    from mbpy.git.changelog import Granularity
else:
    import rich_click as click
    from mbcore.display import safe_print
    from mbpy.cli import base_args
    from mbpy.git.changelog import Granularity

    Any = object


class Anything:
    __call__ = __getitem__ = lambda *args, **kwargs: Anything()
    __getattr__ = classmethod(lambda *args, **kwargs: Anything())

    def __iter__(self):
        return iter([])


def haserr(output: str) -> bool:
    if not isinstance(output, str):
        return False
    out = any(c.lower() in output.lower() for c in ["error", "fatal", "abort"])
    if debug() and out:
        import traceback

        traceback.print_exc()
        safe_print(f"[bold red]Error in output: {output}[/bold red]")
    return out


async def get_log_date(days: int) -> str:
    """Get the correct date format for git log."""
    from datetime import datetime, timedelta

    date = datetime.now() - timedelta(days=days)
    return date.strftime("%Y-%m-%d")


async def undo_last_commit() -> bool:
    from mbcore.display import safe_print
    from mbcore.import_utils import smart_import
    from mbcore.log import debug
    from mbpy.git.state import arun

    console = smart_import("mbcore.display.getconsole")()
    try:
        last_hash = await arun(["git", "rev-parse", "HEAD"])
        if not last_hash:
            console.print("[yellow]No commits to undo[/yellow]")
            return False
        out = await arun(["git", "reset", "--soft", "HEAD~1"])
        if haserr(out):
            raise Exception(out)
        safe_print(f"[green]Successfully undid last commit ({last_hash[:7]})[/green]")
        safe_print("[dim]Changes are still staged in your working directory[/dim]")
        return True
    except Exception as e:
        if debug():
            raise
        safe_print(f"[red]Failed to undo last commit: {str(e)}[/red]")
        return False


async def git_add_commit_push(
    branch: "str | None" = None,
    remote=None,
    dry_run: bool = False,
    commit=False,
    push=False,
    args=None,
    autoyes: bool = False,
    skip_submodules: bool = False,
) -> "GitState":
    from mbpy.git.state import arun
    from mbpy.git.check import check_state, resolve_state

    branch = branch or await arun(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    remote = remote or "origin"
    state = await check_state(branch)

    if commit:
        # If args is a string or a tuple with a single string, use it as the commit message
        commit_msg = (
            args[0] if isinstance(args, (tuple, list)) and len(args) > 0 else None
        )
        # Properly escape the commit message
        if commit_msg:
            commit_msg = f'"{commit_msg}"'
        return await resolve_state(
            branch,
            action="commit",
            dry_run=dry_run,
            args=(commit_msg,),
            autoyes=autoyes,
            skip_submodules=skip_submodules,
        )

    if push and "operation canceled" not in state.msg:
        return await resolve_state(
            state.branch,
            "push",
            dry_run=dry_run,
            args=args,
            autoyes=autoyes,
            skip_submodules=skip_submodules,
        )
    return state


async def intelligently_list_files_and_branches(
    branches: bool = True, files: bool = True
) -> None:
    """Print a list of branches and recently changed files in each branch along with commit timestamps."""
    from pathlib import Path

    from mbcore.display import safe_print

    from mbpy.git.state import arun

    safe_print(
        f"\n[bold white]CURRENT BRANCH: [bold green]{await arun(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])}[/bold green]\n[/bold white]"
    )
    try:
        # Show filenames with timestamps across all branches
        safe_print("\n[bold white]LATEST FILE CHANGES:[/bold white]")
        out = await arun(
            [
                "git",
                "log",
                "--pretty=format:%H %ad %s",
                "--date=format:%Y-%m-%d %H:%M",
                "--name-only",
                "-n",
                "10",
            ]
        )
        if out:
            n = 3
            for i, line in enumerate(out.splitlines()[1:]):
                if i > n:
                    break
                if not line:
                    continue
                if Path(line).exists():
                    if Path(line).is_absolute():
                        line = Path(line).relative_to(
                            Path(await get_repo_root()).resolve()
                        )
                    safe_print(f"\t{line}")
                else:
                    safe_print(f"[dim]{line}[/dim]")

        # Show branch info with timestamps - FIXED FORMAT STRING
        if branches:
            safe_print("\n[bold white]LATEST BRANCHES:[/bold white]")
            for branch_type in ["heads", "remotes"]:
                out = await arun(
                    [
                        "git",
                        "for-each-ref",
                        f"refs/{branch_type}/",
                        "--sort=-committerdate",
                        '--format="%(committerdate:format:%m-%d %H:%M) - %(refname:short)"',
                    ]
                )
                if out:
                    safe_print(
                        f"\n[bold gray15]{branch_type.title().upper()}:[/bold gray15]"
                    )
                    for line in out.splitlines():
                        if line.strip():
                            safe_print(f"{line}")

        # Show compact diff stats
        if files:
            safe_print("\n[bold gray15]RECENT CHANGES[/bold gray15]")
            out = await arun(["git", "diff", "--stat", "--color"])
            if out:
                safe_print(Text.from_ansi(out))
        safe_print("")

    except Exception as e:
        safe_print(f"[red]Error listing git info: {str(e)}[/red]")


async def git_search_across_org(term: str) -> None:
    """Search for a term across all repositories in an organization."""
    from mbpy.cmd import arun

    out = ""
    try:
        # Search across all branches with context
        out = await arun(["git", "rev-list", "--all"])
        if out:
            for commit in out.splitlines()[:10]:
                details = await arun(
                    [
                        "git",
                        "log",
                        "-1",
                        '--pretty="format:%C(yellow)%h%Creset %C(green)%ad%Creset [%C(magenta)%an%Creset] %C(cyan)(%ar)%Creset%n%w(0,4,4)%B"',
                        "--date=short",
                        commit,
                    ]
                )
                # Use color option to highlight matches
                files = await arun(
                    [
                        "git",
                        "grep",
                        "-n",
                        "--heading",
                        "--break",
                        "--context=2",
                        term,
                        commit,
                    ]
                )
                if files:
                    branch_name = await arun(["git", "name-rev", "--name-only", commit])
                    safe_print(f"\n[bold blue]{branch_name.strip()}:[/bold blue]")
                    safe_print(details)
                    safe_print("\n[dim]---[/dim]")
                    safe_print()

        # Search in current state with highlighting
        async for line in await arun_command(
            ["git", "grep", "-n", "--heading", "--break", "--context=2", term]
        ):
            safe_print(line)

    except Exception as e:
        safe_print(f"[red]Error searching repositories: {str(e)}[/red]")


async def git_diff_detailed(commit_hash: str = "HEAD") -> None:
    """Show detailed diff information for a specific commit."""
    from mbcore.display import safe_print

    from mbpy.git.state import arun

    try:
        # Get the basic diff stats
        safe_print(f"\n[bold blue]Diff stats for {commit_hash}:[/bold blue]")
        out = await arun(["git", "diff", "--stat", f"{commit_hash}~1..{commit_hash}"])

        out = await AsyncSpawn(
            [
                "git",
                "log",
                "--name-status",
                '--format="%h %ad %s"',
                "--date=iso",
                "-n",
                "1",
                commit_hash,
            ]
        ).areadtext()
        if out:
            safe_print(out)

    except Exception as e:
        safe_print(f"[red]Error showing diff: {str(e)}[/red]")


EXAMPLES = """ **Examples:**

    ```bash

        # Add, commit, pull, rebase resolving conflicts in new branch and cleaning up.\n

        mb git -p\n

        # Generate a changelog for last 7 days with module or function-level specificity.\n

        mb git changelog --days 7 --output CHANGELOG.md --granularity function\n

        # Undo last commit\n

        mb git undo\n

        # List branches and recent changes\n
        
        mb git -l\n
"""


@click.command("git", no_args_is_help=False, epilog=EXAMPLES)
@click.rich_config(
    help_config=get_help_config(style_helptext=f"{PINK}", text_markup="markdown")
)
@click.argument(
    "subcommand",
    type=click.Choice(
        [
            "add",
            "search",
            "push",
            "pull",
            "status",
            "undo",
            "branch",
            "changelog",
            "reset",
            "switch",
            "ignore",
            "diff",
            "commit",
        ],
        case_sensitive=False,
    ),
    required=False,
)
@click.option(
    "-s", "--status", is_flag=True, help="Check status and auto-resolve conflicts"
)
@click.option("-b", "--branch", type=str, is_flag=True, help="Switch to a new branch")
@click.option("-u", "--undo", is_flag=True, help="Undo last commit")
@click.option("-p", "--push", is_flag=True, help="Push changes to remote")
@click.option("-l", "--list", is_flag=True, help="List branches and recent changes")
@click.option("-cl", "--change-log", is_flag=True, help="Generate changelog")
@click.option("--days", type=int, default=30)
@click.option("--output", type=click.Path(), help="Output file for changelog")
@click.option("--show-code", is_flag=True, help="Show code changes in changelog")
@click.option("--overwrite", is_flag=True)
@click.option("--dry-run", is_flag=True)
@click.option(
    "--yes", "-y", is_flag=True, help="Automatically answer yes to all prompts"
)
@click.option("--max-changes", type=int)
@click.option(
    "--granularity",
    type=click.Choice([g.value for g in Granularity], case_sensitive=False),
    default=Granularity.MODULE.value,
    help="Module,file,function-level granularity. In change and commit logs",
)
@click.argument("args", nargs=-1, type=click.UNPROCESSED, required=False)
@click.pass_context
@base_args
async def main(
    ctx: click.Context,
    subcommand: str,
    status: bool,
    branch: str,
    days: int,
    output: str,
    show_code: bool,
    overwrite: bool,
    dry_run: bool,
    max_changes: int,
    undo: bool,
    push: bool,
    granularity: str,
    list: bool,
    change_log: bool,
    yes: bool,
    args: tuple,
    **kwargs: Any,
):
    r"""Streamlined git workflow with automatic conflict resolution."""
    # Ensure necessary functions are imported within this scope
    from mbcore.log import error
    from mbpy.cmd import arun

    try:
        from pathlib import Path
        import aiofiles
        from mbcore.ctx import chdir
        from mbpy.git.changelog import Granularity, generate_changelog
        from mbpy.git.check import get_diff, handle_new_branch, handle_pull

        didpush = subcommand == "push" or push or "push" in args
        didcommit = subcommand == "commit" or "commit" in args
        didlist = subcommand == "list" or list or "list" in args
        didundo: bool = subcommand == "undo" or undo or "undo" in args
        didpull: bool = subcommand == "pull" or "pull" in args
        didswitch: bool = subcommand == "switch" or "switch" in args
        didstatus = subcommand == "status" or status or "status" in args
        didbranch = subcommand == "branch" or branch or "branch" in args
        didsearch = subcommand == "search" or "search" in args
        didchangelog = (
            subcommand == "changelog"
            or change_log
            or "changelog" in args
            or "cl" in args
        )
        didadd = subcommand == "add" or "add" in args
        didignore = subcommand == "ignore" or "ignore" in args
        diddiff = subcommand == "diff" or "diff" in args
        didstash = subcommand == "stash" or "stash" in args

        try:
            check_output = await arun(
                ["git", "rev-parse", "--is-inside-work-tree"], show=False
            )
            if check_output.strip() != "true":
                error("Not a git repository (or any of the parent directories): .git")
                return None
        except Exception as e:
            if "No such file or directory" in str(e) or "command not found" in str(e):
                error(
                    f"Git command not found. Please ensure Git is installed and in your PATH."
                )
            else:
                error(f"Not a git repository: {e}")
            return None

        if didchangelog:
            await generate_changelog(
                days,
                branch,
                show_code,
                overwrite,
                dry_run,
                granularity=Granularity(granularity),
                max_changes=max_changes,
            )
            return None
        if didsearch:
            await git_search_across_org(*(args + tuple(ctx.args or ())))
            return None
        if didbranch:
            await intelligently_list_files_and_branches(branches=True, files=True)

            return None
        if didstatus:
            branch_name = await get_branch()
            file_status = await get_git_status()

            if len(file_status) > 0:
                # If there are changes, display them nicely
                tables = await display_status_summary(file_status)
                if tables:
                    for table in tables:
                        safe_print(table)
                else:
                    safe_print(
                        f"[bold white]\n\nChanges found on branch [italic green]{branch_name}[/italic green]:[/bold white]"
                    )
                    for fp, st in file_status.items():
                        # Map status to appropriate colors
                        if status == GitStatus.MODIFY:
                            color = "magenta"
                        elif status == GitStatus.ADD:
                            color = "green"
                        elif status == GitStatus.REMOVE:
                            color = "red"
                        elif status == GitStatus.RENAME:
                            color = "blue"
                        elif status == GitStatus.UNTRACKED:
                            color = "yellow"
                        elif status == GitStatus.STAGED:
                            color = "cyan"
                        else:
                            color = "white"
                        safe_print(f"[{color}]{fp} ({str(st)})[/{color}]")
            else:
                # Only if there are truly no changes
                safe_print(
                    f"[bold white]\n\nNo changes found on branch [italic green]{branch_name}[/italic green]\n[/bold white]"
                )

            return None

        if didswitch:
            branch = branch or next(iter(args), "")
            out = await handle_new_branch(branch)
            if out.error:
                out = await git_add_commit_push(
                    branch,
                    dry_run=dry_run,
                    push=push,
                    commit=True,
                    args=args,
                    autoyes=yes,
                )
                cmd = "git checkout -b"
                out = await arun(f"{cmd} {branch}")
                if haserr(out):
                    safe_print(f"[red]Error: {out}[/red]")
                safe_print(f"[green]Switched to branch {branch}[/green]")
        if didcommit:
            await git_add_commit_push(
                branch, dry_run=dry_run, push=push, commit=True, args=args, autoyes=yes
            )

        if didlist:
            await intelligently_list_files_and_branches(branches=True, files=True)
            return None

        if diddiff:
            branch = branch or next(iter(args), "")
            await get_diff(branch=branch, show=True)
            return None

        if didundo:
            await undo_last_commit()
            return None

        if dry_run:
            safe_print("[yellow]DRY RUN - No changes will be made[/yellow]\n")
            getspinner().start()

        if didignore:
            extras = ctx.params.get("args", ())
            with chdir(await get_repo_root()):
                if not Path(".gitignore").exists():
                    Path(".gitignore").touch(exist_ok=True)
                async with aiofiles.open(".gitignore", "r+") as f:
                    text = await f.readlines()
                    await f.seek(0)
                    lines = "".join(
                        filter(bool, unique_everseen(text + [f"{x}\n" for x in extras]))
                    )
                    await f.write(lines)
                await git_add_commit_push(
                    branch,
                    dry_run=dry_run,
                    push=push,
                    commit=True,
                    args=args,
                    autoyes=yes,
                )

            safe_print(f"[green]Added to .gitignore: {' '.join(extras)}[/green]")
            return None
        if didadd:
            extras = ctx.params.get("args", ())
            if not any(extras):
                return await add_untracked()

            cmd = ["git", "add", *extras]
            await arun(cmd, show=True)
            return None

        if didpush or didstash:
            return await git_add_commit_push(
                branch,
                dry_run=dry_run,
                push=didpush,
                commit=didcommit,
                args=args,
                autoyes=yes,
            )

        if didpull:
            return await handle_pull(branch)

        if didchangelog:
            changelog = await generate_changelog(
                days,
                branch,
                show_code,
                overwrite,
                dry_run,
                granularity=Granularity(granularity),
                max_changes=max_changes,
            )

            if not changelog.strip():
                safe_print(
                    "[yellow]No changes found in the specified time period[/yellow]"
                )
                return None

            output = output or "CHANGELOG.md"

            if output:
                async with aiofiles.open(output, "w") as f:
                    await f.write(changelog)
                safe_print(f"[green]Changelog written to {output}[/green]")
            else:
                from rich.markdown import Markdown

                safe_print(Markdown(changelog))
        if args:
            out = await arun(f"git {subcommand} {' '.join(args)}")
            if haserr(out):
                safe_print(f"[red]Error: {out}[/red]")
            safe_print(out)
    except Exception as e:
        from mbcore.log import debug

        if debug():
            raise
        safe_print(f"[red]Error generating changelog: {str(e)}[/red]")
    finally:
        # Add this to your main CLI function before it exits
        try:
            loop = asyncio.get_event_loop()
            if not loop.is_closed():
                loop.close()
        except Exception:
            pass


if __name__ == "__main__":
    import asyncio
    import sys

    from mbpy.git.check import check_state

    branch = next(iter(sys.argv[1:]))
    if branch.startswith("-"):
        branch = None
    asyncio.run(check_state(branch))
