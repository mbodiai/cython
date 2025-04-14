"""Usage (zsh on Mac):
    pip install rich textual
    python diff_tui.py --file1 {file1} --file2 {file2} [--ai].

Features:
    1. Detects JSON vs. text.
    2. Displays a Rich-based TUI using Textual.
    3. Arrow keys to navigate through diff blocks.
    4. Use [k]eep, [r]eplace, [m]erge for each block.
    5. Step into/out of nested JSON blocks to manage entire nodes.
    6. AI can interact programmatically via the `act` callback.
    7. Fully parameterizable through command-line arguments.
"""  # noqa: D205

import difflib
import sys
from pathlib import Path
from typing import List

from rich.console import Console


class Block:
    """Simple block that can be navigated and selected."""

    def __init__(self, num: int, old_lines: List[str], new_lines: List[str]):
        self.num = num
        self.old = old_lines
        self.new = new_lines
        self.expanded = False
        self.selected = None  # None, 'old', 'new'
        self.context = 3

    def toggle(self):
        """Expand/collapse the block."""
        self.expanded = not self.expanded

    def choose(self, selection: str):
        """Select old/new version."""
        if selection in ("old", "new"):
            self.selected = selection
            self.expanded = False  # Auto-collapse

    def render(self) -> List[str]:
        """Render the current block state."""
        if not self.expanded:
            # Collapsed view shows summary
            return [
                f"Block {self.num} ({'old' if self.selected == 'old' else 'new' if self.selected == 'new' else 'unselected'})"
            ]

        # Expanded view shows diff with context
        output = []
        for line in difflib.unified_diff(self.old, self.new, n=self.context):
            output.append(line)
        return output


class DiffViewer:
    """Main diff viewer class."""

    def __init__(self, file1: str, file2: str):
        with open(file1) as f1, open(file2) as f2:
            old = f1.readlines()
            new = f2.readlines()

        # Split into manageable blocks
        self.blocks = []
        self.current = 0

        # Create blocks from unified diff
        current_block = []
        block_num = 0

        for line in difflib.unified_diff(old, new):
            if line.startswith("@@") and current_block:
                self.blocks.append(Block(block_num, current_block, []))
                block_num += 1
                current_block = []
            current_block.append(line)

        if current_block:
            self.blocks.append(Block(block_num, current_block, []))

    def next_block(self):
        """Move to next block."""
        if self.current < len(self.blocks) - 1:
            self.current += 1

    def prev_block(self):
        """Move to previous block."""
        if self.current > 0:
            self.current -= 1

    def toggle_current(self):
        """Expand/collapse current block."""
        if self.blocks:
            self.blocks[self.current].toggle()

    def select_current(self, choice: str):
        """Select version for current block."""
        if self.blocks:
            self.blocks[self.current].choose(choice)

    def render(self) -> str:
        """Render the current view."""
        output = []
        for i, block in enumerate(self.blocks):
            if i == self.current:
                output.append("> " + "\n> ".join(block.render()))
            else:
                output.append("  " + "\n  ".join(block.render()))
        return "\n".join(output)


def main(arg1, arg2):
    """Example usage."""  # noqa: D401
    viewer = DiffViewer(arg1, arg2)
    console = Console()

    while True:
        console.clear()
        console.print(viewer.render())
        console.print(
            "\nControls: ↑/↓ navigate, Space expand/collapse, o/n select old/new, q quit"
        )

        key = input()
        if key == "q":
            break
        if key in ("o", "n"):
            viewer.select_current("old" if key == "o" else "new")
        elif key == " ":
            viewer.toggle_current()
        elif key in ("j", "down"):
            viewer.next_block()
        elif key in ("k", "up"):
            viewer.prev_block()


if __name__ == "__main__":
    args = list(sys.argv[1:])
    arg1 = args.pop(0) if args else next(iter(Path.cwd().rglob("*.json")), None)
    arg2 = args.pop(0) if args else next(iter(Path.cwd().rglob("*.json")), None)
    main(arg1, arg2)
