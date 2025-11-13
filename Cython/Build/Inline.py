import gc
import hashlib
import importlib.util
import inspect
import json
from numpy import ndarray
import os
from pathlib import Path
import re
import sys
import time
from datetime import datetime
from distutils.command.build_ext import build_ext
from distutils.core import Distribution, Extension
from importlib.machinery import ExtensionFileLoader
from typing import TYPE_CHECKING, Any, cast
import Cython
import cython as cython_module

from ..Compiler import Pipeline
from ..Compiler.Main import Context
from ..Compiler.Options import CompilationOptions, default_options, get_directive_defaults, Directives
from ..Compiler.ParseTreeTransforms import SkipDeclarations
from ..Compiler.TreeFragment import parse_from_strings
from ..Compiler.Visitor import EnvTransform
from .Cache import get_cython_cache_dir
from .Dependencies import cached_function, cythonize, strip_string_literals

from mbcore.utils.import_utils import smart_import
if TYPE_CHECKING:
    import numpy as np
else:
    np = smart_import('numpy')

def load_dynamic(name, path):
    spec = importlib.util.spec_from_file_location(name, loader=ExtensionFileLoader(name, path))
    if spec is None:
        raise ImportError(f"Failed to load module {name} from {path}")
    module = importlib.util.module_from_spec(spec)
    if module is None or spec.loader is None:
        raise ImportError(f"Failed to create module from spec for {name}")
    spec.loader.exec_module(module)
    return module









