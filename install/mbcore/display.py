from threading import Thread

from rich.box import Box
from rich.console import Console
from typing_extensions import (
    TYPE_CHECKING,
    Any,
    Callable,
    Generator,
    Literal,
    ParamSpec,
    TypeVar,
)

from mbcore.import_utils import smart_import

NO_BOX = Box("    \n" * 8)
BOX_TYPE: Box = NO_BOX

_progress: "Progress|None" = None  # type: ignore # noqa
_spinner: "Spinner|None" = None  # type: ignore # noqa
from mbcore._logging import _console

if TYPE_CHECKING:
    from types import FunctionType
    from rich.console import RenderableType as Renderable
    from rich.progress import Progress
    from rich.progress import TaskID as TaskID
    from rich.text import Text
    from typing_extensions import (
        Any,
        Callable,
        Literal,
        ParamSpec,
        Protocol,
        TypeIs,
        TypeVar,
    )

    from mbcore.types import wrapafter

    P = ParamSpec("P")
    R = TypeVar("R")
    T = TypeVar("T")

else:
    Progress = Any
    TaskID = Any
    Text = Any
    Renderable = Any

    P = lambda *args, **kwargs: object()
    R = lambda *args, **kwargs: object()
    T = lambda *args, **kwargs: object()

    class Protocol:
        __class_getitem__ = classmethod(lambda cls, item: object)

    class FunctionType:
        __call__ = lambda self, *args, **kwargs: object()

    class TypeIs:
        __args__ = lambda self: object()

    def wrapafter(*args, **kwargs):
        return lambda f: f


def setspinner(spinner) -> None:
    global _spinner
    _spinner = spinner


def getspinner() -> "Spinner":
    global _spinner
    if not _spinner:
        _spinner = SPINNER()
    return _spinner


def raw_print(*args, **kwargs) -> None:
    getspinner().stop()
    getprogress().stop()
    print(*args, **kwargs)


@wrapafter(Progress, returns=Progress)
def getprogress(*args, **kwargs) -> "Progress":
    kw = {"expand": True, "transient": True, "speed_estimate_period": 0.1}
    kw.update(kwargs)
    global _progress
    if not _progress:
        from rich.progress import Progress

        _progress = Progress(*args, **kw)
        setprogress(_progress)
        setconsole(_progress.console)
    return _progress


def setprogress(progress: "Progress") -> None:
    global _progress
    _progress = progress


@wrapafter(Console.print, returns=None)
def safe_print(*args, **kwargs) -> None:
    getspinner().stop()
    getprogress().stop()
    args = tuple(
        list(arg) if isinstance(arg, Generator) else arg for arg in args)
    getconsole().print(*args, **kwargs)


def safe_text(*strs: "str | Text") -> "Text":
    """Handle ANSI and markup in text by combining them into a Text object.

    Args:
        *strs: Variable number of strings or Text objects to combine

    Returns:
        Text: A combined Text object with preserved styling

    """
    from rich.text import Text

    out = []
    for s in strs:
        if isinstance(s, Text):
            out.append(s)
        elif "\x1b[" in s:  # ANSI escape sequence
            out.append(Text.from_ansi(s))
        elif "[" in s and "]" in s:  # Rich markup
            out.append(Text.from_markup(s))
        else:
            out.append(Text(s))

    return Text.assemble(*out)


def safe_str(*strs: "str | Text") -> str:
    """Convert a list of strings or Text objects to a single string."""
    if not TYPE_CHECKING:
        from contextlib import redirect_stderr, redirect_stdout
        from io import StringIO
    else:
        StringIO = smart_import("io.StringIO")
        redirect_stdout = smart_import("contextlib.redirect_stdout")
        redirect_stderr = smart_import("contextlib.redirect_stderr")
    stdout = StringIO()
    stderr = StringIO()

    with redirect_stdout(stdout), redirect_stderr(stderr):
        setconsole(Console(width=120, force_terminal=True))
        safe_print(*strs)
    return stdout.getvalue() + ("" if not stderr.getvalue() else "\n" +
                                stderr.getvalue())


def format_timestamp(timestamp: str) -> str:
    from datetime import datetime

    from dateutil.parser import parse
    from dateutil.relativedelta import relativedelta

    if not timestamp.strip():
        return ""
    dt = parse(timestamp)
    now = datetime.now(dt.tzinfo)
    rd = relativedelta(now, dt)

    if rd.days == 0:
        return "today"
    if rd.days == 1:
        return "yesterday"
    if rd.days < 7:
        return f"{rd.days} days ago"
    if rd.months == 0:
        return f"{rd.weeks} weeks ago"
    if rd.years == 0:
        return dt.strftime("%B %d")  # e.g. "November 22"

    return dt.strftime("%B %d, %Y")  # e.g. "November 22, 2024")


