import ast
import os
from collections.abc import Callable, Coroutine
from dataclasses import dataclass

from typing import Dict, Set, TypedDict

from mbcore.types import wraps
from mbcore.display import safe_print
from typing_extensions import Any, TypeVar

from mbpy.git.state import arun
from mbcore.log import debug

import sys

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from enum import Enum as StrEnum


class ChangeType(StrEnum):
    FEAT = "feat"
    FIX = "fix"
    DOCS = "docs"
    TEST = "test"
    REFACTOR = "refactor"
    STYLE = "style"
    CHORE = "chore"
    PERF = "perf"
    OTHER = "other"


class Granularity(StrEnum):
    MODULE = "module"
    FILE = "file"
    CLASS = "class"
    FUNCTION = "function"


class ModuleChanges(TypedDict):
    classes: list[str]
    functions: list[str]
    module: str


class DiffStats(TypedDict):
    filepath: str
    additions: int
    deletions: int
    total: int


class CommitCategory(TypedDict):
    type: str
    description: str
    emoji: str


@dataclass
class ChangeMetric:
    name: str
    lines_changed: int
    type: Granularity
    module: str
    children: Set[str] | None = None

    def __hash__(self):
        return hash((self.name, self.type, self.module))


T = TypeVar("T")


def try_analyze(
    success_msg: str | None = None, error_msg: str | None = None
) -> Callable[
    [Callable[..., Coroutine[Any, Any, T]]], Callable[..., Coroutine[Any, Any, T]]
]:
    def wrapper(
        func: Callable[..., Coroutine[Any, Any, T]],
    ) -> Callable[..., Coroutine[Any, Any, T]]:
        @wraps(func)
        async def wrapped(*args: Any, **kwargs: Any) -> T | None:
            try:
                result = await func(*args, **kwargs)
                if success_msg:
                    safe_print(f"[green]{success_msg}[/green]")
                return result
            except Exception as e:
                if debug():
                    import traceback

                    traceback.print_exc()
                if error_msg:
                    safe_print(f"[red]{error_msg}: {str(e)}[/red]")
                return None

        return wrapped

    return wrapper


@try_analyze(error_msg="Failed to categorize commit")
async def categorize_commit(message: str) -> CommitCategory:
    """Categorize a commit message and improve its formatting."""
    categories = {
        ChangeType.FEAT: "🚀 Features",
        ChangeType.FIX: "🐛 Bug Fixes",
        ChangeType.DOCS: "📚 Documentation",
        ChangeType.TEST: "🧪 Tests",
        ChangeType.REFACTOR: "♻️ Refactoring",
        ChangeType.STYLE: "💎 Style",
        ChangeType.CHORE: "🔧 Maintenance",
        ChangeType.PERF: "⚡️ Performance",
    }

    parts = message.split(":", 1)
    if len(parts) == 2:
        type_str = parts[0].lower()
        description = parts[1].strip()
    else:
        type_str = ChangeType.OTHER
        description = message.strip()

    if description:
        description = description[0].upper() + description[1:]
        if not description.endswith("."):
            description += "."

    category = categories.get(type_str, "🔍 Other Changes")
    return CommitCategory(type=type_str, description=description, emoji=category)


@try_analyze(error_msg="Failed to get diff stats")
async def get_diff_stats(
    commit_hash: str | None = None, include_unstaged: bool = False
) -> Dict[str, DiffStats]:
    """Get number of changed lines per file."""
    if commit_hash:
        cmd = ["git", "show", "--format=", "--stat", "--numstat", commit_hash]
    else:
        cmd = (
            ["git", "diff", "--numstat"]
            if include_unstaged
            else ["git", "diff", "--cached", "--numstat"]
        )

    output = await arun(cmd)
    changes: Dict[str, DiffStats] = {}

    for line in output.splitlines():
        l = line.strip()
        if not l or line.startswith("/"):
            continue

        try:
            parts = line.split("\t")
            if len(parts) == 3:
                additions, deletions, filepath = parts
                if additions != "-" and deletions != "-":
                    add_count = int(additions)
                    del_count = int(deletions)
                    changes[filepath] = DiffStats(
                        filepath=filepath,
                        additions=add_count,
                        deletions=del_count,
                        total=add_count + del_count,
                    )
        except (ValueError, IndexError):
            verbose("Failed to get diff stats for " + str(line))
            continue

    return changes


@try_analyze(error_msg="Failed to analyze scope changes")
async def analyze_scope_changes(filepath: str, commit_hash: str) -> Granularity:
    """Analyze whether changes affect module, class or function level."""
    exists = await arun(["git", "ls-tree", "-r", commit_hash, "--name-only"])
    if filepath not in exists.split():
        return Granularity.MODULE

    try:
        content = await arun(
            ["git", "show", f"{commit_hash}:{filepath}"]
            if commit_hash
            else ["git", "show", f":{filepath}"]
        )
        tree = ast.parse(content)
        changed_classes = []
        changed_functions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                changed_classes.append(node.name)
            elif isinstance(node, ast.FunctionDef):
                changed_functions.append(node.name)

        if changed_classes:
            return Granularity.CLASS
        if changed_functions:
            return Granularity.FUNCTION
        return Granularity.MODULE
    except Exception:
        if debug():
            import traceback

            traceback.print_exc()
            safe_print(f"[red]Failed to analyze  {filepath}[/red]")

    return Granularity.MODULE


@try_analyze(error_msg="Failed to analyze module changes")
async def analyze_module_changes(
    filepath: str, commit_hash: str | None = None
) -> ModuleChanges:
    """Analyze module changes using AST."""
    try:
        cmd = (
            ["git", "show", f"{commit_hash}:{filepath}"]
            if commit_hash
            else ["git", "show", f":{filepath}"]
        )
        content = await arun(cmd)
        tree = ast.parse(content)

        changes: ModuleChanges = {
            "classes": [],
            "functions": [],
            "module": os.path.basename(filepath),
        }

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                changes["classes"].append(node.name)
            elif isinstance(node, ast.FunctionDef):
                changes["functions"].append(node.name)
        return changes
    except Exception:
        return ModuleChanges(
            module=os.path.basename(filepath), classes=[], functions=[]
        )
