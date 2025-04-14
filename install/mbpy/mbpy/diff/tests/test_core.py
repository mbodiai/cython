import pytest
from rich.console import Console
from rich.errors import NotRenderableError

from mbpy.diff import DiffBlock, DiffContext, DiffParser
from mbpy.diff.diff import DiffViewer


@pytest.fixture
def sample_diff():
    return [
        "@@ -1,3 +1,4 @@",
        " def hello():",
        "-    print('hello')",
        "+    print('hello world')",
        "+    return True",
        " ",
    ]


@pytest.fixture
def diff_block():
    return DiffBlock(
        header="@@ -1,3 +1,4 @@",
        changes=[
            "-    print('hello')",
            "+    print('hello world')",
            "+    return True",
        ],
        context=DiffContext(
            before=[" def hello():"],
            after=[" "],
        ),
    )


def test_diff_block_initialization(diff_block) -> None:
    assert diff_block.header == "@@ -1,3 +1,4 @@"
    assert diff_block.changes == [
        "-    print('hello')",
        "+    print('hello world')",
        "+    return True",
    ]
    assert diff_block.context.before == [" def hello():"]
    assert diff_block.context.after == [" "]
    assert not diff_block.is_folded
    assert not diff_block.is_selected


def test_diff_block_toggle_fold(diff_block) -> None:
    assert not diff_block.is_folded
    diff_block.toggle_fold()
    assert diff_block.is_folded
    diff_block.toggle_fold()
    assert not diff_block.is_folded


def test_diff_block_generate_description_addition(diff_block) -> None:
    expected_description = "print('hello world')"
    assert diff_block.description == expected_description


def test_diff_block_generate_description_no_addition() -> None:
    block = DiffBlock(
        header="@@ -1,0 +1,0 @@",
        changes=["-remove line", "-another remove"],
        context=DiffContext(before=[], after=[]),
    )
    assert block.description == "@@ -1,0 +1,0 @@"


def test_diff_block_description_truncation() -> None:
    long_line = "+" + "x" * 100
    block = DiffBlock(
        header="@@ -1,1 +1,1 @@",
        changes=[long_line],
        context=DiffContext(before=[], after=[]),
    )
    assert len(block.description) <= 60
    assert block.description.endswith("...")


def test_parser_creates_blocks(sample_diff) -> None:
    blocks = DiffParser.parse_blocks(sample_diff)
    assert len(blocks) == 1
    assert blocks[0].header == "@@ -1,3 +1,4 @@"
    assert len(blocks[0].changes) == 3
    assert len(blocks[0].context.before) == 1
    assert len(blocks[0].context.after) == 1


def test_parser_multiple_blocks() -> None:
    multiple_diff = [
        "@@ -1,2 +1,2 @@",
        "-old line",
        "+new line",
        "@@ -4,3 +4,4 @@",
        " unchanged line",
        "-removed line",
        "+added line",
        "+another added line",
    ]
    blocks = DiffParser.parse_blocks(multiple_diff)
    assert len(blocks) == 2
    assert blocks[0].header == "@@ -1,2 +1,2 @@"
    assert blocks[1].header == "@@ -4,3 +4,4 @@"


def test_diff_block_description_prefers_additions() -> None:
    block = DiffBlock(
        header="@@ -1,2 +1,2 @@",
        changes=[
            "-    old code",
            "+    new code",
        ],
        context=DiffContext(before=[], after=[]),
    )
    assert block.description == "new code"


def test_diff_viewer_layout_renderable(sample_diff) -> None:
    """Test that DiffViewer's layout is renderable without errors."""
    blocks = DiffParser.parse_blocks(sample_diff)
    viewer = DiffViewer(blocks)
    console = Console()
    try:
        viewer.update_display()
        console.print(viewer.layout)
    except NotRenderableError:
        pytest.fail("DiffViewer layout is not renderable")
