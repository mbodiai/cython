# cython: language_level=3
import cython

@cython.cfunc
@cython.returns(cython.int)
@cython.locals(x=cython.int)
def _deco_cfunc_impl(x):
    return x + 1

@cython.ccall
@cython.returns(cython.int)
@cython.locals(x=cython.int)
def deco_ccall(x):
    return x + 1

def deco_cfunc_wrapper(x):
    return _deco_cfunc_impl(x)
