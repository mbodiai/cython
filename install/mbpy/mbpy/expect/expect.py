"""Copied and modified to work with asyncio and windows from pexpect.

This seeks through the stream until a pattern is matched. The
pattern is overloaded and may take several types. The pattern can be a
StringType, EOF, a compiled re, or a list of any of those types.
Strings will be compiled to re types. This returns the index into the
pattern list. If the pattern was not a list this returns index 0 on a
successful match. This may raise exceptions for EOF or TIMEOUT. To
avoid the EOF or TIMEOUT exceptions add EOF or TIMEOUT to the pattern
list. That will cause expect to match an EOF or TIMEOUT condition
instead of raising an exception.

If you pass a list of patterns and more than one matches, the first
match in the stream is chosen. If more than one pattern matches at that
point, the leftmost in the pattern list is chosen. For example::

# the input is 'foobar'
index = p.expect(['bar', 'foo', 'foobar'])
# returns 1('foo') even though 'foobar' is a "better" match

Please note, however, that buffering can affect this behavior, since
input arrives in unpredictable chunks. For example::

# the input is 'foobar'
index = p.expect(['foobar', 'foo'])
# returns 0('foobar') if all input is available at once,
# but returns 1('foo') if parts of the final 'bar' arrive late

When a match is found for the given pattern, the class instance
attribute *match* becomes an re.MatchObject result.  Should an EOF
or TIMEOUT pattern match, then the match attribute will be an instance
of that exception class.  The pairing before and after class
instance attributes are views of the data preceding and following
the matching pattern.  On general exception, class attribute
*before* is all data received up to the exception, while *match* and
*after* attributes are value None.

When the keyword argument timeout is -1 (default), then TIMEOUT will
raise after the default value specified by the class timeout
attribute. When None, TIMEOUT will not be raised and may block
indefinitely until match.

When the keyword argument searchwindowsize is -1 (default), then the
value specified by the class maxread attribute is used.

A list entry may be EOF or TIMEOUT instead of a string. This will
catch these exceptions and return the index of the list entry instead
of raising the exception. The attribute 'after' will be set to the
exception type. The attribute 'match' will be None. This allows you to
write code like this::

index = p.expect(['good', 'bad', pexpect.EOF, pexpect.TIMEOUT])
if index == 0:
do_something()
elif index == 1:
do_something_else()
elif index == 2:
do_some_other_thing()
elif index == 3:
do_something_completely_different()

instead of code like this::

try:
index = p.expect(['good', 'bad'])
if index == 0:
do_something()
elif index == 1:
do_something_else()
except EOF:
do_some_other_thing()
except TIMEOUT:
do_something_completely_different()

These two forms are equivalent. It all depends on what you want. You
can also just expect the EOF if you are waiting for all output of a
child to finish. For example::

p = pexpect.spawn('/bin/ls')
p.expect(pexpect.EOF)
print p.before

If you are trying to optimize for speed then see expect_list().

On Python 3.4, or Python 3.3 with asyncio installed, passing
``async_=True``  will make this return an :mod:`asyncio` coroutine,
which you can yield from to get the same result that this method would
normally give directly. So, inside a coroutine, you can replace this code::

index = p.expect(patterns)

With this non-blocking form::

index = yield from p.expect(patterns, async_=True)
"""

from __future__ import annotations

import asyncio
import errno
import logging
import os
import sys
import time
from asyncio.transports import Transport
from typing import Any

from typing_extensions import TYPE_CHECKING, AsyncIterator, Protocol, Self

from mbpy.expect.exceptions import EOF, TIMEOUT
from mbpy.expect.searcher import SearcherStringT

if TYPE_CHECKING:
    from mbpy.expect.spawnbase import SpawnBase
    from mbpy.expect.asyncspawn import AsyncSpawn


