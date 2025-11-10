# mode: run
# tag: cpdef, ccall, closures

import cython

cpdef cpdef_closure(x):
    def inner():
        return x
    return inner

@cython.ccall
def ccall_closure(x):
    def inner():
        return x
    return inner

def test():
    f = cpdef_closure(123)
    assert f() == 123
    g = ccall_closure(456)
    assert g() == 456
    print("Test passed")


def main():
    test()


if __name__ == "__main__":
    main()