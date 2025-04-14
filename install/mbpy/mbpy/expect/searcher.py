from collections.abc import Iterable
import re
from re import Pattern, Match
from typing import Any, Protocol, TypeVar, cast
from mbpy.expect.exceptions import EOF, TIMEOUT

# TypeVar changed to invariant to fix covariance error
_T = TypeVar("_T", str, bytes)
AnyStrT = TypeVar("AnyStrT", str, bytes)
AnyStrT_co = TypeVar("AnyStrT_co", str, bytes, covariant=True)


class SearcherStringT(Protocol[AnyStrT]):
    eof_index: int
    timeout_index: int
    match: AnyStrT | Match[AnyStrT] | None
    start: int
    end: int
    longest_string: int | None = None
    ignorecase: bool = False
    encoding: str | None = None
    _string_type: type[AnyStrT]

    def __new__(
        cls, patterns: Any | None = None, ignore_case: bool = False, exact: bool = True
    ):
        if not hasattr(cls, "_string_type"):
            cls._string_type = cast(type[AnyStrT], str)
        inst = super().__new__(cls)
        if not hasattr(inst, "_string_type"):
            inst._string_type = cls._string_type
        return inst

    def search(
        self, buffer: AnyStrT, freshlen: int, searchwindowsize: int | None = None
    ) -> int: ...
    def prepare_patterns(self, patterns: Iterable[AnyStrT | EOF | TIMEOUT]): ...

    def __init__(
        self, patterns: Any | None = None, ignore_case: bool = False, exact: bool = True
    ):
        self.eof_index = -1
        self.timeout_index = -1
        self.match = None
        self.start = 0
        self.end = 0
        self.ignorecase = ignore_case
        self.encoding = None
        self.longest_string = 0

        if patterns is not None and exact:
            patterns = self.compile_exact(patterns, ignore_case)
            self.prepare_patterns(patterns)
        elif patterns is not None and not exact:
            patterns = self.compile_pattern_list(patterns, ignore_case, exact)
            self.prepare_patterns(patterns)

    @property
    def string_type(self) -> type[AnyStrT]:
        return self._string_type

    def _coerce_expect_string(self, s: Any) -> AnyStrT | EOF | TIMEOUT:
        if isinstance(s, self._string_type):
            return cast(
                AnyStrT,
                s.encode("ascii")
                if not isinstance(s, bytes | bytearray | memoryview)
                else s,
            )
        return cast(AnyStrT | EOF | TIMEOUT, s)

    def _coerce_expect_re(self, r: "re.Pattern"):
        p = r.pattern
        if self.encoding is None and not isinstance(p, bytes):
            return re.compile(p.encode("utf-8"))
        if self.encoding is not None and isinstance(p, bytes):
            return re.compile(p.decode("utf-8"))
        return r

    def _pattern_type_err(self, pattern):
        raise TypeError(
            "got {badtype} ({badobj!r}) as pattern, must be one"
            " of: {goodtypes}, EOF, TIMEOUT".format(
                badtype=type(pattern),
                badobj=pattern,
                goodtypes=", ".join([str(ast) for ast in (self._string_type,)]),
            ),
        )

    def compile_exact(
        self,
        patterns: AnyStrT | EOF | TIMEOUT | list[AnyStrT | EOF | TIMEOUT],
        ignorecase: bool = False,
    ) -> list[AnyStrT | EOF | TIMEOUT]:
        pattern_list = patterns if isinstance(patterns, list) else [patterns]

        def prepare_pattern(
            pattern: AnyStrT | TIMEOUT | EOF,
        ) -> AnyStrT | TIMEOUT | EOF | None:
            if pattern in (TIMEOUT, EOF):
                return pattern
            if isinstance(pattern, self._string_type):
                return pattern
            if isinstance(pattern, type(re.compile(""))):
                return self._coerce_expect_string(pattern)
            self._pattern_type_err(pattern)
            return None

        return [p for p in [prepare_pattern(p) for p in pattern_list] if p is not None]

    def compile_pattern_list(
        self, patterns: Any | list[Any], ignorecase: bool = False, exact: bool = True
    ) -> "list[re.Pattern[AnyStrT]|type[EOF]|type[TIMEOUT]]":
        if patterns is None:
            return []

        compile_flags = re.DOTALL
        if ignorecase:
            compile_flags = compile_flags | re.IGNORECASE
        compiled_pattern_list: list[re.Pattern | type[EOF] | type[TIMEOUT]] = []
        pattern_list = patterns if isinstance(patterns, list) else [patterns]
        for _idx, p in enumerate(pattern_list):
            p = self._coerce_expect_string(p)
            if isinstance(p, self._string_type) and p not in (EOF, TIMEOUT):
                compiled_pattern_list.append(re.compile(cast(Any, p), compile_flags))
            elif p is EOF:
                compiled_pattern_list.append(EOF)
            elif p is TIMEOUT:
                compiled_pattern_list.append(TIMEOUT)
            elif isinstance(p, type(re.compile(""))):
                p = self._coerce_expect_re(p)
                compiled_pattern_list.append(p)
            else:
                self._pattern_type_err(p)
        return compiled_pattern_list


