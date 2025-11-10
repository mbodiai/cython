cimport cython
try:
    import typing
    import dataclasses
except ImportError:
    pass  # The modules don't actually have to exists for Cython to use them as annotations

import time
@dataclasses.dataclass
cdef class MyDataclass:
    # fields can be declared using annotations
    a: cython.int = 0
    b: cython.double = dataclasses.field(default_factory = lambda: 10, repr=False)

    # fields can also be declared using `cdef`:
    cdef str c  # add `readonly` or `public` to if `c` needs to be accessible from Python
    c = "hello"  # assignment of default value on a separate line
    # note: `@dataclass(frozen)` is not enforced on `cdef` attributes

    # typing.InitVar and typing.ClassVar also work
    d: dataclasses.InitVar[cython.double] = 5
    e: typing.ClassVar[list] = []

class MyDataclass2:
    a:int = 0
    b:int = 1
    c:int = 2
    d:int = 3
    e:int = 4

MyDataclass2 = dataclasses.dataclass(MyDataclass2)

def time_it(func):
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    print(f"Time taken: {end - start} seconds for {func.__name__}")

cpdef void main():
    time_it(lambda: MyDataclass())
    time_it(lambda: MyDataclass2())

    m = MyDataclass()
    m2 = MyDataclass2()
    time_it(lambda: m.a)
    time_it(lambda: m2.a)
    time_it(lambda: setattr(m, "a", 1))