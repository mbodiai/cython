from multiprocessing import Process, Pipe, Event, Value
import multiprocessing
from multiprocessing.connection import Connection
from multiprocessing.sharedctypes import Synchronized
from multiprocessing.shared_memory import SharedMemory
from multiprocessing.context import BaseContext
import time
import os
import numpy as np
import socket
import http.server
import socketserver
import queue
import sys
import zmq
import struct # Import struct
import zenoh # Import zenoh
from typing import Tuple, Dict, Any
from abc import ABC, abstractmethod

# ANSI Color codes (if stdout is a TTY)
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# --- Helper Functions ---

def verify_data_access(data):
    """Verify data access by performing an operation that forces memory access."""
    if isinstance(data, np.ndarray):
        # Using np.sum() is efficient and ensures access
        return np.sum(data)
    elif isinstance(data, (bytearray, bytes)):
        # Simple sum for bytes/bytearray
        return sum(data)
    elif isinstance(data, zmq.Frame):
        # Handle ZMQ Frame by accessing buffer
        return sum(data.buffer)
    elif isinstance(data, zenoh.ZBytes):
         # Handle Zenoh ZBytes by converting to bytes
         # Note: This might involve a copy, depending on ZBytes implementation
         return sum(bytes(data))
    else:
        raise TypeError(f"Unsupported data type for verification: {type(data)}")

# --- Abstract Base Class for Benchmarks ---

class BenchmarkMethod(ABC):
    """Abstract base class for different data transfer benchmark methods."""

    def __init__(self, name: str, size_mb: int, data: np.ndarray | None, ctx: BaseContext):
        self.name = name
        self.size_mb = size_mb
        # Data might not be needed for consumer-only part, but useful for producer
        self.data = data
        self.ctx = ctx
        self.write_time: "Synchronized[float]" = ctx.Value("d", 0.0)
        self.read_time: "Synchronized[float]" = ctx.Value("d", 0.0)
        # Pipe for dynamic info (port, shm_name, etc.) between producer and main/consumer
        self.parent_conn, self.child_conn = ctx.Pipe()

    @abstractmethod
    def run(self) -> Dict[str, Any]:
        """Executes the benchmark for this method and returns results."""
        pass

# --- Concrete Benchmark Implementations ---

class SameProcessBenchmark(BenchmarkMethod):
    """Benchmark using an in-process queue."""
    def __init__(self, size_mb: int, data: np.ndarray, ctx):
        super().__init__("Same Process", size_mb, data, ctx)

    def run(self) -> Dict[str, Any]:
        q: queue.Queue[np.ndarray] = queue.Queue()

        start = time.time()
        q.put(self.data)
        self.write_time.value = time.time() - start

        start = time.time()
        received = q.get()
        verify_data_access(received)
        self.read_time.value = time.time() - start

        return {
            'method': self.name,
            'write': self.write_time.value,
            'read': self.read_time.value,
        }

class DiskBenchmark(BenchmarkMethod):
    """Benchmark using disk I/O."""
    def __init__(self, size_mb: int, data: np.ndarray, ctx):
        super().__init__("Disk", size_mb, data, ctx)
        self.filename = f"temp_data_{os.getpid()}.bin"

    def run(self) -> Dict[str, Any]:
        try:
            start = time.time()
            self.data.tofile(self.filename)
            self.write_time.value = time.time() - start

            start = time.time()
            loaded_data = np.fromfile(self.filename, dtype=self.data.dtype)
            # Reshape if necessary, although verify handles flat array sum ok
            # loaded_data = loaded_data.reshape(self.data.shape)
            verify_data_access(loaded_data)
            self.read_time.value = time.time() - start
        finally:
            if os.path.exists(self.filename):
                os.remove(self.filename)

        return {
            'method': self.name,
            'write': self.write_time.value,
            'read': self.read_time.value,
        }