def confirm(
    *prompt: "str| Renderable",
    default: bool = False,
    show_choices: bool = True,
    choices: list[str] | None = None,
) -> bool:
    """Prompt the user with a yes/no question."""
    from rich.prompt import Confirm

    safe_print(*prompt)

    return Confirm.ask("",
                       default=default,
                       show_choices=show_choices,
                       choices=choices,
                       console=Console(width=120))


enumer = enumerate


def prompt_ask(
    prompt: str,
    choices: list[str] | None = None,
    show_choices: bool = True,
    default=None,
    enumerate=False,
    prelude=None,
    display_rows=None,
    type: Literal["auto", "form", "confirm"] = "auto",
) -> str | int | bool:
    """Prompt the user with a question.

    Usage:
    ```python
    >>> prompt_ask("What is your name?", choices=["Alice", "Bob", "Charlie"])
    What is your name?
    (1) Alice
    (2) Bob
    (3) Charlie
    Enter a number:
    ```
    """
    from rich.console import Console
    from rich.prompt import Confirm, Prompt
    from rich.table import Table

    from mbcore.log import verbose

    # Stop any spinners or progress bars
    getspinner().stop()
    getprogress().stop()

    # Create a new console for the prompt
    console = Console()

    try:
        # Handle prelude and display rows if present
        if prelude:
            console.print(prelude)
        if display_rows:
            table = Table(show_header=False, box=NO_BOX, border_style="")
            for row in display_rows:
                table.add_row(*row)
            console.print(table)

        # Handle different types of prompts
        if not choices and type == "confirm":
            verbose(f"Prompting user with {prompt}")
            return Confirm.ask(prompt, console=console)

        if choices and enumerate:
            cs = list(enumer(choices))
            prompt += " " + "\n" + "\n".join(f"({i + 1}) {choice}"
                                             for i, choice in cs)
            choices = [str(i + 1) for i, choice in cs]
            show_choices = False

        verbose(f"Prompting user with {prompt}")
        out = Prompt.ask(prompt,
                         choices=choices,
                         show_choices=show_choices,
                         default=default,
                         console=console)
        return int(out) if enumerate else out

    except KeyboardInterrupt:
        console.print("[cyan]Operation cancelled.[/cyan]")
        raise


def iscallable(v: Any) -> "TypeIs[FunctionType]":
    """Check if a value is callable."""
    return callable(v)


def getkeys(obj: "dict[str,Any]|list[Any]|object") -> "list[str]":
    if isinstance(obj, dict):
        return list(obj.keys())
    if isinstance(obj, list):
        return obj
    raise TypeError(f"Expected dict or list, got {type(obj)}")


