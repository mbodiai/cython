import asyncio
import re
import sys
from inspect import cleandoc
from inspect import getdoc as inspect_getdoc
from pathlib import Path
from pydoc import getdoc as pydoc_getdoc
from pydoc import splitdoc, synopsis
from typing import Any, Dict, Tuple

from mbcore.display import prompt_ask, safe_print
from typing_extensions import Final

from mbpy.cmd import arun_command
from mbcore.resolve import resolve_name
from mbcore.log import debug
from mbpy.helpers._static import SPHINX_API, SPHINX_CONF, SPHINX_INDEX, SPHINX_MODULE

visit: set = set()
PathLike = Path

CONTROL_ESCAPE: Final = {
    7: "\\a",
    8: "\\b",
    11: "\\v",
    12: "\\f",
    13: "\\r",
}


def escape_control_codes(
    text: str,
    _translate_table: Dict[int, str] = CONTROL_ESCAPE,
) -> str:
    r"""Replace control codes with their "escaped" equivalent in the given text.

    (e.g. "\b" becomes "\\b")

    Args:
        text (str): A string possibly containing control codes.

    Returns:
        str: String with control codes replaced with their escaped version.

    """
    return text.translate(_translate_table)


visit: set = set()


def first_paragraph(doc: str) -> Tuple[str, str, str]:
    """Split the docstring into the first paragraph and the rest."""
    return doc.partition("\n\n")


async def get_formatted_doc(obj: Any, verbose: bool = False) -> None | str:
    """Extract the docstring of an object, process it, and return it.

    The processing consists of cleaning up the docstring's indentation,
    taking only its first paragraph if `verbose` is False,
    and escaping its control codes.

    Args:
        obj (Any): The object to get the docstring from.
        verbose (bool): Whether to include the full docstring.

    Returns:
        Optional[str]: The processed docstring, or None if no docstring was found.

    """
    docs = pydoc_getdoc(obj)
    if docs is None:
        docs = inspect_getdoc(obj) or ""
    if not docs:
        return None

    docs = cleandoc(docs).strip()
    if not verbose:
        docs, _, _ = first_paragraph(docs)
    return escape_control_codes(docs)


async def brief_summary(obj: object) -> Tuple[str, str]:
    """Extract the first sentence (brief) and returns the.

    Args:
        obj (object): The object from which to extract the docstring.

    Returns:
        Tuple[str, str]: A tuple containing the summary and the remaining documentation.
                         Both elements are empty strings if no docstring is found.

    """
    doc = pydoc_getdoc(obj)
    if not doc:
        doc = inspect_getdoc(obj) or ""

    if not doc:
        # Attempt to locate the object and get a synopsis
        full_name = (
            f"{getattr(obj, '__module__', '')}.{getattr(obj, '__qualname__', '')}"
        )
        try:
            located = resolve_name(full_name)
            if located:
                if hasattr(located, "__file__"):
                    doc = synopsis(located.__file__)
                elif hasattr(obj, "__file__"):
                    doc = synopsis(obj.__file__)
        except Exception as e:
            debug(f"Failed to locate synopsis for {full_name}: {e}")
            doc = ""

    if not doc:
        # Fallback to get_formatted_doc with verbose=True
        formatted_doc = await get_formatted_doc(obj, verbose=True)
        if formatted_doc:
            doc = formatted_doc

    # If doc is still empty, set to empty string to avoid None
    if not doc:
        doc = ""

    # Split the docstring into summary and remaining parts
    summary, remaining = splitdoc(doc)
    if not summary or not remaining:
        # Attempt to split manually using first_paragraph
        summary, sep, remaining = first_paragraph(doc)
        summary = summary.strip()
        remaining = remaining.strip()

    # Ensure both summary and remaining are strings
    summary = summary if summary else ""
    remaining = remaining if remaining else ""

    return summary, remaining


async def generate_sphinx_docs(
    project_dir: PathLike, docs_dir: PathLike, third_party=False
) -> None:
    """Generate initial Sphinx structure."""
    project_dir = Path(project_dir)
    docs_dir = Path(docs_dir)

    # Create required directories
    for dir in ["_static", "_templates", "api", "_build/html"]:
        (docs_dir / dir).mkdir(parents=True, exist_ok=True)

    # Generate file stubs only - no content yet
    (docs_dir / "index.rst").touch()
    (docs_dir / "api/index.rst").touch()
    (docs_dir / "conf.py").touch()
    (docs_dir / "_templates/module.rst").touch()


