import asyncio
from typing_extensions import TYPE_CHECKING
from mbpy.expect.asyncspawn import AsyncSpawn
import aiohttp.web

if TYPE_CHECKING:
    from aiohttp import ClientSession


class AIOSpawn(AsyncSpawn):
    """Base class for async spawners with expect-like functionality."""

    def __init__(self, command: str, show: bool = False):
        super().__init__(command, show=show)
        self._buffer = bytearray()
        self.CHUNK_SIZE = 8192


class AsyncUDP(AIOSpawn):
    """UDP-based async spawner with expect-like functionality."""

    def __init__(self, host, port, show: bool = False):
        super().__init__(
            "", show=show
        )  # Empty command since we're not spawning a process
        self.host, self.port = host, port
        self.transport = None
        self.protocol = None

    async def start(self) -> asyncio.DatagramTransport:
        """Start UDP connection."""

        class DatagramProtocol(asyncio.DatagramProtocol):
            def __init__(self, parent):
                self.parent = parent

            def datagram_received(self, data, addr):
                self.parent._buffer.extend(data)

        loop = asyncio.get_event_loop()
        self.transport, self.protocol = await loop.create_datagram_endpoint(
            lambda: DatagramProtocol(self), remote_addr=(self.host, self.port)
        )
        return self.transport

    def sync_start(self) -> asyncio.DatagramTransport:
        """Synchronous version of start()."""

        class DatagramProtocol(asyncio.DatagramProtocol):
            def __init__(self, parent):
                self.parent = parent

            def datagram_received(self, data, addr):
                self.parent._buffer.extend(data)

        loop = asyncio.get_event_loop()
        self.transport, self.protocol = loop.run_until_complete(
            loop.create_datagram_endpoint(
                lambda: DatagramProtocol(self), remote_addr=(self.host, self.port)
            )
        )
        return self.transport

    @classmethod
    def factory(cls, host, port):
        return lambda: cls(host, port)

    async def send(self, data: str):
        """Send UDP datagram."""
        transport = self.transport or await self.start()
        transport.sendto(data.encode())


class AsyncHTTP(AIOSpawn):
    """HTTP-based async spawner with expect-like functionality."""

    def __init__(
        self, url: str, method: str = "GET", headers: dict = None, show: bool = False
    ):
        super().__init__("", show=show)
        self.url = url
        self.method = method.upper()
        self.headers = headers or {}
        self.client_session: "ClientSession|None" = None

    async def start(self) -> "ClientSession":
        """Start HTTP session."""
        import aiohttp

        self.client_session = aiohttp.ClientSession(headers=self.headers)
        return self.client_session

    async def send(self, data: str):
        """Send HTTP request with data."""

        client_session = self.client_session or await self.start()
        async with client_session.request(
            self.method, self.url, data=data, chunked=True
        ) as response:
            async for chunk in response.content.iter_chunked(self.CHUNK_SIZE):
                if chunk:
                    self._buffer[:] = chunk

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Cleanup HTTP session."""
        if self.client_session:
            await self.client_session.close()
        await super().__aexit__(exc_type, exc_val, exc_tb)


# Simple HTTP Server that streams numbers
async def stream_handler(request):
    response = aiohttp.web.StreamResponse()
    response.headers["Content-Type"] = "text/plain"
    await response.prepare(request)

    for i in range(5):
        await response.write(f"status: {i}\n".encode())
        await asyncio.sleep(0.5)

    return response


# UDP Echo Server
class EchoServerProtocol(asyncio.DatagramProtocol):
    """UDP Echo Server Protocol"""

    def __init__(self, host: str, port: int):
        super().__init__()
        self.transport: asyncio.DatagramTransport | None = None
        self.host = host
        self.port = port
        self.stdout = None
        self.stderr = None

    def connection_made(self, transport: asyncio.DatagramTransport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message: str = data.decode()
        print(f"Received: {message}")
        response = f"response {len(message)}"
        self.transport = self.transport or AsyncUDP(self.host, self.port).sync_start()
        self.transport.sendto(response.encode(), addr)

    @classmethod
    def factory(cls, host, port):
        return lambda: cls(host, port)


async def main():
    # Start UDP Server
    loop = asyncio.get_event_loop()
    local_addr = ("0.0.0.0", 9999)
    udp_transport, _ = await loop.create_datagram_endpoint(
        EchoServerProtocol.factory(local_addr[0], local_addr[1]), local_addr=local_addr
    )

    # Start HTTP Server
    app = aiohttp.web.Application()
    app.router.add_get("/stream", stream_handler)
    runner = aiohttp.web.AppRunner(app)
    await runner.setup()
    site = aiohttp.web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

    try:
        # Test UDP
        print("Testing UDP...")
        async with AsyncUDP("0.0.0.0", 9999) as udp:
            await udp.send("Hello UDP")
            async for i in udp.expect(r"response\s+(\d+)"):
                print(f"Got UDP response: {udp.match.group(1)}")

        # Test HTTP
        print("\nTesting HTTP...")
        async with AsyncHTTP("http://localhost:8080/stream") as http:
            await http.send("")  # Empty data for GET request
            async for i in http.expect(r"status:\s*(\d+)"):
                print(f"Got HTTP status: {http.match.group(1)}")

    finally:
        # Cleanup
        udp_transport.close()
        await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