class searcher_string(SearcherStringT[AnyStrT]):
    """String searcher implementation"""

    _string_type: type[AnyStrT]

    def __init__(
        self, patterns: Any | None = None, ignore_case: bool = False, exact: bool = True
    ):
        self._strings: list[tuple[int, AnyStrT]] = []
        super().__init__(patterns, ignore_case, exact)

    def prepare_patterns(self, strings: Iterable[AnyStrT | EOF | TIMEOUT]):
        self.eof_index = -1
        self.timeout_index = -1
        self._strings = []
        self.longest_string = 0
        self.match = None

        for idx, s in enumerate(strings):
            if s is EOF:
                self.eof_index = idx
                continue
            if s is TIMEOUT:
                self.timeout_index = idx
                continue
            if isinstance(s, self._string_type):
                self._strings.append((idx, cast(AnyStrT, s)))
                self.longest_string = max(self.longest_string, len(cast(Any, s)))

    def __str__(self):
        entries = [(idx, f"    {idx}: {repr(s)}") for idx, s in self._strings]
        if self.eof_index >= 0:
            entries.append((self.eof_index, f"    {self.eof_index}: EOF"))
        if self.timeout_index >= 0:
            entries.append((self.timeout_index, f"    {self.timeout_index}: TIMEOUT"))
        entries.sort()
        return "\n".join(map(str, entries))

    def search(
        self, buffer: AnyStrT, freshlen: int, searchwindowsize: int | None = None
    ) -> int:
        first_match = None
        best_index = -1
        best_match = None

        for index, s in self._strings:
            if searchwindowsize is not None:
                searchstart = max(0, len(buffer) - searchwindowsize)
            else:
                searchstart = max(0, len(buffer) - freshlen - len(s) + 1)

            n = buffer.find(s, searchstart)
            if n >= 0 and (first_match is None or n < first_match):
                first_match = n
                best_index = index
                best_match = s

        if first_match is None or best_match is None:
            return -1

        self.match = best_match
        self.start = first_match
        self.end = first_match + len(best_match)
        return best_index


class searcher_re(SearcherStringT[str]):
    """Regular expression searcher implementation"""

    _string_type: type[str] = str

    def __init__(
        self, patterns: Any | None = None, ignore_case: bool = False, exact: bool = True
    ):
        self._searches: list[tuple[int, Pattern]] = []
        super().__init__(patterns, ignore_case, exact)

    def _coerce_expect_string(self, s: Any) -> str | EOF | TIMEOUT:
        if isinstance(s, self._string_type):
            return cast(str, s)
        return cast(str | EOF | TIMEOUT, s)

    def prepare_patterns(self, patterns: Iterable[Pattern | EOF | TIMEOUT]):
        self.eof_index = -1
        self.timeout_index = -1
        self._searches = []
        self.longest_string = None

        for idx, pat in enumerate(patterns):
            if pat is EOF:
                self.eof_index = idx
                continue
            if pat is TIMEOUT:
                self.timeout_index = idx
                continue
            if isinstance(pat, Pattern):
                self._searches.append((idx, pat))

    def search(
        self, buffer: str, freshlen: int, searchwindowsize: int | None = None
    ) -> int:
        first_match = None
        best_index = -1
        best_match = None

        searchstart = (
            max(0, len(buffer) - searchwindowsize)
            if searchwindowsize is not None
            else 0
        )

        for index, pattern in self._searches:
            match = pattern.search(buffer, searchstart)
            if match is None:
                continue

            match_pos = match.start()
            if first_match is None or match_pos < first_match:
                first_match = match_pos
                best_match = match
                best_index = index

        if first_match is None or best_match is None:
            return -1

        self.start = first_match
        self.match = best_match
        self.end = best_match.end()
        return best_index


searcher_string_str = searcher_string[str]
searcher_string_bytes = searcher_string[bytes]

if __name__ == "__main__":
    s = searcher_string[str](["hello", "world"])
    print(s)
    print(s.search("hello world", 11))
    print(s.match)
    print(s.start)
    print(s.end)

    import re

    s = searcher_re([re.compile(r"hello"), re.compile(r"world")])
    assert s.search("hello world", 11) == 0, (
        f"Expected 0, got {s.search('hello world', 11)}"
    )
    print(s)
    print(s.search("hello world", 11))
    assert str(s.match) == "<re.Match object; span=(0, 5), match='hello'>", (
        f"Expected <re.Match object; span=(0, 5), match='hello'>, got {s.match}"
    )
    print(s.match)
    assert s.start == 0, f"Expected 0, got {s.start}"
    print(s.start)
    print(s.end)
