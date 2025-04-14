import argparse
import asyncio
import contextlib
import gc
import os.path
import socket as stdsock

PRINT = 0


async def echo_client_streams(reader, writer) -> None:
    sock = writer.get_extra_info("socket")
    with contextlib.suppress(OSError, NameError):
        sock.setsockopt(stdsock.IPPROTO_TCP, stdsock.TCP_NODELAY, 1)
    if PRINT:
        pass
    while True:
        data = await reader.readline()
        if not data:
            break
        writer.write(data)
    if PRINT:
        pass
    writer.close()


async def print_debug(loop) -> None:
    while True:
        loop.print_debug_info()
        await asyncio.sleep(0.5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--uvloop", default=False, action="store_true")
    parser.add_argument("--addr", default="127.0.0.1:25000", type=str)
    parser.add_argument("--print", default=False, action="store_true")
    args = parser.parse_args()

    if args.uvloop:
        import uvloop

        loop = uvloop.new_event_loop()
    else:
        loop = asyncio.new_event_loop()

    asyncio.set_event_loop(loop)
    loop.set_debug(False)

    if args.print:
        PRINT = 1

    if hasattr(loop, "print_debug_info"):
        loop.create_task(print_debug(loop))
        PRINT = 0

    unix = False
    if args.addr.startswith("file:"):
        unix = True
        addr = args.addr[5:]
        if os.path.exists(addr):
            os.remove(addr)
    else:
        addr = args.addr.split(":")
        addr[1] = int(addr[1])
        addr = tuple(addr)

    if unix:
        coro = asyncio.start_unix_server(echo_client_streams, addr, limit=256000)
    else:
        coro = asyncio.start_server(echo_client_streams, *addr, limit=256000)
    srv = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    finally:
        if hasattr(loop, "print_debug_info"):
            gc.collect()
            loop.print_debug_info()

        loop.close()
