import sys
import os
from typing import Any

from Cython.Compiler.Options import Directives

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
        except ImportError:
            raise ImportError("'distutils' cannot be imported. Please install setuptools.")


# setuptools remembers the original distutils "build_ext" as "_du_build_ext"
_build_ext = getattr(_build_ext_module, '_du_build_ext', None)
if _build_ext is None:
    _build_ext = getattr(_build_ext_module, 'build_ext', None)
if _build_ext is None:
    from distutils.command.build_ext import build_ext as _build_ext


class build_ext(_build_ext):

    # Keep a separator constant (for help text) like distutils' build_ext
    sep_by = getattr(_build_ext, 'sep_by', os.pathsep)

    # Extend options with Cython-specific flags, plus legacy "pyrex-*" aliases.
    user_options = _build_ext.user_options + [
        ('cython-cplus', None,
             "generate C++ source files"),
        ('cython-create-listing', None,
             "write errors to a listing file"),
        ('cython-line-directives', None,
             "emit source line directives"),
        ('cython-include-dirs=', None,
             "path to the Cython include files" + (getattr(_build_ext, 'sep_by', os.pathsep))),
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

        # Legacy aliases for backwards compatibility with old_build_ext
        ('pyrex-cplus', None, "generate C++ source files (legacy)"),
        ('pyrex-create-listing', None, "write errors to a listing file (legacy)"),
        ('pyrex-line-directives', None, "emit source line directives (legacy)"),
        ('pyrex-include-dirs=', None, "path to the Cython include files (legacy)" + (getattr(_build_ext, 'sep_by', os.pathsep))),
        ('pyrex-c-in-temp', None, "put generated C files in temp directory (legacy)"),
        ('pyrex-gen-pxi', None, "generate .pxi file for public declarations (legacy)"),
        ('pyrex-directives=', None, "compiler directive overrides (legacy)"),
        ('pyrex-gdb', None, "generate debug information for cygdb (legacy)"),
        ]

    boolean_options = _build_ext.boolean_options + [
        'cython-cplus', 'cython-create-listing', 'cython-line-directives',
        'cython-c-in-temp', 'cython-gdb',

        # Legacy aliases
        'pyrex-cplus', 'pyrex-create-listing', 'pyrex-line-directives',
        'pyrex-c-in-temp', 'pyrex-gdb',
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

        # Legacy aliases (mirrored to cython_* in __getattr__/__setattr__)
        self.pyrex_cplus = None
        self.pyrex_create_listing = None
        self.pyrex_line_directives = None
        self.pyrex_include_dirs = None
        self.pyrex_c_in_temp = None
        self.pyrex_gen_pxi = None
        self.pyrex_directives = None
        self.pyrex_gdb = None

    def finalize_options(self):
        super().finalize_options()
        if self.cython_include_dirs is None:
            self.cython_include_dirs = []
        elif isinstance(self.cython_include_dirs, str):
            self.cython_include_dirs = \
                self.cython_include_dirs.split(os.pathsep)
        if self.cython_directives is None:
            self.cython_directives = Directives()

        # Accept legacy pyrex_* options if provided and map them to cython_*
        # Only override cython_* if pyrex_* is explicitly set (not None)
        def _apply_legacy(name: str):
            legacy_val = getattr(self, f'pyrex_{name}', None)
            if legacy_val is not None and not getattr(self, f'cython_{name}', None):
                setattr(self, f'cython_{name}', legacy_val)

        for opt in (
            'cplus', 'create_listing', 'line_directives', 'include_dirs',
            'c_in_temp', 'gen_pxi', 'directives', 'gdb'
        ):
            _apply_legacy(opt)

    # Legacy attribute accessors for backwards compatibility
    def __getattr__(self, name: str) -> Any:  # type: ignore[override]
        if name.startswith('pyrex_'):
            mapped = 'cython_' + name[6:]
            # Delegate to normal attribute resolution for the mapped name
            return super().__getattribute__(mapped)
        # Delegate to parent class' __getattr__ to preserve distutils behavior
        return super().__getattr__(name)

    def __setattr__(self, name: str, value: Any) -> None:  # type: ignore[override]
        if name.startswith('pyrex_'):
            super().__setattr__('cython_' + name[6:], value)
        else:
            super().__setattr__(name, value)

    # Mirror old_build_ext behavior: disable compiler optimizations when gdb debug requested
    def run(self):
        opt_disabler = None
        try:
            if self.cython_gdb or any(getattr(ext, 'cython_gdb', False) for ext in getattr(self, 'extensions', []) or []):
                try:
                    opt_disabler = Optimization()
                    opt_disabler.disable_optimization()
                except Exception:
                    opt_disabler = None
            super().run()
        finally:
            if opt_disabler is not None:
                try:
                    opt_disabler.restore_state()
                except Exception:
                    pass

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
        directives = dict(self.cython_directives or {})
        if hasattr(ext, "cython_directives"):
            directives.update(ext.cython_directives)

        if self.get_extension_attr(ext, 'cython_cplus'):
            ext.language = 'c++'

        if hasattr(ext, 'no_c_in_traceback'):
            c_line_in_traceback = not ext.no_c_in_traceback
        else:
            c_line_in_traceback = None
        options = {
            'use_listing_file': self.get_extension_attr(ext, 'cython_create_listing'),
            'emit_linenums': self.get_extension_attr(ext, 'cython_line_directives'),
            'include_path': includes,
            'compiler_directives': directives,
            'build_dir': self.build_temp if self.get_extension_attr(ext, 'cython_c_in_temp') else None,
            'generate_pxi': self.get_extension_attr(ext, 'cython_gen_pxi'),
            'gdb_debug': self.get_extension_attr(ext, 'cython_gdb'),
            'c_line_in_traceback': c_line_in_traceback,
            'compile_time_env': self.get_extension_attr(ext, 'cython_compile_time_env', default=None),
            'shared_utility_qualified_name': self.get_extension_attr(ext, 'shared_utility_qualified_name', default=None),
        }

        # Be noisy by default to show "Compiling/Cythonizing" messages unless explicitly silenced.
        new_ext = cythonize(
            ext, force=self.force, quiet=False, **options
        )[0]

        # Ensure paths are relative to the project root directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        compile_sources: list[str] = []  # paths passed to the C compiler
        packaging_sources: list[str] = []  # paths stored in metadata (must be relative)

        for source in new_ext.sources:
            if os.path.isabs(source):
                abs_source = source
            else:
                # Resolve relative path with respect to the *current* working directory.
                # run_distutils already chdir()'d into the extension's base_dir, so this will
                # point at the freshly generated source file (e.g. tests/run/list.c).
                abs_source = os.path.abspath(source)

            if source.endswith(('.c', '.cpp')):
                # Generated C/C++ sources: compiler needs absolute, but metadata must be relative
                compile_sources.append(abs_source)
                packaging_sources.append(os.path.relpath(abs_source, project_root))
            else:
                # Other sources: keep relative where possible; absolute only if outside project tree.
                rel = os.path.relpath(abs_source, project_root) if abs_source.startswith(project_root) else source
                compile_sources.append(rel)
                packaging_sources.append(rel)

        # Use absolute/relative mix for compilation
        new_ext.sources = compile_sources

        # DEBUG: show source paths to verify they are absolute where needed
        if self.debug or os.environ.get('CYTHON_PATH_DEBUG'):
            import inspect
            print("[build_ext] Module:", inspect.getfile(self.__class__))
            print("[build_ext] Debug sources for", new_ext.name, ":", new_ext.sources)
        # Keep the original Extension in sync to avoid further processing errors.
        # Temporarily point original Extension to compile_sources so Cython"s internal logic (e.g., dependency tracking)
        # matches what we feed the compiler, then restore relative paths afterwards.
        ext.sources = compile_sources

        # Build the *cythonized* extension rather than the original one so
        # that our path fixes actually take effect.
        super().build_extension(new_ext)

        # After successful compilation, reset both Extension objects to packaging-friendly relative paths
        ext.sources = packaging_sources
        new_ext.sources = packaging_sources


# Provide an Optimization helper for compatibility with old_build_ext
try:
    # Prefer stdlib distutils if present (<=3.11)
    from distutils import sysconfig as _du_sysconfig  # type: ignore
except Exception:  # pragma: no cover - fallback when stdlib distutils is gone
    try:
        # Fallback to setuptools' vendored distutils (3.12+)
        import setuptools._distutils.sysconfig as _du_sysconfig  # type: ignore
    except Exception:  # last resort
        _du_sysconfig = None  # type: ignore


class Optimization:
    def __init__(self):
        self.flags = (
            'OPT',
            'CFLAGS',
            'CPPFLAGS',
            'EXTRA_CFLAGS',
            'BASECFLAGS',
            'PY_CFLAGS',
        )
        self._cfg = _du_sysconfig.get_config_vars() if _du_sysconfig else {}
        # Capture current state to restore later
        self.state = [self._cfg.get(flag) for flag in self.flags]

    def disable_optimization(self) -> None:
        badoptions = ('-O1', '-O2', '-O3')
        for flag, option in zip(self.flags, self.state):
            if option:
                keep = [opt for opt in option.split() if opt not in badoptions]
                self._cfg[flag] = ' '.join(keep)

    def restore_state(self) -> None:
        for flag, option in zip(self.flags, self.state):
            if option is not None:
                self._cfg[flag] = option


# Backwards-compatible alias
optimization = Optimization()

# backward compatibility
new_build_ext = build_ext
