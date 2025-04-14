from mbcore.display import NO_BOX
import rich_click as click
from dataclasses import dataclass, field
import os
from typing import Literal, List, Dict
import rich
import rich.style
import rich.align
from rich.box import Box
from rich.text import Text
from rich.align import AlignMethod
from rich.padding import PaddingDimensions
from rich_click.rich_help_configuration import RichHelpConfiguration
from rich_click.utils import CommandGroupDict, OptionGroupDict


@dataclass
class RichHelpConfig(RichHelpConfiguration):
    """Streamlined help configuration with consistent branding."""

    # # Fixed strings
    # header_text: "Text | str|None" = field(default=None)
    # footer_text: "Text | str|None" = field(default=None)
    # deprecated_string: str = field(default="(Deprecated) ")
    # default_string: str = field(default="[default: {}]")
    # envvar_string: str = field(default="[env var: {}]")
    # required_short_string: str = field(default="*")
    # required_long_string: str = field(default="[required]")
    # range_string: str = field(default=" [{}]")
    # arguments_panel_title: str = field(default="Arguments")
    # options_panel_title: str = field(default="Options")
    # commands_panel_title: str = field(default="Commands")
    # errors_panel_title: str = field(default="Error")
    # errors_suggestion: "Text | str | None" = field(default="Try ' --help' for help.")
    # """Defaults to Try 'cmd -h' for help. Set to False to disable."""
    # errors_epilogue: "Text | str | None" = field(default=None)
    # aborted_text: str = field(default="Aborted.")

    # Behaviours
    show_arguments: bool = field(default=True)
    """Show positional arguments"""
    show_metavars_column: bool = field(default=True)
    """Show a column with the option metavar (eg. INTEGER)"""
    append_metavars_help: bool = field(default=False)
    """Append metavar (eg. [TEXT]) after the help text"""
    option_envvar_first: bool = field(default=False)
    """Show env vars before option help text instead of after"""
    text_markup: Literal["ansi", "rich", "markdown", None] = "rich"

    use_markdown_emoji: bool = field(default=True)
    """Parse emoji codes in markdown :smile:"""
    # command_groups: "Dict[str, List[CommandGroupDict]]" = field(default_factory=lambda: {
    #     "CORE": [CommandGroupDict(
    #     name="PACKAGING", commands=["install", "uninstall", "freeze", "list", "search", "show", "upload"],
    # )]
    # })
    """Define sorted groups of panels to display subcommands"""
    # option_groups: "Dict[str, List[OptionGroupDict]]" = field(default_factory=lambda: {})
    """Define sorted groups of panels to display options and arguments"""
    # use_click_short_help: bool = field(default=True)
    """Use click's default function to truncate help text"""

    highlighter_patterns: List[str] = field(
        default_factory=lambda: [
            r"(^|[^\w\-])(?P<switch>-([^\W0-9][\w\-]*\w|[^\W0-9]))",
            r"(^|[^\w\-])(?P<option>--([^\W0-9][\w\-]*\w|[^\W0-9]))",
            r"(?P<metavar><[^>]+>)",
        ]
    )

    # Core brand colors
    PINK_BOLD = "bold #ffd7e5"
    GOLD_BOLD = "bold #ffd7af"
    WHITE_BOLD = "bold white"
    PINK = "#ffd7e5"
    GOLD = "#ffd7af"
    style_helptext_first_line: "rich.style.StyleType" = field(default="bold white")
    # Essential styles
    style_command: "rich.style.StyleType" = field(default=GOLD_BOLD)
    style_option: "rich.style.StyleType" = field(default=PINK_BOLD)
    style_usage: "rich.style.StyleType" = field(default=PINK_BOLD)
    style_header_text: "rich.style.StyleType" = field(default=WHITE_BOLD)
    style_helptext: "rich.style.StyleType" = field(default="bold dark_slate_gray3")

    # Remove all panels/boxes
    style_options_panel_box: "str | Box | None" = field(default=NO_BOX)
    style_commands_panel_box: "str | Box | None" = field(default=NO_BOX)
    style_errors_panel_box: "str | Box | None " = field(default=NO_BOX)

    # Layout settings
    align_options_panel: "rich.align.AlignMethod" = field(default="left")
    align_commands_panel: "rich.align.AlignMethod" = field(default="left")
    align_errors_panel: "rich.align.AlignMethod" = field(default="left")
    style_options_table_show_lines: bool = field(default=False)
    style_commands_table_show_lines: bool = field(default=False)
    style_options_table_padding: "PaddingDimensions" = field(
        default_factory=lambda: (0, 2)
    )

    # Section titles
    arguments_panel_title: str = field(default="ARGUMENTS:")
    options_panel_title: str = field(default="OPTIONS:")
    commands_panel_title: str = field(default="COMMANDS:")

    # Error handling

    style_errors_suggestion: "rich.style.StyleType" = field(default=PINK_BOLD)
    style_errors_suggestion_command: "rich.style.StyleType" = field(default=PINK_BOLD)
    errors_panel_title: str = field(default="")
    # errors_suggestion: "str| rich.text.Text | None" = field(default=

    # Width settings
    try:
        width: int | None = field(default=os.get_terminal_size().columns)
        max_width: int | None = field(default=120)
    except OSError:
        width: int | None = field(default=120)
        max_width: int | None = field(default=120)

    # Enable command grouping
    group_arguments_options: bool = field(default=True)
    command_groups: Dict[str, List[CommandGroupDict]] = field(
        default_factory=lambda: {
            "PACKAGE": [
                CommandGroupDict(
                    name="commands",
                    commands=[
                        "install/add",
                        "uninstall/remove",
                        "list/show",
                        "search",
                        "upload",
                        "publish",
                    ],
                )
            ],
            "DEVELOP": [
                CommandGroupDict(
                    name="DEVELOP",
                    commands=["build", "clean", "log", "git", "sync", "undo", "docs"],
                )
            ],
            "ANALYZE": [
                CommandGroupDict(
                    name="ANALYZE", commands=["graph", "run", "time", "log"]
                )
            ],
        }
    )
    """Define sorted groups of panels to display subcommands"""
    option_groups: Dict[str, List[OptionGroupDict]] = field(
        default_factory=lambda: {
            "GLOBAL": [
                OptionGroupDict(
                    name="GLOBAL",
                    options=[
                        "--debug",
                        "--env",
                        "--no-third-party",
                        "--verbose",
                        "--quiet",
                        "--vverbose",
                    ],
                )
            ]
        }
    )