class PatternWaiter(Protocol):
    transport: Transport
    fut: asyncio.Future
    expecter: Expecter

    def set_expecter(self, expecter: "Expecter") -> Self:
        self.expecter = expecter
        self.fut = asyncio.Future()
        return self

    def found(self, result) -> Self:  # noqa: F821
        if not self.fut.done():
            self.fut.set_result(result)
            self.transport.pause_reading()
        return self

    def error(self, exc) -> None:
        if not self.fut.done() and not self.expecter.spawn.before:
            self.expecter.spawn.before = self.expecter.spawn._before.getvalue()
        self.fut.set_exception(exc)
        self.transport.pause_reading()

    def connection_made(self, transport) -> Self:
        self.transport = transport
        return self

    def data_received(self, data) -> Self:
        spawn = self.expecter.spawn
        s = spawn._decoder.decode(data)

        if self.fut.done():
            spawn._before = spawn._before + s
            spawn._buffer.write(s)
            return self

        try:
            index = self.expecter.new_data(s)
            if index is not None:
                self.found(index)
        except Exception as e:
            self.expecter.errored()
            self.error(e)
        return self

    def eof_received(self) -> Self:
        try:
            self.expecter.spawn.flag_eof = True
            index = self.expecter.eof()
        except EOF as e:
            self.error(e)
        else:
            self.found(index)
        return self

    def connection_lost(self, exc) -> Self:
        if isinstance(exc, OSError) and exc.errno == errno.EIO:
            self.eof_received()
        elif exc is not None:
            self.error(exc)
        return self


async def expect_async(
    expecter: "AsyncExpecter", timeout: int | float | None = None
) -> AsyncIterator[int | None]:
    idx = expecter.existing_data()
    if idx is not None:
        logging.debug(f"idx {idx}")
        yield idx
        return
    if not expecter.spawn.pw_transport:
        pw = APatternWaiter()
        pw.set_expecter(expecter)
        transport, pw = await asyncio.get_event_loop().connect_read_pipe(
            lambda: pw, os.fdopen(sys.stdin.fileno(), "rb")
        )
        expecter.spawn.pw_transport = pw, transport
        # logging.debug("set transport and pw")
    else:
        pw, transport = expecter.spawn.pw_transport
        pw.set_expecter(expecter)
        transport.resume_reading()
        logging.debug("resumed reading")
    try:
        yield await asyncio.wait_for(pw.fut, timeout)
        return
    except TimeoutError as e:
        transport.pause_reading()
        yield expecter.timeout(e)
        return


class APatternWaiter(asyncio.Protocol):
    transport: Transport

    def set_expecter(self, expecter: "Expecter"):
        self.expecter = expecter
        self.fut = asyncio.Future()
        return self

    def found(self, result) -> Self:
        if not self.fut.done():
            self.fut.set_result(result)
            self.transport.pause_reading()
        return self

    def error(self, exc) -> Self:
        if not self.fut.done():
            self.fut.set_exception(exc)
            self.transport.pause_reading()
        return self

    def connection_made(self, transport: Transport) -> None:
        self.transport = transport

    def data_received(self, data) -> None:
        spawn = self.expecter.spawn
        s = spawn._decoder.decode(data)

        if self.fut.done():
            spawn._before.write(s)
            spawn._buffer.write(s)
            return

        try:
            index = self.expecter.new_data(s)
            if index is not None:
                self.found(index)
        except Exception as e:
            self.expecter.errored()
            self.error(e)

    def eof_received(self) -> None:
        try:
            self.expecter.spawn.flag_eof = True
            index = self.expecter.eof()
        except EOF as e:
            self.error(e)
        else:
            self.found(index)

    def connection_lost(self, exc) -> None:
        if isinstance(exc, OSError) and exc.errno == errno.EIO:
            self.eof_received()
        elif exc is not None:
            self.error(exc)


