# Python-callable Function Overhead (Upstream Cython)

Hardware: Apple M-series (ARM64) macOS 11+  
Python: 3.11.13 (cpython-3.11.13-macos-aarch64)  
Cython: upstream master (`pip install git+https://github.com/cython/cython.git`)  
Iterations: 5,000,000 per function

| Origin     | Kind              | Total Time (s) | ns / call | M calls / s |
|------------|------------------|---------------:|----------:|------------:|
| pyx        | cpdef            | 0.12085        | 24.17     | 41.37       |
| pyx        | cdef_wrapper     | 0.12042        | 24.08     | 41.52       |
| decorator  | ccall            | 0.12169        | 24.34     | 41.09       |
| decorator  | cfunc_wrapper    | 0.12031        | 24.06     | 41.56       |
| cdef       | direct_cdef_loop | 0.00000104     | 0.000208  | 4,798,310   |

Notes:
- `pyx_cpdef` is a standard `cpdef int f(int)` defined in a `.pyx` file.
- `pyx_cdef_wrapper` is a Python `def` that forwards to a typed `cdef` implementation.
- `decorator` cases use pure-Python source with `@cython.ccall` / `@cython.cfunc` decorators.
- `direct_cdef_loop` runs entirely in Cython (no Python entry), showing raw cdef speed.
- All Python-visible entries sit around ~24 ns per call, indicating the existing wrapper overhead.
- These numbers form the baseline before implementing optimized vectorcall/keyword parsing in our fork.
