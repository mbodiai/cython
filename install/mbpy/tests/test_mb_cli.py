import pytest
from click.testing import CliRunner
from mbpy.main import (
    add_command,
    build_command,
    clean_command,
    create_command,
    docs_command,
    repair_command,
    search_command,
    show_command,
    time_command,
    undo_command,
    uninstall_command,
)

from mbcore.display import prompt_ask


@pytest.fixture
def runner():
    return CliRunner()


@pytest.mark.asyncio
async def test_add_package(runner):
    """Test the add command"""
    with runner.isolation():
        # Test adding a package
        result = runner.invoke(add_command, ["pytest"])
        assert result.exit_code == 0

        # Test adding multiple packages
        result = runner.invoke(add_command, ["pytest", "black"])
        assert result.exit_code == 0

        # Test adding with version constraint
        result = runner.invoke(add_command, ["pytest>=7.0.0"])
        assert result.exit_code == 0


@pytest.mark.asyncio
async def test_uninstall_package(runner):
    """Test the uninstall command"""
    with runner.isolation():
        # First add a package
        await runner.invoke(add_command, ["pytest"])

        # Test uninstalling the package
        result = runner.invoke(uninstall_command, ["pytest"])
        assert result.exit_code == 0

        # Test uninstalling with confirmation
        result = runner.invoke(uninstall_command, ["pytest", "--yes"])
        assert result.exit_code == 0


@pytest.mark.asyncio
async def test_show_dependencies(runner):
    """Test the show command"""
    with runner.isolation():
        result = runner.invoke(show_command)
        assert result.exit_code == 0


@pytest.mark.asyncio
async def test_search_package(runner):
    """Test the search command"""
    with runner.isolation():
        result = runner.invoke(search_command, ["pytest"])
        assert result.exit_code == 0
        assert "pytest" in result.output


@pytest.mark.asyncio
async def test_build_package(runner):
    """Test the build command"""
    with runner.isolation():
        result = runner.invoke(build_command)
        assert result.exit_code == 0


@pytest.mark.asyncio
async def test_clean_artifacts(runner):
    """Test the clean command"""
    with runner.isolation():
        result = runner.invoke(clean_command)
        assert result.exit_code == 0

        # Test clean with all options
        result = runner.invoke(clean_command, ["--all"])
        assert result.exit_code == 0


@pytest.mark.asyncio
async def test_create_project(runner):
    """Test the create command"""
    with runner.isolation():
        # Test creating a new project
        result = runner.invoke(create_command, ["test-project", "test-author"])
        assert result.exit_code == 0

        # Test creating with dependencies
        result = runner.invoke(create_command, ["test-project", "test-author", "--deps", "pytest,black"])
        assert result.exit_code == 0

        # Test creating with CLI
        result = runner.invoke(create_command, ["test-project", "test-author", "--no-cli"])
        assert result.exit_code == 0


@pytest.mark.asyncio
async def test_docs_generation(runner):
    """Test the docs command"""
    with runner.isolation():
        result = runner.invoke(docs_command, ["test-project", "test-author"])
        assert result.exit_code == 0


@pytest.mark.asyncio
async def test_repair_imports(runner):
    """Test the repair command"""
    with runner.isolation():
        result = runner.invoke(repair_command, ["."])
        assert result.exit_code == 0


@pytest.mark.asyncio
async def test_time_command(runner):
    """Test the time command"""
    with runner.isolation():
        result = runner.invoke(time_command, ['echo "test"'])
        assert result.exit_code == 0
        assert "Execution time" in result.output


@pytest.mark.asyncio
async def test_undo_commit(runner):
    """Test the undo command"""
    with runner.isolation():
        result = runner.invoke(undo_command)
        assert result.exit_code == 0


def test_prompt_ask_with_table():
    """Test the prompt_ask function with table display"""
    display_rows = [
        ["Package", "Version", "Status"],
        ["CairoSVG", "2.7.1", "Installed"],
        ["Pillow", "10.0.0", "Installed"],
        ["numpy", "1.24.0", "Installed"],
    ]

    runner = CliRunner()
    with runner.isolation():
        # Simulate user input '1' for the first option
        with runner.isolation(input="1\n"):
            result = prompt_ask(
                "Select a package to uninstall:",
                display_rows=display_rows,
                choices=["CairoSVG", "Pillow", "numpy"],
                enumerate=True,
            )
            assert result == 1, f"Expected result to be 1, got {result}"


def test_who_imports(runner):
    """Test the who-imports command"""
    with runner.isolation():
        result = runner.invoke(cli, ["who-imports", "pytest"])
        assert result.exit_code == 0


def test_cache_commands(runner):
    """Test the cache commands"""
    with runner.isolation():
        # Test cache info
        result = runner.invoke(cli, ["cache", "info"])
        assert result.exit_code == 0

        # Test cache clear
        result = runner.invoke(cli, ["cache", "clear"])
        assert result.exit_code == 0


if __name__ == "__main__":
    pytest.main(["-v", __file__])
