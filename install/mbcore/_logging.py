import logging
import os
from datetime import datetime
from logging import Handler, LogRecord
from pathlib import Path
from types import ModuleType

from rich._null_file import NullFile
from rich.console import Console, ConsoleRenderable
from rich.highlighter import Highlighter, ReprHighlighter
from rich.text import Text, TextType
from typing_extensions import TYPE_CHECKING, Callable, ClassVar, Iterable, List, Type

from mbcore._traceback import Traceback

LIGHT_CYAN_BOLD = "#87d7ff"
CYAN_BOLD = "#00ffff"
PINK_BOLD = "#ffafd7"
LIGHT_BLUE = "#afd7ff"
LIGHT_BLUE_BOLD = "#afd7ff"
RESET = ""  # Resetting the color, no hex value
PINK = "#ffafd7"

THEME = {
    "info": f"{LIGHT_CYAN_BOLD}",
    "success": f"{LIGHT_BLUE}",
    "light_blue": f"{LIGHT_BLUE_BOLD}",
    "reset": RESET,
    "pink": f"{PINK}",
}


FormatTimeCallable = Callable[[datetime], Text]
if TYPE_CHECKING:
    from rich.console import RenderableType
    from rich.table import Table

_in_print: bool = False  # Recursion guard
_console: "Console | None" = None  # type: ignore # noqa


def setconsole(console) -> None:
    global _console
    _console = console


def _safe_print(print_func, *args, **kwargs):
    from rich.text import Text

    global _in_print

    # Prevent infinite recursion
    if _in_print:
        print(*args)
        return lambda *a, **kw: None

    _in_print = True
    try:

        def sp(arg, **kwargs):
            if isinstance(arg, str):
                if "\x1b[" in arg:
                    print_func(Text.from_ansi(arg), **kwargs)
                elif "[" in arg and "]" in arg:
                    print_func(Text.from_markup(arg), **kwargs)
                else:
                    print_func(arg, **kwargs)

        for a in args:
            if isinstance(a, list) and all(isinstance(x, str) for x in a):
                for x in a:
                    sp(x, **kwargs)
            else:
                sp(a, **kwargs)
        return sp
    finally:
        _in_print = False


def getconsole() -> "Console":
    from rich.console import Console
    from rich.theme import Theme

    global _console
    if not _console:
        _console = Console(theme=Theme(THEME), force_terminal=True)
        _console.print = _safe_print(_console.print)  # type: ignore
    return _console


class LogRender:
    def __init__(
        self,
        show_time: bool = True,
        show_level: bool = True,
        show_path: bool = True,
        time_format: str | FormatTimeCallable = "[%D %X]",
        omit_repeated_times: bool = True,
        level_width: int | None = 4,
    ) -> None:
        self.show_time = show_time
        self.show_level = show_level
        self.show_path = show_path
        self.time_format = time_format
        self.omit_repeated_times = omit_repeated_times
        self.level_width = level_width
        self._last_time: Text | None = None
        self.console = getconsole()

    def __call__(
        self,
        console: "Console",
        renderables: Iterable["ConsoleRenderable"],
        log_time: datetime | None = None,
        time_format: str | FormatTimeCallable | None = None,
        level: TextType = "",
        path: str | None = None,
        line_no: int | None = None,
        link_path: str | None = None,
    ) -> "Table":
        from rich.containers import Renderables
        from rich.table import Table

        output = Table.grid(padding=(0, 1))
        output.expand = True
        if self.show_time:
            output.add_column(style="log.time")
        if self.show_level:
            output.add_column(style="log.level", width=self.level_width)
        output.add_column(ratio=1, style="log.message", overflow="fold")
        if self.show_path and path:
            output.add_column(style="log.path")
        row: List["RenderableType"] = []
        if self.show_time:
            log_time = log_time or console.get_datetime()
            time_format = time_format or self.time_format
            log_time_display = time_format(log_time) if callable(time_format) else Text(log_time.strftime(time_format))
            if log_time_display == self._last_time and self.omit_repeated_times:
                row.append(Text(" " * len(log_time_display)))
            else:
                row.append(log_time_display)
                self._last_time = log_time_display
        if level and self.show_level:
            row.append(level)

        row.append(Renderables(renderables))
        if self.show_path and path:
            path_text = Text()
            uri = "file://"
            if any("cursor" in os.environ.get(e, "").lower() for e in os.environ):
                uri = f"cursor://{uri}"
            elif any(e.startswith("VSCODE") for e in os.environ):
                uri = f"vscode://{uri}"

            path_text.append(f"{path}:{line_no}", style=f"link {uri}{link_path}:{line_no}" if link_path else "")
            row.append(path_text)

        output.add_row(*row)
        return output


