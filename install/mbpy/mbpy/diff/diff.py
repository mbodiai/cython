import atexit
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List

import rich_click as click
from rich.console import Console
from rich.tree import Tree

console = Console()

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.STYLE_ERRORS_SUGGESTION = "yellow italic"
click.rich_click.STYLE_OPTION = "green"
click.rich_click.STYLE_SWITCH = "bold cyan"

HELP_TEXT = "j/k: Move | Space: Select | z: Toggle fold | ?: Help | q: Quit"
SUCCESS = 0


def cleanup(backup, source) -> None:
    """Cleanup temporary files and exit."""
    if not SUCCESS:
        shutil.copy2(backup, source)
        return
    shutil.rmtree(Path.home() / ".cache" / "mb" / "diff")


def create_backup(file_path):
    """Create a backup of the given file."""
    p = Path.home() / ".cache" / "mb" / "diff" / file_path
    p.parent.mkdir(parents=True, exist_ok=True)
    backup_path = f"{p}.{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
    shutil.copy2(file_path, backup_path)
    atexit.register(cleanup, backup_path, file_path)
    return backup_path


def escape_markup(text):
    """Escape square brackets in text to prevent markup parsing errors."""
    return text.replace("[", "\\[").replace("]", "\\]").replace("\\\\", "\\")


def display_tree_view(blocks):
    """Display diff blocks in a tree structure with proper markup escaping."""
    tree = Tree("[bold cyan]Diff Overview[/bold cyan]")

    for i, block in enumerate(blocks, 1):
        block_tree = tree.add(f"[bold yellow]Block {i}[/bold yellow]")

        # Show header/location
        block_tree.add(f"[dim]{escape_markup(block.header.strip())}[/dim]")

        # Changes
        changes = block_tree.add("[bold green]Changes[/bold green]")
        for line in block.changes:
            if line.startswith("+"):
                changes.add(f"[green]{escape_markup(line.strip())}[/green]")
            elif line.startswith("-"):
                changes.add(f"[red]{escape_markup(line.strip())}[/red]")
            else:
                changes.add(f"[dim]{escape_markup(line.strip())}[/dim]")

        # Context
        if block.context.before:
            context = block_tree.add("[dim]Context[/dim]")
            for line in block.context.before[:2]:
                context.add(f"[dim]{escape_markup(line.strip())}[/dim]")

    return tree


@dataclass
class DiffBlockPreview:
    header: str
    description: str
    is_folded: bool = False
    is_selected: bool = False


@dataclass
class DiffContext:
    parents: List[DiffBlockPreview]
    siblings: List[DiffBlockPreview]
    children: List[DiffBlockPreview]
    before: List[str]
    after: List[str]


@dataclass
class DiffBlock:
    header: str
    changes: List[str]
    context: DiffContext
    is_folded: bool = False
    is_selected: bool = False

    def toggle_fold(self) -> None:
        """Toggle the folded state of the block."""
        self.is_folded = not self.is_folded

    @property
    def description(self) -> str:
        """Generate a meaningful description from the changes."""
        for change in self.changes:
            if change.startswith("+"):
                line = change[1:].strip()
                if line and not line.isspace():
                    return line[:57] + ("..." if len(line) > 57 else "")
        return self.header.strip()


class DiffParser:
    @staticmethod
    def parse_blocks(diff: List[str]) -> List[DiffBlock]:
        """Parse unified diff into structured diff blocks."""
        blocks = []
        current_block = None
        context_before = []
        context_after = []
        changes = []
        header = ""

        for line in diff:
            if line.startswith("@@"):
                if current_block:
                    blocks.append(
                        DiffBlock(
                            header,
                            changes,
                            DiffContext([], [], [], context_before, context_after),
                        )
                    )
                header = line
                changes = []
                context_before = []
                context_after = []
                current_block = True
            elif current_block:
                if line.startswith(" "):
                    if changes:
                        context_after.append(line)
                    else:
                        context_before.append(line)
                else:
                    changes.append(line)

        if current_block:
            blocks.append(
                DiffBlock(
                    header,
                    changes,
                    DiffContext([], [], [], context_before, context_after),
                )
            )

        return blocks