# Base class for methods using separate producer/consumer processes
class ProcessPairBenchmark(BenchmarkMethod):
    """Base class for benchmarks involving a producer and consumer process."""

    @abstractmethod
    def producer_target(self, child_conn: Connection, *args):
        """Target function for the producer process."""
        pass

    @abstractmethod
    def consumer_target(self, dynamic_info: Any, *args):
        """Target function for the consumer process."""
        pass

    def run(self, producer_args=(), consumer_args=()) -> Dict[str, Any]:
        """Runs the producer and consumer in separate processes."""
        producer_p = self.ctx.Process(
            target=self.producer_target,
            args=(self.child_conn,) + producer_args # Pass pipe conn first
        )
        producer_p.start()

        # Wait for dynamic info from producer (e.g., port number, shm name)
        # Use a timeout?
        try:
            dynamic_info = self.parent_conn.recv()
        except EOFError:
             print(f"Warning: Producer for {self.name} closed pipe without sending info.", file=sys.stderr)
             dynamic_info = None # Or raise error
             # Ensure processes are joined even if pipe fails
             producer_p.join(timeout=1)
             # Cannot start consumer
             return {'method': self.name, 'write': self.write_time.value, 'read': -1.0} # Indicate error


        consumer_p = self.ctx.Process(
            target=self.consumer_target,
            args=(dynamic_info,) + consumer_args # Pass dynamic info first
        )
        consumer_p.start()

        producer_p.join()
        consumer_p.join()

        return {
            'method': self.name,
            'write': self.write_time.value,
            'read': self.read_time.value,
        }


class ShmBenchmark(ProcessPairBenchmark):
    """Benchmark using Shared Memory."""
    def __init__(self, size_mb: int, data: np.ndarray, ctx):
        super().__init__("Shared Memory", size_mb, data, ctx)
        # Shorten name for OS compatibility (macOS limit)
        self.shm_name = f"psm_{os.getpid()}_{size_mb}" 
        self.shape = data.shape
        self.dtype = data.dtype

    def producer_target(self, child_conn: Connection):
        shm = None
        try:
            # Use data.nbytes which is independent of dtype for total size
            shm = SharedMemory(name=self.shm_name, create=True, size=self.data.nbytes)
            shared_array = np.ndarray(self.shape, dtype=self.dtype, buffer=shm.buf)

            start = time.time()
            shared_array[:] = self.data[:]
            self.write_time.value = time.time() - start

            # Send necessary info (name, shape, dtype) to consumer via pipe
            child_conn.send({'name': self.shm_name, 'shape': self.shape, 'dtype': self.dtype})

            # Keep SHM alive until consumer likely finished (replace with proper sync if needed)
            time.sleep(2) # Reduce sleep time

        finally:
            if shm:
                shm.close()
                # Unlink should only happen once, ideally after consumer is done.
                # This is slightly racy. A dedicated Event could signal consumer exit.
                try:
                     shm.unlink()
                except FileNotFoundError:
                     pass # Consumer might have unlinked already if we implement that

    def consumer_target(self, dynamic_info: Dict):
        shm_name = dynamic_info['name']
        shape = dynamic_info['shape']
        dtype = dynamic_info['dtype']
        shm = None
        try:
            # Wait briefly for producer to fully create/write? Might not be needed.
            # time.sleep(0.1)
            shm = SharedMemory(name=shm_name)
            shared_array = np.ndarray(shape, dtype=dtype, buffer=shm.buf)

            start = time.time()
            verify_data_access(shared_array)
            self.read_time.value = time.time() - start
        finally:
             if shm:
                 shm.close()
                 # Optionally, consumer could unlink if producer guarantees cleanup isn't needed
                 # try:
                 #    SharedMemory(name=shm_name).unlink()
                 # except FileNotFoundError:
                 #    pass