class Expecter:
    def _validate_fd(self):
        """Validate that the file descriptor is in a valid state."""
        if self.spawn.child_fd is None or self.spawn.child_fd < 0:
            if (
                self.spawn.process
                and self.spawn.process.stdout
                and self.spawn.process.stdout.fileno() != -1
            ):
                self.spawn.child_fd = self.spawn.process.stdout.fileno()
            elif (
                self.spawn.process
                and self.spawn.process.stderr
                and self.spawn.process.stderr.fileno() != -1
            ):
                self.spawn.child_fd = self.spawn.process.stderr.fileno()
            else:
                return False

        if self.spawn.platform_is_windows:
            # Windows specific handle validation
            try:
                # Use os.open on Windows instead of msvcrt
                return self.spawn.child_fd != -1
            except (ImportError, OSError):
                return False
        else:
            # Unix file descriptor validation
            try:
                os.fstat(self.spawn.child_fd)
                return True
            except OSError:
                return False

    def __init__(
        self,
        spawn: "SpawnBase[Any]",
        searcher: SearcherStringT,
        searchwindowsize: int | None = None,
        timeout: int | float | None = None,
    ) -> None:
        self.spawn = spawn
        self.searcher = searcher
        if searchwindowsize == -1:
            searchwindowsize = spawn.searchwindowsize
        self.searchwindowsize = searchwindowsize
        self.lookback = (
            searcher.longest_string if hasattr(searcher, "longest_string") else None
        )
        self._timeout = timeout
        self._validate_fd()

    def do_search(self, window, freshlen):
        spawn = self.spawn
        searcher = self.searcher
        if freshlen > len(window):
            freshlen = len(window)
        index = searcher.search(window, freshlen, self.searchwindowsize)
        if index >= 0:
            spawn._buffer = spawn.buffer_type()
            spawn._buffer.write(window[searcher.end :])
            spawn.before = spawn._before.getvalue()[0 : -(len(window) - searcher.start)]
            spawn._before = spawn.buffer_type()
            spawn._before.write(window[searcher.end :])
            spawn.after = window[searcher.start : searcher.end]
            spawn.match = searcher.match
            spawn.match_index = index
            return index

        maintain = self.searchwindowsize or self.lookback
        if maintain is not None and spawn._buffer.tell() > maintain:
            spawn._buffer = spawn.buffer_type()
            spawn._buffer.write(window[-maintain:])
        return None

    def existing_data(self):
        spawn = self.spawn
        before_len = len(spawn._before)
        buf_len = spawn._buffer.tell()
        freshlen = before_len
        if before_len > buf_len:
            if not self.searchwindowsize:
                spawn._buffer = spawn.buffer_type()
                window = spawn._before.getvalue()
                spawn._buffer.write(window)
            elif buf_len < self.searchwindowsize:
                spawn._buffer = spawn.buffer_type()
                spawn._before.seek(max(0, before_len - self.searchwindowsize))
                window = spawn._before.read()
                spawn._buffer.write(window)
            else:
                spawn._buffer.seek(max(0, buf_len - self.searchwindowsize))
                window = spawn._buffer.read()
        else:
            if self.searchwindowsize:
                spawn._buffer.seek(max(0, buf_len - self.searchwindowsize))
                window = spawn._buffer.read()
            else:
                window = spawn._buffer.getvalue()
        return self.do_search(window, freshlen)

    def new_data(self, data):
        spawn = self.spawn
        freshlen = len(data)
        spawn._before.write(data)
        if not self.searchwindowsize:
            if self.lookback:
                old_len = spawn._buffer.tell()
                spawn._buffer.write(data)
                spawn._buffer.seek(max(0, old_len - self.lookback))
                window = spawn._buffer.read()
            else:
                spawn._buffer.write(data)
                window = spawn.buffer
        else:
            if len(data) >= self.searchwindowsize or not spawn._buffer.tell():
                window = data[-self.searchwindowsize :]
                spawn._buffer = spawn.buffer_type()
                spawn._buffer.write(window[-self.searchwindowsize :])
            else:
                spawn._buffer.write(data)
                new_len = spawn._buffer.tell()
                spawn._buffer.seek(max(0, new_len - self.searchwindowsize))
                window = spawn._buffer.read()
        return self.do_search(window, freshlen)

    def eof(self, err=None):
        spawn = self.spawn

        spawn.before = spawn._before.getvalue()
        spawn._buffer = spawn.buffer_type()
        spawn._before = spawn.buffer_type()
        spawn.after = EOF
        index = self.searcher.eof_index
        if index >= 0:
            spawn.match = EOF
            spawn.match_index = index
            return index
        spawn.match = None
        spawn.match_index = None
        msg = str(spawn)
        msg += f"\nsearcher: {self.searcher}"
        if err is not None:
            msg = str(err) + "\n" + msg

        exc = EOF(msg)
        exc.__cause__ = None
        return exc

    def timeout(self, err=None):
        spawn = self.spawn

        spawn.before = spawn._buffer.getvalue()
        spawn.after = str(TIMEOUT)
        index = self.searcher.timeout_index
        if index >= 0:
            spawn.match = TIMEOUT
            spawn.match_index = index
            return index
        spawn.match = None
        spawn.match_index = None
        msg = str(spawn)
        msg += f"\nsearcher: {self.searcher}"

        # Prevent recursion if already a TIMEOUT
        if isinstance(err, TIMEOUT):
            return index if index >= 0 else None

        if err is not None:
            msg = str(err) + "\n" + msg
        if isinstance(err, Exception):
            raise TIMEOUT(err)
        raise TIMEOUT(msg)

    def errored(self) -> None:
        spawn = self.spawn
        spawn.before = spawn._before
        spawn.after = None
        spawn.match = None
        spawn.match_index = None

    def expect_loop(self, timeout: float | None = -1):
        """Blocking expect."""
        spawn = self.spawn
        timeout = float(timeout or self._timeout or -1)
        if timeout > 0:
            end_time = time.time() + timeout

        try:
            idx = self.existing_data()
            if idx is not None:
                return idx
            while True:
                if (timeout is not None) and (timeout < 0):
                    return self.timeout()
                try:
                    incoming = spawn.read_nonblocking(spawn.maxread, timeout)
                    idx = self.new_data(incoming)
                    if idx is not None:
                        return idx
                except (EOF, TIMEOUT) as e:
                    if isinstance(e, EOF):
                        return self.eof(e)
                    else:
                        return self.timeout(e)
                if timeout > 0:
                    timeout = end_time - time.time()
                    if timeout <= 0:
                        return self.timeout()
        except EOF as e:
            return self.eof(e)
        except TIMEOUT as e:
            return self.timeout(e)
        except Exception:
            self.errored()
            raise


class AsyncExpecter(Expecter):
    spawn: "AsyncSpawn"

    def __init__(
        self,
        spawn: "SpawnBase[Any]",
        searcher: SearcherStringT,
        searchwindowsize: int | None = None,
        timeout: int | float | None = None,
    ) -> None:
        super().__init__(spawn, searcher, searchwindowsize, timeout)
        from mbpy.expect.asyncspawn import AsyncSpawn

        self.pw_transport = None
        self.pw = APatternWaiter()
        self.pw.set_expecter(self)
        self.spawn = AsyncSpawn(
            self.spawn.command,
            show=self.spawn.show,
            cwd=self.spawn.cwd,
            shell=self.spawn.shell,
        )

    @property
    def pw(self) -> APatternWaiter:
        return self._pw

    @pw.setter
    def pw(self, value: APatternWaiter):
        self._pw = value

    async def astart(self):
        self.pw_transport, self.pw = await asyncio.get_event_loop().connect_read_pipe(
            lambda: self.pw, os.fdopen(sys.stdin.fileno(), "rb")
        )

    async def expect_async(
        self, timeout: float | None = None
    ) -> AsyncIterator[int | None]:
        async for idx in expect_async(self, timeout):
            yield idx
