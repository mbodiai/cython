from distutils.core import setup
from Cython.Build import cythonize
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Cython.Compiler.Options import DirectivesDict

directives:"DirectivesDict" = {"optimize": {"inline_defnode_calls": True}}
import mbcore

setup(
    name="benchmarks",
    ext_modules=cythonize(
        "*.py",
        language_level=3,
        annotate=True,
        compiler_directives=directives,
        exclude=["setup.py"],
    ),
    include_dirs=[mbcore.get_include()],
    py_modules=["mbcore"]
)


if __name__ == "__main__":
    print(mbcore.get_include())