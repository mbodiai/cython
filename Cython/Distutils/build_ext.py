import sys
import os   
from pathlib import Path
from typing import TYPE_CHECKING

from Cython.Compiler.Directives import DirectivesDict



# Always inherit from the "build_ext" in distutils since setuptools already imports
# it from Cython if available, and does the proper distutils fallback otherwise.
# https://github.com/pypa/setuptools/blob/9f1822ee910df3df930a98ab99f66d18bb70659b/setuptools/command/build_ext.py#L16

# setuptools imports Cython's "build_ext", so make sure we go first.
_build_ext_module = sys.modules.get('setuptools.command.build_ext')
if _build_ext_module is None:
    try:
        import distutils.command.build_ext as _build_ext_module
    except ImportError:
        # Python 3.12 no longer has distutils, but setuptools can replace it.
        try:
            import setuptools.command.build_ext as _build_ext_module
        except ImportError as e:
            raise ImportError("'distutils' cannot be imported. Please install setuptools.") from e

if TYPE_CHECKING:
     from distutils.command.build_ext import build_ext as _build_ext
else:
    # setuptools remembers the original distutils "build_ext" as "_du_build_ext"
    _build_ext = getattr(_build_ext_module, '_du_build_ext', None)
    if _build_ext is None:
        _build_ext = getattr(_build_ext_module, 'build_ext', None)
    if _build_ext is None:
        from distutils.command.build_ext import build_ext as _build_ext


class build_ext(_build_ext):
    verbose:int
    force:bool
    user_options = _build_ext.user_options + [
        ('cython-cplus', None,
             "generate C++ source files"),
        ('cython-create-listing', None,
             "write errors to a listing file"),
        ('cython-line-directives', None,
             "emit source line directives"),
        ('cython-include-dirs=', None,
             "path to the Cython include files" + _build_ext.sep_by),
        ('cython-c-in-temp', None,
             "put generated C files in temp directory"),
        ('cython-gen-pxi', None,
            "generate .pxi file for public declarations"),
        ('cython-directives=', None,
            "compiler directive overrides"),
        ('cython-gdb', None,
             "generate debug information for cygdb"),
        ('cython-compile-time-env', None,
            "cython compile time environment"),
        ]

    boolean_options = _build_ext.boolean_options + [
        'cython-cplus', 'cython-create-listing', 'cython-line-directives',
        'cython-c-in-temp', 'cython-gdb',
    ]

    def initialize_options(self):
        super().initialize_options()
        self.cython_cplus = 0
        self.cython_create_listing = 0
        self.cython_line_directives = 0
        self.cython_include_dirs = None
        self.cython_directives = None
        self.cython_c_in_temp = 0
        self.cython_gen_pxi = 0
        self.cython_gdb = False
        self.cython_compile_time_env = None
        self.shared_utility_qualified_name = None

    def finalize_options(self):
        super().finalize_options()
        if self.cython_include_dirs is None:
            self.cython_include_dirs = []
        elif isinstance(self.cython_include_dirs, str):
            self.cython_include_dirs = \
                self.cython_include_dirs.split(os.pathsep)
        if self.cython_directives is None:
            self.cython_directives = DirectivesDict()

    def get_extension_attr(self, extension, option_name, default=False):
        return getattr(self, option_name) or getattr(extension, option_name, default)

    def build_extension(self, ext):
        from Cython.Build.Dependencies import cythonize

        # Set up the include_path for the Cython compiler:
        #    1.    Start with the command line option.
        #    2.    Add in any (unique) paths from the extension
        #        cython_include_dirs (if Cython.Distutils.extension is used).
        #    3.    Add in any (unique) paths from the extension include_dirs
        includes = list(self.cython_include_dirs or [])
        for include_dir in getattr(ext, 'cython_include_dirs', []):
            if include_dir not in includes:
                includes.append(include_dir)

        # In case extension.include_dirs is a generator, evaluate it and keep
        # result
        ext.include_dirs = list(ext.include_dirs)
        for include_dir in ext.include_dirs + list(self.include_dirs):
            if include_dir not in includes:
                includes.append(include_dir)

        # Set up Cython compiler directives:
        #    1. Start with the command line option.
        #    2. Add in any (unique) entries from the extension
        #         cython_directives (if Cython.Distutils.extension is used).
        directives = self.cython_directives or DirectivesDict()
        if hasattr(ext, "cython_directives"):
            directives.update(ext.cython_directives)

        if self.get_extension_attr(ext, 'cython_cplus'):
            ext.language = 'c++'

        if hasattr(ext, 'no_c_in_traceback'):
            c_line_in_traceback = not ext.no_c_in_traceback
        else:
            c_line_in_traceback = None

        # Decide where to put generated C/C++ sources from cythonize.
        # - If cython_c_in_temp is set, respect build_temp as before.
        # - Otherwise, default to a project-local "generated" directory.
        if self.get_extension_attr(ext, 'cython_c_in_temp'):
            build_dir = self.build_temp
        else:
            build_dir = str((Path.cwd() / "generated").resolve())
        try:
            os.makedirs(build_dir, exist_ok=True)
        except Exception:
            # If directory creation fails, fall back to previous behavior (None)
            build_dir = None

        options = {
            'use_listing_file': self.get_extension_attr(ext, 'cython_create_listing'),
            'emit_linenums': self.get_extension_attr(ext, 'cython_line_directives'),
            'include_path': includes,
            'compiler_directives': directives,
            'build_dir': build_dir,
            'generate_pxi': self.get_extension_attr(ext, 'cython_gen_pxi'),
            'gdb_debug': self.get_extension_attr(ext, 'cython_gdb'),
            'c_line_in_traceback': c_line_in_traceback,
            'compile_time_env': self.get_extension_attr(ext, 'cython_compile_time_env', default=None),
            'shared_utility_qualified_name': self.get_extension_attr(ext, 'shared_utility_qualified_name', default=None),
        }

        new_ext = cythonize(
            ext, force=self.force, quiet=self.verbose == 0, **options
        )[0]

        # Keep the cythonised sources, but patch up any known bootstrap
        # mismatches in the generated C before compiling.  In particular,
        # wire the legacy ``__pyx_string_tab`` alias to the module-state
        # string table so that the ``__pyx_k*`` macros used in static
        # initialisers (fast-arg metadata etc.) have a valid target.
        for i, src in enumerate(new_ext.sources):
            if not src.endswith((".c", ".cpp", ".cc", ".cxx")):
                continue
            try:
                with open(src, "r", encoding="utf-8") as f:
                    code = f.read()
            except OSError:
                continue
            if "__pyx_string_tab" not in code or "/* #### Code section: constant_name_defines ### */" not in code:
                continue
            if "static PyObject **__pyx_string_tab;" in code:
                # Already patched.
                continue
            updated = code
            updated = updated.replace(
                "/* #### Code section: string_decls ### */",
                "/* #### Code section: string_decls ### */\nstatic PyObject **__pyx_string_tab;",
                1,
            )
            updated = updated.replace(
                "PyObject **stringtab = __pyx_mstate->__pyx_string_tab;",
                "PyObject **stringtab = __pyx_mstate->__pyx_string_tab;\n    __pyx_string_tab = stringtab;",
                1,
            )
            if updated != code:
                try:
                    with open(src, "w", encoding="utf-8") as f:
                        f.write(updated)
                except OSError:
                    pass

        ext.sources = new_ext.sources
        super().build_extension(ext)

# backward compatibility
new_build_ext = build_ext