class TcpBenchmark(ProcessPairBenchmark):
    """Benchmark using TCP Sockets."""
    DEFAULT_CHUNK_SIZE = 64 * 1024 # Define default chunk size

    def __init__(self, size_mb: int, data: np.ndarray, ctx, chunk_size: int = DEFAULT_CHUNK_SIZE):
        super().__init__("TCP Socket", size_mb, data, ctx)
        self.chunk_size = chunk_size

    def producer_target(self, child_conn: Connection):
        sock = socket.socket()
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        try:
            sock.bind(("localhost", 0))
            port = sock.getsockname()[1]
            child_conn.send(port) # Send port back
            sock.listen(1)
            conn, addr = sock.accept()
            conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # No delay on connection too
            with conn:
                start = time.time()
                data_bytes = self.data.tobytes()
                # Explicit chunked send loop
                total_size = len(data_bytes)
                bytes_sent = 0
                while bytes_sent < total_size:
                    chunk = data_bytes[bytes_sent : bytes_sent + self.chunk_size]
                    sent = conn.send(chunk)
                    if sent == 0:
                        raise RuntimeError("Socket connection broken during send")
                    bytes_sent += sent
                self.write_time.value = time.time() - start
        finally:
            sock.close()

    def consumer_target(self, port: int):
        sock = socket.socket()
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        try:
            # Add small delay/retry? ZMQ does this internally more robustly.
            time.sleep(0.05)
            sock.connect(("localhost", port))
            start = time.time()
            data = bytearray()
            expected_bytes = self.size_mb * 1024 * 1024
            # Receive loop using chunk_size
            while len(data) < expected_bytes:
                # Use self.chunk_size for recv buffer size
                chunk = sock.recv(self.chunk_size)
                if not chunk:
                    break # Connection closed
                data.extend(chunk)
            verify_data_access(data)
            self.read_time.value = time.time() - start
        finally:
            sock.close()

class HttpBenchmark(ProcessPairBenchmark):
    """Benchmark using HTTP."""
    DEFAULT_CHUNK_SIZE = 64 * 1024 # Define default chunk size

    def __init__(self, size_mb: int, data: np.ndarray, ctx, chunk_size: int = DEFAULT_CHUNK_SIZE):
        super().__init__("HTTP", size_mb, data, ctx)
        self.data_bytes = data.tobytes()
        self.chunk_size = chunk_size

    # Factory function needs access to chunk_size now
    def _make_handler(self, data_bytes: bytes, write_time_shared: Synchronized, chunk_size: int):
        class CustomHTTPHandler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header("Content-type", "application/octet-stream")
                self.send_header("Content-Length", str(len(data_bytes)))
                self.end_headers()
                start_ts = time.time()
                try:
                    # Chunked write loop
                    total_size = len(data_bytes)
                    bytes_sent = 0
                    while bytes_sent < total_size:
                        chunk = data_bytes[bytes_sent : bytes_sent + chunk_size]
                        self.wfile.write(chunk)
                        bytes_sent += len(chunk)
                    self.wfile.flush()
                except BrokenPipeError:
                    pass
                finally:
                    # Ensure time is recorded even if pipe breaks mid-write
                    if write_time_shared:
                         write_time_shared.value = time.time() - start_ts

            def log_message(self, format, *args):
                pass # Suppress logging
        return CustomHTTPHandler

    def producer_target(self, child_conn: Connection):
        # Pass chunk_size to the handler factory
        HandlerClass = self._make_handler(self.data_bytes, self.write_time, self.chunk_size)
        with socketserver.TCPServer(("localhost", 0), HandlerClass, bind_and_activate=False) as httpd:
            httpd.allow_reuse_address = True
            try:
                httpd.server_bind()
                httpd.server_activate()
                port = httpd.server_address[1]
                child_conn.send(port) # Send port back
                # Handle a single request
                httpd.handle_request()
            finally:
                 # Server should close automatically via context manager
                 pass
                 # httpd.server_close() # Explicit close if not using context manager


    def consumer_target(self, port: int):
        import urllib.request
        # Add delay?
        time.sleep(0.05)
        url = f"http://localhost:{port}"
        start = time.time()
        try:
            with urllib.request.urlopen(url, timeout=5) as response: # Add timeout
                data = bytearray()
                expected_bytes = self.size_mb * 1024 * 1024
                while True: # Read until EOF or expected size
                    # Read in chunks using self.chunk_size
                    chunk = response.read(self.chunk_size)
                    if not chunk:
                        break
                    data.extend(chunk)
                    if len(data) >= expected_bytes: # Stop if we got expected amount
                        break
                verify_data_access(data)
        except urllib.error.URLError as e:
            print(f"HTTP consumer error: {e}", file=sys.stderr)
            self.read_time.value = -1.0 # Indicate error
            return
        except socket.timeout:
             print(f"HTTP consumer timed out connecting to {url}", file=sys.stderr)
             self.read_time.value = -1.0 # Indicate error
             return

        self.read_time.value = time.time() - start


