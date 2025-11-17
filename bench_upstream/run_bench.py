import importlib
import time

N = 5_000_000

mod_pyx = importlib.import_module("pyx_module")
mod_dec = importlib.import_module("decorator_module")
mod_cdef = importlib.import_module("bench_cdef_call")

cases = [
    ("pyx", "cpdef", mod_pyx.pyx_cpdef),
    ("pyx", "cdef_wrapper", mod_pyx.pyx_cdef_wrapper),
    ("decorator", "ccall", mod_dec.deco_ccall),
    ("decorator", "cfunc_wrapper", mod_dec.deco_cfunc_wrapper),
]

results = []
for origin, kind, func in cases:
    start = time.perf_counter()
    res = 0
    for _ in range(N):
        res = func(1)
    duration = time.perf_counter() - start
    results.append({
        "origin": origin,
        "kind": kind,
        "result": res,
        "total_s": duration,
        "ns_per_call": duration / N * 1e9,
        "m_calls_per_s": (N / duration) / 1e6,
    })

# Benchmark pure cdef loop (running inside Cython)
start = time.perf_counter()
res = mod_cdef.run_cdef_loop(N)
duration = time.perf_counter() - start
results.append({
    "origin": "cdef",
    "kind": "direct_cdef_loop",
    "result": res,
    "total_s": duration,
    "ns_per_call": duration / N * 1e9,
    "m_calls_per_s": (N / duration) / 1e6,
})

from pprint import pprint
print(f"Ran {N} iterations per function")
pprint(results)
