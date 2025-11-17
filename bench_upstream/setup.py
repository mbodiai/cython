from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("pyx_module", ["pyx_module.pyx"]),
    Extension("decorator_module", ["decorator_module.py"]),
    Extension("bench_cdef_call", ["bench_cdef_call.pyx"]),
]

setup(
    name="cython_bench_upstream",
    ext_modules=cythonize(
        extensions,
        compiler_directives={"language_level": 3},
    ),
)