async def setup_sphinx_docs(
    *,
    docs_dir: PathLike,
    project_name: str,
    author: str,
    description: str,
    source_dir: PathLike,
    theme: str = "furo",
    env=None,
) -> None:
    """Setup Sphinx configuration and build docs."""
    docs_path = Path(docs_dir).resolve()

    # 1. Create directory structure
    for dir in ["_static", "_templates", "api/_autosummary", "_build/html"]:
        (docs_path / dir).mkdir(parents=True, exist_ok=True)

    # 2. Write templates and content
    underline = "=" * len(project_name)

    # Write index.rst
    (docs_path / "index.rst").write_text(
        SPHINX_INDEX.format(
            project_name=project_name,
            underline=underline,
            description=description,
        )
    )

    # Write API index
    (docs_path / "api/index.rst").write_text(
        SPHINX_API.format(
            project_name=project_name,
        )
    )

    # Write config
    (docs_path / "conf.py").write_text(
        SPHINX_CONF(
            project_name=project_name,
            author=author,
            description=description,
            theme=theme,
        )
    )

    # Write module template
    (docs_path / "_templates/module.rst").write_text(SPHINX_MODULE)

    # 3. Build docs
    try:
        await arun_command(
            f"sphinx-build -b html -v {docs_path} {docs_path}/_build/html"
        )
        safe_print("[bold green]Documentation built successfully[/bold green]")
    except Exception as e:
        if "No module named" in str(e) and prompt_ask("Install Sphinx dependencies?"):
            await arun_command(
                f"{get_executable(env)} -m pip install sphinx sphinx-rtd-theme"
            )
            return await setup_sphinx_docs(
                docs_dir=docs_dir,
                project_name=project_name,
                author=author,
                description=description,
                source_dir=source_dir,
                theme=theme,
            )
        raise Exception(f"Documentation build failed: {e}")


async def generate_recipe_docs(
    test_dir: PathLike, output_dir: PathLike, show: bool = False, third_party=False
) -> None:
    """Generate recipe documentation from test files.

    Args:
        test_dir: Test files directory
        output_dir: Output documentation directory
        show: Whether to print processing information

    """
    if show:
        pass

    recipes_dir = output_dir / "recipes"
    recipes_dir.mkdir(parents=True, exist_ok=True)

    recipes_index = recipes_dir / "index.rst"
    with recipes_index.open("w") as index_file:
        index_file.write("Recipes\n=======\n\n")
        index_file.write(".. toctree::\n   :maxdepth: 2\n\n")

        for test_file in test_dir.rglob("test_*.py"):
            if (
                not third_party
                and "venv" in str(test_file)
                or "site-packages" in str(test_file)
            ):
                continue
            if show:
                pass

            module_name = test_file.stem.replace("test_", "")
            index_file.write(f"   {module_name}\n")

            recipe_rst = recipes_dir / f"{module_name}.rst"
            with recipe_rst.open("w") as recipe_file:
                title = f"{module_name.capitalize()} Recipes"
                recipe_file.write(f"{title}\n{'=' * len(title)}\n")
                recipe_file.write(".. code-block:: python\n\n")

                with test_file.open() as tf:
                    content = tf.read()
                    if show:
                        pass
                    cleaned = await clean_code(content)
                    if show:
                        pass
                    for line in cleaned.splitlines():
                        recipe_file.write(f"    {line}\n")


async def one_liner(package_name: str, openai: bool = False):
    """Generate a one-liner description for the package."""
    try:
        from mbodied import LanguageAgent
        from mbcore.import_utils import smart_import
    except ImportError:
        from mbpy.cmd import arun

        await arun("pip install -U mbodied")
        smart_import("mbodied.agents.language.LanguageAgent")
    return await get_formatted_doc(locate(package_name), verbose=False)


async def summary(package_name: str):
    """Generate a summary for the package."""
    return await one_liner(package_name)


async def outline(package_name: str):
    """Generate an outline for the package."""
    return await one_liner(package_name)