class ZmqBenchmark(ProcessPairBenchmark):
    """Benchmark using ZMQ PUSH/PULL Sockets with chunking."""
    DEFAULT_CHUNK_SIZE = 64 * 1024 # Define default chunk size

    def __init__(self, size_mb: int, data: np.ndarray, ctx, chunk_size: int = DEFAULT_CHUNK_SIZE):
        # Use standard name, remove chunk size from it
        super().__init__("ZMQ PUSH/PULL", size_mb, data, ctx)
        self.chunk_size = chunk_size
        if self.chunk_size <= 0:
            raise ValueError("Chunk size must be positive")

    def producer_target(self, child_conn: Connection):
        context = zmq.Context.instance()
        socket = context.socket(zmq.PUSH)
        try:
            port = socket.bind_to_random_port("tcp://127.0.0.1")
            child_conn.send(port)
            time.sleep(0.05)

            start = time.time()
            data_bytes = self.data.tobytes()
            total_size = len(data_bytes)

            # 1. Send total size as uint64
            size_msg = struct.pack("!Q", total_size)
            socket.send(size_msg)

            # 2. Send data in chunks
            bytes_sent = 0
            while bytes_sent < total_size:
                chunk = data_bytes[bytes_sent : bytes_sent + self.chunk_size]
                socket.send(chunk, copy=False)
                bytes_sent += len(chunk)

            self.write_time.value = time.time() - start
        finally:
            socket.close()

    def consumer_target(self, port: int):
        context = zmq.Context.instance()
        socket = context.socket(zmq.PULL)
        # Set PULL timeout?
        socket.RCVTIMEO = 5000 # 5 seconds timeout
        try:
            socket.connect(f"tcp://127.0.0.1:{port}")

            start = time.time()

            # 1. Receive total size
            size_msg = socket.recv()
            if len(size_msg) != 8:
                 raise RuntimeError(f"ZMQ Consumer: Invalid size message received (length {len(size_msg)})")
            total_size = struct.unpack("!Q", size_msg)[0]

            # 2. Receive data chunks until total size is met
            received_data = bytearray()
            bytes_received = 0
            while bytes_received < total_size:
                try:
                    frame = socket.recv(copy=False)
                    received_data.extend(frame.buffer)
                    bytes_received += len(frame.buffer)
                except zmq.Again:
                    print("ZMQ Consumer timed out waiting for chunk", file=sys.stderr)
                    self.read_time.value = -1.0
                    return # Exit on timeout

            # Verify the complete data
            verify_data_access(received_data)
            self.read_time.value = time.time() - start

        except Exception as e:
             print(f"Error in ZMQ consumer: {e}", file=sys.stderr)
             self.read_time.value = -1.0 # Indicate error
        finally:
            socket.close()