def list_or_dict_table(
    items: "Iterable[T]",
    title: str | None = None,
    title_style: "Style|str|None" = None,
    columns:
    "list[str]|dict[str, Style|str] | dict[str, Style|str| Callable[[T]]]|None" = None,
    stylemap: "Callable[[T], dict[str, Style|str]]|None" = None,
    console: "Console | None" = None,
    column_width: int | None = None,
) -> "Columns|Table|Group":
    # Calculate number of rows based on terminal height with more buffer

    from rich.columns import Columns
    from rich.console import Group
    from rich.style import Style
    from rich.table import Table
    from rich.text import Text

    from mbcore.display import getconsole
    from mbcore.more import ilen

    def identity(x):
        return x

    from collections.abc import Mapping
    from itertools import islice

    from mbcore.display import NO_BOX

    console = console or getconsole()
    term_height = console.height
    num_items = ilen(items)

    keys = getkeys(
        columns if not callable(columns) and columns is not None else
        columns(next(iter(items), {})) if columns is not None else next(
            iter(items), {}), )

    max_rows = term_height - 15  # Increased buffer for better spacing

    # Calculate optimal number of columns based on terminal width
    avg_item_width = 25  # Estimated average width for package name + version
    term_width = console.width
    max_columns = max(1, term_width //
                      (avg_item_width + 8))  # Add padding consideration

    # Recalculate   rows needed based on number of packages and max columns
    max_rows = min(max_rows, (num_items + max_columns - 1) // max_columns)
    num_columns = (num_items + max_rows - 1) // max_rows if max_rows > 0 else 1

    cs = (dict(map(lambda x: (x[0].lower(), x[1]), columns.items()))
          if isinstance(columns, Mapping) else
          dict(map(lambda x: (x.lower(), x), columns)) if isinstance(
              columns, list) else dict(map(lambda x: (x.lower(), x), keys)))

    # Create all tables first
    tables = []
    if column_width:
        for col_idx in range(num_columns):
            start_idx = col_idx * max_rows
            end_idx = min((col_idx + 1) * max_rows, num_items)
            row = []
            table = Table(title=Text(""), box=NO_BOX, show_edge=False)
            for key in keys:
                key = key.lower()
                style = cs[key] if not iscallable(cs[key]) else None
                table.add_column(key,
                                 style=style if isinstance(style, Style
                                                           | str) else None)

            for item in islice(items, start_idx, end_idx):
                row = []
                for k in keys:
                    if isinstance(item, tuple):
                        it, style = item

                        c = cs[k] if not iscallable(cs[k]) else None
                        style = c if isinstance(
                            c, Style
                            | str) else stylemap(it).get(k) if stylemap else ""
                        val = c(it) if iscallable(c) else getattr(
                            it, k.lower())
                        row.append(Text.from_markup(str(val)))

                    else:
                        c = cs[k.lower()]
                        val = c(item) if iscallable(c) else getattr(
                            item, k.lower())
                        style = c if isinstance(c, Style | str) else stylemap(
                            item).get(k) if stylemap else ""
                        row.append(Text.from_markup(str(val)))
                table.add_row(*row)
            tables.append(table)
        table = None
    else:
        table = Table(title=Text(""), box=NO_BOX, show_edge=False)
        for key in keys:
            key = key.lower()
            c = cs[key]
            table.add_column(key,
                             style=c if isinstance(c, Style | str) else None)

        for item in items:
            row = []
            for k in keys:
                if isinstance(item, tuple):
                    it, style = item

                    c = cs[k]
                    style = c if isinstance(c, Style | str) else stylemap(
                        it).get(k.capitalize()) if stylemap else ""
                    val = c(it) if iscallable(c) else getattr(it, k)
                    row.append(
                        Text.from_markup(str(val), style=style)
                        if not isinstance(val, Text) else val)
                else:
                    k = k.lower()
                    c = cs[k]
                    val = c(item) if iscallable(c) else getattr(item, k)
                    style = c if isinstance(c, Style | str) else stylemap(
                        item).get(k.capitalize()) if stylemap else ""
                    row.append(
                        Text.from_markup(str(val), style=style)
                        if not isinstance(val, Text) else val)

            table.add_row(*row)

    stylekwargs = {}
    if title_style:
        stylekwargs["style"] = title_style
    titled = Text(title.capitalize() if title else " ", **stylekwargs)
    if not column_width and title and table:
        return Group(Text(""), titled, Text(""), table)
    if not column_width and table:
        return table
    if title:
        return Group(
            Text(""), titled, Text(""),
            Columns(tables, padding=(0, 4), equal=True, width=column_width))
    return Columns(tables, padding=(0, 4), equal=True, width=column_width)


class Spinner(Protocol):

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...

    spinning: bool


def SPINNER() -> Spinner:
    global _spinner
    if _spinner:
        return _spinner

    import asyncio
    import signal
    import threading
    from time import sleep

    from rich.spinner import Spinner as RichSpinner

    from mbcore.even._internal._display import Live

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    class Spinner:

        def __init__(self,
                     text: str = "Working...",
                     spinner_type: str = "dots2",
                     console=None):
            self.text = text
            self.spinner_type = spinner_type
            self.spinning = False
            self.stop_requested = False
            self._spinner = RichSpinner(spinner_type, text)
            self._console = console or Console()
            self._live = Live(self._spinner,
                              refresh_per_second=20,
                              transient=True,
                              console=self._console)

            self._thread: "Thread | None" = None
            self._stop_event = threading.Event()

            import atexit

            atexit.register(self.cleanup)

        def _spin(self):
            with self._live:
                try:
                    while not self._stop_event.is_set(
                    ) and not self.stop_requested:
                        sleep(0.1)
                        self._live.update(self._spinner)
                    self.spinning = False
                except KeyboardInterrupt:
                    print("KeyboardInterrupt")
                    self.stop_requested = True
                    self._live.console.clear_live()
                    getconsole().clear_live()
                    self._live.stop()
                    self.stop()

        async def astart(self) -> None:
            await asyncio.to_thread(self.start)

        def start(self) -> None:
            if self.spinning:
                return
            self.spinning = True
            self._thread = threading.Thread(target=self._spin, daemon=True)
            self._thread.start()

        async def astop(self) -> None:
            if not self.spinning or self.stop_requested:
                return
            self.stop()

        def stop(self) -> None:
            self._live.stop()
            self._live.console.clear_live()
            getconsole().clear_live()
            if not self.spinning:
                return
            self.stop_requested = True
            self._stop_event.set()
            if self._thread and self._thread.is_alive():
                self._thread.join()
                self._thread = None
            self._console.clear_live()
            self._live.stop()
            self.spinning = False
            self._spinner = None
            global _spinner
            _spinner = None

        def cleanup(self, signum: int | None = None, frame=None) -> None:
            self.stop()

    _spinner = Spinner()
    return _spinner


def getconsole() -> Console:
    """Get the current console."""
    global _console
    if _console is None:
        _console = Console()
    return _console


def setconsole(console: Console) -> None:
    """Set the current console."""
    global _console
    _console = console