async def clean_code(code: str) -> str:
    """Clean the test code by removing pytest imports, fixtures, mocks, and assert statements."""
    if not code.strip():
        return "No content found"

    # Remove pytest and mock imports
    code = re.sub(
        r"(^import pytest.*\n|^from pytest.*\n|^from unittest.mock.*\n|^import mock.*\n)",
        "",
        code,
        flags=re.MULTILINE,
    )

    # Remove pytest decorators and mocks
    code = re.sub(
        r"(@pytest\.fixture.*\n|@mock\.patch.*\n|@patch.*\n)",
        "",
        code,
        flags=re.MULTILINE,
    )

    # Remove commented sections
    code = re.sub(r"^\s*#.*\n", "", code, flags=re.MULTILINE)

    # Remove unused imports
    code = re.sub(r"(^from .*?\n|^import .*?\n)", "", code, flags=re.MULTILINE)

    # Improved function name cleaning
    code = re.sub(
        r"def test_(\w+)\(.*?\):",
        lambda m: m.group(1).replace("_", " "),
        code,
        flags=re.MULTILINE,
    )
    code = re.sub(
        r"@.*\nmock\s+(\w+)", r"\1", code, flags=re.MULTILINE
    )  # Clean mock fixtures
    code = re.sub(
        r"^\s*mock\s+(\w+)\s*=", r"\1 =", code, flags=re.MULTILINE
    )  # Clean mock variables

    # Extract clean functions
    functions = {}
    current_fn = None
    current_body = []

    for line in code.splitlines():
        if line.strip() in ['if __name__ == "__main__":', "pytest.main([", "]):"]:
            continue
        if line.strip() and not line.strip().startswith(("assert", "pytest", "mock")):
            if line.strip() in functions:
                current_fn = line.strip()
                current_body = []
            elif line[0].isupper() and line[-1] == "=":
                current_fn = line.strip("=").strip()
                current_body = []
            elif re.match(
                r"^[a-zA-Z][\w\s]+$", line.strip()
            ):  # Match cleaned function names
                current_fn = line.strip()
                current_body = []
            else:
                if current_fn:
                    current_body.append(line)
                    functions[current_fn] = "\n".join(current_body).strip()

    # Format recipes
    recipe = []
    if not functions:
        return "No recipes found in this test file"

    for fn_name, fn_body in functions.items():
        if fn_body.strip():
            recipe.append(fn_name)
            recipe.append("=" * len(fn_name))
            recipe.append(fn_body.strip())
            recipe.append("")

    return "\n".join(recipe) if recipe else "No valid recipes extracted"


if __name__ == "__main__":
    from mbcore.display import getconsole
    from rich.progress import Progress

    from mbpy.helpers.traverse import search_children_for_file

    console = getconsole()

    # Validate project structure
    test_dir = search_children_for_file(".", cwd=Path.cwd())
    if not test_dir:
        console.print("[red]Error: Could not find project directory[/red]")
        sys.exit(1)

    output_dir = PathLike("docs2")

    async def main():
        with Progress() as progress:
            task1 = progress.add_task("[green]Generating Sphinx docs...", total=1)
            task2 = progress.add_task("[blue]Setting up documentation...", total=1)

            try:
                results = await asyncio.gather(
                    generate_sphinx_docs(test_dir, output_dir, third_party=True),
                    setup_sphinx_docs(
                        docs_dir=output_dir,
                        project_name="mbpy",
                        author="mbodiai",
                        description="build and package",
                        source_dir="mbpy",
                    ),
                    return_exceptions=True,
                )

                for result in results:
                    if isinstance(result, Exception):
                        raise result

                progress.update(task1, advance=1)
                progress.update(task2, advance=1)

                # Verify output
                build_dir = Path(output_dir) / "build" / "html"
                if build_dir.exists() and any(build_dir.iterdir()):
                    console.print(
                        f"[green]✓ Documentation generated successfully at {build_dir}[/green]"
                    )
                else:
                    console.print(
                        "[red]Warning: Documentation directory is empty[/red]"
                    )

            except Exception as e:
                console.print(f"[red bold]Error: {str(e)}[/red bold]")
                logger.error(
                    f"Documentation generation failed: {str(e)}", exc_info=True
                )
                raise

    try:
        asyncio.run(main())
    except Exception as e:
        console.print(f"[red bold]Error: {str(e)}[/red bold]")
        logger.error(f"Documentation generation failed: {str(e)}", exc_info=True)
        sys.exit(1)