class RichHandler(Handler):
    """A logging handler that renders output with Rich. The time / level / message and file are displayed in columns.
    The level is color coded, and the message is syntax highlighted.

    Note:
        Be careful when enabling console markup in log messages if you have configured logging for libraries not
        under your control. If a dependency writes messages containing square brackets, it may not produce the intended output.

    Args:
        level (Union[int, str], optional): Log level. Defaults to logging.NOTSET.
        console (:class:`~rich.console.Console`, optional): Optional console instance to write logs.
            Default will use a global console instance writing to stdout.
        show_time (bool, optional): Show a column for the time. Defaults to True.
        omit_repeated_times (bool, optional): Omit repetition of the same time. Defaults to True.
        show_level (bool, optional): Show a column for the level. Defaults to True.
        show_path (bool, optional): Show the path to the original log call. Defaults to True.
        enable_link_path (bool, optional): Enable terminal link of path column to file. Defaults to True.
        highlighter (Highlighter, optional): Highlighter to style log messages, or None to use ReprHighlighter. Defaults to None.
        markup (bool, optional): Enable console markup in log messages. Defaults to False.
        rich_tracebacks (bool, optional): Enable rich tracebacks with syntax highlighting and formatting. Defaults to False.
        tracebacks_width (Optional[int], optional): Number of characters used to render tracebacks, or None for full width. Defaults to None.
        tracebacks_code_width (int, optional): Number of code characters used to render tracebacks, or None for full width. Defaults to 88.
        tracebacks_extra_lines (int, optional): Additional lines of code to render tracebacks, or None for full width. Defaults to None.
        tracebacks_theme (str, optional): Override pygments theme used in traceback.
        tracebacks_word_wrap (bool, optional): Enable word wrapping of long tracebacks lines. Defaults to True.
        tracebacks_show_locals (bool, optional): Enable display of locals in tracebacks. Defaults to False.
        tracebacks_suppress (Sequence[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.
        tracebacks_max_frames (int, optional): Optional maximum number of frames returned by traceback.
        locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to 10.
        locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
        log_time_format (Union[str, TimeFormatterCallable], optional): If ``log_time`` is enabled, either string for strftime or callable that formats the time. Defaults to "[%x %X] ".
        keywords (List[str], optional): List of words to highlight instead of ``RichHandler.KEYWORDS``.

    """  # noqa: D205

    KEYWORDS: ClassVar[List[str] | None] = [
        "GET",
        "POST",
        "HEAD",
        "PUT",
        "DELETE",
        "OPTIONS",
        "TRACE",
        "PATCH",
    ]
    HIGHLIGHTER_CLASS: ClassVar[Type[Highlighter]] = ReprHighlighter

    def __init__(
        self,
        level: int | str = logging.NOTSET,
        console: Console | None = None,
        *,
        show_time: bool = True,
        omit_repeated_times: bool = True,
        show_level: bool = True,
        show_path: bool = True,
        enable_link_path: bool = True,
        highlighter: Highlighter | None = None,
        markup: bool = False,
        rich_tracebacks: bool = False,
        tracebacks_width: int | None = None,
        tracebacks_code_width: int = 88,
        tracebacks_extra_lines: int = 3,
        tracebacks_theme: str | None = None,
        tracebacks_word_wrap: bool = True,
        tracebacks_show_locals: bool = False,
        tracebacks_suppress: Iterable[str | ModuleType] = (),
        tracebacks_max_frames: int = 100,
        locals_max_length: int = 10,
        locals_max_string: int = 80,
        log_time_format: str | FormatTimeCallable = "[%x %X]",
        show_locals: bool = False,
        keywords: List[str] | None = None,
        ignore_third_party: bool = True,
    ) -> None:
        super().__init__(level=level)
        self.highlighter = highlighter or self.HIGHLIGHTER_CLASS()
        self._log_render = LogRender(
            show_time=show_time,
            show_level=show_level,
            show_path=show_path,
            time_format=log_time_format,
            omit_repeated_times=omit_repeated_times,
            level_width=None,
        )
        tracebacks_show_locals = show_locals
        self.enable_link_path = enable_link_path
        self.markup = markup
        self.rich_tracebacks = rich_tracebacks
        self.tracebacks_width = tracebacks_width
        self.tracebacks_extra_lines = tracebacks_extra_lines
        self.tracebacks_theme = tracebacks_theme
        self.tracebacks_word_wrap = tracebacks_word_wrap
        self.tracebacks_show_locals = tracebacks_show_locals
        self.tracebacks_suppress = tracebacks_suppress
        self.tracebacks_max_frames = tracebacks_max_frames
        self.tracebacks_code_width = tracebacks_code_width
        self.locals_max_length = locals_max_length
        self.locals_max_string = locals_max_string
        self.keywords = keywords
        self.ignore_third_party = ignore_third_party
        self.console = console or Console()

    def get_level_text(self, record: LogRecord) -> Text:
        """Get the level name from the record.

        Args:
            record (LogRecord): LogRecord instance.

        Returns:
            Text: A tuple of the style and level name.

        """
        level_name = record.levelname if record.levelno >= 5 else "VERBOSE"
        style = f"logging.level.{level_name.strip().lower()}"
        if record.levelno == -1:
            style = "logging.level.error"
        elif record.levelno >= 50:
            style = "logging.level.critical"
        elif record.levelno >= 40:
            style = "logging.level.error"
        elif record.levelno >= 30:
            style = "logging.level.warning"
        elif record.levelno >= 20:
            style = "logging.level.info"
        elif record.levelno == 11:
            style = "logging.level.error"
        elif record.levelno >= 10:
            style = "logging.level.debug"
        elif record.levelno == 6:
            style = "logging.level.error"
        elif record.levelno >= 5:
            style = "sea_green1"
        elif record.levelno == 2:
            style = "logging.level.error"
        elif record.levelno >= 1:
            style = "sky_blue1"
        level_text = Text.styled(level_name.ljust(8), style)
        return level_text

    def emit(self, record: LogRecord) -> None:
        """Invoke logging."""
        message = self.format(record)
        traceback = None
        if self.rich_tracebacks and record.exc_info and record.exc_info != (None, None, None):
            exc_type, exc_value, exc_traceback = record.exc_info
            traceback = Traceback.from_exception(
                exc_type or Exception,
                exc_value or Exception(),
                exc_traceback,
                width=self.tracebacks_width,
                code_width=self.tracebacks_code_width,
                extra_lines=self.tracebacks_extra_lines,
                theme=self.tracebacks_theme,
                word_wrap=self.tracebacks_word_wrap,
                show_locals=self.tracebacks_show_locals,
                locals_max_length=self.locals_max_length,
                locals_max_string=self.locals_max_string,
                excluded_modules=self.tracebacks_suppress,
                max_frames=self.tracebacks_max_frames,
                ignore_third_party=self.ignore_third_party,
            )
            message = record.getMessage()
            if self.formatter:
                record.message = record.getMessage()
                formatter = self.formatter
                if hasattr(formatter, "usesTime") and formatter.usesTime():
                    record.asctime = formatter.formatTime(record, formatter.datefmt)
                message = formatter.formatMessage(record)

        message_renderable = self.render_message(record, message)
        log_renderable = self.render(record=record, traceback=traceback, message_renderable=message_renderable)
        self.console = self.console or Console()
        if isinstance(self.console.file, NullFile):
            # Handles pythonw, where stdout/stderr are null, and we return NullFile
            # instance from Console.file. In this case, we still want to make a log record
            # even though we won't be writing anything to a file.
            self.handleError(record)
        else:
            try:
                self.console = Console()
                self.console.print(log_renderable)
            except Exception as e:
                record.msg = f"Error occurred while logging message: {record.msg}"
                record.levelname = "ERROR"
                record.levelno = logging.ERROR
                record.exc_info = (type(e), e, e.__traceback__)
                self.handleError(record)

    def handleError(self, record: LogRecord) -> None:
        """Handle an error during logging.

        Args:
            record (LogRecord): LogRecord instance.

        """
        record = logging.makeLogRecord(record.__dict__)
        record.msg = f"Error occurred while logging message: {record.msg}"
        raise Exception("Error occurred while logging message" + record.msg)

    def render_message(self, record: LogRecord, message: str) -> "ConsoleRenderable":
        """Render message text in to Text.

        Args:
            record (LogRecord): logging Record.
            message (str): String containing log message.

        Returns:
            ConsoleRenderable: Renderable to display log message.

        """
        use_markup = getattr(record, "markup", self.markup)
        try:
            message_text = Text.from_markup(message) if use_markup else Text(message)
        except Exception:
            message_text = Text(message)

        highlighter = getattr(record, "highlighter", self.highlighter)
        if highlighter:
            message_text = highlighter(message_text)

        if self.keywords is None:
            self.keywords = self.KEYWORDS

        if self.keywords:
            message_text.highlight_words(self.keywords, "logging.keyword")
        if record.module:
            message_text.highlight_words([record.module], "logging.module")
        return message_text

    def render(
        self,
        *,
        record: LogRecord,
        traceback: Traceback | None,
        message_renderable: "ConsoleRenderable",
    ) -> "ConsoleRenderable":
        """Render log for display.

        Args:
            record (LogRecord): logging Record.
            traceback (Optional[Traceback]): Traceback instance or None for no Traceback.
            message_renderable (ConsoleRenderable): Renderable (typically Text) containing log message contents.

        Returns:
            ConsoleRenderable: Renderable to display log.

        """
        path = Path(record.pathname).name
        level = self.get_level_text(record)
        time_format = None if self.formatter is None else self.formatter.datefmt
        log_time = datetime.fromtimestamp(record.created)

        return self._log_render(
            self.console,
            [message_renderable] if not traceback else [message_renderable, traceback],
            log_time=log_time,
            time_format=time_format,
            level=level,
            path=path,
            line_no=record.lineno,
            link_path=record.pathname if self.enable_link_path else None,
        )


