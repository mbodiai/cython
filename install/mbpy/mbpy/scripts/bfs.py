import os
import subprocess

from blessed import Terminal
from rich.console import Console
from rich.tree import Tree

term = Terminal()
console = Console()


def get_git_diff():
    """Retrieve git diff and structure it as a tree."""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain=v1"], capture_output=True, text=True
        )
        lines = result.stdout.strip().split("\n")
        git_tree = {}

        for line in lines:
            status, file_path = line[:2].strip(), line[3:].strip()
            git_tree[file_path] = status

        return git_tree
    except Exception:
        return {}


def build_tree(directory, depth=2):
    """Build a directory tree up to a certain depth."""
    root = Tree(f"📂 [bold]{directory}[/bold]")

    for dirpath, dirnames, filenames in os.walk(directory):
        relative_path = os.path.relpath(dirpath, directory)

        if relative_path == ".":
            parent = root
        else:
            parent = root
            for part in relative_path.split(os.sep):
                if part not in [child.label for child in parent.children]:
                    parent = parent.add(f"📁 {part}")
                else:
                    parent = [
                        child
                        for child in parent.children
                        if child.label == f"📁 {part}"
                    ][0]

        for filename in filenames:
            parent.add(f"📄 {filename}")

        if depth is not None and relative_path.count(os.sep) >= depth - 1:
            del dirnames[:]

    return root


def explore():
    """Main interactive explorer loop."""
    git_tree = get_git_diff()

    while True:
        os.system("clear")
        console.print(build_tree(os.getcwd(), depth=2))

        if git_tree:
            console.print("\n[bold]Git Status:[/bold]")
            for file, status in git_tree.items():
                console.print(f"{status} {file}")

        with term.cbreak():
            key = term.inkey()
            if key.lower() == "q":
                break


if __name__ == "__main__":
    explore()
