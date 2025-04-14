from distutils.core import setup
from Cython.Build import cythonize

# Direct compilation
setup(
    ext_modules=cythonize("test_stdlib.pyx", language_level=3),
    script_args=["build_ext", "--inplace"]
) 