class UdpBenchmark(ProcessPairBenchmark):
    """Benchmark using UDP Sockets with chunking."""
    # Reduce UDP chunk size significantly
    DEFAULT_CHUNK_SIZE = 8 * 1024 # 8KB
    READY_MSG = b"READY"

    def __init__(self, size_mb: int, data: np.ndarray, ctx, chunk_size: int = DEFAULT_CHUNK_SIZE):
        super().__init__("UDP Socket", size_mb, data, ctx)
        self.chunk_size = chunk_size
        if self.chunk_size <= 0 or self.chunk_size > 65507: # Practical UDP limit
            raise ValueError("Invalid UDP chunk size")

    def producer_target(self, child_conn: Connection):
        # Producer binds, sends its port, waits for consumer ready msg
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.bind(("localhost", 0))
            producer_port = sock.getsockname()[1]
            child_conn.send(producer_port) # Send producer port

            # Wait for consumer's "ready" message to get its address
            sock.settimeout(5.0) # Timeout for waiting
            try:
                ready_data, consumer_addr = sock.recvfrom(len(self.READY_MSG) + 10) # Buffer size
                if ready_data != self.READY_MSG:
                     raise RuntimeError(f"Producer received unexpected ready msg: {ready_data}")
            except socket.timeout:
                raise RuntimeError("Producer timed out waiting for consumer ready signal")
            sock.settimeout(None) # Disable timeout for sending

            # Now we have consumer_addr, start sending
            start = time.time()
            data_bytes = self.data.tobytes()
            total_size = len(data_bytes)

            # 1. Send total size as uint64
            size_msg = struct.pack("!Q", total_size)
            sock.sendto(size_msg, consumer_addr)

            # 2. Send data in chunks
            bytes_sent = 0
            while bytes_sent < total_size:
                chunk = data_bytes[bytes_sent : bytes_sent + self.chunk_size]
                sock.sendto(chunk, consumer_addr)
                bytes_sent += len(chunk)
                # Small sleep might be needed for UDP buffer/loss issues?
                # time.sleep(0.00001)

            self.write_time.value = time.time() - start
        finally:
            sock.close()

    def consumer_target(self, producer_port: int):
        # Consumer binds, sends ready msg to producer, receives
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5.0) # Timeout for receiving
        try:
            sock.bind(("localhost", 0)) # Bind to ephemeral port
            consumer_port = sock.getsockname()[1]

            # Send ready message to producer
            producer_addr = ("localhost", producer_port)
            sock.sendto(self.READY_MSG, producer_addr)

            # Now ready to receive
            start = time.time()

            # 1. Receive total size
            try:
                size_msg, src_addr = sock.recvfrom(8 + 10)
                # Remove source address check for localhost simplicity
                if len(size_msg) != 8:
                    raise RuntimeError(f"Consumer: Invalid size message (len {len(size_msg)})")
                total_size = struct.unpack("!Q", size_msg)[0]
            except socket.timeout:
                 raise RuntimeError("Consumer timed out waiting for size message")

            # 2. Receive data chunks
            received_data = bytearray()
            bytes_received = 0
            while bytes_received < total_size:
                 try:
                     # Buffer size should accommodate chunk
                     chunk, src_addr = sock.recvfrom(self.chunk_size + 512)
                     # Ignore src_addr check on localhost
                     received_data.extend(chunk)
                     bytes_received += len(chunk)
                 except socket.timeout:
                      # This is more likely with UDP - indicate data loss/failure
                      print(f"UDP Consumer timed out waiting for data chunk at {bytes_received}/{total_size} bytes", file=sys.stderr)
                      self.read_time.value = -1.0
                      return # Exit on timeout/loss

            # Verify the complete data (if received fully)
            verify_data_access(received_data)
            self.read_time.value = time.time() - start

        except Exception as e:
             print(f"Error in UDP consumer: {e}", file=sys.stderr)
             self.read_time.value = -1.0 # Indicate error
        finally:
            sock.close()

