import difflib
import shutil
from dataclasses import dataclass
from datetime import datetime
from typing import List

from mbcore.display import getconsole, safe_print


@dataclass
class DiffContext:
    before: List[str]
    after: List[str]
    is_folded: bool = False
    is_selected: bool = False

    def toggle_fold(self) -> None:
        self.is_folded = not self.is_folded

    def toggle_selection(self) -> None:
        self.is_selected = not self.is_selected


@dataclass
class DiffBlock:
    header: str
    changes: List[str]
    context: DiffContext
    is_folded: bool = False
    is_selected: bool = False

    @property
    def description(self) -> str:
        """Generate a meaningful description from the changes."""
        for change in self.changes:
            if change.startswith("+"):
                line = change[1:].strip()  # Fixed typo: changed trip() to strip()
                if line and not line.isspace():
                    return line[:60] + ("..." if len(line) > 60 else "")
        return self.header.strip()

    @property
    def has_changes(self) -> bool:
        return any(line.startswith(("+", "-")) for line in self.changes)


class DiffParser:
    @staticmethod
    def parse_blocks(diff_lines: List[str]) -> List[DiffBlock]:
        blocks = []
        current = {
            "header": None,
            "changes": [],
            "context": {"before": [], "after": []},
        }

        for line in diff_lines:
            if line.startswith("@@"):
                if current["header"]:
                    blocks.append(
                        DiffBlock(
                            header=current["header"],
                            changes=current["changes"],
                            context=DiffContext(
                                before=current["context"]["before"],
                                after=current["context"]["after"],
                            ),
                        )
                    )
                    current = {
                        "header": line,
                        "changes": [],
                        "context": {"before": [], "after": []},
                    }
                else:
                    current["header"] = line
            elif line.startswith(("+", "-")):
                current["changes"].append(line)
            else:
                target = (
                    current["context"]["before"]
                    if not current["changes"]
                    else current["context"]["after"]
                )
                target.append(line)

        if current["header"]:
            blocks.append(
                DiffBlock(
                    header=current["header"],
                    changes=current["changes"],
                    context=DiffContext(
                        before=current["context"]["before"],
                        after=current["context"]["after"],
                    ),
                )
            )

        return blocks


class DiffManager:
    def __init__(self, file1: str, file2: str):
        self.file1 = file1
        self.file2 = file2
        self.blocks: List[DiffBlock] = []

    def backup_files(self) -> tuple[str, str]:
        """Create backups of both files."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup1 = f"{self.file1}.{timestamp}.bak"
        backup2 = f"{self.file2}.{timestamp}.bak"

        shutil.copy2(self.file1, backup1)
        shutil.copy2(self.file2, backup2)
        return backup1, backup2

    def generate_diff(self, context_lines: int = 3) -> List[DiffBlock]:
        """Generate diff blocks between the two files."""
        with open(self.file1) as f1, open(self.file2) as f2:
            diff = list(
                difflib.unified_diff(
                    f1.readlines(),
                    f2.readlines(),
                    fromfile=self.file1,
                    tofile=self.file2,
                    n=context_lines,
                )
            )

        self.blocks = DiffParser.parse_blocks(diff)
        return self.blocks

    def get_selected_changes(self) -> List[str]:
        """Get all selected changes."""
        return [
            change
            for block in self.blocks
            if block.is_selected
            for change in block.changes
        ]


def parse_start_line(diff_text: str) -> int:
    lines = diff_text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("@@"):
            return i + 1
    return 0


async def display_git_diff(
    diff_text: str | list[str], branch=None, remote="origin"
) -> None:
    """Render Git diff with syntax highlighting using Rich."""
    from rich.table import Table

    lines = diff_text.splitlines() if isinstance(diff_text, str) else diff_text
    console = getconsole()

    # Track line numbers for both sides
    left_line = 1
    right_line = 1

    # Group changes into blocks
    current_block = []
    blocks = []

    for line in lines:
        if not line.strip():
            continue
        if line.startswith("@@") and current_block:
            blocks.append(current_block)
            current_block = []
        current_block.append(line)

    if current_block:
        blocks.append(current_block)

    # Display each block
    for block_num, block in enumerate(blocks, 1):
        console.print(f"\nBlock {block_num}", style="bold blue")

        # Create table for side-by-side view
        table = Table(show_header=False, box=None)
        table.add_column("Left #", style="dim")
        table.add_column("Left", style="red")
        table.add_column("Right #", style="dim")
        table.add_column("Right", style="green")

        # Process block lines
        for line in block:
            if line.startswith("@@"):
                # Parse hunk header for line numbers
                left_line = int(
                    line.split("-")[1].split(",")[0].strip().replace("\n", "")
                )
                right_line = int(
                    line.split("+")[1].split(",")[0].strip().replace("\n", "")
                )
                table.add_row("...", "", "...", "")
            elif line.startswith("-"):
                table.add_row(f"{left_line}", line[1:], "", "")
                left_line += 1
            elif line.startswith("+"):
                table.add_row(
                    "", "", f"{right_line}", line[1:].strip().replace("\n", "")
                )
                right_line += 1
            else:
                table.add_row(
                    f"{left_line}",
                    line[1:],
                    f"{right_line}",
                    line[1:].strip().replace("\n", ""),
                )
                left_line += 1
                right_line += 1

        console.print(table, end="")


# Test the implementation
async def main():
    """Test the diff functionality with sample files."""
    from pathlib import Path

    # Find mbcore Python files
    mbcore_files = [
        str(p)
        for p in Path(".").rglob("*.py")
        if "mbcore" in p.parts and "test" not in str(p)
    ]

    if len(mbcore_files) < 2:
        safe_print("Need at least 2 files to compare")
        return

    # Create diff manager and generate diff
    dm = DiffManager(mbcore_files[0], mbcore_files[1])
    blocks = dm.generate_diff()

    if not blocks:
        safe_print(
            f"No differences found between:\n{mbcore_files[0]}\n{mbcore_files[1]}"
        )
        return

    # Set up test data for first block
    if blocks:
        blocks[0].context.before = ["line1", "line2", "line3"]
        blocks[0].context.after = ["line1", "line2", "line3"]
        blocks[0].is_selected = True

        # Only set second block if it exists
        if len(blocks) > 1:
            blocks[1].context.before = ["line4", "line5", "line6"]
            blocks[1].context.after = ["line4", "line5", "line6"]
            blocks[1].is_selected = True

    # Display diff
    await display_git_diff(dm.get_selected_changes())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