if __name__ == "__main__":  # pragma: no cover
    from time import sleep

    FORMAT = "%(message)s"
    # FORMAT = "%(asctime)-15s - %(levelname)s - %(message)s"
    logging.basicConfig(
        level="NOTSET",
        format=FORMAT,
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True, tracebacks_show_locals=True)],
    )
    log = logging.getLogger("rich")

    log.info("Server starting...")
    log.info("Listening on http://127.0.0.1:8080")
    sleep(1)

    log.info("GET /index.html 200 1298")
    log.info("GET /imgs/backgrounds/back1.jpg 200 54386")
    log.info("GET /css/styles.css 200 54386")
    log.warning("GET /favicon.ico 404 242")
    sleep(1)

    log.debug(
        "JSONRPC request\n--> %r\n<-- %r",
        {
            "version": "1.1",
            "method": "confirmFruitPurchase",
            "params": [["apple", "orange", "mangoes", "pomelo"], 1.123],
            "id": "194521489",
        },
        {"version": "1.1", "result": True, "error": None, "id": "194521489"},
    )
    log.debug(
        "Loading configuration file /adasd/asdasd/qeqwe/qwrqwrqwr/sdgsdgsdg/werwerwer/dfgerert/ertertert/ertetert/werwerwer",
    )
    log.error("Unable to find 'pomelo' in database!")
    log.info("POST /jsonrpc/ 200 65532")
    log.info("POST /admin/ 401 42234")
    log.warning("password was rejected for admin site.")

    def divide() -> None:
        number = 1
        divisor = 0
        foos = ["foo"] * 100
        log.debug("in divide")
        try:
            number / divisor
        except:
            log.exception("An error of some kind occurred!")

    divide()
    sleep(1)
    log.critical("Out of memory!")
    log.info("Server exited with code=-1")
    log.info("[bold]EXITING...[/bold]", extra=dict(markup=True))