class ZenohBenchmark(ProcessPairBenchmark):
    """Benchmark using Zenoh Pub/Sub."""
    # Using single message for simplicity first

    def __init__(self, size_mb: int, data: np.ndarray, ctx):
        super().__init__("Zenoh Pub/Sub", size_mb, data, ctx)
        self.key_expr = f"ipc_bench/{os.getpid()}/data"
        # Use a separate event for pub/sub synchronization
        self.ready_event = ctx.Event()

    def producer_target(self, child_conn: Connection):
        session = None
        publisher = None
        try:
            print("Zenoh Producer: Opening session...")
            # Pass zenoh.Config()
            session = zenoh.open(zenoh.Config())
            print(f"Zenoh Producer: Declaring publisher for key {self.key_expr}...")
            publisher = session.declare_publisher(self.key_expr)
            print("Zenoh Producer: Publisher declared.")

            # Signal consumer via Pipe that publisher is ready
            child_conn.send("READY")

            # Wait briefly for subscriber to be ready (better sync needed for reliability)
            time.sleep(0.5)

            start = time.time()
            data_bytes = self.data.tobytes()
            print(f"Zenoh Producer: Publishing {len(data_bytes)} bytes...")
            publisher.put(data_bytes)
            print("Zenoh Producer: Put complete.")
            self.write_time.value = time.time() - start
            # Add a small delay to ensure data might be sent before closing
            time.sleep(0.1)

        except Exception as e:
            print(f"Error in Zenoh producer: {e}", file=sys.stderr)
        finally:
            print("Zenoh Producer: Cleaning up...")
            if publisher:
                try:
                    publisher.undeclare()
                    print("Zenoh Producer: Publisher undeclared.")
                except Exception as e_und:
                    print(f"Zenoh Producer: Error undeclaring publisher: {e_und}", file=sys.stderr)
            if session:
                session.close()
                print("Zenoh Producer: Session closed.")
            print("Zenoh Producer: Done.")


    def consumer_target(self, ready_signal: str):
        if ready_signal != "READY":
            print(f"Zenoh Consumer: Did not receive READY signal from pipe.", file=sys.stderr)
            self.read_time.value = -1.0
            return

        session = None
        subscriber = None
        received_sample = None # To store the received data
        sample_received_event = self.ctx.Event() # Use MP Event

        def listener(sample):
            nonlocal received_sample
            # print(f"Zenoh Listener received sample: key={sample.key_expr}, size={len(sample.payload)}")
            received_sample = sample.payload # Store the payload
            sample_received_event.set() # Signal that data was received

        try:
            print("Zenoh Consumer: Opening session...")
            # Pass zenoh.Config()
            session = zenoh.open(zenoh.Config())
            print(f"Zenoh Consumer: Declaring subscriber for key {self.key_expr}...")
            subscriber = session.declare_subscriber(self.key_expr, listener)
            print("Zenoh Consumer: Subscriber declared, waiting for data...")

            start = time.time()
            # Wait for the listener to receive the data, with a timeout
            if sample_received_event.wait(timeout=10.0): # 10 second timeout
                print(f"Zenoh Consumer: Sample received (size={len(received_sample)}). Verifying...")
                # Verify data directly from the received payload
                verify_data_access(received_sample)
                self.read_time.value = time.time() - start
                print("Zenoh Consumer: Verification complete.")
            else:
                print("Zenoh Consumer: Timed out waiting for sample.", file=sys.stderr)
                self.read_time.value = -1.0 # Indicate timeout

        except Exception as e:
            print(f"Error in Zenoh consumer: {e}", file=sys.stderr)
            self.read_time.value = -1.0 # Indicate error
        finally:
            print("Zenoh Consumer: Cleaning up...")
            if subscriber:
                 try:
                      subscriber.undeclare()
                      print("Zenoh Consumer: Subscriber undeclared.")
                 except Exception as e_und:
                     print(f"Zenoh Consumer: Error undeclaring subscriber: {e_und}", file=sys.stderr)
            if session:
                session.close()
                print("Zenoh Consumer: Session closed.")
            print("Zenoh Consumer: Done.")

# --- Main Execution Logic ---

