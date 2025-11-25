# cython: language_level=3
"""
Internal helper used by Tools/regenerate_common_includes.py to exercise a wide
range of utility code so hashed headers get emitted when regenerating
Cython/Common/Include.
"""


def probe_collections(obj=None):
    """Touch list/dict/set operations to emit SetItem/GetItem helpers."""
    cdef list lst = [1, 2, 3]
    lst[1] = 5
    lst.append(7)
    lst[0:1] = [0, 1]
    try:
        del lst[2]
    except Exception:
        pass

    cdef dict d = {0: 1}
    d[1] = 2
    d.get(0, None)
    d.setdefault(3, 4)

    cdef set s = {1, 2, 3}
    s.add(4)
    s.discard(2)


def probe_numeric():
    """Exercise integer conversions and binary ops."""
    cdef int i = 5
    cdef long long ll = i * 2
    cdef unsigned int ui = i + 3
    cdef double d = ll / 3.0
    return i, ll, ui, d


def probe_slicing(buf):
    """Exercise slice objects to ensure slice helpers get emitted."""
    return buf[1:-1], buf[:], buf[::2]


def gen():
    """A generator to force generator support utilities."""
    for i in range(3):
        yield i


cdef class CClass:
    """Simple cdef class to pull in extension-type support helpers."""
    cdef int count
    def __cinit__(self):
        self.count = 0
    def incr(self, int delta=1):
        self.count += delta
        return self.count


def kwonly_probe(x, *, required, optional=1):
    """Exercise fastcall keyword parsing (required and optional kwonly args)."""
    return x, required, optional