def write_metadata(lib_dir, module_name, metadata):
    """Write compilation metadata to a .json file next to the module."""
    metadata_file = Path(lib_dir) / f"{module_name}.meta.json"
    with Path(metadata_file).open('w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, default=str)


def generate_pxd_file(pyx_file, lib_dir, module_name):
    """Generate a minimal .pxd header file from a .pyx.

    Extracts cimports and cdef class headers to allow cimporting extension types.
    """
    with Path(pyx_file).open('r', encoding='utf-8') as f:
        pyx_content = f.read()

    lines = pyx_content.split('\n')
    pxd_lines = []
    in_class = False
    class_indent = 0

    for line in lines:
        stripped = line.strip()
        if (stripped.startswith('cimport ') or (stripped.startswith('from ') and ' cimport ' in stripped)) and not in_class:
            pxd_lines.append(line)
            continue
        if stripped.startswith('cdef class '):
            in_class = True
            class_indent = len(line) - len(line.lstrip())
            pxd_lines.append(line)
            continue
        if in_class and stripped.startswith('cdef public '):
            pxd_lines.append(line)
            continue
        if in_class:
            current_indent = len(line) - len(line.lstrip())
            if stripped and current_indent <= class_indent:
                in_class = False
                pxd_lines.append("")

    pxd_file = Path(lib_dir) / f"{module_name}.pxd"
    with Path(pxd_file).open('w', encoding='utf-8') as f:
        f.write('\n'.join(pxd_lines))


class UnboundSymbols(EnvTransform, SkipDeclarations):
    def __init__(self):
        super(EnvTransform, self).__init__(context=None)
        self.unbound = set()
    def visit_NameNode(self, node):
        if not self.current_env().lookup(node.name):
            self.unbound.add(node.name)
        return node
    def __call__(self, node):
        super().__call__(node)
        return self.unbound


@cached_function
def unbound_symbols(code, context=None):
    if context is None:
        context = Context([], get_directive_defaults(),
                          options=CompilationOptions(**default_options))
    from ..Compiler.ParseTreeTransforms import AnalyseDeclarationsTransform
    tree = parse_from_strings('(tree fragment)', code)
    for phase in Pipeline.create_pipeline(context, 'pyx'):
        if phase is None:
            continue
        tree = phase(tree)
        if isinstance(phase, AnalyseDeclarationsTransform):
            break
    import builtins
    return tuple(UnboundSymbols()(tree) - set(dir(builtins)))


def unsafe_type(arg, context=None):
    py_type = type(arg)
    if py_type is int:
        return 'long'

    return safe_type(arg, context)


def safe_type(arg:"np.ndarray[Any,np.dtype[np.generic]]|Any", context:"Context|None"=None):
    py_type = type(arg)
    if py_type in (list, tuple, dict, str):
        return py_type.__name__
    if py_type is complex:
        return 'double complex'
    if py_type is float:
        return 'double'
    if py_type is bool:
        return 'bint'
    if 'numpy' in sys.modules and isinstance(arg, np.ndarray):
        return f'numpy.ndarray[numpy.{arg.dtype.name}_t, ndim={arg.ndim}]'

    for base_type in py_type.__mro__:
        if base_type.__module__ in ('__builtin__', 'builtins'):
            return 'object'
        module = context.find_module(base_type.__module__, need_pxd=False)
        if module:
            entry = module.lookup(base_type.__name__)
            if entry.is_type:
                return '%s.%s' % (base_type.__module__, base_type.__name__)
    return 'object'


def _get_build_extension():
    dist = Distribution()
    # Ensure the build respects distutils configuration by parsing
    # the configuration files
    config_files = dist.find_config_files()
    dist.parse_config_files(config_files)
    build_extension = build_ext(dist)
    build_extension.finalize_options()
    return build_extension


@cached_function
def _create_context(cython_include_dirs):
    return Context(
        list(cython_include_dirs),
        get_directive_defaults(),
        options=CompilationOptions(**default_options)
    )


_cython_inline_cache = {}
_cython_inline_default_context = _create_context(('.',))


def _populate_unbound(kwds, unbound_symbols, locals=None, globals=None):
    for symbol in unbound_symbols:
        if symbol not in kwds:
            if locals is None or globals is None:
                calling_frame = inspect.currentframe().f_back.f_back.f_back
                if locals is None:
                    locals = calling_frame.f_locals
                if globals is None:
                    globals = calling_frame.f_globals
            if not isinstance(locals, dict):
                # FrameLocalsProxy is stricter than dict on how it looks up keys
                # and this means our "EncodedStrings" don't match the keys in locals.
                # Therefore copy to a dict.
                locals = dict(locals)
            if symbol in locals:
                kwds[symbol] = locals[symbol]
            elif symbol in globals:
                kwds[symbol] = globals[symbol]
            else:
                print("Couldn't find %r" % symbol)


def _inline_key(orig_code, arg_sigs, language_level):
    key = orig_code, arg_sigs, sys.version_info, sys.executable, language_level, Cython.__version__
    return hashlib.sha256(str(key).encode('utf-8')).hexdigest()


def cython_inline(code, get_type=unsafe_type,
                  lib_dir=None,
                  cython_include_dirs=None, cython_compiler_directives=None,
                  force=False, quiet=False, locals=None, globals=None, language_level=None,
                  cache_config=None, *,
                  pyx_references=None,
                  **kwds):

        
    ctx = _create_context(tuple(cython_include_dirs)) if cython_include_dirs else _cython_inline_default_context

    cython_compiler_directives = cython_compiler_directives.copy() if cython_compiler_directives else Directives()
    if language_level is None and 'language_level' not in cython_compiler_directives:
        language_level = '3'
    if language_level is not None:
        cython_compiler_directives['language_level'] = language_level


    key_hash = None

    # Fast path if this has been called in this session.
    _unbound_symbols = _cython_inline_cache.get(code)
    if _unbound_symbols is not None:
        _populate_unbound(kwds, _unbound_symbols, locals, globals)
        args = sorted(kwds.items())
        arg_sigs = tuple([(get_type(value, ctx), arg) for arg, value in args])
        key_hash = _inline_key(code, arg_sigs, language_level)
        invoke = _cython_inline_cache.get((code, arg_sigs, key_hash))
        if invoke is not None:
            arg_list = [arg[1] for arg in args]
            return invoke(*arg_list)

    orig_code = code
    code, literals = strip_string_literals(code)
    code = strip_common_indent(code)
    if locals is None:
        locals = inspect.currentframe().f_back.f_back.f_locals
    if globals is None:
        globals = inspect.currentframe().f_back.f_back.f_globals
    try:
        _cython_inline_cache[orig_code] = _unbound_symbols = unbound_symbols(code)
        _populate_unbound(kwds, _unbound_symbols, locals, globals)
    except AssertionError:
        if not quiet:
            # Parsing from strings not fully supported (e.g. cimports).
            print("Could not parse code as a string (to extract unbound symbols).")

    cimports = []
    for name, arg in list(kwds.items()):
        if arg is cython_module:
            cimports.append('\ncimport cython as %s' % name)
            del kwds[name]
    arg_names = sorted(kwds)
    arg_sigs = tuple([(get_type(kwds[arg], ctx), arg) for arg in arg_names])
    if key_hash is None:
        key_hash = _inline_key(orig_code, arg_sigs, language_level)
    # Build module name (semantic or hashed)
    caller_info = _get_caller_info()
    module_name = _make_semantic_name(key_hash, caller_info, cache_config)

    if module_name in sys.modules:
        module = sys.modules[module_name]

    else:
        build_extension = None
        if cython_inline.so_ext is None:
            # Figure out and cache current extension suffix
            build_extension = _get_build_extension()
            cython_inline.so_ext = build_extension.get_ext_filename('')

        lib_dir = os.path.abspath(lib_dir)
        module_path = os.path.join(lib_dir, module_name + cython_inline.so_ext)

        if not os.path.exists(lib_dir):
            os.makedirs(lib_dir)
        if force or not os.path.isfile(module_path):
            cflags = []
            define_macros = []
            c_include_dirs = []
            qualified = re.compile(r'([.\w]+)[.]')
            for type, _ in arg_sigs:
                m = qualified.match(type)
                if m:
                    cimports.append('\ncimport %s' % m.groups()[0])
                    # one special case
                    if m.groups()[0] == 'numpy':
                        import numpy
                        c_include_dirs.append(numpy.get_include())
                        define_macros.append(("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION"))
                        cflags.append('-Wno-unused')
            module_body, func_body = extract_func_code(code)
            params = ', '.join(['%s %s' % a for a in arg_sigs])
            module_code = """
%(module_body)s
%(cimports)s
def __invoke(%(params)s):
%(func_body)s
    return locals()
            """ % {'cimports': '\n'.join(cimports),
                   'module_body': module_body,
                   'params': params,
                   'func_body': func_body }
            for key, value in literals.items():
                module_code = module_code.replace(key, value)
            pyx_file = os.path.join(lib_dir, module_name + '.pyx')
            fh = open(pyx_file, 'w')
            try:
                fh.write(module_code)
            finally:
                fh.close()
            extension = Extension(
                name=module_name,
                sources=[pyx_file],
                include_dirs=c_include_dirs or None,
                extra_compile_args=cflags or None,
                define_macros=define_macros or None,
            )
            if build_extension is None:
                build_extension = _get_build_extension()
            # Source-reference behavior: one flag + one env var
            # pyx_references (bool) controls: line-directives to .pyx, hide C lines in traceback,
            # and remove C link from annotation HTML.
            # Defaults to True unless overridden by env or flag.
            if pyx_references is None:
                v = os.environ.get('CYTHON_INLINE_PYX_REFERENCES')
                if v is None:
                    pyx_references = True
                else:
                    pyx_references = v not in ('0', 'false', 'False')
            emit_linenums = bool(pyx_references)
            c_line_in_traceback = not bool(pyx_references)
            annotate_no_c_link = bool(pyx_references)

            cythonize_kwargs = {
                'module_list': [extension],
                'include_path': cython_include_dirs or ['.'],
                'compiler_directives': cython_compiler_directives,
                # Inline should show normal compile output (Compiling/Cythonizing) by default.
                'quiet': False,
                'annotate': True,
            }
            cythonize_kwargs['emit_linenums'] = emit_linenums
            cythonize_kwargs['c_line_in_traceback'] = c_line_in_traceback
            cythonize_kwargs['annotate_no_c_link'] = annotate_no_c_link
            build_extension.extensions = cythonize(**cythonize_kwargs)
            build_extension.build_temp = os.path.dirname(pyx_file)
            build_extension.build_lib  = lib_dir
            build_extension.run()

        if sys.platform == 'win32' and sys.version_info >= (3, 8):
            with os.add_dll_directory(os.path.abspath(lib_dir)):
                module = load_dynamic(module_name, module_path)
        else:
            module = load_dynamic(module_name, module_path)

    _cython_inline_cache[orig_code, arg_sigs, key_hash] = module.__invoke
    arg_list = [kwds[arg] for arg in arg_names]
    return module.__invoke(*arg_list)


# Compile a full module-level Cython code string and import it.
def cython_inline_module(code, lib_dir=None,
                         cython_include_dirs=None, cython_compiler_directives=None,
                         force=False, quiet=False,
                         *, pyx_references=None, module_name=None, output_path=None):
    """Compile a full module-level Cython code string (pure decorators allowed) and import it.

    - No function wrapper is added; code is written as-is to a .pyx file in the cache dir
      or at 'output_path' if provided.
    - Returns the imported module object.
    - Generates a minimal .pxd file for cimporting extension types.
    - If 'module_name' is provided, it is used verbatim (sanitized) as the module name,
      instead of generated hash/semantic names.
    - If 'output_path' is provided, it is treated as the exact base path (without extension)
      for generated files: '{output_path}.pyx', '{output_path}.pxd', and the compiled shared
      library at '{output_path}{so_ext}'. The module name will be the basename of
      'output_path'.
    """

    directives = cython_compiler_directives.copy() if cython_compiler_directives else {}
    language_level = directives.get('language_level', '3')
    key_hash = _inline_key(code, (), language_level)


    # If an explicit output_path is specified, derive everything from it.
    base_path = None
    if output_path is not None:
        # Treat output_path as a base path without extension. If an extension is present,
        # strip it to form the base path.
        base_path = os.path.abspath(str(output_path))
        # Strip some known source extensions if present
        for ext in ('.pyx', '.pxd', '.c', '.cpp', '.html', '.md'):
            if base_path.endswith(ext):
                base_path = base_path[: -len(ext)]
                break
        # Ensure directory exists later; choose module_name from basename
        module_name = os.path.basename(base_path)
        # Sanitize module_name to a valid python identifier
        module_name = re.sub(r'[^a-zA-Z0-9_]', '_', module_name)
        if module_name and not (module_name[0].isalpha() or module_name[0] == '_'):
            module_name = '_' + module_name
        # The library dir is the directory of the base_path
        lib_dir = os.path.dirname(base_path) or '.'
    else:
        # Respect an explicit user-provided module name when given.
        if module_name:
            # Sanitize to a valid module name (letters, digits, underscore, not starting with digit)
            sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', str(module_name))
            if sanitized and not (sanitized[0].isalpha() or sanitized[0] == '_'):
                sanitized = '_' + sanitized
            module_name = sanitized


    if cython_inline.so_ext is None:
        build_extension = _get_build_extension()
        cython_inline.so_ext = build_extension.get_ext_filename('')
    # If the output_path pointed to a filename including the shared extension,
    # strip it now that we know the platform-specific suffix.
    if base_path is not None and base_path.endswith(cython_inline.so_ext):
        base_path = base_path[: -len(cython_inline.so_ext)]
    lib_dir = os.path.abspath(lib_dir)
    if base_path is None:
        module_path = os.path.join(lib_dir, module_name + cython_inline.so_ext)
        pyx_file = os.path.join(lib_dir, module_name + '.pyx')
        pxd_path = os.path.join(lib_dir, module_name + '.pxd')
    else:
        module_path = base_path + cython_inline.so_ext
        pyx_file = base_path + '.pyx'
        pxd_path = base_path + '.pxd'

    if module_name in sys.modules and os.path.isfile(module_path):
        return sys.modules[module_name]

    if not os.path.exists(lib_dir):
        os.makedirs(lib_dir)

    if force or not os.path.isfile(module_path) or not os.path.isfile(pxd_path):
        with open(pyx_file, 'w', encoding='utf-8') as fh:
            fh.write(code)

        # Suppress noisy "unused" warnings by default for inline builds (POSIX compilers).
        cflags = []
        if os.name == 'posix':
            cflags.extend(['-Wno-unused-function', '-Wno-unused'])
        extension = Extension(name=module_name, sources=[pyx_file], extra_compile_args=cflags or None)
        build_extension = _get_build_extension()
        include_path = (cython_include_dirs or []) + [lib_dir]
        # Single env var + flag behavior (see cython_inline)
        if pyx_references is None:
            v = os.environ.get('CYTHON_INLINE_PYX_REFERENCES')
            if v is None:
                pyx_references = True
            else:
                pyx_references = v not in ('0', 'false', 'False')
        emit_linenums = bool(pyx_references)
        c_line_in_traceback = not bool(pyx_references)
        annotate_no_c_link = bool(pyx_references)

        cythonize_kwargs = dict(
            module_list=[extension],
            include_path=include_path,
            compiler_directives=directives,
            quiet=quiet,
            annotate=True,
        )
        cythonize_kwargs['emit_linenums'] = emit_linenums
        cythonize_kwargs['c_line_in_traceback'] = c_line_in_traceback
        cythonize_kwargs['annotate_no_c_link'] = annotate_no_c_link
        build_extension.extensions = cythonize(**cythonize_kwargs)
        build_extension.build_temp = os.path.dirname(pyx_file)
        build_extension.build_lib = lib_dir
        build_extension.run()

        # If a specific output_path was requested and the built path differs,
        # move the built artifact to the requested path so that we load from it.
        if base_path is not None:
            built_path = os.path.join(lib_dir, module_name + cython_inline.so_ext)
            if os.path.isfile(built_path) and os.path.abspath(built_path) != os.path.abspath(module_path):
                try:
                    os.replace(built_path, module_path)
                except Exception:
                    # If moving fails, try copying as a fallback.
                    try:
                        import shutil
                        shutil.copy2(built_path, module_path)
                    except Exception:
                        pass

        # Generate .pxd for cimporting extension types
        _generate_pxd_file(pyx_file, lib_dir, module_name)

        # Metadata
        if getattr(cache_config, 'keep_metadata', False):
            annotated_html = (base_path + '.html') if base_path is not None else os.path.join(lib_dir, module_name + '.html')
            annotated_md = (base_path + '.md') if base_path is not None else os.path.join(lib_dir, module_name + '.md')
            metadata = {
                "compiled_at": datetime.now().isoformat(),
                "cython_version": Cython.__version__,
                "python_version": sys.version,
                "caller": caller_info,
                "module_name": module_name,
                "hash": key_hash,
                "language_level": language_level,
                "directives": directives,
                "pyx_file": pyx_file,
                "pxd_file": pxd_path,
                "annotated_html": annotated_html,
                "annotated_md": annotated_md,
                "module_path": module_path,
                "code_length": len(code),
            }
            _write_metadata(lib_dir, module_name, metadata)

    if sys.platform == 'win32' and sys.version_info >= (3, 8):
        with os.add_dll_directory(os.path.abspath(lib_dir)):
            module = load_dynamic(module_name, module_path)
    else:
        module = load_dynamic(module_name, module_path)
    return module


# The code template used for cymeit benchmark runs.
# We keep the benchmark repetition separate from the benchmarked code
# to prevent the C compiler from doing unhelpful loop optimisations.
_CYMEIT_TEMPLATE = """
def __PYX_repeat_benchmark(benchmark, timer, size_t number):
    cdef size_t i

    t0 = timer()
    for i in range(number):
        benchmark()
    t1 = timer()
    return t1 - t0

def __PYX_make_benchmark():
    {setup_code}

    def __PYX_run_benchmark():
        {benchmark_code}

    return __PYX_run_benchmark
"""


def cymeit(code, setup_code=None, import_module=None, directives=None, timer=time.perf_counter, repeat=9):
    """Benchmark a Cython code string similar to 'timeit'.

    'setup_code': string of setup code that will be run before taking the timings.

    'import_module': a module namespace to run the benchmark in
                     (usually a compiled Cython module).

    'directives': Cython directives to use when compiling the benchmark code.

    'timer': The timer function. Defaults to 'time.perf_counter', returning float seconds.
             Nanosecond timers are detected (and can only be used) if they return integers.

    'repeat': The number of timings to take and return.

    Returns a tuple: (list of single-loop timings, number of loops run for each)
    """
    import textwrap

    # Compile the benchmark code as an inline closure function.

    setup_code = strip_common_indent(setup_code) if setup_code else ''
    code = strip_common_indent(code) if code.strip() else 'pass'

    module_namespace = __import__(import_module).__dict__ if import_module else None

    cymeit_code = _CYMEIT_TEMPLATE.format(
        setup_code=textwrap.indent(setup_code, ' '*4).strip(),
        benchmark_code=textwrap.indent(code, ' '*8).strip(),

    )

    namespace = cython_inline(
        cymeit_code,
        cython_compiler_directives=directives,
        locals=module_namespace,
    )

    make_benchmark = namespace['__PYX_make_benchmark']
    repeat_benchmark = namespace['__PYX_repeat_benchmark']

    # Based on 'timeit' in CPython 3.13.

    def timeit(number):
        benchmark = make_benchmark()

        gcold = gc.isenabled()
        gc.disable()
        try:
            timing = repeat_benchmark(benchmark, timer, number)
        finally:
            if gcold:
                gc.enable()
        return timing

    # Find a sufficiently large number of loops, warm up the system.

    timer_returns_nanoseconds = isinstance(timer(), int)
    one_second = 1_000_000_000 if timer_returns_nanoseconds else 1.0

    # Run for at least 0.2 seconds, either as integer nanoseconds or floating point seconds.
    min_runtime = one_second // 5 if timer_returns_nanoseconds else one_second / 5

    def autorange():
        i = 1
        while True:
            for j in 1, 2, 5:
                number = i * j
                time_taken = timeit(number)
                assert isinstance(time_taken, int if timer_returns_nanoseconds else float)
                if time_taken >= min_runtime:
                    return number
                elif timer_returns_nanoseconds and (time_taken < 10 and number >= 10):
                    # Arbitrary sanity check to prevent endless loops for non-ns timers.
                    raise RuntimeError(f"Timer seems to return non-ns timings: {timer}")
            i *= 10

    autorange()  # warmup
    number = autorange()

    # Run and repeat the benchmark.
    timings = [
        timeit(number)
        for _ in range(repeat)
    ]

    half = number // 2  # for integer rounding

    timings = [
        (timing + half) // number if timer_returns_nanoseconds else timing / number
        for timing in timings
    ]

    return (timings, number)


# Cached suffix used by cython_inline above.  None should get
# overridden with actual value upon the first cython_inline invocation
cython_inline.so_ext = None

_find_non_space = re.compile(r'\S').search


def strip_common_indent(code):
    min_indent = None
    lines = code.splitlines()
    for line in lines:
        match = _find_non_space(line)
        if not match:
            continue  # blank
        indent = match.start()
        if line[indent] == '#':
            continue  # comment
        if min_indent is None or min_indent > indent:
            min_indent = indent
    for ix, line in enumerate(lines):
        match = _find_non_space(line)
        if not match or not line or line[indent:indent+1] == '#':
            continue
        lines[ix] = line[min_indent:]
    return '\n'.join(lines)


module_statement = re.compile(r'^((cdef +(extern|class))|cimport|(from .+ cimport)|(from .+ import +[*]))')
def extract_func_code(code):
    module = []
    function = []
    current = function
    code = code.replace('\t', ' ')
    lines = code.split('\n')
    for line in lines:
        if not line.startswith(' '):
            if module_statement.match(line):
                current = module
            else:
                current = function
        current.append(line)
    return '\n'.join(module), '    ' + '\n    '.join(function)


def get_body(source):
    ix = source.index(':')
    if source[:5] == 'lambda':
        return "return %s" % source[ix+1:]
    else:
        return source[ix+1:]


# Lots to be done here... It would be especially cool if compiled functions
# could invoke each other quickly.
class RuntimeCompiledFunction:

    def __init__(self, f):
        self._f = f
        self._body = get_body(inspect.getsource(f))

    def __call__(self, *args, **kwds):
        all = inspect.getcallargs(self._f, *args, **kwds)
        return cython_inline(self._body, locals=self._f.__globals__, globals=self._f.__globals__, **all)