def run_benchmark(sizes_mb=[1, 10, 100]):
    print(f"{'Size (MB)':<12} {'Method':<15} {'Write (s)':<15} {'Read (s)':<15} {'Write xBase':<12} {'Read xBase':<12}")
    print("-" * 84)
    # Use spawn context for better cross-platform compatibility/isolation
    ctx = multiprocessing.get_context("spawn")
    use_colors = sys.stdout.isatty()

    for size in sizes_mb:
        print(f"Benchmarking {size} MB...")
        # Generate data (float64)
        num_elements = size * 1024 * 1024 // np.dtype(np.float64).itemsize
        data = np.random.rand(num_elements)

        # --- Calculate Baseline ---
        baseline_runner = SameProcessBenchmark(size, data, ctx)
        baseline_result = baseline_runner.run()
        baseline_write = baseline_result['write']
        baseline_read = baseline_result['read']

        # --- Define IPC Methods ---
        ipc_methods = [
            DiskBenchmark(size, data, ctx),
            ShmBenchmark(size, data, ctx),
            TcpBenchmark(size, data, ctx),
            HttpBenchmark(size, data, ctx),
            ZmqBenchmark(size, data, ctx),
            UdpBenchmark(size, data, ctx),
            ZenohBenchmark(size, data, ctx),
        ]

        # --- Run IPC Benchmarks ---
        ipc_results = []
        for method in ipc_methods:
            print(f"  Running {method.name}...")
            try:
                result = method.run()
                if result['read'] >= 0: # Check for error indicator
                    ipc_results.append(result)
                else:
                     print(f"    Skipping {method.name} due to error.", file=sys.stderr)
            except Exception as e:
                print(f"    Error running {method.name}: {e}", file=sys.stderr)


        # --- Calculate Multipliers ---
        def get_multiplier(value, baseline):
            if baseline <= 0: return "inf" # Avoid division by zero/negative
            if value <= 0: return "0.0x" # Handle zero/error values
            multiplier = value / baseline
            return f"{multiplier:.1f}x"

        for res in ipc_results:
            res['w_mult'] = get_multiplier(res['write'], baseline_write)
            res['r_mult'] = get_multiplier(res['read'], baseline_read)

        # --- Print Baseline and Sorted IPC Results ---
        print( # Print results table header again for clarity if verbose
             f"\n{'Size (MB)':<12} {'Method':<15} {'Write (s)':<15} {'Read (s)':<15} {'Write xBase':<12} {'Read xBase':<12}"
        )
        print("-" * 84)

        print(
            f"{size:<12} {baseline_result['method']:<15} {baseline_write:<15.6f} {baseline_read:<15.6f} {'1.0x':<12} {'1.0x':<12}"
        )

        ipc_results.sort(key=lambda x: (x['read'], x['write']))

        for i, res in enumerate(ipc_results):
            line = (
                f"{'':<12} {res['method']:<15} {res['write']:<15.6f} "
                f"{res['read']:<15.6f} {res['w_mult']:<12} {res['r_mult']:<12}"
            )
            if use_colors:
                if i == 0 and len(ipc_results) > 0: # Fastest IPC
                    print(f"{GREEN}{line}{RESET}")
                elif i == len(ipc_results) - 1 and len(ipc_results) > 0: # Slowest IPC
                    print(f"{RED}{line}{RESET}")
                else:
                    print(line)
            else:
                print(line)

        print() # Add space between sizes

    # Optional: Clean up global ZMQ context if necessary
    # zmq.Context.instance().term()


if __name__ == "__main__":
    # Consider adding argument parsing for sizes, repeats, etc.
    run_benchmark()

# Cleanup potential leftover SHM segments (optional, requires caution)
# from multiprocessing.resource_tracker import unregister
# from glob import glob
# if __name__ == "__main__":
#     run_benchmark()
#     print("Cleaning up potential leftover SHM segments...")
#     prefix = f"/psm_{os.getpid()}_"
#     for name in SharedMemory._tracked_names:
#         if name.startswith(prefix):
#              try:
#                  shm = SharedMemory(name=name)
#                  shm.close()
#                  shm.unlink()
#                  unregister(name, 'shared_memory')
#                  print(f"  Cleaned up {name}")
#              except FileNotFoundError:
#                  pass
#              except Exception as e:
#                   print(f" Error cleaning up {name}: {e}")
