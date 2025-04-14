import argparse
import asyncio
import contextlib
import gc
import os.path
import pathlib
import socket
import ssl
from typing import Any, Self, Tuple

PRINT: int = 0


async def echo_server(
    loop: asyncio.AbstractEventLoop, address: str | Tuple[str, int], unix: bool
) -> None:
    if unix:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    sock.setblocking(False)
    if PRINT:
        pass
    with sock:
        while True:
            client, addr = await loop.sock_accept(sock)
            if PRINT:
                pass
            loop.create_task(echo_client(loop, client))


async def echo_client(loop: asyncio.AbstractEventLoop, client: socket.socket) -> None:
    with contextlib.suppress(OSError, NameError):
        client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    with client:
        while True:
            data = await loop.sock_recv(client, 1000000)
            if not data:
                break
            await loop.sock_sendall(client, data)
    if PRINT:
        pass


async def echo_client_streams(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter
) -> None:
    sock = writer.get_extra_info("socket")
    with contextlib.suppress(OSError, NameError):
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    if PRINT:
        pass
    while True:
        data = await reader.read(1000000)
        if not data:
            break
        writer.write(data)
    if PRINT:
        pass
    writer.close()


class EchoProtocol(asyncio.Protocol):
    def __init__(self) -> None:
        self.transport: asyncio.BaseTransport | None = None

    def connection_made(self: Self, transport: asyncio.BaseTransport) -> None:
        self.transport = transport

    def connection_lost(self, exc: Exception | None) -> None:
        self.transport = None

    def data_received(self, data: bytes) -> None:
        if self.transport:
            self.transport.write(data)


class EchoBufferedProtocol(asyncio.BufferedProtocol):
    def __init__(self: Self) -> None:
        self.transport: asyncio.WriteTransport | None = None
        self.buffer: bytearray = bytearray(256 * 1024)

    def connection_made(self: Self, transport: asyncio.WriteTransport) -> None:
        self.transport = transport

    def connection_lost(self: Self, exc: Exception | None) -> None:
        self.transport = None

    def get_buffer(self: Self, sizehint: int) -> bytearray:
        return self.buffer

    def buffer_updated(self: Self, nbytes: int) -> None:
        if self.transport:
            self.transport.write(self.buffer[:nbytes])


async def print_debug(loop: asyncio.AbstractEventLoop) -> None:
    while True:
        await asyncio.sleep(0.5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--uvloop", default=False, action="store_true")
    parser.add_argument("--streams", default=False, action="store_true")
    parser.add_argument("--proto", default=False, action="store_true")
    parser.add_argument("--addr", default="127.0.0.1:25000", type=str)
    parser.add_argument("--print", default=False, action="store_true")
    parser.add_argument("--ssl", default=False, action="store_true")
    parser.add_argument("--buffered", default=False, action="store_true")
    args: argparse.Namespace = parser.parse_args()

    if args.uvloop:
        import uvloop

        loop: asyncio.AbstractEventLoop = uvloop.new_event_loop()
    else:
        loop = asyncio.new_event_loop()

    asyncio.set_event_loop(loop)
    loop.set_debug(False)

    if args.print:
        PRINT = 1

    if hasattr(loop, "print_debug_info"):
        loop.create_task(print_debug(loop))
        PRINT = 0

    unix: bool = False
    addr: str | Tuple[str, int]
    if args.addr.startswith("file:"):
        unix = True
        addr = args.addr[5:]
        if os.path.exists(addr):
            os.remove(addr)
    else:
        addr_parts = args.addr.split(":")
        addr = (addr_parts[0], int(addr_parts[1]))

    server_context: ssl.SSLContext | None = None
    if args.ssl:
        if hasattr(ssl, "PROTOCOL_TLS"):
            server_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        else:
            server_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        server_context.load_cert_chain(
            (
                pathlib.Path(__file__).parent.parent.parent
                / "tests"
                / "certs"
                / "ssl_cert.pem"
            ),
            (
                pathlib.Path(__file__).parent.parent.parent
                / "tests"
                / "certs"
                / "ssl_key.pem"
            ),
        )
        if hasattr(server_context, "check_hostname"):
            server_context.check_hostname = False
        server_context.verify_mode = ssl.CERT_NONE

    srv: Any
    if args.streams:
        if args.proto:
            exit(1)

        if args.buffered:
            exit(1)

        if unix:
            coro = asyncio.start_unix_server(
                echo_client_streams, addr, ssl=server_context
            )
        else:
            coro = asyncio.start_server(
                echo_client_streams, addr[0], addr[1], ssl=server_context
            )
        srv = loop.run_until_complete(coro)
    elif args.proto:
        if args.streams:
            exit(1)

        protocol: Type[EchoProtocol] | Type[EchoBufferedProtocol]
        protocol = EchoBufferedProtocol if args.buffered else EchoProtocol

        if unix:
            coro = loop.create_unix_server(protocol, addr, ssl=server_context)
        else:
            coro = loop.create_server(protocol, addr[0], addr[1], ssl=server_context)
        srv = loop.run_until_complete(coro)
    else:
        if args.ssl:
            exit(1)

        loop.create_task(echo_server(loop, addr, unix))
    try:
        loop.run_forever()
    finally:
        if hasattr(loop, "print_debug_info"):
            gc.collect()
            loop.print_debug_info()

        loop.close()
