import ast
import collections
import os
import re
from datetime import datetime
from typing import Dict, List

from mbcore.display import getspinner, getconsole
from mbcore.more import unique_everseen
from mbpy.git.analyze import (
    ChangeMetric,
    DiffStats,
    Granularity,
    ModuleChanges,
    analyze_module_changes,
    get_diff_stats,
)
from mbpy.git.state import arun, get_repo_root

console = getconsole()
spinner = getspinner()


async def amend_commit_message(commit_hash: str, new_message: str) -> bool:
    """Amend a commit message using git filter-branch."""
    try:
        script = f'''
if [ "$GIT_COMMIT" = "{commit_hash}" ]; then
    echo "{new_message}"
else
    cat
fi
'''
        script_path = "/tmp/filter-msg"
        with open(script_path, "w") as f:
            f.write(script)
        os.chmod(script_path, 0o755)

        cmd = [
            "git",
            "filter-branch",
            "-f",
            "--msg-filter",
            f"/bin/bash {script_path}",
            f"{commit_hash}^..{commit_hash}",
        ]
        await arun(cmd)
        os.remove(script_path)
        return True
    except Exception as e:
        console.print(f"[red]Failed to amend commit message: {str(e)}[/red]")
        return False


async def generate_change_message(
    changes: ModuleChanges,
    lines: int,
    granularity: Granularity = Granularity.MODULE,
) -> tuple[str, List[ChangeMetric]]:
    """Generate a structured change message and return metrics."""
    module = changes["module"]
    metrics = []

    if lines["total"] > 1000:
        header = "Major Changes"
    elif lines["total"] >= 100:
        header = "Significant Changes"
    else:
        header = "Minor Changes"

    msg_parts = []

    if granularity == Granularity.FILE:
        msg_parts.append(f"{header}")
        msg_parts.append(f"- Module: {module}")
        metrics.append(ChangeMetric(module, lines, Granularity.FILE, module))

    elif granularity == Granularity.CLASS and changes["classes"]:
        classes = changes["classes"]
        msg_parts.append(f"{header}")
        msg_parts.append(f"- Module: {module}")
        msg_parts.extend([f"  - Class: {c}" for c in classes])
        metrics.extend(
            [
                ChangeMetric(c, lines // len(classes), Granularity.CLASS, module)
                for c in classes
            ]
        )

    elif granularity == Granularity.FUNCTION and changes["functions"]:
        functions = changes["functions"]
        msg_parts.append(f"{header}")
        msg_parts.append(f"- Module: {module}")
        msg_parts.extend([f"  - Function: {f}" for f in functions])
        metrics.extend(
            [
                ChangeMetric(f, lines // len(functions), Granularity.FUNCTION, module)
                for f in functions
            ]
        )
    else:
        msg_parts.append(f"{header}")
        msg_parts.append(f"- Module: {module}")
        if changes["classes"]:
            msg_parts.append("  - Classes:")
            msg_parts.extend([f"    * {c}" for c in changes["classes"]])
        if changes["functions"]:
            msg_parts.append("  - Functions:")
            msg_parts.extend([f"    * {f}" for f in changes["functions"]])

        metric = ChangeMetric(
            module,
            lines,
            Granularity.MODULE,
            module,
            children=set(changes["classes"] + changes["functions"]),
        )
        metrics.append(metric)

    return "\n".join(msg_parts), metrics


async def get_commit_history(
    days: int | None = None,
    branch: str | None = None,
    overwrite: bool = False,
    dry_run: bool = False,
    granularity: Granularity = Granularity.MODULE,
    max_changes: int | None = 10,
    commit_filters: Dict[str, str] | None = None,
    min_lines: int = 1,
    file_patterns: List[str] | None = None,
) -> tuple[List[dict], List[ChangeMetric]]:
    """Get commit history and change metrics."""
    from mbcore.log import debug

    console.print("\n[blue]Git Repository Info[/blue]")
    console.print(f"[dim]Working directory:[/dim] {os.getcwd()}")
    try:
        repo_root = await get_repo_root()
        console.print(f"[dim]Git root:[/dim] {repo_root}")
    except Exception as e:
        console.print(f"[yellow]Could not get repo root: {e}[/yellow]")

    cmd = ["git", "log"]

    if days is not None:
        cmd.extend([f"--since={days}.days.ago"])

    cmd.extend(
        [
            "--all",
            "--full-history",
            "--no-merges",
            '--date="format:%Y-%m-%d"',
            '--pretty="format:%H|%ad|%s|%ae"',
        ],
    )

    if branch:
        cmd.append(branch)

    if file_patterns:
        cmd.extend(["--"] + file_patterns)

    getspinner().stop()
    console.print("\n[blue]Commit History[/blue]")
    output = await arun(cmd)
    if not output:
        console.print("[yellow]No commits found in the specified time period[/yellow]")
        return [], []

    commits = []
    all_metrics: List[ChangeMetric] = []
    lines_out = output.splitlines()

    if max_changes:
        lines_out = lines_out[:max_changes]
    if debug:
        console.print(f"\n[blue]Found {len(lines_out)} commits to analyze[/blue]")

    for line in lines_out:
        try:
            out = line.split("|")
            hash_val, date, msg, author = out

            if commit_filters:
                skip = False
                for key, pattern in commit_filters.items():
                    if (
                        key == "author"
                        and not re.search(pattern, author)
                        or key == "message"
                        and not re.search(pattern, msg)
                    ):
                        skip = True
                        break
                if skip:
                    continue

            if debug:
                spinner.stop()
                console.print(
                    f"\n[blue]Analyzing commit[/blue] {hash_val[:7]} from {date}"
                )

            changes = await get_diff_stats(hash_val)
            if not changes:
                console.print("[yellow]No file changes found[/yellow]")
                continue

            changes = {k: v for k, v in changes.items() if v["total"] >= min_lines}

            messages = []
            commit_metrics = []

            for filepath, lines_changed in changes.items():
                if filepath.endswith(".py"):
                    if debug:
                        console.print(
                            f"[blue]Analyzing Python file:[/blue] {filepath} ({lines_changed} lines)"
                        )
                    module_changes = await analyze_module_changes(filepath, hash_val)
                    message, metrics = await generate_change_message(
                        module_changes, lines_changed, granularity
                    )
                    messages.append(message)
                    commit_metrics.extend(metrics)

            if commit_metrics:
                all_metrics.extend(commit_metrics)

            final_message = (
                " && \n".join(filter(None, messages)) if messages else "minor fixes"
            )
            spinner.stop()
            console.print("\n[yellow]Commit Message Change:[/yellow]")
            if debug:
                console.print(f"[green]+ New:[/green] {final_message}")

            if commit_metrics:
                console.print("\n[blue]Change Metrics:[/blue]")
                for metric in commit_metrics:
                    console.print(
                        f"  - {metric.type.value}: {metric.name} ({metric.lines_changed} lines)"
                    )

            if overwrite and not dry_run:
                if await amend_commit_message(hash_val, final_message):
                    console.print(
                        f"[green]✓ Successfully rewrote commit {hash_val[:7]}[/green]"
                    )
                else:
                    console.print(
                        f"[red]✗ Failed to rewrite commit {hash_val[:7]}[/red]"
                    )

            commits.append(
                {
                    "hash": hash_val,
                    "date": date,
                    "message": final_message,
                    "author": author,
                    "category": "🔄 Changes",
                    "metrics": commit_metrics,
                },
            )
        except ValueError as e:
            import traceback

            traceback.print_exc()
            console.print(f"[red]Error processing commit: {str(e)}[/red]")
            continue

    if max_changes:
        filtered_metrics = sorted(
            all_metrics, key=lambda m: m.lines_changed["total"], reverse=True
        )[:max_changes]
        filtered_hashes = {
            commit["hash"]
            for commit in commits
            if any(m in filtered_metrics for m in commit["metrics"])
        }
        commits = [c for c in commits if c["hash"] in filtered_hashes]

    console.print(f"\n[blue]Processed {len(commits)} commits total[/blue]")
    return commits, all_metrics


async def extract_code_changes(commit_hash: str) -> Dict[str, List[str]]:
    """Extract meaningful code changes from a commit."""
    cmd = ["git", "show", "--format=", "--unified=3", commit_hash, "--", "*.py"]
    diff = await arun(cmd)

    changes = collections.defaultdict(list)
    current_file = None
    current_block = []

    for line in diff.splitlines():
        if line.startswith("diff --git"):
            if current_file and current_block:
                code = "\n".join(current_block)
                try:
                    ast.parse(code)
                    changes[current_file].append(code)
                except SyntaxError:
                    pass
            current_file = line.split(" b/")[-1]
            current_block = []
        elif line.startswith("+") and not line.startswith("+++"):
            current_block.append(line[1:])

    return dict(changes)


async def generate_changelog(
    days: int = -1,
    branch: str | None = None,
    show_code: bool = False,
    overwrite: bool = False,
    dry_run: bool = False,
    granularity: Granularity = Granularity.MODULE,
    max_changes: int | None = 100,
    commit_filters: Dict[str, str] | None = None,
    min_lines: int = 100,
    file_patterns: List[str] | None = None,
) -> str:
    cmd = ["git", "rev-parse", "HEAD"] if days == -1 else None
    if days == -1:
        commit_hash = await arun(cmd)
        if commit_hash:
            commits, metrics = await get_commit_history(
                1,
                commit_hash,
                overwrite,
                dry_run,
                granularity,
                max_changes,
                commit_filters=commit_filters,
                min_lines=min_lines,
                file_patterns=file_patterns,
            )
        else:
            commits, metrics = [], []
    else:
        commits, metrics = await get_commit_history(
            days,
            branch,
            overwrite,
            dry_run,
            granularity,
            max_changes,
            commit_filters=commit_filters,
            min_lines=min_lines,
            file_patterns=file_patterns,
        )

    repo_url = await arun(["git", "config", "--get", "remote.origin.url"])
    if repo_url and repo_url.endswith(".git"):
        repo_url = repo_url[:-4]

    lines = [
        "# Changelog",
        "",
        f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
    ]

    grouped_commits = collections.defaultdict(list)
    for c in commits:
        if c["message"].strip():
            grouped_commits[c["category"]].append(c)

    def format_file_link(filepath: str) -> str:
        filename = os.path.basename(filepath)
        if repo_url:
            return f"[{filename}]({repo_url}/blob/main/{filepath}) ([local](file://{filepath}))"
        return f"[{filename}](file://{filepath})"

    def format_changes(message: str) -> str:
        parts = message.split(" && ")
        formatted = []
        for part in parts:
            if ("affecting classes:" in part) or ("with function changes in:" in part):
                if "affecting classes:" in part:
                    file_part, *details = part.split(" affecting classes:")
                else:
                    file_part, *details = part.split("with function changes in:")
                file_name = file_part.split("for ")[-1].strip()
                change_type = (
                    "major overhaul to"
                    if "major overhaul" in file_part
                    else "modified"
                    if "modified" in file_part
                    else "minor fixes for"
                )
                formatted.append(f"- **{change_type}** {format_file_link(file_name)}")
                if details:
                    detail_text = details[0].strip()
                    if "with function changes in:" in detail_text:
                        funcs = detail_text.split("with function changes in:")[
                            -1
                        ].strip()
                        formatted.append(f"  - 🔧 Functions: `{funcs}`")
                    else:
                        classes = detail_text.strip()
                        formatted.append(f"  - 📦 Classes: `{classes}`")
            else:
                formatted.append(f"- {part.strip()}")
        return "\n".join(formatted)

    for category, cat_commits in grouped_commits.items():
        if not cat_commits:
            continue
        lines.append(f"## {category}")
        lines.append("")
        for commit in cat_commits:
            date = datetime.strptime(commit["date"], "%Y-%m-%d").strftime("%b %d")
            lines.append(f"### [{date}] Commit {commit['hash'][:7]}")
            formatted_message = format_changes(commit["message"])
            lines.extend(formatted_message.splitlines())

            if show_code:
                changes = await extract_code_changes(commit["hash"])
                for file_path, snippets in changes.items():
                    if snippets:
                        lines.append(f"\n  Changes in `{file_path}`:")
                        for snippet in snippets:
                            lines.append("  ```python")
                            lines.extend("  " + line for line in snippet.splitlines())
                            lines.append("  ```")
                        lines.append("")

            lines.append("")
        lines.append("")

    if metrics:
        lines.append("\n## Change Metrics Summary\n")
        metrics_by_type = collections.defaultdict(list)
        for m in metrics:
            metrics_by_type[m.type].append(m)

        for ttype, tmetrics in metrics_by_type.items():
            lines.append(f"### {ttype.value.title()} Changes")
            sorted_metrics = sorted(
                tmetrics, key=lambda x: x.lines_changed["total"], reverse=True
            )
            significant = [x for x in sorted_metrics if x.lines_changed["total"] > 10][
                :5
            ]
            for metric in significant:
                lines.append(f"- {metric.name}")
                lines.append(f"  Lines changed: {metric.lines_changed}")
                if metric.children:
                    affected = list(metric.children)
                    if len(affected) > 3:
                        lines.append("  Affects:")
                        for item in affected:
                            lines.append(f"    - {item}")
                    else:
                        lines.append(f"  Affects: {', '.join(affected)}")
                lines.append("")
            lines.append("")

    try:
        return "\n".join(unique_everseen(lines))
    except Exception as e:
        if True:
            import traceback

            traceback.print_exc()
        console.print(f"[red]Error generating changelog: {str(e)}[/red]")
        return ""


async def brief_commit_message() -> str:
    changes: Dict[str, DiffStats] = await get_diff_stats(include_unstaged=False)
    if not changes:
        return "No changes to commit"

    # Collect changes and sort by significance
    file_changes = []
    for filepath, lines in changes.items():
        if not filepath.endswith(".py"):
            continue

        module_changes = await analyze_module_changes(filepath)
        base_name = os.path.basename(filepath)

        # Determine significance score (class changes > function changes > line count)
        significance = 0
        description = ""

        if module_changes["classes"]:
            cls = ", ".join(module_changes["classes"])
            description = f"Updated {cls} in {base_name}"
            significance = 3 * len(module_changes["classes"]) + lines["total"] // 10
        elif module_changes["functions"]:
            funcs = ", ".join(module_changes["functions"])
            description = f"Modified {funcs} in {base_name}"
            significance = 2 * len(module_changes["functions"]) + lines["total"] // 20
        elif lines["total"] > 50:
            description = f"Major changes to {base_name}"
            significance = 1 * (lines["total"] // 50)
        else:
            description = f"Minor updates to {base_name}"
            significance = lines["total"] // 100

        file_changes.append((significance, description, base_name))

    if not file_changes:
        return "chore: Minor updates"

    # Sort by significance score (highest first)
    file_changes.sort(reverse=True)
    significant_changes = [desc for _, desc, _ in file_changes]
    top_files = [name for _, _, name in file_changes[:3]]

    # Determine commit type
    prefix = (
        "feat"
        if any("Major changes" in s or "Updated" in s for s in significant_changes[:5])
        else "fix"
    )

    # Format the summary line based on number of changes
    if len(significant_changes) <= 2:
        summary = f"{prefix}: {' and '.join(significant_changes)}"
    elif len(significant_changes) <= 5:
        summary = f"{prefix}: Updated {', '.join(top_files[:2])} and {len(significant_changes) - 2} other files"
    else:
        len(significant_changes)
        summary = f"{prefix}: Updated {len(significant_changes)} files including {', '.join(top_files)}"

    return summary


async def thorough_commit_msg() -> str:
    changes: Dict[str, DiffStats] = await get_diff_stats(include_unstaged=False)
    if not changes:
        return "No changes to commit"

    significant_changes = []
    for filepath, lines in changes.items():
        if not filepath.endswith(".py"):
            continue
        module_changes = await analyze_module_changes(filepath)
        if module_changes["classes"]:
            cls = ", ".join(module_changes["classes"])
            significant_changes.append(f"Updated {cls} in {os.path.basename(filepath)}")
        elif module_changes["functions"]:
            funcs = ", ".join(module_changes["functions"])
            significant_changes.append(
                f"Modified {funcs} in {os.path.basename(filepath)}"
            )
        elif changes[filepath]["total"] > 50:
            significant_changes.append(f"Major changes to {os.path.basename(filepath)}")
        else:
            significant_changes.append(f"Minor updates to {os.path.basename(filepath)}")

    if not significant_changes:
        return "chore: Minor updates"

    if len(significant_changes) > 5:
        total_files = len(significant_changes)
        base_changes = significant_changes[:4]
        base_changes.append(f"...and {total_files - 4} more files")
        significant_changes = base_changes

    prefix = (
        "feat"
        if any("Major changes" in s or "Updated" in s for s in significant_changes)
        else "fix"
    )

    out = f"{prefix}: " + " && ".join(significant_changes)
    return out
