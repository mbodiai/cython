# Cython annotation for Code.py

Raw output: Code.c

L1  ⚪  (score=0)
```python
#
```
L2  ⚪  (score=0)
```python
#   Code output module
```
L3  ⚪  (score=0)
```python
#
```
L4  ⚪  (score=0)
```python
from __future__ import annotations
```
L5  ⚪  (score=0)
```python
```
L6  ⚪  (score=0)
```python
import cython
```
L7  ⚪  (score=0)
```python
cython.declare(os=object, re=object, operator=object, textwrap=object,
```
L8  ⚪  (score=0)
```python
               Template=object, Naming=object, Options=object, StringEncoding=object,
```
L9  ⚪  (score=0)
```python
               Utils=object, SourceDescriptor=object, StringIOTree=object,
```
L10  ⚪  (score=0)
```python
               DebugFlags=object, defaultdict=object,
```
L11  ⚪  (score=0)
```python
               closing=object, partial=object, wraps=object,
```
L12  ⚪  (score=0)
```python
               zlib_compress=object, bz2_compress=object, lzma_compress=object, zstd_compress=object)
```
L13  ⚪  (score=0)
```python
```
L14  ⚪  (score=0)
```python
import hashlib
```
L15  ⚪  (score=0)
```python
import operator
```
L16  ⚪  (score=0)
```python
import os
```
L17  ⚪  (score=0)
```python
import re
```
L18  ⚪  (score=0)
```python
import shutil
```
L19  ⚪  (score=0)
```python
import textwrap
```
L20  ⚪  (score=0)
```python
from dataclasses import dataclass
```
L21  ⚪  (score=0)
```python
from string import Template
```
L22  ⚪  (score=0)
```python
from functools import partial, wraps
```
L23  ⚪  (score=0)
```python
from contextlib import closing, contextmanager
```
L24  ⚪  (score=0)
```python
from collections import defaultdict
```
L25  ⚪  (score=0)
```python
```
L26  ⚪  (score=0)
```python
from . import Naming
```
L27  ⚪  (score=0)
```python
from . import Options, Directives
```
L28  ⚪  (score=0)
```python
from . import DebugFlags
```
L29  ⚪  (score=0)
```python
from . import StringEncoding
```
L30  ⚪  (score=0)
```python
from .. import Utils
```
L31  ⚪  (score=0)
```python
from .Scanning import SourceDescriptor
```
L32  ⚪  (score=0)
```python
from ..StringIOTree import StringIOTree
```
L33  ⚪  (score=0)
```python
```
L34  ⚪  (score=0)
```python
```
L35  ⚪  (score=0)
```python
# Set up available compression algorithms for maximum compression.
```
L36  ⚪  (score=0)
```python
from zlib import compress as zlib_compress
```
L37  ⚪  (score=0)
```python
try:
```
L38  ⚪  (score=0)
```python
    from bz2 import compress as bz2_compress
```
L39  ⚪  (score=0)
```python
except ImportError:
```
L40  ⚪  (score=0)
```python
    bz2_compress = None
```
L41  ⚪  (score=0)
```python
else:
```
L42  ⚪  (score=0)
```python
    bz2_compress = partial(bz2_compress, compresslevel=9)
```
L43  ⚪  (score=0)
```python
#try:
```
L44  ⚪  (score=0)
```python
#    from lzma import compress as lzma_compress
```
L45  ⚪  (score=0)
```python
#except ImportError:
```
L46  ⚪  (score=0)
```python
#    lzma_compress = None
```
L47  ⚪  (score=0)
```python
try:
```
L48  ⚪  (score=0)
```python
    from compression.zstd import (
```
L49  ⚪  (score=0)
```python
        compress as zstd_compress,
```
L50  ⚪  (score=0)
```python
        CompressionParameter as zstd_CompressionParameter,
```
L51  ⚪  (score=0)
```python
        Strategy as zstd_Strategy,
```
L52  ⚪  (score=0)
```python
    )
```
L53  ⚪  (score=0)
```python
except ImportError:
```
L54  ⚪  (score=0)
```python
    zstd_compress = None
```
L55  ⚪  (score=0)
```python
else:
```
L56  ⚪  (score=0)
```python
    zstd_compress = partial(zstd_compress, options={
```
L57  ⚪  (score=0)
```python
        zstd_CompressionParameter.strategy: zstd_Strategy.btultra2,
```
L58  ⚪  (score=0)
```python
        zstd_CompressionParameter.compression_level: zstd_CompressionParameter.compression_level.bounds()[1],
```
L59  ⚪  (score=0)
```python
    })
```
L60  ⚪  (score=0)
```python
    del zstd_CompressionParameter
```
L61  ⚪  (score=0)
```python
    del zstd_Strategy
```
L62  ⚪  (score=0)
```python
```
L63  ⚪  (score=0)
```python
compression_algorithms = [
```
L64  ⚪  (score=0)
```python
    # Note: order is important and defines values for "CYTHON_COMPRESS_STRINGS" !
```
L65  ⚪  (score=0)
```python
    (1, 'zlib', partial(zlib_compress, level=9)),
```
L66  ⚪  (score=0)
```python
    (2, 'bz2', bz2_compress),
```
L67  ⚪  (score=0)
```python
    (3, 'zstd', zstd_compress),
```
L68  ⚪  (score=0)
```python
    # LZMA is difficult to configure for efficient output from C code
```
L69  ⚪  (score=0)
```python
    # and the default output tends to be quite large.
```
L70  ⚪  (score=0)
```python
    #(4, 'lzma', lzma_compress),
```
L71  ⚪  (score=0)
```python
]
```
L72  ⚪  (score=0)
```python
```
L73  ⚪  (score=0)
```python
```
L74  ⚪  (score=0)
```python
renamed_py2_builtins_map = {
```
L75  ⚪  (score=0)
```python
    # builtins that had different names in Py2 code
```
L76  ⚪  (score=0)
```python
    'unicode'    : 'str',
```
L77  ⚪  (score=0)
```python
    'basestring' : 'str',
```
L78  ⚪  (score=0)
```python
    'xrange'     : 'range',
```
L79  ⚪  (score=0)
```python
    'raw_input'  : 'input',
```
L80  ⚪  (score=0)
```python
}
```
L81  ⚪  (score=0)
```python
```
L82  ⚪  (score=0)
```python
ctypedef_builtins_map = {
```
L83  ⚪  (score=0)
```python
    # types of builtins in "ctypedef class" statements which we don't
```
L84  ⚪  (score=0)
```python
    # import either because the names conflict with C types or because
```
L85  ⚪  (score=0)
```python
    # the type simply is not exposed.
```
L86  ⚪  (score=0)
```python
    'py_int'             : '&PyLong_Type',
```
L87  ⚪  (score=0)
```python
    'py_long'            : '&PyLong_Type',
```
L88  ⚪  (score=0)
```python
    'py_float'           : '&PyFloat_Type',
```
L89  ⚪  (score=0)
```python
    'wrapper_descriptor' : '&PyWrapperDescr_Type',
```
L90  ⚪  (score=0)
```python
}
```
L91  ⚪  (score=0)
```python
```
L92  ⚪  (score=0)
```python
basicsize_builtins_map = {
```
L93  ⚪  (score=0)
```python
    # builtins whose type has a different tp_basicsize than sizeof(...)
```
L94  ⚪  (score=0)
```python
    'PyTypeObject': 'PyHeapTypeObject',
```
L95  ⚪  (score=0)
```python
}
```
L96  ⚪  (score=0)
```python
```
L97  ⚪  (score=0)
```python
# Builtins as of Python version ...
```
L98  ⚪  (score=0)
```python
KNOWN_PYTHON_BUILTINS_VERSION = (3, 14, 0, 'beta', 1)
```
L99  ⚪  (score=0)
```python
KNOWN_PYTHON_BUILTINS = frozenset([
```
L100  ⚪  (score=0)
```python
    'ArithmeticError',
```
L101  ⚪  (score=0)
```python
    'AssertionError',
```
L102  ⚪  (score=0)
```python
    'AttributeError',
```
L103  ⚪  (score=0)
```python
    'BaseException',
```
L104  ⚪  (score=0)
```python
    'BaseExceptionGroup',
```
L105  ⚪  (score=0)
```python
    'BlockingIOError',
```
L106  ⚪  (score=0)
```python
    'BrokenPipeError',
```
L107  ⚪  (score=0)
```python
    'BufferError',
```
L108  ⚪  (score=0)
```python
    'BytesWarning',
```
L109  ⚪  (score=0)
```python
    'ChildProcessError',
```
L110  ⚪  (score=0)
```python
    'ConnectionAbortedError',
```
L111  ⚪  (score=0)
```python
    'ConnectionError',
```
L112  ⚪  (score=0)
```python
    'ConnectionRefusedError',
```
L113  ⚪  (score=0)
```python
    'ConnectionResetError',
```
L114  ⚪  (score=0)
```python
    'DeprecationWarning',
```
L115  ⚪  (score=0)
```python
    'EOFError',
```
L116  ⚪  (score=0)
```python
    'Ellipsis',
```
L117  ⚪  (score=0)
```python
    'EncodingWarning',
```
L118  ⚪  (score=0)
```python
    'EnvironmentError',
```
L119  ⚪  (score=0)
```python
    'Exception',
```
L120  ⚪  (score=0)
```python
    'ExceptionGroup',
```
L121  ⚪  (score=0)
```python
    'False',
```
L122  ⚪  (score=0)
```python
    'FileExistsError',
```
L123  ⚪  (score=0)
```python
    'FileNotFoundError',
```
L124  ⚪  (score=0)
```python
    'FloatingPointError',
```
L125  ⚪  (score=0)
```python
    'FutureWarning',
```
L126  ⚪  (score=0)
```python
    'GeneratorExit',
```
L127  ⚪  (score=0)
```python
    'IOError',
```
L128  ⚪  (score=0)
```python
    'ImportError',
```
L129  ⚪  (score=0)
```python
    'ImportWarning',
```
L130  ⚪  (score=0)
```python
    'IndentationError',
```
L131  ⚪  (score=0)
```python
    'IndexError',
```
L132  ⚪  (score=0)
```python
    'InterruptedError',
```
L133  ⚪  (score=0)
```python
    'IsADirectoryError',
```
L134  ⚪  (score=0)
```python
    'KeyError',
```
L135  ⚪  (score=0)
```python
    'KeyboardInterrupt',
```
L136  ⚪  (score=0)
```python
    'LookupError',
```
L137  ⚪  (score=0)
```python
    'MemoryError',
```
L138  ⚪  (score=0)
```python
    'ModuleNotFoundError',
```
L139  ⚪  (score=0)
```python
    'NameError',
```
L140  ⚪  (score=0)
```python
    'None',
```
L141  ⚪  (score=0)
```python
    'NotADirectoryError',
```
L142  ⚪  (score=0)
```python
    'NotImplemented',
```
L143  ⚪  (score=0)
```python
    'NotImplementedError',
```
L144  ⚪  (score=0)
```python
    'OSError',
```
L145  ⚪  (score=0)
```python
    'OverflowError',
```
L146  ⚪  (score=0)
```python
    'PendingDeprecationWarning',
```
L147  ⚪  (score=0)
```python
    'PermissionError',
```
L148  ⚪  (score=0)
```python
    'ProcessLookupError',
```
L149  ⚪  (score=0)
```python
    'PythonFinalizationError',
```
L150  ⚪  (score=0)
```python
    'RecursionError',
```
L151  ⚪  (score=0)
```python
    'ReferenceError',
```
L152  ⚪  (score=0)
```python
    'ResourceWarning',
```
L153  ⚪  (score=0)
```python
    'RuntimeError',
```
L154  ⚪  (score=0)
```python
    'RuntimeWarning',
```
L155  ⚪  (score=0)
```python
    'StopAsyncIteration',
```
L156  ⚪  (score=0)
```python
    'StopIteration',
```
L157  ⚪  (score=0)
```python
    'SyntaxError',
```
L158  ⚪  (score=0)
```python
    'SyntaxWarning',
```
L159  ⚪  (score=0)
```python
    'SystemError',
```
L160  ⚪  (score=0)
```python
    'SystemExit',
```
L161  ⚪  (score=0)
```python
    'TabError',
```
L162  ⚪  (score=0)
```python
    'TimeoutError',
```
L163  ⚪  (score=0)
```python
    'True',
```
L164  ⚪  (score=0)
```python
    'TypeError',
```
L165  ⚪  (score=0)
```python
    'UnboundLocalError',
```
L166  ⚪  (score=0)
```python
    'UnicodeDecodeError',
```
L167  ⚪  (score=0)
```python
    'UnicodeEncodeError',
```
L168  ⚪  (score=0)
```python
    'UnicodeError',
```
L169  ⚪  (score=0)
```python
    'UnicodeTranslateError',
```
L170  ⚪  (score=0)
```python
    'UnicodeWarning',
```
L171  ⚪  (score=0)
```python
    'UserWarning',
```
L172  ⚪  (score=0)
```python
    'ValueError',
```
L173  ⚪  (score=0)
```python
    'Warning',
```
L174  ⚪  (score=0)
```python
    'WindowsError',
```
L175  ⚪  (score=0)
```python
    'ZeroDivisionError',
```
L176  ⚪  (score=0)
```python
    '_IncompleteInputError',
```
L177  ⚪  (score=0)
```python
    '__build_class__',
```
L178  ⚪  (score=0)
```python
    '__debug__',
```
L179  ⚪  (score=0)
```python
    '__import__',
```
L180  ⚪  (score=0)
```python
    'abs',
```
L181  ⚪  (score=0)
```python
    'aiter',
```
L182  ⚪  (score=0)
```python
    'all',
```
L183  ⚪  (score=0)
```python
    'anext',
```
L184  ⚪  (score=0)
```python
    'any',
```
L185  ⚪  (score=0)
```python
    'ascii',
```
L186  ⚪  (score=0)
```python
    'bin',
```
L187  ⚪  (score=0)
```python
    'bool',
```
L188  ⚪  (score=0)
```python
    'breakpoint',
```
L189  ⚪  (score=0)
```python
    'bytearray',
```
L190  ⚪  (score=0)
```python
    'bytes',
```
L191  ⚪  (score=0)
```python
    'callable',
```
L192  ⚪  (score=0)
```python
    'chr',
```
L193  ⚪  (score=0)
```python
    'classmethod',
```
L194  ⚪  (score=0)
```python
    'compile',
```
L195  ⚪  (score=0)
```python
    'complex',
```
L196  ⚪  (score=0)
```python
    'copyright',
```
L197  ⚪  (score=0)
```python
    'credits',
```
L198  ⚪  (score=0)
```python
    'delattr',
```
L199  ⚪  (score=0)
```python
    'dict',
```
L200  ⚪  (score=0)
```python
    'dir',
```
L201  ⚪  (score=0)
```python
    'divmod',
```
L202  ⚪  (score=0)
```python
    'enumerate',
```
L203  ⚪  (score=0)
```python
    'eval',
```
L204  ⚪  (score=0)
```python
    'exec',
```
L205  ⚪  (score=0)
```python
    'exit',
```
L206  ⚪  (score=0)
```python
    'filter',
```
L207  ⚪  (score=0)
```python
    'float',
```
L208  ⚪  (score=0)
```python
    'format',
```
L209  ⚪  (score=0)
```python
    'frozenset',
```
L210  ⚪  (score=0)
```python
    'getattr',
```
L211  ⚪  (score=0)
```python
    'globals',
```
L212  ⚪  (score=0)
```python
    'hasattr',
```
L213  ⚪  (score=0)
```python
    'hash',
```
L214  ⚪  (score=0)
```python
    'help',
```
L215  ⚪  (score=0)
```python
    'hex',
```
L216  ⚪  (score=0)
```python
    'id',
```
L217  ⚪  (score=0)
```python
    'input',
```
L218  ⚪  (score=0)
```python
    'int',
```
L219  ⚪  (score=0)
```python
    'isinstance',
```
L220  ⚪  (score=0)
```python
    'issubclass',
```
L221  ⚪  (score=0)
```python
    'iter',
```
L222  ⚪  (score=0)
```python
    'len',
```
L223  ⚪  (score=0)
```python
    'license',
```
L224  ⚪  (score=0)
```python
    'list',
```
L225  ⚪  (score=0)
```python
    'locals',
```
L226  ⚪  (score=0)
```python
    'map',
```
L227  ⚪  (score=0)
```python
    'max',
```
L228  ⚪  (score=0)
```python
    'memoryview',
```
L229  ⚪  (score=0)
```python
    'min',
```
L230  ⚪  (score=0)
```python
    'next',
```
L231  ⚪  (score=0)
```python
    'object',
```
L232  ⚪  (score=0)
```python
    'oct',
```
L233  ⚪  (score=0)
```python
    'open',
```
L234  ⚪  (score=0)
```python
    'ord',
```
L235  ⚪  (score=0)
```python
    'pow',
```
L236  ⚪  (score=0)
```python
    'print',
```
L237  ⚪  (score=0)
```python
    'property',
```
L238  ⚪  (score=0)
```python
    'quit',
```
L239  ⚪  (score=0)
```python
    'range',
```
L240  ⚪  (score=0)
```python
    'repr',
```
L241  ⚪  (score=0)
```python
    'reversed',
```
L242  ⚪  (score=0)
```python
    'round',
```
L243  ⚪  (score=0)
```python
    'set',
```
L244  ⚪  (score=0)
```python
    'setattr',
```
L245  ⚪  (score=0)
```python
    'slice',
```
L246  ⚪  (score=0)
```python
    'sorted',
```
L247  ⚪  (score=0)
```python
    'staticmethod',
```
L248  ⚪  (score=0)
```python
    'str',
```
L249  ⚪  (score=0)
```python
    'sum',
```
L250  ⚪  (score=0)
```python
    'super',
```
L251  ⚪  (score=0)
```python
    'tuple',
```
L252  ⚪  (score=0)
```python
    'type',
```
L253  ⚪  (score=0)
```python
    'vars',
```
L254  ⚪  (score=0)
```python
    'zip',
```
L255  ⚪  (score=0)
```python
])
```
L256  ⚪  (score=0)
```python
```
L257  ⚪  (score=0)
```python
uncachable_builtins = [
```
L258  ⚪  (score=0)
```python
    # Global/builtin names that cannot be cached because they may or may not
```
L259  ⚪  (score=0)
```python
    # be available at import time, for various reasons:
```
L260  ⚪  (score=0)
```python
    ## Python 3.13+
```
L261  ⚪  (score=0)
```python
    '_IncompleteInputError',
```
L262  ⚪  (score=0)
```python
    'PythonFinalizationError',
```
L263  ⚪  (score=0)
```python
    ## Python 3.11+
```
L264  ⚪  (score=0)
```python
    'BaseExceptionGroup',
```
L265  ⚪  (score=0)
```python
    'ExceptionGroup',
```
L266  ⚪  (score=0)
```python
    ## - Py3.10+
```
L267  ⚪  (score=0)
```python
    'aiter',
```
L268  ⚪  (score=0)
```python
    'anext',
```
L269  ⚪  (score=0)
```python
    'EncodingWarning',
```
L270  ⚪  (score=0)
```python
    ## - Py3.7+
```
L271  ⚪  (score=0)
```python
    'breakpoint',  # might deserve an implementation in Cython
```
L272  ⚪  (score=0)
```python
    ## - platform specific
```
L273  ⚪  (score=0)
```python
    'WindowsError',
```
L274  ⚪  (score=0)
```python
    ## - others
```
L275  ⚪  (score=0)
```python
    '_',  # e.g. used by gettext
```
L276  ⚪  (score=0)
```python
]
```
L277  ⚪  (score=0)
```python
```
L278  ⚪  (score=0)
```python
special_py_methods = cython.declare(frozenset, frozenset((
```
L279  ⚪  (score=0)
```python
    '__cinit__', '__dealloc__', '__richcmp__', '__next__',
```
L280  ⚪  (score=0)
```python
    '__await__', '__aiter__', '__anext__',
```
L281  ⚪  (score=0)
```python
    '__getbuffer__', '__releasebuffer__',
```
L282  ⚪  (score=0)
```python
)))
```
L283  ⚪  (score=0)
```python
```
L284  ⚪  (score=0)
```python
modifier_output_mapper = {
```
L285  ⚪  (score=0)
```python
    'inline': 'CYTHON_INLINE'
```
L286  ⚪  (score=0)
```python
}.get
```
L287  ⚪  (score=0)
```python
```
L288  ⚪  (score=0)
```python
cleanup_level_for_type_prefix = cython.declare(object, {
```
L289  ⚪  (score=0)
```python
    'ustring': None,
```
L290  ⚪  (score=0)
```python
    'tuple': 2,
```
L291  ⚪  (score=0)
```python
    'slice': 2,
```
L292  ⚪  (score=0)
```python
}.get)
```
L293  ⚪  (score=0)
```python
```
L294  ⚪  (score=0)
```python
```
L295  ⚪  (score=0)
```python
class IncludeCode:
```
L296  ⚪  (score=0)
```python
    """
```
L297  ⚪  (score=0)
```python
    An include file and/or verbatim C code to be included in the
```
L298  ⚪  (score=0)
```python
    generated sources.
```
L299  ⚪  (score=0)
```python
    """
```
L300  ⚪  (score=0)
```python
    # attributes:
```
L301  ⚪  (score=0)
```python
    #
```
L302  ⚪  (score=0)
```python
    #  pieces    {order: unicode}: pieces of C code to be generated.
```
L303  ⚪  (score=0)
```python
    #            For the included file, the key "order" is zero.
```
L304  ⚪  (score=0)
```python
    #            For verbatim include code, the "order" is the "order"
```
L305  ⚪  (score=0)
```python
    #            attribute of the original IncludeCode where this piece
```
L306  ⚪  (score=0)
```python
    #            of C code was first added. This is needed to prevent
```
L307  ⚪  (score=0)
```python
    #            duplication if the same include code is found through
```
L308  ⚪  (score=0)
```python
    #            multiple cimports.
```
L309  ⚪  (score=0)
```python
    #  location  int: where to put this include in the C sources, one
```
L310  ⚪  (score=0)
```python
    #            of the constants INITIAL, EARLY, LATE
```
L311  ⚪  (score=0)
```python
    #  order     int: sorting order (automatically set by increasing counter)
```
L312  ⚪  (score=0)
```python
```
L313  ⚪  (score=0)
```python
    # Constants for location. If the same include occurs with different
```
L314  ⚪  (score=0)
```python
    # locations, the earliest one takes precedence.
```
L315  ⚪  (score=0)
```python
    INITIAL = 0
```
L316  ⚪  (score=0)
```python
    EARLY = 1
```
L317  ⚪  (score=0)
```python
    LATE = 2
```
L318  ⚪  (score=0)
```python
```
L319  ⚪  (score=0)
```python
    counter = 1   # Counter for "order"
```
L320  ⚪  (score=0)
```python
```
L321  ⚪  (score=0)
```python
    def __init__(self, include=None, verbatim=None, late=True, initial=False):
```
L322  ⚪  (score=0)
```python
        self.order = self.counter
```
L323  ⚪  (score=0)
```python
        type(self).counter += 1
```
L324  ⚪  (score=0)
```python
        self.pieces = {}
```
L325  ⚪  (score=0)
```python
```
L326  ⚪  (score=0)
```python
        if include:
```
L327  ⚪  (score=0)
```python
            if include[0] == '<' and include[-1] == '>':
```
L328  ⚪  (score=0)
```python
                self.pieces[0] = '#include {}'.format(include)
```
L329  ⚪  (score=0)
```python
                late = False  # system include is never late
```
L330  ⚪  (score=0)
```python
            else:
```
L331  ⚪  (score=0)
```python
                self.pieces[0] = '#include "{}"'.format(include)
```
L332  ⚪  (score=0)
```python
```
L333  ⚪  (score=0)
```python
        if verbatim:
```
L334  ⚪  (score=0)
```python
            self.pieces[self.order] = verbatim
```
L335  ⚪  (score=0)
```python
```
L336  ⚪  (score=0)
```python
        if initial:
```
L337  ⚪  (score=0)
```python
            self.location = self.INITIAL
```
L338  ⚪  (score=0)
```python
        elif late:
```
L339  ⚪  (score=0)
```python
            self.location = self.LATE
```
L340  ⚪  (score=0)
```python
        else:
```
L341  ⚪  (score=0)
```python
            self.location = self.EARLY
```
L342  ⚪  (score=0)
```python
```
L343  ⚪  (score=0)
```python
    def dict_update(self, d, key):
```
L344  ⚪  (score=0)
```python
        """
```
L345  ⚪  (score=0)
```python
        Insert `self` in dict `d` with key `key`. If that key already
```
L346  ⚪  (score=0)
```python
        exists, update the attributes of the existing value with `self`.
```
L347  ⚪  (score=0)
```python
        """
```
L348  ⚪  (score=0)
```python
        if key in d:
```
L349  ⚪  (score=0)
```python
            other = d[key]
```
L350  ⚪  (score=0)
```python
            other.location = min(self.location, other.location)
```
L351  ⚪  (score=0)
```python
            other.pieces.update(self.pieces)
```
L352  ⚪  (score=0)
```python
        else:
```
L353  ⚪  (score=0)
```python
            d[key] = self
```
L354  ⚪  (score=0)
```python
```
L355  ⚪  (score=0)
```python
    def sortkey(self):
```
L356  ⚪  (score=0)
```python
        return self.order
```
L357  ⚪  (score=0)
```python
```
L358  ⚪  (score=0)
```python
    def mainpiece(self):
```
L359  ⚪  (score=0)
```python
        """
```
L360  ⚪  (score=0)
```python
        Return the main piece of C code, corresponding to the include
```
L361  ⚪  (score=0)
```python
        file. If there was no include file, return None.
```
L362  ⚪  (score=0)
```python
        """
```
L363  ⚪  (score=0)
```python
        return self.pieces.get(0)
```
L364  ⚪  (score=0)
```python
```
L365  ⚪  (score=0)
```python
    def write(self, code):
```
L366  ⚪  (score=0)
```python
        # Write values of self.pieces dict, sorted by the keys
```
L367  ⚪  (score=0)
```python
        for k in sorted(self.pieces):
```
L368  ⚪  (score=0)
```python
            code.putln(self.pieces[k])
```
L369  ⚪  (score=0)
```python
```
L370  ⚪  (score=0)
```python
```
L371  ⚪  (score=0)
```python
def get_utility_dir():
```
L372  ⚪  (score=0)
```python
    # make this a function and not global variables:
```
L373  ⚪  (score=0)
```python
    # http://trac.cython.org/cython_trac/ticket/475
```
L374  ⚪  (score=0)
```python
    Cython_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
```
L375  ⚪  (score=0)
```python
    return os.path.join(Cython_dir, "Utility")
```
L376  ⚪  (score=0)
```python
```
L377  ⚪  (score=0)
```python
read_utilities_hook = None
```
L378  ⚪  (score=0)
```python
"""
```
L379  ⚪  (score=0)
```python
Override the hook for reading a utilities file that contains code fragments used
```
L380  ⚪  (score=0)
```python
by the codegen.
```
L381  ⚪  (score=0)
```python
```
L382  ⚪  (score=0)
```python
The hook functions takes the path of the utilities file, and returns a list
```
L383  ⚪  (score=0)
```python
of strings, one per line.
```
L384  ⚪  (score=0)
```python
```
L385  ⚪  (score=0)
```python
The default behavior is to open a file relative to get_utility_dir().
```
L386  ⚪  (score=0)
```python
"""
```
L387  ⚪  (score=0)
```python
```
L388  ⚪  (score=0)
```python
def read_utilities_from_utility_dir(path):
```
L389  ⚪  (score=0)
```python
    """
```
L390  ⚪  (score=0)
```python
    Read all lines of the file at the provided path from a path relative
```
L391  ⚪  (score=0)
```python
    to get_utility_dir().
```
L392  ⚪  (score=0)
```python
    """
```
L393  ⚪  (score=0)
```python
    filename = os.path.join(get_utility_dir(), path)
```
L394  ⚪  (score=0)
```python
    with closing(Utils.open_source_file(filename, encoding='UTF-8')) as f:
```
L395  ⚪  (score=0)
```python
        return f.readlines()
```
L396  ⚪  (score=0)
```python
```
L397  ⚪  (score=0)
```python
# by default, read utilities from the utility directory.
```
L398  ⚪  (score=0)
```python
read_utilities_hook = read_utilities_from_utility_dir
```
L399  ⚪  (score=0)
```python
```
L400  ⚪  (score=0)
```python
```
L401  ⚪  (score=0)
```python
class AbstractUtilityCode:
```
L402  ⚪  (score=0)
```python
```
L403  ⚪  (score=0)
```python
    requires = None
```
L404  ⚪  (score=0)
```python
```
L405  ⚪  (score=0)
```python
    def put_code(self, globalstate:"GlobalState", used_by=None) -> None:
```
L406  ⚪  (score=0)
```python
        pass
```
L407  ⚪  (score=0)
```python
```
L408  ⚪  (score=0)
```python
    def get_tree(self, **kwargs):
```
L409  ⚪  (score=0)
```python
        return None
```
L410  ⚪  (score=0)
```python
```
L411  ⚪  (score=0)
```python
    def get_shared_library_scope(self, **kwargs):
```
L412  ⚪  (score=0)
```python
        return None
```
L413  ⚪  (score=0)
```python
```
L414  ⚪  (score=0)
```python
```
L415  ⚪  (score=0)
```python
class UtilityCodeBase(AbstractUtilityCode):
```
L416  ⚪  (score=0)
```python
    """
```
L417  ⚪  (score=0)
```python
    Support for loading utility code from a file.
```
L418  ⚪  (score=0)
```python
```
L419  ⚪  (score=0)
```python
    Code sections in the file can be specified as follows:
```
L420  ⚪  (score=0)
```python
```
L421  ⚪  (score=0)
```python
        ##### MyUtility.proto #####
```
L422  ⚪  (score=0)
```python
```
L423  ⚪  (score=0)
```python
        [proto declarations]
```
L424  ⚪  (score=0)
```python
```
L425  ⚪  (score=0)
```python
        ##### MyUtility.init #####
```
L426  ⚪  (score=0)
```python
```
L427  ⚪  (score=0)
```python
        [code run at module initialization]
```
L428  ⚪  (score=0)
```python
```
L429  ⚪  (score=0)
```python
        ##### MyUtility #####
```
L430  ⚪  (score=0)
```python
        #@requires: MyOtherUtility
```
L431  ⚪  (score=0)
```python
        #@substitute: naming
```
L432  ⚪  (score=0)
```python
```
L433  ⚪  (score=0)
```python
        [definitions]
```
L434  ⚪  (score=0)
```python
```
L435  ⚪  (score=0)
```python
        ##### MyUtility #####
```
L436  ⚪  (score=0)
```python
        #@substitute: tempita
```
L437  ⚪  (score=0)
```python
```
L438  ⚪  (score=0)
```python
        [requires tempita substitution
```
L439  ⚪  (score=0)
```python
         - context can't be specified here though so only
```
L440  ⚪  (score=0)
```python
           tempita utility that requires no external context
```
L441  ⚪  (score=0)
```python
           will benefit from this tag
```
L442  ⚪  (score=0)
```python
         - only necessary when @required from non-tempita code]
```
L443  ⚪  (score=0)
```python
```
L444  ⚪  (score=0)
```python
    for prototypes and implementation respectively.  For non-python or
```
L445  ⚪  (score=0)
```python
    -cython files backslashes should be used instead.  5 to 30 comment
```
L446  ⚪  (score=0)
```python
    characters may be used on either side.
```
L447  ⚪  (score=0)
```python
```
L448  ⚪  (score=0)
```python
    If the @cname decorator is not used and this is a CythonUtilityCode,
```
L449  ⚪  (score=0)
```python
    one should pass in the 'name' keyword argument to be used for name
```
L450  ⚪  (score=0)
```python
    mangling of such entries.
```
L451  ⚪  (score=0)
```python
    """
```
L452  ⚪  (score=0)
```python
```
L453  ⚪  (score=0)
```python
    is_cython_utility = False
```
L454  ⚪  (score=0)
```python
    _utility_cache = {}
```
L455  ⚪  (score=0)
```python
```
L456  ⚪  (score=0)
```python
    match_section_title = re.compile(
```
L457  ⚪  (score=0)
```python
        r'(.+)[.](proto(?:[.]\S+)?|impl|init|cleanup|module_state_decls|module_state_traverse|module_state_clear|export)$'
```
L458  ⚪  (score=0)
```python
    ).match
```
L459  ⚪  (score=0)
```python
```
L460  ⚪  (score=0)
```python
    @staticmethod
```
L461  ⚪  (score=0)
```python
    def get_special_comment_matcher(line_comment_char):
```
L462  ⚪  (score=0)
```python
        return re.compile((
```
L463  ⚪  (score=0)
```python
            # section title
```
L464  ⚪  (score=0)
```python
            r'^%(C)s{5,30}  \s*  (?P<name> (?:\w|\.)+ )  \s*  %(C)s{5,30} |'
```
L465  ⚪  (score=0)
```python
            # section tags and dependencies
```
L466  ⚪  (score=0)
```python
            r'^%(C)s+  @(?P<tag> .+)'
```
L467  ⚪  (score=0)
```python
        ) % {'C': re.escape(line_comment_char)}, re.VERBOSE).match
```
L468  ⚪  (score=0)
```python
```
L469  ⚪  (score=0)
```python
    @classmethod
```
L470  ⚪  (score=0)
```python
    def _add_utility(cls, utility, name, type, lines, begin_lineno, tags=None):
```
L471  ⚪  (score=0)
```python
        if utility is None:
```
L472  ⚪  (score=0)
```python
            return
```
L473  ⚪  (score=0)
```python
```
L474  ⚪  (score=0)
```python
        code = '\n'.join(lines)
```
L475  ⚪  (score=0)
```python
        if tags and 'substitute' in tags and 'naming' in tags['substitute']:
```
L476  ⚪  (score=0)
```python
            try:
```
L477  ⚪  (score=0)
```python
                new_code = Template(code).substitute(vars(Naming))
```
L478  ⚪  (score=0)
```python
            except (KeyError, ValueError) as e:
```
L479  ⚪  (score=0)
```python
                raise RuntimeError(
```
L480  ⚪  (score=0)
```python
                    f"Error parsing templated utility code '{name}.{type}' at line {begin_lineno:d}: {e}")
```
L481  ⚪  (score=0)
```python
            if new_code == code:
```
L482  ⚪  (score=0)
```python
                raise RuntimeError(
```
L483  ⚪  (score=0)
```python
                    f"Found useless 'substitute: naming' declaration without replacements. ({name}.{type}:{begin_lineno:d})")
```
L484  ⚪  (score=0)
```python
            code = new_code
```
L485  ⚪  (score=0)
```python
```
L486  ⚪  (score=0)
```python
        # remember correct line numbers at least until after templating
```
L487  ⚪  (score=0)
```python
        code = '\n' * begin_lineno + code
```
L488  ⚪  (score=0)
```python
```
L489  ⚪  (score=0)
```python
        if type == 'proto':
```
L490  ⚪  (score=0)
```python
            utility[0] = code
```
L491  ⚪  (score=0)
```python
        elif type == 'impl':
```
L492  ⚪  (score=0)
```python
            utility[1] = code
```
L493  ⚪  (score=0)
```python
        else:
```
L494  ⚪  (score=0)
```python
            all_tags = utility[2]
```
L495  ⚪  (score=0)
```python
            all_tags[type] = code
```
L496  ⚪  (score=0)
```python
```
L497  ⚪  (score=0)
```python
        if tags:
```
L498  ⚪  (score=0)
```python
            all_tags = utility[2]
```
L499  ⚪  (score=0)
```python
            for tag_name, tag_values in tags.items():
```
L500  ⚪  (score=0)
```python
                all_tags.setdefault(tag_name, set()).update(tag_values)
```
L501  ⚪  (score=0)
```python
```
L502  ⚪  (score=0)
```python
    @classmethod
```
L503  ⚪  (score=0)
```python
    def load_utilities_from_file(cls, path):
```
L504  ⚪  (score=0)
```python
        utilities = cls._utility_cache.get(path)
```
L505  ⚪  (score=0)
```python
        if utilities:
```
L506  ⚪  (score=0)
```python
            return utilities
```
L507  ⚪  (score=0)
```python
```
L508  ⚪  (score=0)
```python
        _, ext = os.path.splitext(path)
```
L509  ⚪  (score=0)
```python
        if ext in ('.pyx', '.py', '.pxd', '.pxi'):
```
L510  ⚪  (score=0)
```python
            comment = '#'
```
L511  ⚪  (score=0)
```python
            strip_comments = partial(re.compile(r'^\s*#(?!\s*cython\s*:).*').sub, '')
```
L512  ⚪  (score=0)
```python
            rstrip = str.rstrip
```
L513  ⚪  (score=0)
```python
        else:
```
L514  ⚪  (score=0)
```python
            comment = '/'
```
L515  ⚪  (score=0)
```python
            strip_comments = partial(re.compile(r'^\s*//.*|/\*[^*]*\*/').sub, '')
```
L516  ⚪  (score=0)
```python
            rstrip = partial(re.compile(r'\s+(\\?)$').sub, r'\1')
```
L517  ⚪  (score=0)
```python
```
L518  ⚪  (score=0)
```python
        match_special = cls.get_special_comment_matcher(comment)
```
L519  ⚪  (score=0)
```python
        match_type = cls.match_section_title
```
L520  ⚪  (score=0)
```python
```
L521  ⚪  (score=0)
```python
        all_lines = read_utilities_hook(path)
```
L522  ⚪  (score=0)
```python
```
L523  ⚪  (score=0)
```python
        utilities = defaultdict(lambda: [None, None, {}])
```
L524  ⚪  (score=0)
```python
        lines = []
```
L525  ⚪  (score=0)
```python
        tags = defaultdict(set)
```
L526  ⚪  (score=0)
```python
        utility = name = type = None
```
L527  ⚪  (score=0)
```python
        begin_lineno = 0
```
L528  ⚪  (score=0)
```python
```
L529  ⚪  (score=0)
```python
        for lineno, line in enumerate(all_lines):
```
L530  ⚪  (score=0)
```python
            m = match_special(line)
```
L531  ⚪  (score=0)
```python
            if m is None:
```
L532  ⚪  (score=0)
```python
                lines.append(rstrip(strip_comments(line)))
```
L533  ⚪  (score=0)
```python
            elif m.group('name'):
```
L534  ⚪  (score=0)
```python
                cls._add_utility(utility, name, type, lines, begin_lineno, tags)
```
L535  ⚪  (score=0)
```python
```
L536  ⚪  (score=0)
```python
                begin_lineno = lineno + 1
```
L537  ⚪  (score=0)
```python
                del lines[:]
```
L538  ⚪  (score=0)
```python
                tags.clear()
```
L539  ⚪  (score=0)
```python
```
L540  ⚪  (score=0)
```python
                name = m.group('name')
```
L541  ⚪  (score=0)
```python
                mtype = match_type(name)
```
L542  ⚪  (score=0)
```python
                if mtype:
```
L543  ⚪  (score=0)
```python
                    name, type = mtype.groups()
```
L544  ⚪  (score=0)
```python
                else:
```
L545  ⚪  (score=0)
```python
                    type = 'impl'
```
L546  ⚪  (score=0)
```python
                utility = utilities[name]
```
L547  ⚪  (score=0)
```python
            else:
```
L548  ⚪  (score=0)
```python
                raw_tag = m.group('tag').strip()
```
L549  ⚪  (score=0)
```python
                if ':' in raw_tag:
```
L550  ⚪  (score=0)
```python
                    tag_name, _, tag_value = raw_tag.partition(':')
```
L551  ⚪  (score=0)
```python
                    tag_name = tag_name.rstrip()
```
L552  ⚪  (score=0)
```python
                    tag_value = tag_value.strip()
```
L553  ⚪  (score=0)
```python
                else:
```
L554  ⚪  (score=0)
```python
                    # Accept legacy/alternative syntax without colon: "@requires Foo"
```
L555  ⚪  (score=0)
```python
                    parts = raw_tag.split(None, 1)
```
L556  ⚪  (score=0)
```python
                    if len(parts) < 2:
```
L557  ⚪  (score=0)
```python
                        raise RuntimeError(f"Found invalid tag '{raw_tag}' in utility section {name}.{type}")
```
L558  ⚪  (score=0)
```python
                    tag_name, tag_value = parts[0], parts[1].strip()
```
L559  ⚪  (score=0)
```python
```
L560  ⚪  (score=0)
```python
                if tag_name not in ('requires', 'substitute', 'proto_block'):
```
L561  ⚪  (score=0)
```python
                    raise RuntimeError(f"Found unknown tag name '{tag_name}' in utility section {name}.{type}")
```
L562  ⚪  (score=0)
```python
                if not re.match(r'\S+$', tag_value):
```
L563  ⚪  (score=0)
```python
                    raise RuntimeError(f"Found invalid tag value '{tag_value}' in utility section {name}.{type}")
```
L564  ⚪  (score=0)
```python
```
L565  ⚪  (score=0)
```python
                tags[tag_name].add(tag_value)
```
L566  ⚪  (score=0)
```python
                lines.append('')  # keep line number correct
```
L567  ⚪  (score=0)
```python
```
L568  ⚪  (score=0)
```python
        if utility is None:
```
L569  ⚪  (score=0)
```python
            raise ValueError("Empty utility code file")
```
L570  ⚪  (score=0)
```python
```
L571  ⚪  (score=0)
```python
        # Don't forget to add the last utility code
```
L572  ⚪  (score=0)
```python
        cls._add_utility(utility, name, type, lines, begin_lineno, tags)
```
L573  ⚪  (score=0)
```python
```
L574  ⚪  (score=0)
```python
        utilities = dict(utilities)  # un-defaultdict-ify
```
L575  ⚪  (score=0)
```python
        cls._utility_cache[path] = utilities
```
L576  ⚪  (score=0)
```python
        return utilities
```
L577  ⚪  (score=0)
```python
```
L578  ⚪  (score=0)
```python
    @classmethod
```
L579  ⚪  (score=0)
```python
    def load(cls, util_code_name, from_file, **kwargs):
```
L580  ⚪  (score=0)
```python
        """
```
L581  ⚪  (score=0)
```python
        Load utility code from a file specified by from_file (relative to
```
L582  ⚪  (score=0)
```python
        Cython/Utility) and name util_code_name.
```
L583  ⚪  (score=0)
```python
        """
```
L584  ⚪  (score=0)
```python
```
L585  ⚪  (score=0)
```python
        if '::' in util_code_name:
```
L586  ⚪  (score=0)
```python
            from_file, util_code_name = util_code_name.rsplit('::', 1)
```
L587  ⚪  (score=0)
```python
        assert from_file
```
L588  ⚪  (score=0)
```python
        utilities = cls.load_utilities_from_file(from_file)
```
L589  ⚪  (score=0)
```python
        proto, impl, tags = utilities[util_code_name]
```
L590  ⚪  (score=0)
```python
```
L591  ⚪  (score=0)
```python
        if tags:
```
L592  ⚪  (score=0)
```python
            if "substitute" in tags and "tempita" in tags["substitute"]:
```
L593  ⚪  (score=0)
```python
                if not issubclass(cls, TempitaUtilityCode):
```
L594  ⚪  (score=0)
```python
                    return TempitaUtilityCode.load(util_code_name, from_file, **kwargs)
```
L595  ⚪  (score=0)
```python
            orig_kwargs = kwargs.copy()
```
L596  ⚪  (score=0)
```python
            for name, values in tags.items():
```
L597  ⚪  (score=0)
```python
                if name in kwargs:
```
L598  ⚪  (score=0)
```python
                    continue
```
L599  ⚪  (score=0)
```python
                # only pass lists when we have to: most argument expect one value or None
```
L600  ⚪  (score=0)
```python
                if name == 'requires':
```
L601  ⚪  (score=0)
```python
                    if orig_kwargs:
```
L602  ⚪  (score=0)
```python
                        values = [cls.load(dep, from_file, **orig_kwargs)
```
L603  ⚪  (score=0)
```python
                                  for dep in sorted(values)]
```
L604  ⚪  (score=0)
```python
                    else:
```
L605  ⚪  (score=0)
```python
                        # dependencies are rarely unique, so use load_cached() when we can
```
L606  ⚪  (score=0)
```python
                        values = [cls.load_cached(dep, from_file)
```
L607  ⚪  (score=0)
```python
                                  for dep in sorted(values)]
```
L608  ⚪  (score=0)
```python
                elif name == 'substitute':
```
L609  ⚪  (score=0)
```python
                    # don't want to pass "naming" or "tempita" to the constructor
```
L610  ⚪  (score=0)
```python
                    # since these will have been handled
```
L611  ⚪  (score=0)
```python
                    values = values - {'naming', 'tempita'}
```
L612  ⚪  (score=0)
```python
                    if not values:
```
L613  ⚪  (score=0)
```python
                        continue
```
L614  ⚪  (score=0)
```python
                elif not values:
```
L615  ⚪  (score=0)
```python
                    values = None
```
L616  ⚪  (score=0)
```python
                elif len(values) == 1:
```
L617  ⚪  (score=0)
```python
                    values = list(values)[0]
```
L618  ⚪  (score=0)
```python
                kwargs[name] = values
```
L619  ⚪  (score=0)
```python
```
L620  ⚪  (score=0)
```python
        if proto is not None:
```
L621  ⚪  (score=0)
```python
            kwargs['proto'] = proto
```
L622  ⚪  (score=0)
```python
        if impl is not None:
```
L623  ⚪  (score=0)
```python
            kwargs['impl'] = impl
```
L624  ⚪  (score=0)
```python
```
L625  ⚪  (score=0)
```python
        if 'name' not in kwargs:
```
L626  ⚪  (score=0)
```python
            kwargs['name'] = util_code_name
```
L627  ⚪  (score=0)
```python
```
L628  ⚪  (score=0)
```python
        if 'file' not in kwargs and from_file:
```
L629  ⚪  (score=0)
```python
            kwargs['file'] = from_file
```
L630  ⚪  (score=0)
```python
        return cls(**kwargs)
```
L631  ⚪  (score=0)
```python
```
L632  ⚪  (score=0)
```python
    @classmethod
```
L633  ⚪  (score=0)
```python
    def load_cached(cls, utility_code_name, from_file, __cache={}):
```
L634  ⚪  (score=0)
```python
        """
```
L635  ⚪  (score=0)
```python
        Calls .load(), but using a per-type cache based on utility name and file name.
```
L636  ⚪  (score=0)
```python
        """
```
L637  ⚪  (score=0)
```python
        key = (utility_code_name, from_file, cls)
```
L638  ⚪  (score=0)
```python
        try:
```
L639  ⚪  (score=0)
```python
            return __cache[key]
```
L640  ⚪  (score=0)
```python
        except KeyError:
```
L641  ⚪  (score=0)
```python
            pass
```
L642  ⚪  (score=0)
```python
        code = __cache[key] = cls.load(utility_code_name, from_file)
```
L643  ⚪  (score=0)
```python
        return code
```
L644  ⚪  (score=0)
```python
```
L645  ⚪  (score=0)
```python
    @classmethod
```
L646  ⚪  (score=0)
```python
    def load_as_string(cls, util_code_name, from_file, include_requires=False, **kwargs):
```
L647  ⚪  (score=0)
```python
        """
```
L648  ⚪  (score=0)
```python
        Load a utility code as a string. Returns (proto, implementation).
```
L649  ⚪  (score=0)
```python
```
L650  ⚪  (score=0)
```python
        If 'include_requires=True', concatenates all requirements before the actually
```
L651  ⚪  (score=0)
```python
        requested utility code, separately for proto and impl part.
```
L652  ⚪  (score=0)
```python
```
L653  ⚪  (score=0)
```python
        In a lot of cases it may be better to use regular "load" and "CCodeWriter.put_code_here"
```
L654  ⚪  (score=0)
```python
        since that is able to apply the code transformations to the code too.
```
L655  ⚪  (score=0)
```python
        """
```
L656  ⚪  (score=0)
```python
        util = cls.load(util_code_name, from_file, **kwargs)
```
L657  ⚪  (score=0)
```python
```
L658  ⚪  (score=0)
```python
        if not include_requires:
```
L659  ⚪  (score=0)
```python
            return (util.format_code(util.proto),
```
L660  ⚪  (score=0)
```python
                    util.format_code(util.impl))
```
L661  ⚪  (score=0)
```python
```
L662  ⚪  (score=0)
```python
        protos, impls = [], []
```
L663  ⚪  (score=0)
```python
        def prepend(util_code):
```
L664  ⚪  (score=0)
```python
            if util_code.requires:
```
L665  ⚪  (score=0)
```python
                for dep in util_code.requires:
```
L666  ⚪  (score=0)
```python
                    prepend(dep)
```
L667  ⚪  (score=0)
```python
            if util_code.proto:
```
L668  ⚪  (score=0)
```python
                protos.append(util_code.format_code(util_code.proto))
```
L669  ⚪  (score=0)
```python
            if util_code.impl:
```
L670  ⚪  (score=0)
```python
                impls.append(util_code.format_code(util_code.impl))
```
L671  ⚪  (score=0)
```python
```
L672  ⚪  (score=0)
```python
        prepend(util)
```
L673  ⚪  (score=0)
```python
        return "".join(protos), "".join(impls)
```
L674  ⚪  (score=0)
```python
```
L675  ⚪  (score=0)
```python
    def format_code(self, code_string, replace_empty_lines=re.compile(r'\n\n+').sub):
```
L676  ⚪  (score=0)
```python
        """
```
L677  ⚪  (score=0)
```python
        Format a code section for output.
```
L678  ⚪  (score=0)
```python
        """
```
L679  ⚪  (score=0)
```python
        if code_string:
```
L680  ⚪  (score=0)
```python
            code_string = replace_empty_lines('\n', code_string.strip()) + '\n\n'
```
L681  ⚪  (score=0)
```python
        return code_string
```
L682  ⚪  (score=0)
```python
```
L683  ⚪  (score=0)
```python
    def __repr__(self):
```
L684  ⚪  (score=0)
```python
        return "<%s(%s)>" % (type(self).__name__, self.name)
```
L685  ⚪  (score=0)
```python
```
L686  ⚪  (score=0)
```python
    def get_tree(self, **kwargs):
```
L687  ⚪  (score=0)
```python
        return None
```
L688  ⚪  (score=0)
```python
```
L689  ⚪  (score=0)
```python
    def get_shared_library_scope(self, **kwargs):
```
L690  ⚪  (score=0)
```python
        return None
```
L691  ⚪  (score=0)
```python
```
L692  ⚪  (score=0)
```python
    def __deepcopy__(self, memodict=None):
```
L693  ⚪  (score=0)
```python
        # No need to deep-copy utility code since it's essentially immutable.
```
L694  ⚪  (score=0)
```python
        return self
```
L695  ⚪  (score=0)
```python
```
L696  ⚪  (score=0)
```python
@dataclass
```
L697  ⚪  (score=0)
```python
class SharedFunctionDecl:
```
L698  ⚪  (score=0)
```python
    """Contains parsed declaration of shared utility function"""
```
L699  ⚪  (score=0)
```python
    name: str
```
L700  ⚪  (score=0)
```python
    ret: str
```
L701  ⚪  (score=0)
```python
    params: str
```
L702  ⚪  (score=0)
```python
```
L703  ⚪  (score=0)
```python
class UtilityCode(UtilityCodeBase):
```
L704  ⚪  (score=0)
```python
    """
```
L705  ⚪  (score=0)
```python
    Stores utility code to add during code generation.
```
L706  ⚪  (score=0)
```python
```
L707  ⚪  (score=0)
```python
    See GlobalState.put_utility_code.
```
L708  ⚪  (score=0)
```python
```
L709  ⚪  (score=0)
```python
    hashes/equals by instance
```
L710  ⚪  (score=0)
```python
```
L711  ⚪  (score=0)
```python
    proto           C prototypes
```
L712  ⚪  (score=0)
```python
    export          C prototypes exported from the shared utility code module
```
L713  ⚪  (score=0)
```python
    impl            implementation code
```
L714  ⚪  (score=0)
```python
    init            code to call on module initialization
```
L715  ⚪  (score=0)
```python
    requires        utility code dependencies
```
L716  ⚪  (score=0)
```python
    proto_block     the place in the resulting file where the prototype should
```
L717  ⚪  (score=0)
```python
                    end up
```
L718  ⚪  (score=0)
```python
    name            name of the utility code (or None)
```
L719  ⚪  (score=0)
```python
    file            filename of the utility code file this utility was loaded
```
L720  ⚪  (score=0)
```python
                    from (or None)
```
L721  ⚪  (score=0)
```python
    shared_utility_functions        List of parsed declaration line of the shared utility function
```
L722  ⚪  (score=0)
```python
    """
```
L723  ⚪  (score=0)
```python
    code_parts = ["proto", "export", "impl", "init", "cleanup", "module_state_decls", "module_state_traverse", "module_state_clear"]
```
L724  ⚪  (score=0)
```python
```
L725  ⚪  (score=0)
```python
    def __init__(self, proto=None, impl=None, init=None, cleanup=None,
```
L726  ⚪  (score=0)
```python
                 module_state_decls=None, module_state_traverse=None,
```
L727  ⚪  (score=0)
```python
                 module_state_clear=None, requires=None,
```
L728  ⚪  (score=0)
```python
                 proto_block='utility_code_proto', name=None, file=None, export=None):
```
L729  ⚪  (score=0)
```python
        # proto_block: Which code block to dump prototype in. See GlobalState.
```
L730  ⚪  (score=0)
```python
        self.proto = proto
```
L731  ⚪  (score=0)
```python
        self.impl = impl
```
L732  ⚪  (score=0)
```python
        self.init = init
```
L733  ⚪  (score=0)
```python
        self.cleanup = cleanup
```
L734  ⚪  (score=0)
```python
        self.module_state_decls = module_state_decls
```
L735  ⚪  (score=0)
```python
        self.module_state_traverse = module_state_traverse
```
L736  ⚪  (score=0)
```python
        self.module_state_clear = module_state_clear
```
L737  ⚪  (score=0)
```python
        self.requires = requires
```
L738  ⚪  (score=0)
```python
        self._cache = {}
```
L739  ⚪  (score=0)
```python
        self.specialize_list = []
```
L740  ⚪  (score=0)
```python
        self.proto_block = proto_block
```
L741  ⚪  (score=0)
```python
        self.name = name
```
L742  ⚪  (score=0)
```python
        self.file = file
```
L743  ⚪  (score=0)
```python
        self.export = export
```
L744  ⚪  (score=0)
```python
        self.shared_utility_functions = self.parse_export_functions(export) if export else []
```
L745  ⚪  (score=0)
```python
        if export:
```
L746  ⚪  (score=0)
```python
            self._validate_suitable_for_sharing()
```
L747  ⚪  (score=0)
```python
```
L748  ⚪  (score=0)
```python
        # cached for use in hash and eq
```
L749  ⚪  (score=0)
```python
        self._parts_tuple = tuple(getattr(self, part, None) for part in self.code_parts)
```
L750  ⚪  (score=0)
```python
```
L751  ⚪  (score=0)
```python
    def parse_export_functions(self, export_proto: str) -> list:
```
L752  ⚪  (score=0)
```python
```
L753  ⚪  (score=0)
```python
        assert '//' not in export_proto and '/*' not in export_proto and '*/' not in export_proto, \
```
L754  ⚪  (score=0)
```python
            f'Export block must not contain comments:\n{export_proto.strip()}\n in file {self.file}'
```
L755  ⚪  (score=0)
```python
```
L756  ⚪  (score=0)
```python
        parsed_protos = []
```
L757  ⚪  (score=0)
```python
        proto_regex=r'''
```
L758  ⚪  (score=0)
```python
            ^static\s                                         # `static` keyword
```
L759  ⚪  (score=0)
```python
            (?P<ret_type>[^;()]+[\s*])                        # return type + modifier with optional * - e.g.: int *, float, const str *, ...
```
L760  ⚪  (score=0)
```python
            (?P<func_name>\w+)\((?P<func_params>[^)]*)\)$     # function with params - e.g. foo(int, float, *PyObject)
```
L761  ⚪  (score=0)
```python
        '''
```
L762  ⚪  (score=0)
```python
```
L763  ⚪  (score=0)
```python
        for proto in export_proto.split(';\n'):
```
L764  ⚪  (score=0)
```python
            proto = proto.strip().replace('\n', '')
```
L765  ⚪  (score=0)
```python
            proto = re.sub(r'\s+', ' ', proto)
```
L766  ⚪  (score=0)
```python
```
L767  ⚪  (score=0)
```python
            if len(proto) == 0:
```
L768  ⚪  (score=0)
```python
                continue
```
L769  ⚪  (score=0)
```python
            matched = re.match(proto_regex, proto, re.VERBOSE)
```
L770  ⚪  (score=0)
```python
            assert matched is not None, \
```
L771  ⚪  (score=0)
```python
                f"Wrong format of function definition in export block \n{proto!r}\n in {self.file}"
```
L772  ⚪  (score=0)
```python
```
L773  ⚪  (score=0)
```python
            ret_type, func_name, func_params = matched.groups()
```
L774  ⚪  (score=0)
```python
            parsed_protos.append(
```
L775  ⚪  (score=0)
```python
                SharedFunctionDecl(name=func_name.strip(), ret=ret_type.strip(), params=func_params.strip())
```
L776  ⚪  (score=0)
```python
            )
```
L777  ⚪  (score=0)
```python
```
L778  ⚪  (score=0)
```python
        return parsed_protos
```
L779  ⚪  (score=0)
```python
```
L780  ⚪  (score=0)
```python
```
L781  ⚪  (score=0)
```python
    def __hash__(self):
```
L782  ⚪  (score=0)
```python
        return hash(self._parts_tuple)
```
L783  ⚪  (score=0)
```python
```
L784  ⚪  (score=0)
```python
    def __eq__(self, other):
```
L785  ⚪  (score=0)
```python
        if self is other:
```
L786  ⚪  (score=0)
```python
            return True
```
L787  ⚪  (score=0)
```python
        self_type, other_type = type(self), type(other)
```
L788  ⚪  (score=0)
```python
        if self_type is not other_type and not (isinstance(other, self_type) or isinstance(self, other_type)):
```
L789  ⚪  (score=0)
```python
            return False
```
L790  ⚪  (score=0)
```python
```
L791  ⚪  (score=0)
```python
        return self._parts_tuple == other._parts_tuple
```
L792  ⚪  (score=0)
```python
```
L793  ⚪  (score=0)
```python
    def none_or_sub(self, s, context):
```
L794  ⚪  (score=0)
```python
        """
```
L795  ⚪  (score=0)
```python
        Format a string in this utility code with context. If None, do nothing.
```
L796  ⚪  (score=0)
```python
        """
```
L797  ⚪  (score=0)
```python
        if s is None:
```
L798  ⚪  (score=0)
```python
            return None
```
L799  ⚪  (score=0)
```python
        return s % context
```
L800  ⚪  (score=0)
```python
```
L801  ⚪  (score=0)
```python
    def specialize(self, pyrex_type=None, **data):
```
L802  ⚪  (score=0)
```python
        name = self.name
```
L803  ⚪  (score=0)
```python
        if pyrex_type is not None:
```
L804  ⚪  (score=0)
```python
            data['type'] = pyrex_type.empty_declaration_code()
```
L805  ⚪  (score=0)
```python
            data['type_name'] = pyrex_type.specialization_name()
```
L806  ⚪  (score=0)
```python
            name = "%s[%s]" % (name, data['type_name'])
```
L807  ⚪  (score=0)
```python
        # Dicts aren't hashable...
```
L808  ⚪  (score=0)
```python
        key = tuple(sorted(data.items()))
```
L809  ⚪  (score=0)
```python
        try:
```
L810  ⚪  (score=0)
```python
            return self._cache[key]
```
L811  ⚪  (score=0)
```python
        except KeyError:
```
L812  ⚪  (score=0)
```python
            if self.requires is None:
```
L813  ⚪  (score=0)
```python
                requires = None
```
L814  ⚪  (score=0)
```python
            else:
```
L815  ⚪  (score=0)
```python
                requires = [r.specialize(data) for r in self.requires]
```
L816  ⚪  (score=0)
```python
```
L817  ⚪  (score=0)
```python
            s = self._cache[key] = UtilityCode(
```
L818  ⚪  (score=0)
```python
                self.none_or_sub(self.proto, data),
```
L819  ⚪  (score=0)
```python
                self.none_or_sub(self.impl, data),
```
L820  ⚪  (score=0)
```python
                self.none_or_sub(self.init, data),
```
L821  ⚪  (score=0)
```python
                self.none_or_sub(self.cleanup, data),
```
L822  ⚪  (score=0)
```python
                self.none_or_sub(self.module_state_decls, data),
```
L823  ⚪  (score=0)
```python
                self.none_or_sub(self.module_state_traverse, data),
```
L824  ⚪  (score=0)
```python
                self.none_or_sub(self.module_state_clear, data),
```
L825  ⚪  (score=0)
```python
                requires,
```
L826  ⚪  (score=0)
```python
                self.proto_block,
```
L827  ⚪  (score=0)
```python
                name,
```
L828  ⚪  (score=0)
```python
            )
```
L829  ⚪  (score=0)
```python
```
L830  ⚪  (score=0)
```python
            self.specialize_list.append(s)
```
L831  ⚪  (score=0)
```python
            return s
```
L832  ⚪  (score=0)
```python
```
L833  ⚪  (score=0)
```python
    def _validate_suitable_for_sharing(self):
```
L834  ⚪  (score=0)
```python
        code_string = getattr(self, "impl")
```
L835  ⚪  (score=0)
```python
        if not code_string: return
```
L836  ⚪  (score=0)
```python
        assert "NAMED_CGLOBAL(moddict_cname)" not in code_string, \
```
L837  ⚪  (score=0)
```python
            f"moddict_cname should not be shared: {self}"
```
L838  ⚪  (score=0)
```python
```
L839  ⚪  (score=0)
```python
    @cython.final
```
L840  ⚪  (score=0)
```python
    def _put_code_section(self, writer: "CCodeWriter", output: "GlobalState", code_type: str, used_by=None):
```
L841  ⚪  (score=0)
```python
        code_string = getattr(self, code_type)
```
L842  ⚪  (score=0)
```python
        if not code_string:
```
L843  ⚪  (score=0)
```python
            return
```
L844  ⚪  (score=0)
```python
```
L845  ⚪  (score=0)
```python
        can_be_reused = code_type in ('proto', 'impl')
```
L846  ⚪  (score=0)
```python
```
L847  ⚪  (score=0)
```python
        code_string, result_is_module_specific = process_utility_ccode(self, output, code_string)
```
L848  ⚪  (score=0)
```python
```
L849  ⚪  (score=0)
```python
        used_by = f" (used by {used_by})" if used_by else ''
```
L850  ⚪  (score=0)
```python
        name = f"{self.name}.{code_type}" if code_type != 'impl' else self.name
```
L851  ⚪  (score=0)
```python
```
L852  ⚪  (score=0)
```python
        writer.putln(f"/* {name}{used_by} */")
```
L853  ⚪  (score=0)
```python
```
L854  ⚪  (score=0)
```python
        if can_be_reused and not result_is_module_specific:
```
L855  ⚪  (score=0)
```python
            # can be reused across modules
```
L856  ⚪  (score=0)
```python
            writer.put_or_include(code_string, f'{self.name}_{code_type}')
```
L857  ⚪  (score=0)
```python
        else:
```
L858  ⚪  (score=0)
```python
            writer.put_multilines(code_string)
```
L859  ⚪  (score=0)
```python
```
L860  ⚪  (score=0)
```python
    def _put_init_code_section(self, output):
```
L861  ⚪  (score=0)
```python
        if not self.init:
```
L862  ⚪  (score=0)
```python
            return
```
L863  ⚪  (score=0)
```python
        writer = output['init_globals']
```
L864  ⚪  (score=0)
```python
        self._put_code_section(writer, output, 'init')
```
L865  ⚪  (score=0)
```python
        # 'init' code can end with an 'if' statement for an error condition like:
```
L866  ⚪  (score=0)
```python
        # if (check_ok()) ; else
```
L867  ⚪  (score=0)
```python
        writer.putln("  " + writer.error_goto_if_PyErr(output.module_pos))
```
L868  ⚪  (score=0)
```python
        writer.putln()
```
L869  ⚪  (score=0)
```python
```
L870  ⚪  (score=0)
```python
    def _put_shared_function_declarations(self, code: CCodeWriter) -> None:
```
L871  ⚪  (score=0)
```python
        code.putln(f'/* {self.name} */')
```
L872  ⚪  (score=0)
```python
        for shared in self.shared_utility_functions:
```
L873  ⚪  (score=0)
```python
            # Convert function declarations to static function pointers.
```
L874  ⚪  (score=0)
```python
            code.putln(f'static {shared.ret}(*{shared.name})({shared.params}); /*proto*/')
```
L875  ⚪  (score=0)
```python
        code.putln()
```
L876  ⚪  (score=0)
```python
```
L877  ⚪  (score=0)
```python
    def put_code(self, globalstate: GlobalState, used_by: str | None = None) -> None:
```
L878  ⚪  (score=0)
```python
        has_shared_utility_code = bool(
```
L879  ⚪  (score=0)
```python
            self.shared_utility_functions and globalstate.module_node.scope.context.shared_utility_qualified_name
```
L880  ⚪  (score=0)
```python
        )
```
L881  ⚪  (score=0)
```python
```
L882  ⚪  (score=0)
```python
        if self.requires and not has_shared_utility_code:
```
L883  ⚪  (score=0)
```python
            for dependency in self.requires:
```
L884  ⚪  (score=0)
```python
                globalstate.use_utility_code(dependency, used_by=self.name)
```
L885  ⚪  (score=0)
```python
```
L886  ⚪  (score=0)
```python
        if has_shared_utility_code:
```
L887  ⚪  (score=0)
```python
            self._put_shared_function_declarations(globalstate[self.proto_block])
```
L888  ⚪  (score=0)
```python
        globalstate.shared_utility_functions.extend(self.shared_utility_functions)
```
L889  ⚪  (score=0)
```python
```
L890  ⚪  (score=0)
```python
        if self.proto:
```
L891  ⚪  (score=0)
```python
            self._put_code_section(globalstate[self.proto_block], globalstate, 'proto', used_by=used_by)
```
L892  ⚪  (score=0)
```python
        if not has_shared_utility_code:
```
L893  ⚪  (score=0)
```python
            self._put_code_section(globalstate[self.proto_block], globalstate, 'export')
```
L894  ⚪  (score=0)
```python
        if self.impl and not has_shared_utility_code:
```
L895  ⚪  (score=0)
```python
            self._put_code_section(globalstate['utility_code_def'], globalstate, 'impl', used_by=used_by)
```
L896  ⚪  (score=0)
```python
        if self.cleanup and Directives.generate_cleanup_code:
```
L897  ⚪  (score=0)
```python
            self._put_code_section(globalstate['cleanup_globals'], globalstate, 'cleanup')
```
L898  ⚪  (score=0)
```python
        if self.module_state_decls:
```
L899  ⚪  (score=0)
```python
            self._put_code_section(globalstate['module_state_contents'], globalstate, 'module_state_decls')
```
L900  ⚪  (score=0)
```python
        if self.module_state_traverse:
```
L901  ⚪  (score=0)
```python
            self._put_code_section(globalstate['module_state_traverse_contents'], globalstate, 'module_state_traverse')
```
L902  ⚪  (score=0)
```python
        if self.module_state_clear:
```
L903  ⚪  (score=0)
```python
            self._put_code_section(globalstate['module_state_clear_contents'], globalstate, 'module_state_clear')
```
L904  ⚪  (score=0)
```python
```
L905  ⚪  (score=0)
```python
        if self.init:
```
L906  ⚪  (score=0)
```python
            self._put_init_code_section(globalstate)
```
L907  ⚪  (score=0)
```python
```
L908  ⚪  (score=0)
```python
```
L909  ⚪  (score=0)
```python
def add_macro_processor(*macro_names, regex=None, is_module_specific=False, _last_macro_processor = [None]):
```
L910  ⚪  (score=0)
```python
    """Decorator to chain the code macro processors below.
```
L911  ⚪  (score=0)
```python
    """
```
L912  ⚪  (score=0)
```python
    last_processor = _last_macro_processor[0]
```
L913  ⚪  (score=0)
```python
```
L914  ⚪  (score=0)
```python
    def build_processor(func):
```
L915  ⚪  (score=0)
```python
        @wraps(func)
```
L916  ⚪  (score=0)
```python
        def process(utility_code: UtilityCode, output, code_string: str):
```
L917  ⚪  (score=0)
```python
            # First, call the processing chain in FIFO function definition order.
```
L918  ⚪  (score=0)
```python
            result_is_module_specific = False
```
L919  ⚪  (score=0)
```python
            if last_processor is not None:
```
L920  ⚪  (score=0)
```python
                code_string, result_is_module_specific = last_processor(utility_code, output, code_string)
```
L921  ⚪  (score=0)
```python
```
L922  ⚪  (score=0)
```python
            # Detect if we need to do something.
```
L923  ⚪  (score=0)
```python
            if macro_names:
```
L924  ⚪  (score=0)
```python
                for macro in macro_names:
```
L925  ⚪  (score=0)
```python
                    if macro in code_string:
```
L926  ⚪  (score=0)
```python
                        break
```
L927  ⚪  (score=0)
```python
                else:
```
L928  ⚪  (score=0)
```python
                    return code_string, result_is_module_specific
```
L929  ⚪  (score=0)
```python
```
L930  ⚪  (score=0)
```python
            # Process the code.
```
L931  ⚪  (score=0)
```python
            if regex is None:
```
L932  ⚪  (score=0)
```python
                code_string = func(utility_code, output, code_string)
```
L933  ⚪  (score=0)
```python
            else:
```
L934  ⚪  (score=0)
```python
                code_string = re.sub(regex, partial(func, output), code_string)
```
L935  ⚪  (score=0)
```python
```
L936  ⚪  (score=0)
```python
            # Make sure we found and replaced all macro occurrences.
```
L937  ⚪  (score=0)
```python
            for macro in macro_names:
```
L938  ⚪  (score=0)
```python
                if macro in code_string:
```
L939  ⚪  (score=0)
```python
                    raise RuntimeError(f"Left-over utility code macro '{macro}()' found in '{utility_code.name}'")
```
L940  ⚪  (score=0)
```python
```
L941  ⚪  (score=0)
```python
            result_is_module_specific |= is_module_specific
```
L942  ⚪  (score=0)
```python
            return code_string, result_is_module_specific
```
L943  ⚪  (score=0)
```python
```
L944  ⚪  (score=0)
```python
        _last_macro_processor[0] = process
```
L945  ⚪  (score=0)
```python
        return process
```
L946  ⚪  (score=0)
```python
```
L947  ⚪  (score=0)
```python
    return build_processor
```
L948  ⚪  (score=0)
```python
```
L949  ⚪  (score=0)
```python
```
L950  ⚪  (score=0)
```python
@add_macro_processor(
```
L951  ⚪  (score=0)
```python
    'CSTRING',
```
L952  ⚪  (score=0)
```python
    regex=r'CSTRING\(\s*"""([^"]*(?:"[^"]+)*)"""\s*\)',
```
L953  ⚪  (score=0)
```python
)
```
L954  ⚪  (score=0)
```python
def _wrap_c_string(_, matchobj):
```
L955  ⚪  (score=0)
```python
    """Replace CSTRING('''xyz''') by a C compatible string, taking care of line breaks.
```
L956  ⚪  (score=0)
```python
    """
```
L957  ⚪  (score=0)
```python
    content = matchobj.group(1).replace('"', r'\042')
```
L958  ⚪  (score=0)
```python
    return ''.join(
```
L959  ⚪  (score=0)
```python
        f'"{line}\\n"\n' if not line.endswith('\\') or line.endswith('\\\\') else f'"{line[:-1]}"\n'
```
L960  ⚪  (score=0)
```python
        for line in content.splitlines())
```
L961  ⚪  (score=0)
```python
```
L962  ⚪  (score=0)
```python
```
L963  ⚪  (score=0)
```python
@add_macro_processor()
```
L964  ⚪  (score=0)
```python
def _format_impl_code(utility_code: UtilityCode, _, impl):
```
L965  ⚪  (score=0)
```python
    return utility_code.format_code(impl)
```
L966  ⚪  (score=0)
```python
```
L967  ⚪  (score=0)
```python
```
L968  ⚪  (score=0)
```python
@add_macro_processor(
```
L969  ⚪  (score=0)
```python
    'CALL_UNBOUND_METHOD',
```
L970  ⚪  (score=0)
```python
    is_module_specific=True,
```
L971  ⚪  (score=0)
```python
    regex=(
```
L972  ⚪  (score=0)
```python
        r'CALL_UNBOUND_METHOD\('
```
L973  ⚪  (score=0)
```python
        r'([a-zA-Z_]+),\s*'   # type cname
```
L974  ⚪  (score=0)
```python
        r'"([^"]+)",\s*'      # method name
```
L975  ⚪  (score=0)
```python
        r'([^),\s]+)'         # object cname
```
L976  ⚪  (score=0)
```python
        r'((?:,[^),]+)*)'     # args*
```
L977  ⚪  (score=0)
```python
        r'\)'
```
L978  ⚪  (score=0)
```python
    ),
```
L979  ⚪  (score=0)
```python
)
```
L980  ⚪  (score=0)
```python
def _inject_unbound_method(output, matchobj):
```
L981  ⚪  (score=0)
```python
    """Replace 'UNBOUND_METHOD(type, "name")' by a constant Python identifier cname.
```
L982  ⚪  (score=0)
```python
    """
```
L983  ⚪  (score=0)
```python
    type_cname, method_name, obj_cname, args = matchobj.groups()
```
L984  ⚪  (score=0)
```python
    type_cname = '&%s' % type_cname
```
L985  ⚪  (score=0)
```python
    args = [arg.strip() for arg in args[1:].split(',')] if args else []
```
L986  ⚪  (score=0)
```python
    assert len(args) < 3, f"CALL_UNBOUND_METHOD() does not support {len(args):d} call arguments"
```
L987  ⚪  (score=0)
```python
    return output.cached_unbound_method_call_code(
```
L988  ⚪  (score=0)
```python
        f"{Naming.modulestateglobal_cname}->",
```
L989  ⚪  (score=0)
```python
        obj_cname, type_cname, method_name, args)
```
L990  ⚪  (score=0)
```python
```
L991  ⚪  (score=0)
```python
```
L992  ⚪  (score=0)
```python
@add_macro_processor(
```
L993  ⚪  (score=0)
```python
    'PYIDENT', 'PYUNICODE',
```
L994  ⚪  (score=0)
```python
    is_module_specific=True,
```
L995  ⚪  (score=0)
```python
    regex=r'PY(IDENT|UNICODE)\("([^"]+)"\)',
```
L996  ⚪  (score=0)
```python
)
```
L997  ⚪  (score=0)
```python
def _inject_string_constant(output, matchobj):
```
L998  ⚪  (score=0)
```python
    """Replace 'PYIDENT("xyz")' by a constant Python identifier cname.
```
L999  ⚪  (score=0)
```python
    """
```
L1000  ⚪  (score=0)
```python
    str_type, name = matchobj.groups()
```
L1001  ⚪  (score=0)
```python
    return "%s->%s" % (
```
L1002  ⚪  (score=0)
```python
        Naming.modulestateglobal_cname,
```
L1003  ⚪  (score=0)
```python
        output.get_py_string_const(
```
L1004  ⚪  (score=0)
```python
            StringEncoding.EncodedString(name), identifier=str_type == 'IDENT').cname)
```
L1005  ⚪  (score=0)
```python
```
L1006  ⚪  (score=0)
```python
```
L1007  ⚪  (score=0)
```python
@add_macro_processor(
```
L1008  ⚪  (score=0)
```python
    'EMPTY',
```
L1009  ⚪  (score=0)
```python
    # As long as we use the same C access macros for these names, they are not module specific.
```
L1010  ⚪  (score=0)
```python
    # is_module_specific=True,
```
L1011  ⚪  (score=0)
```python
    regex=r'EMPTY\((bytes|unicode|tuple)\)',
```
L1012  ⚪  (score=0)
```python
)
```
L1013  ⚪  (score=0)
```python
def _inject_empty_collection_constant(output, matchobj):
```
L1014  ⚪  (score=0)
```python
    """Replace 'EMPTY(bytes|tuple|...)' by a constant Python identifier cname.
```
L1015  ⚪  (score=0)
```python
    """
```
L1016  ⚪  (score=0)
```python
    type_name = matchobj.group(1)
```
L1017  ⚪  (score=0)
```python
    return "%s->%s" % (
```
L1018  ⚪  (score=0)
```python
        Naming.modulestateglobal_cname,
```
L1019  ⚪  (score=0)
```python
        getattr(Naming, f'empty_{type_name}'))
```
L1020  ⚪  (score=0)
```python
```
L1021  ⚪  (score=0)
```python
```
L1022  ⚪  (score=0)
```python
@add_macro_processor(
```
L1023  ⚪  (score=0)
```python
    'CGLOBAL',  # 'NAMED_CGLOBAL',  # first is part of second and thus not needed
```
L1024  ⚪  (score=0)
```python
    is_module_specific=False,
```
L1025  ⚪  (score=0)
```python
    regex=r'(NAMED_)?CGLOBAL\(([^)]+)\)',
```
L1026  ⚪  (score=0)
```python
)
```
L1027  ⚪  (score=0)
```python
def _inject_cglobal(output, matchobj):
```
L1028  ⚪  (score=0)
```python
    is_named, name = matchobj.groups()
```
L1029  ⚪  (score=0)
```python
    if is_named:
```
L1030  ⚪  (score=0)
```python
        name = getattr(Naming, name)
```
L1031  ⚪  (score=0)
```python
    return f"{Naming.modulestateglobal_cname}->{name}"
```
L1032  ⚪  (score=0)
```python
```
L1033  ⚪  (score=0)
```python
```
L1034  ⚪  (score=0)
```python
@add_macro_processor()
```
L1035  ⚪  (score=0)
```python
def process_utility_ccode(utility_code, _, code_string):
```
L1036  ⚪  (score=0)
```python
    """Entry point for code processors, must be defined last.
```
L1037  ⚪  (score=0)
```python
    """
```
L1038  ⚪  (score=0)
```python
    return code_string
```
L1039  ⚪  (score=0)
```python
```
L1040  ⚪  (score=0)
```python
```
L1041  ⚪  (score=0)
```python
def sub_tempita(s, context, file=None, name=None, __cache={}):
```
L1042  ⚪  (score=0)
```python
    "Run tempita on string s with given context."
```
L1043  ⚪  (score=0)
```python
    if not s:
```
L1044  ⚪  (score=0)
```python
        return None
```
L1045  ⚪  (score=0)
```python
```
L1046  ⚪  (score=0)
```python
    if file:
```
L1047  ⚪  (score=0)
```python
        name = f"{file}:{name}"
```
L1048  ⚪  (score=0)
```python
    if name:
```
L1049  ⚪  (score=0)
```python
        context['__name'] = name
```
L1050  ⚪  (score=0)
```python
```
L1051  ⚪  (score=0)
```python
    try:
```
L1052  ⚪  (score=0)
```python
        template = __cache[s]
```
L1053  ⚪  (score=0)
```python
    except KeyError:
```
L1054  ⚪  (score=0)
```python
        from ..Tempita import Template
```
L1055  ⚪  (score=0)
```python
        template = __cache[s] = Template(s, name=name)
```
L1056  ⚪  (score=0)
```python
```
L1057  ⚪  (score=0)
```python
    return template.substitute(context)
```
L1058  ⚪  (score=0)
```python
```
L1059  ⚪  (score=0)
```python
```
L1060  ⚪  (score=0)
```python
class TempitaUtilityCode(UtilityCode):
```
L1061  ⚪  (score=0)
```python
    def __init__(self, name=None, proto=None, impl=None, init=None, file=None, context=None, **kwargs):
```
L1062  ⚪  (score=0)
```python
        if context is None:
```
L1063  ⚪  (score=0)
```python
            context = {}
```
L1064  ⚪  (score=0)
```python
        else:
```
L1065  ⚪  (score=0)
```python
            # prevent changes propagating back if context is shared between multiple utility codes.
```
L1066  ⚪  (score=0)
```python
            context = context.copy()
```
L1067  ⚪  (score=0)
```python
        proto = sub_tempita(proto, context, file, name)
```
L1068  ⚪  (score=0)
```python
        impl = sub_tempita(impl, context, file, name)
```
L1069  ⚪  (score=0)
```python
        init = sub_tempita(init, context, file, name)
```
L1070  ⚪  (score=0)
```python
        super().__init__(
```
L1071  ⚪  (score=0)
```python
            proto, impl, init=init, name=name, file=file, **kwargs)
```
L1072  ⚪  (score=0)
```python
```
L1073  ⚪  (score=0)
```python
    @classmethod
```
L1074  ⚪  (score=0)
```python
    def load_cached(cls, utility_code_name, from_file=None, context=None, __cache={}):
```
L1075  ⚪  (score=0)
```python
        context_key = tuple(sorted(context.items())) if context else None
```
L1076  ⚪  (score=0)
```python
        assert hash(context_key) is not None  # raise TypeError if not hashable
```
L1077  ⚪  (score=0)
```python
        key = (cls, from_file, utility_code_name, context_key)
```
L1078  ⚪  (score=0)
```python
        try:
```
L1079  ⚪  (score=0)
```python
            return __cache[key]
```
L1080  ⚪  (score=0)
```python
        except KeyError:
```
L1081  ⚪  (score=0)
```python
            pass
```
L1082  ⚪  (score=0)
```python
        code = __cache[key] = cls.load(utility_code_name, from_file, context=context)
```
L1083  ⚪  (score=0)
```python
        return code
```
L1084  ⚪  (score=0)
```python
```
L1085  ⚪  (score=0)
```python
    def none_or_sub(self, s, context):
```
L1086  ⚪  (score=0)
```python
        """
```
L1087  ⚪  (score=0)
```python
        Format a string in this utility code with context. If None, do nothing.
```
L1088  ⚪  (score=0)
```python
        """
```
L1089  ⚪  (score=0)
```python
        if s is None:
```
L1090  ⚪  (score=0)
```python
            return None
```
L1091  ⚪  (score=0)
```python
        return sub_tempita(s, context, self.file, self.name)
```
L1092  ⚪  (score=0)
```python
```
L1093  ⚪  (score=0)
```python
```
L1094  ⚪  (score=0)
```python
class LazyUtilityCode(UtilityCodeBase):
```
L1095  ⚪  (score=0)
```python
    """
```
L1096  ⚪  (score=0)
```python
    Utility code that calls a callback with the root code writer when
```
L1097  ⚪  (score=0)
```python
    available. Useful when you only have 'env' but not 'code'.
```
L1098  ⚪  (score=0)
```python
    """
```
L1099  ⚪  (score=0)
```python
    __name__ = '<lazy>'
```
L1100  ⚪  (score=0)
```python
    requires = None
```
L1101  ⚪  (score=0)
```python
```
L1102  ⚪  (score=0)
```python
    def __init__(self, callback):
```
L1103  ⚪  (score=0)
```python
        self.callback = callback
```
L1104  ⚪  (score=0)
```python
```
L1105  ⚪  (score=0)
```python
    def put_code(self, globalstate: "GlobalState", used_by=None) -> None:
```
L1106  ⚪  (score=0)
```python
        utility = self.callback(globalstate.rootwriter)
```
L1107  ⚪  (score=0)
```python
        globalstate.use_utility_code(utility, used_by=used_by)
```
L1108  ⚪  (score=0)
```python
```
L1109  ⚪  (score=0)
```python
```
L1110  ⚪  (score=0)
```python
class FunctionState:
```
L1111  ⚪  (score=0)
```python
    # return_label     string          function return point label
```
L1112  ⚪  (score=0)
```python
    # error_label      string          error catch point label
```
L1113  ⚪  (score=0)
```python
    # error_without_exception  boolean Can go to the error label without an exception (e.g. __next__ can return NULL)
```
L1114  ⚪  (score=0)
```python
    # continue_label   string          loop continue point label
```
L1115  ⚪  (score=0)
```python
    # break_label      string          loop break point label
```
L1116  ⚪  (score=0)
```python
    # return_from_error_cleanup_label string
```
L1117  ⚪  (score=0)
```python
    # label_counter    integer         counter for naming labels
```
L1118  ⚪  (score=0)
```python
    # exc_vars         (string * 3)    exception variables for reraise, or None
```
L1119  ⚪  (score=0)
```python
    # can_trace        boolean         line tracing is supported in the current context
```
L1120  ⚪  (score=0)
```python
    # scope            Scope           the scope object of the current function
```
L1121  ⚪  (score=0)
```python
```
L1122  ⚪  (score=0)
```python
    # Not used for now, perhaps later
```
L1123  ⚪  (score=0)
```python
    def __init__(self, owner, names_taken=set(), scope=None):
```
L1124  ⚪  (score=0)
```python
        self.names_taken = names_taken
```
L1125  ⚪  (score=0)
```python
        self.owner = owner
```
L1126  ⚪  (score=0)
```python
        self.scope = scope
```
L1127  ⚪  (score=0)
```python
```
L1128  ⚪  (score=0)
```python
        self.error_label = None
```
L1129  ⚪  (score=0)
```python
        self.label_counter = 0
```
L1130  ⚪  (score=0)
```python
        self.labels_used = set()
```
L1131  ⚪  (score=0)
```python
        self.return_label = self.new_label()
```
L1132  ⚪  (score=0)
```python
        self.new_error_label()
```
L1133  ⚪  (score=0)
```python
        self.continue_label = None
```
L1134  ⚪  (score=0)
```python
        self.break_label = None
```
L1135  ⚪  (score=0)
```python
        self.yield_labels = []
```
L1136  ⚪  (score=0)
```python
```
L1137  ⚪  (score=0)
```python
        self.exc_vars = None
```
L1138  ⚪  (score=0)
```python
        self.current_except = None
```
L1139  ⚪  (score=0)
```python
        self.can_trace = False
```
L1140  ⚪  (score=0)
```python
        self.gil_owned = True
```
L1141  ⚪  (score=0)
```python
```
L1142  ⚪  (score=0)
```python
        self.temps_allocated = []  # of (name, type, manage_ref, static)
```
L1143  ⚪  (score=0)
```python
        self.temps_free = {}  # (type, manage_ref) -> list of free vars with same type/managed status
```
L1144  ⚪  (score=0)
```python
        self.temps_used_type = {}  # name -> (type, manage_ref)
```
L1145  ⚪  (score=0)
```python
        self.zombie_temps = set()  # temps that must not be reused after release
```
L1146  ⚪  (score=0)
```python
        self.temp_counter = 0
```
L1147  ⚪  (score=0)
```python
        self.closure_temps = None
```
L1148  ⚪  (score=0)
```python
```
L1149  ⚪  (score=0)
```python
        # This is used to collect temporaries, useful to find out which temps
```
L1150  ⚪  (score=0)
```python
        # need to be privatized in parallel sections
```
L1151  ⚪  (score=0)
```python
        self.collect_temps_stack = []
```
L1152  ⚪  (score=0)
```python
```
L1153  ⚪  (score=0)
```python
        # This is used for the error indicator, which needs to be local to the
```
L1154  ⚪  (score=0)
```python
        # function. It used to be global, which relies on the GIL being held.
```
L1155  ⚪  (score=0)
```python
        # However, exceptions may need to be propagated through 'nogil'
```
L1156  ⚪  (score=0)
```python
        # sections, in which case we introduce a race condition.
```
L1157  ⚪  (score=0)
```python
        self.should_declare_error_indicator = False
```
L1158  ⚪  (score=0)
```python
        self.uses_error_indicator = False
```
L1159  ⚪  (score=0)
```python
```
L1160  ⚪  (score=0)
```python
        self.error_without_exception = False
```
L1161  ⚪  (score=0)
```python
```
L1162  ⚪  (score=0)
```python
        self.needs_refnanny = False
```
L1163  ⚪  (score=0)
```python
```
L1164  ⚪  (score=0)
```python
    # safety checks
```
L1165  ⚪  (score=0)
```python
```
L1166  ⚪  (score=0)
```python
    def validate_exit(self):
```
L1167  ⚪  (score=0)
```python
        # validate that all allocated temps have been freed
```
L1168  ⚪  (score=0)
```python
        if self.temps_allocated:
```
L1169  ⚪  (score=0)
```python
            leftovers = self.temps_in_use()
```
L1170  ⚪  (score=0)
```python
            if leftovers:
```
L1171  ⚪  (score=0)
```python
                msg = "TEMPGUARD: Temps left over at end of '%s': %s" % (self.scope.name, ', '.join([
```
L1172  ⚪  (score=0)
```python
                    '%s [%s]' % (name, ctype)
```
L1173  ⚪  (score=0)
```python
                    for name, ctype, is_pytemp in sorted(leftovers)]),
```
L1174  ⚪  (score=0)
```python
                )
```
L1175  ⚪  (score=0)
```python
                #print(msg)
```
L1176  ⚪  (score=0)
```python
                raise RuntimeError(msg)
```
L1177  ⚪  (score=0)
```python
```
L1178  ⚪  (score=0)
```python
    # labels
```
L1179  ⚪  (score=0)
```python
```
L1180  ⚪  (score=0)
```python
    def new_label(self, name=None):
```
L1181  ⚪  (score=0)
```python
        n: cython.size_t = self.label_counter
```
L1182  ⚪  (score=0)
```python
        self.label_counter = n + 1
```
L1183  ⚪  (score=0)
```python
        label = "%s%d" % (Naming.label_prefix, n)
```
L1184  ⚪  (score=0)
```python
        if name is not None:
```
L1185  ⚪  (score=0)
```python
            label += '_' + name
```
L1186  ⚪  (score=0)
```python
        return label
```
L1187  ⚪  (score=0)
```python
```
L1188  ⚪  (score=0)
```python
    def new_yield_label(self, expr_type='yield'):
```
L1189  ⚪  (score=0)
```python
        label = self.new_label('resume_from_%s' % expr_type)
```
L1190  ⚪  (score=0)
```python
        num_and_label = (len(self.yield_labels) + 1, label)
```
L1191  ⚪  (score=0)
```python
        self.yield_labels.append(num_and_label)
```
L1192  ⚪  (score=0)
```python
        return num_and_label
```
L1193  ⚪  (score=0)
```python
```
L1194  ⚪  (score=0)
```python
    def new_error_label(self, prefix=""):
```
L1195  ⚪  (score=0)
```python
        old_err_lbl = self.error_label
```
L1196  ⚪  (score=0)
```python
        self.error_label = self.new_label(prefix + 'error')
```
L1197  ⚪  (score=0)
```python
        return old_err_lbl
```
L1198  ⚪  (score=0)
```python
```
L1199  ⚪  (score=0)
```python
    def get_loop_labels(self):
```
L1200  ⚪  (score=0)
```python
        return (
```
L1201  ⚪  (score=0)
```python
            self.continue_label,
```
L1202  ⚪  (score=0)
```python
            self.break_label)
```
L1203  ⚪  (score=0)
```python
```
L1204  ⚪  (score=0)
```python
    def set_loop_labels(self, labels):
```
L1205  ⚪  (score=0)
```python
        (self.continue_label,
```
L1206  ⚪  (score=0)
```python
         self.break_label) = labels
```
L1207  ⚪  (score=0)
```python
```
L1208  ⚪  (score=0)
```python
    def new_loop_labels(self, prefix=""):
```
L1209  ⚪  (score=0)
```python
        old_labels = self.get_loop_labels()
```
L1210  ⚪  (score=0)
```python
        self.set_loop_labels(
```
L1211  ⚪  (score=0)
```python
            (self.new_label(prefix + "continue"),
```
L1212  ⚪  (score=0)
```python
             self.new_label(prefix + "break")))
```
L1213  ⚪  (score=0)
```python
        return old_labels
```
L1214  ⚪  (score=0)
```python
```
L1215  ⚪  (score=0)
```python
    def get_all_labels(self):
```
L1216  ⚪  (score=0)
```python
        return (
```
L1217  ⚪  (score=0)
```python
            self.continue_label,
```
L1218  ⚪  (score=0)
```python
            self.break_label,
```
L1219  ⚪  (score=0)
```python
            self.return_label,
```
L1220  ⚪  (score=0)
```python
            self.error_label)
```
L1221  ⚪  (score=0)
```python
```
L1222  ⚪  (score=0)
```python
    def set_all_labels(self, labels):
```
L1223  ⚪  (score=0)
```python
        (self.continue_label,
```
L1224  ⚪  (score=0)
```python
         self.break_label,
```
L1225  ⚪  (score=0)
```python
         self.return_label,
```
L1226  ⚪  (score=0)
```python
         self.error_label) = labels
```
L1227  ⚪  (score=0)
```python
```
L1228  ⚪  (score=0)
```python
    def all_new_labels(self):
```
L1229  ⚪  (score=0)
```python
        old_labels = self.get_all_labels()
```
L1230  ⚪  (score=0)
```python
        new_labels = []
```
L1231  ⚪  (score=0)
```python
        for old_label, name in zip(old_labels, ['continue', 'break', 'return', 'error']):
```
L1232  ⚪  (score=0)
```python
            if old_label:
```
L1233  ⚪  (score=0)
```python
                new_labels.append(self.new_label(name))
```
L1234  ⚪  (score=0)
```python
            else:
```
L1235  ⚪  (score=0)
```python
                new_labels.append(old_label)
```
L1236  ⚪  (score=0)
```python
        self.set_all_labels(new_labels)
```
L1237  ⚪  (score=0)
```python
        return old_labels
```
L1238  ⚪  (score=0)
```python
```
L1239  ⚪  (score=0)
```python
    def use_label(self, lbl):
```
L1240  ⚪  (score=0)
```python
        self.labels_used.add(lbl)
```
L1241  ⚪  (score=0)
```python
```
L1242  ⚪  (score=0)
```python
    def label_used(self, lbl):
```
L1243  ⚪  (score=0)
```python
        return lbl in self.labels_used
```
L1244  ⚪  (score=0)
```python
```
L1245  ⚪  (score=0)
```python
    # temp handling
```
L1246  ⚪  (score=0)
```python
```
L1247  ⚪  (score=0)
```python
    def allocate_temp(self, type, manage_ref, static=False, reusable=True):
```
L1248  ⚪  (score=0)
```python
        """
```
L1249  ⚪  (score=0)
```python
        Allocates a temporary (which may create a new one or get a previously
```
L1250  ⚪  (score=0)
```python
        allocated and released one of the same type). Type is simply registered
```
L1251  ⚪  (score=0)
```python
        and handed back, but will usually be a PyrexType.
```
L1252  ⚪  (score=0)
```python
```
L1253  ⚪  (score=0)
```python
        If type.needs_refcounting, manage_ref comes into play. If manage_ref is set to
```
L1254  ⚪  (score=0)
```python
        True, the temp will be decref-ed on return statements and in exception
```
L1255  ⚪  (score=0)
```python
        handling clauses. Otherwise the caller has to deal with any reference
```
L1256  ⚪  (score=0)
```python
        counting of the variable.
```
L1257  ⚪  (score=0)
```python
```
L1258  ⚪  (score=0)
```python
        If not type.needs_refcounting, then manage_ref will be ignored, but it
```
L1259  ⚪  (score=0)
```python
        still has to be passed. It is recommended to pass False by convention
```
L1260  ⚪  (score=0)
```python
        if it is known that type will never be a reference counted type.
```
L1261  ⚪  (score=0)
```python
```
L1262  ⚪  (score=0)
```python
        static=True marks the temporary declaration with "static".
```
L1263  ⚪  (score=0)
```python
        This is only used when allocating backing store for a module-level
```
L1264  ⚪  (score=0)
```python
        C array literals.
```
L1265  ⚪  (score=0)
```python
```
L1266  ⚪  (score=0)
```python
        if reusable=False, the temp will not be reused after release.
```
L1267  ⚪  (score=0)
```python
```
L1268  ⚪  (score=0)
```python
        A C string referring to the variable is returned.
```
L1269  ⚪  (score=0)
```python
        """
```
L1270  ⚪  (score=0)
```python
        if type.is_cv_qualified and not type.is_reference:
```
L1271  ⚪  (score=0)
```python
            type = type.cv_base_type
```
L1272  ⚪  (score=0)
```python
        elif type.is_reference and not type.is_fake_reference:
```
L1273  ⚪  (score=0)
```python
            type = type.ref_base_type
```
L1274  ⚪  (score=0)
```python
        elif type.is_cfunction:
```
L1275  ⚪  (score=0)
```python
            from . import PyrexTypes
```
L1276  ⚪  (score=0)
```python
            type = PyrexTypes.c_ptr_type(type)  # A function itself isn't an l-value
```
L1277  ⚪  (score=0)
```python
        elif type.is_cpp_class and not type.is_fake_reference and self.scope.directives['cpp_locals']:
```
L1278  ⚪  (score=0)
```python
            self.scope.use_utility_code(UtilityCode.load_cached("OptionalLocals", "CppSupport.cpp"))
```
L1279  ⚪  (score=0)
```python
        if not type.needs_refcounting:
```
L1280  ⚪  (score=0)
```python
            # Make manage_ref canonical, so that manage_ref will always mean
```
L1281  ⚪  (score=0)
```python
            # a decref is needed.
```
L1282  ⚪  (score=0)
```python
            manage_ref = False
```
L1283  ⚪  (score=0)
```python
```
L1284  ⚪  (score=0)
```python
        freelist = self.temps_free.get((type, manage_ref))
```
L1285  ⚪  (score=0)
```python
        if reusable and freelist is not None and freelist[0]:
```
L1286  ⚪  (score=0)
```python
            result = freelist[0].pop()
```
L1287  ⚪  (score=0)
```python
            freelist[1].remove(result)
```
L1288  ⚪  (score=0)
```python
        else:
```
L1289  ⚪  (score=0)
```python
            while True:
```
L1290  ⚪  (score=0)
```python
                self.temp_counter += 1
```
L1291  ⚪  (score=0)
```python
                result = "%s%d" % (Naming.codewriter_temp_prefix, self.temp_counter)
```
L1292  ⚪  (score=0)
```python
                if result not in self.names_taken: break
```
L1293  ⚪  (score=0)
```python
            self.temps_allocated.append((result, type, manage_ref, static))
```
L1294  ⚪  (score=0)
```python
            if not reusable:
```
L1295  ⚪  (score=0)
```python
                self.zombie_temps.add(result)
```
L1296  ⚪  (score=0)
```python
        self.temps_used_type[result] = (type, manage_ref)
```
L1297  ⚪  (score=0)
```python
        if DebugFlags.debug_temp_code_comments:
```
L1298  ⚪  (score=0)
```python
            self.owner.putln("/* %s allocated (%s)%s */" % (result, type, "" if reusable else " - zombie"))
```
L1299  ⚪  (score=0)
```python
```
L1300  ⚪  (score=0)
```python
        if self.collect_temps_stack:
```
L1301  ⚪  (score=0)
```python
            self.collect_temps_stack[-1].add((result, type))
```
L1302  ⚪  (score=0)
```python
```
L1303  ⚪  (score=0)
```python
        return result
```
L1304  ⚪  (score=0)
```python
```
L1305  ⚪  (score=0)
```python
    def release_temp(self, name):
```
L1306  ⚪  (score=0)
```python
        """
```
L1307  ⚪  (score=0)
```python
        Releases a temporary so that it can be reused by other code needing
```
L1308  ⚪  (score=0)
```python
        a temp of the same type.
```
L1309  ⚪  (score=0)
```python
        """
```
L1310  ⚪  (score=0)
```python
        type, manage_ref = self.temps_used_type[name]
```
L1311  ⚪  (score=0)
```python
        freelist = self.temps_free.get((type, manage_ref))
```
L1312  ⚪  (score=0)
```python
        if freelist is None:
```
L1313  ⚪  (score=0)
```python
            freelist = ([], set())  # keep order in list and make lookups in set fast
```
L1314  ⚪  (score=0)
```python
            self.temps_free[(type, manage_ref)] = freelist
```
L1315  ⚪  (score=0)
```python
        if name in freelist[1]:
```
L1316  ⚪  (score=0)
```python
            raise RuntimeError("Temp %s freed twice!" % name)
```
L1317  ⚪  (score=0)
```python
        if name not in self.zombie_temps:
```
L1318  ⚪  (score=0)
```python
            freelist[0].append(name)
```
L1319  ⚪  (score=0)
```python
        freelist[1].add(name)
```
L1320  ⚪  (score=0)
```python
        if DebugFlags.debug_temp_code_comments:
```
L1321  ⚪  (score=0)
```python
            self.owner.putln("/* %s released %s*/" % (
```
L1322  ⚪  (score=0)
```python
                name, " - zombie" if name in self.zombie_temps else ""))
```
L1323  ⚪  (score=0)
```python
```
L1324  ⚪  (score=0)
```python
    def temps_in_use(self):
```
L1325  ⚪  (score=0)
```python
        """Return a list of (cname,type,manage_ref) tuples of temp names and their type
```
L1326  ⚪  (score=0)
```python
        that are currently in use.
```
L1327  ⚪  (score=0)
```python
        """
```
L1328  ⚪  (score=0)
```python
        used = []
```
L1329  ⚪  (score=0)
```python
        for name, type, manage_ref, static in self.temps_allocated:
```
L1330  ⚪  (score=0)
```python
            freelist = self.temps_free.get((type, manage_ref))
```
L1331  ⚪  (score=0)
```python
            if freelist is None or name not in freelist[1]:
```
L1332  ⚪  (score=0)
```python
                used.append((name, type, manage_ref and type.needs_refcounting))
```
L1333  ⚪  (score=0)
```python
        return used
```
L1334  ⚪  (score=0)
```python
```
L1335  ⚪  (score=0)
```python
    def temps_holding_reference(self):
```
L1336  ⚪  (score=0)
```python
        """Return a list of (cname,type) tuples of temp names and their type
```
L1337  ⚪  (score=0)
```python
        that are currently in use. This includes only temps
```
L1338  ⚪  (score=0)
```python
        with a reference counted type which owns its reference.
```
L1339  ⚪  (score=0)
```python
        """
```
L1340  ⚪  (score=0)
```python
        return [(name, type)
```
L1341  ⚪  (score=0)
```python
                for name, type, manage_ref in self.temps_in_use()
```
L1342  ⚪  (score=0)
```python
                if manage_ref and type.needs_refcounting]
```
L1343  ⚪  (score=0)
```python
```
L1344  ⚪  (score=0)
```python
    def all_managed_temps(self):
```
L1345  ⚪  (score=0)
```python
        """Return a list of (cname, type) tuples of refcount-managed Python objects.
```
L1346  ⚪  (score=0)
```python
        """
```
L1347  ⚪  (score=0)
```python
        return [(cname, type)
```
L1348  ⚪  (score=0)
```python
                for cname, type, manage_ref, static in self.temps_allocated
```
L1349  ⚪  (score=0)
```python
                if manage_ref]
```
L1350  ⚪  (score=0)
```python
```
L1351  ⚪  (score=0)
```python
    def all_free_managed_temps(self):
```
L1352  ⚪  (score=0)
```python
        """Return a list of (cname, type) tuples of refcount-managed Python
```
L1353  ⚪  (score=0)
```python
        objects that are not currently in use.  This is used by
```
L1354  ⚪  (score=0)
```python
        try-except and try-finally blocks to clean up temps in the
```
L1355  ⚪  (score=0)
```python
        error case.
```
L1356  ⚪  (score=0)
```python
        """
```
L1357  ⚪  (score=0)
```python
        return sorted([  # Enforce deterministic order.
```
L1358  ⚪  (score=0)
```python
            (cname, type)
```
L1359  ⚪  (score=0)
```python
            for (type, manage_ref), freelist in self.temps_free.items() if manage_ref
```
L1360  ⚪  (score=0)
```python
            for cname in freelist[0]
```
L1361  ⚪  (score=0)
```python
        ])
```
L1362  ⚪  (score=0)
```python
```
L1363  ⚪  (score=0)
```python
    def start_collecting_temps(self):
```
L1364  ⚪  (score=0)
```python
        """
```
L1365  ⚪  (score=0)
```python
        Useful to find out which temps were used in a code block
```
L1366  ⚪  (score=0)
```python
        """
```
L1367  ⚪  (score=0)
```python
        self.collect_temps_stack.append(set())
```
L1368  ⚪  (score=0)
```python
```
L1369  ⚪  (score=0)
```python
    def stop_collecting_temps(self):
```
L1370  ⚪  (score=0)
```python
        return self.collect_temps_stack.pop()
```
L1371  ⚪  (score=0)
```python
```
L1372  ⚪  (score=0)
```python
    def init_closure_temps(self, scope):
```
L1373  ⚪  (score=0)
```python
        self.closure_temps = ClosureTempAllocator(scope)
```
L1374  ⚪  (score=0)
```python
```
L1375  ⚪  (score=0)
```python
```
L1376  ⚪  (score=0)
```python
class NumConst:
```
L1377  ⚪  (score=0)
```python
    """Global info about a Python number constant held by GlobalState.
```
L1378  ⚪  (score=0)
```python
```
L1379  ⚪  (score=0)
```python
    cname       string
```
L1380  ⚪  (score=0)
```python
    value       string
```
L1381  ⚪  (score=0)
```python
    py_type     string     int, long, float
```
L1382  ⚪  (score=0)
```python
    value_code  string     evaluation code if different from value
```
L1383  ⚪  (score=0)
```python
    """
```
L1384  ⚪  (score=0)
```python
```
L1385  ⚪  (score=0)
```python
    def __init__(self, cname, value, py_type, value_code=None):
```
L1386  ⚪  (score=0)
```python
        self.cname = cname
```
L1387  ⚪  (score=0)
```python
        self.value = value
```
L1388  ⚪  (score=0)
```python
        self.py_type = py_type
```
L1389  ⚪  (score=0)
```python
        self.value_code = value_code or value
```
L1390  ⚪  (score=0)
```python
```
L1391  ⚪  (score=0)
```python
```
L1392  ⚪  (score=0)
```python
class PyObjectConst:
```
L1393  ⚪  (score=0)
```python
    """Global info about a generic constant held by GlobalState.
```
L1394  ⚪  (score=0)
```python
    """
```
L1395  ⚪  (score=0)
```python
    # cname       string
```
L1396  ⚪  (score=0)
```python
    # type        PyrexType
```
L1397  ⚪  (score=0)
```python
```
L1398  ⚪  (score=0)
```python
    def __init__(self, cname, type):
```
L1399  ⚪  (score=0)
```python
        self.cname = cname
```
L1400  ⚪  (score=0)
```python
        self.type = type
```
L1401  ⚪  (score=0)
```python
```
L1402  ⚪  (score=0)
```python
```
L1403  ⚪  (score=0)
```python
cython.declare(possible_unicode_identifier=object, possible_bytes_identifier=object,
```
L1404  ⚪  (score=0)
```python
               replace_identifier=object, find_alphanums=object)
```
L1405  ⚪  (score=0)
```python
possible_unicode_identifier = re.compile(r"(?![0-9])\w+$", re.U).match
```
L1406  ⚪  (score=0)
```python
possible_bytes_identifier = re.compile(br"(?![0-9])\w+$").match
```
L1407  ⚪  (score=0)
```python
replace_identifier = re.compile(r'[^a-zA-Z0-9_]+').sub
```
L1408  ⚪  (score=0)
```python
find_alphanums = re.compile('([a-zA-Z0-9]+)').findall
```
L1409  ⚪  (score=0)
```python
```
L1410  ⚪  (score=0)
```python
class StringConst:
```
L1411  ⚪  (score=0)
```python
    """Global info about a C string constant held by GlobalState.
```
L1412  ⚪  (score=0)
```python
    """
```
L1413  ⚪  (score=0)
```python
    # cname            string
```
L1414  ⚪  (score=0)
```python
    # text             EncodedString or BytesLiteral
```
L1415  ⚪  (score=0)
```python
    # escaped_value    str        The string value as C code byte sequence.
```
L1416  ⚪  (score=0)
```python
    # py_strings       {(identifier, encoding) : PyStringConst}
```
L1417  ⚪  (score=0)
```python
    # c_used           boolean  Is the plain C string used (or only the Python object?)
```
L1418  ⚪  (score=0)
```python
```
L1419  ⚪  (score=0)
```python
    def __init__(self, cname, text, byte_string):
```
L1420  ⚪  (score=0)
```python
        self.cname = cname
```
L1421  ⚪  (score=0)
```python
        self.text = text
```
L1422  ⚪  (score=0)
```python
        self.escaped_value = StringEncoding.escape_byte_string(byte_string)
```
L1423  ⚪  (score=0)
```python
        self.py_strings = None
```
L1424  ⚪  (score=0)
```python
        self.c_used = False
```
L1425  ⚪  (score=0)
```python
```
L1426  ⚪  (score=0)
```python
    def get_py_string_const(self, encoding, identifier=None):
```
L1427  ⚪  (score=0)
```python
        text = self.text
```
L1428  ⚪  (score=0)
```python
        intern: cython.bint
```
L1429  ⚪  (score=0)
```python
        is_unicode: cython.bint
```
L1430  ⚪  (score=0)
```python
```
L1431  ⚪  (score=0)
```python
        if identifier or encoding is None:
```
L1432  ⚪  (score=0)
```python
            # unicode string
```
L1433  ⚪  (score=0)
```python
            encoding = encoding_key = None
```
L1434  ⚪  (score=0)
```python
            is_unicode = True
```
L1435  ⚪  (score=0)
```python
        else:
```
L1436  ⚪  (score=0)
```python
            # bytes
```
L1437  ⚪  (score=0)
```python
            is_unicode = False
```
L1438  ⚪  (score=0)
```python
            encoding = encoding.lower()
```
L1439  ⚪  (score=0)
```python
            if encoding in ('utf8', 'utf-8', 'ascii', 'usascii', 'us-ascii'):
```
L1440  ⚪  (score=0)
```python
                encoding = None
```
L1441  ⚪  (score=0)
```python
                encoding_key = None
```
L1442  ⚪  (score=0)
```python
            else:
```
L1443  ⚪  (score=0)
```python
                encoding_key = ''.join(find_alphanums(encoding))
```
L1444  ⚪  (score=0)
```python
```
L1445  ⚪  (score=0)
```python
        if identifier:
```
L1446  ⚪  (score=0)
```python
            intern = True
```
L1447  ⚪  (score=0)
```python
        elif identifier is None:
```
L1448  ⚪  (score=0)
```python
            if isinstance(text, bytes):
```
L1449  ⚪  (score=0)
```python
                intern = bool(possible_bytes_identifier(text))
```
L1450  ⚪  (score=0)
```python
            else:
```
L1451  ⚪  (score=0)
```python
                intern = bool(possible_unicode_identifier(text))
```
L1452  ⚪  (score=0)
```python
        else:
```
L1453  ⚪  (score=0)
```python
            intern = False
```
L1454  ⚪  (score=0)
```python
```
L1455  ⚪  (score=0)
```python
        key = (intern, is_unicode, encoding_key)
```
L1456  ⚪  (score=0)
```python
        if self.py_strings is None:
```
L1457  ⚪  (score=0)
```python
            self.py_strings = {}
```
L1458  ⚪  (score=0)
```python
        else:
```
L1459  ⚪  (score=0)
```python
            try:
```
L1460  ⚪  (score=0)
```python
                return self.py_strings[key]
```
L1461  ⚪  (score=0)
```python
            except KeyError:
```
L1462  ⚪  (score=0)
```python
                pass
```
L1463  ⚪  (score=0)
```python
```
L1464  ⚪  (score=0)
```python
        pystring_cname = (
```
L1465  ⚪  (score=0)
```python
            f"{Naming.interned_prefixes['str'] if intern else Naming.py_const_prefix}"
```
L1466  ⚪  (score=0)
```python
            f"{'u' if is_unicode else 'b'}"
```
L1467  ⚪  (score=0)
```python
            f"{'_' + encoding_key if encoding_key else ''}"
```
L1468  ⚪  (score=0)
```python
            f"_{self.cname[len(Naming.const_prefix):]}"
```
L1469  ⚪  (score=0)
```python
        )
```
L1470  ⚪  (score=0)
```python
```
L1471  ⚪  (score=0)
```python
        py_string = PyStringConst(pystring_cname, encoding, intern, is_unicode)
```
L1472  ⚪  (score=0)
```python
        self.py_strings[key] = py_string
```
L1473  ⚪  (score=0)
```python
        return py_string
```
L1474  ⚪  (score=0)
```python
```
L1475  ⚪  (score=0)
```python
```
L1476  ⚪  (score=0)
```python
class PyStringConst:
```
L1477  ⚪  (score=0)
```python
    """Global info about a Python string constant held by GlobalState.
```
L1478  ⚪  (score=0)
```python
    """
```
L1479  ⚪  (score=0)
```python
    # cname       string
```
L1480  ⚪  (score=0)
```python
    # encoding    string
```
L1481  ⚪  (score=0)
```python
    # intern      boolean
```
L1482  ⚪  (score=0)
```python
    # is_unicode  boolean
```
L1483  ⚪  (score=0)
```python
```
L1484  ⚪  (score=0)
```python
    def __init__(self, cname, encoding, intern=False, is_unicode=False):
```
L1485  ⚪  (score=0)
```python
        self.cname = cname
```
L1486  ⚪  (score=0)
```python
        self.encoding = encoding
```
L1487  ⚪  (score=0)
```python
        self.is_unicode = is_unicode
```
L1488  ⚪  (score=0)
```python
        self.intern = intern
```
L1489  ⚪  (score=0)
```python
```
L1490  ⚪  (score=0)
```python
    def __lt__(self, other):
```
L1491  ⚪  (score=0)
```python
        return self.cname < other.cname
```
L1492  ⚪  (score=0)
```python
```
L1493  ⚪  (score=0)
```python
```
L1494  ⚪  (score=0)
```python
class GlobalState:
```
L1495  ⚪  (score=0)
```python
    # filename_table   {string : int}  for finding filename table indexes
```
L1496  ⚪  (score=0)
```python
    # filename_list    [string]        filenames in filename table order
```
L1497  ⚪  (score=0)
```python
    # input_file_contents dict         contents (=list of lines) of any file that was used as input
```
L1498  ⚪  (score=0)
```python
    #                                  to create this output C code.  This is
```
L1499  ⚪  (score=0)
```python
    #                                  used to annotate the comments.
```
L1500  ⚪  (score=0)
```python
    #
```
L1501  ⚪  (score=0)
```python
    # utility_codes   set                IDs of used utility code (to avoid reinsertion)
```
L1502  ⚪  (score=0)
```python
    #
```
L1503  ⚪  (score=0)
```python
    # declared_cnames  {string:Entry}  used in a transition phase to merge pxd-declared
```
L1504  ⚪  (score=0)
```python
    #                                  constants etc. into the pyx-declared ones (i.e,
```
L1505  ⚪  (score=0)
```python
    #                                  check if constants are already added).
```
L1506  ⚪  (score=0)
```python
    #                                  In time, hopefully the literals etc. will be
```
L1507  ⚪  (score=0)
```python
    #                                  supplied directly instead.
```
L1508  ⚪  (score=0)
```python
    #
```
L1509  ⚪  (score=0)
```python
    # const_cnames_used  dict          global counter for unique constant identifiers
```
L1510  ⚪  (score=0)
```python
    # shared_utility_functions         List of parsed declaration lines of the shared utility functions
```
L1511  ⚪  (score=0)
```python
```
L1512  ⚪  (score=0)
```python
    # parts            {string:CCodeWriter}
```
L1513  ⚪  (score=0)
```python
```
L1514  ⚪  (score=0)
```python
```
L1515  ⚪  (score=0)
```python
    # interned_strings
```
L1516  ⚪  (score=0)
```python
    # consts
```
L1517  ⚪  (score=0)
```python
    # interned_nums
```
L1518  ⚪  (score=0)
```python
```
L1519  ⚪  (score=0)
```python
    # directives       set             Temporary variable used to track
```
L1520  ⚪  (score=0)
```python
    #                                  the current set of directives in the code generation
```
L1521  ⚪  (score=0)
```python
    #                                  process.
```
L1522  ⚪  (score=0)
```python
```
L1523  ⚪  (score=0)
```python
    directives = {}
```
L1524  ⚪  (score=0)
```python
```
L1525  ⚪  (score=0)
```python
    code_layout = [
```
L1526  ⚪  (score=0)
```python
        'h_code',
```
L1527  ⚪  (score=0)
```python
        'filename_table',
```
L1528  ⚪  (score=0)
```python
        'utility_code_proto_before_types',
```
L1529  ⚪  (score=0)
```python
        'numeric_typedefs',           # Let these detailed individual parts stay!,
```
L1530  ⚪  (score=0)
```python
        'complex_type_declarations',  # as the proper solution is to make a full DAG...
```
L1531  ⚪  (score=0)
```python
        'type_declarations',          # More coarse-grained blocks would simply hide
```
L1532  ⚪  (score=0)
```python
        'utility_code_proto',         # the ugliness, not fix it
```
L1533  ⚪  (score=0)
```python
        'module_declarations',
```
L1534  ⚪  (score=0)
```python
        'typeinfo',
```
L1535  ⚪  (score=0)
```python
        'before_global_var',
```
L1536  ⚪  (score=0)
```python
        'global_var',
```
L1537  ⚪  (score=0)
```python
        'string_decls',
```
L1538  ⚪  (score=0)
```python
        # Make the string name macros (``__pyx_n_*`` / ``__pyx_k_*``) available
```
L1539  ⚪  (score=0)
```python
        # before we emit any of the static fast-arg metadata that references
```
L1540  ⚪  (score=0)
```python
        # them in the ``decls`` section.
```
L1541  ⚪  (score=0)
```python
        'constant_name_defines',
```
L1542  ⚪  (score=0)
```python
        'decls',
```
L1543  ⚪  (score=0)
```python
        'late_includes',
```
L1544  ⚪  (score=0)
```python
        'module_state',
```
L1545  ⚪  (score=0)
```python
        'module_state_contents',  # can be used to inject declarations into the modulestate struct
```
L1546  ⚪  (score=0)
```python
        'module_state_end',
```
L1547  ⚪  (score=0)
```python
        'module_state_clear',
```
L1548  ⚪  (score=0)
```python
        'module_state_clear_contents',
```
L1549  ⚪  (score=0)
```python
        'module_state_clear_end',
```
L1550  ⚪  (score=0)
```python
        'module_state_traverse',
```
L1551  ⚪  (score=0)
```python
        'module_state_traverse_contents',
```
L1552  ⚪  (score=0)
```python
        'module_state_traverse_end',
```
L1553  ⚪  (score=0)
```python
        'module_code',  # user code goes here
```
L1554  ⚪  (score=0)
```python
        'module_exttypes',
```
L1555  ⚪  (score=0)
```python
        'initfunc_declarations',
```
L1556  ⚪  (score=0)
```python
        'init_module',
```
L1557  ⚪  (score=0)
```python
        'pystring_table',
```
L1558  ⚪  (score=0)
```python
        'cached_builtins',
```
L1559  ⚪  (score=0)
```python
        'cached_constants',
```
L1560  ⚪  (score=0)
```python
        'init_constants',
```
L1561  ⚪  (score=0)
```python
        'init_codeobjects',
```
L1562  ⚪  (score=0)
```python
        'init_globals',  # (utility code called at init-time)
```
L1563  ⚪  (score=0)
```python
        'cleanup_globals',
```
L1564  ⚪  (score=0)
```python
        'cleanup_module',
```
L1565  ⚪  (score=0)
```python
        'main_method',
```
L1566  ⚪  (score=0)
```python
        'utility_code_pragmas',  # silence some irrelevant warnings in utility code
```
L1567  ⚪  (score=0)
```python
        'utility_code_def',
```
L1568  ⚪  (score=0)
```python
        'utility_code_pragmas_end',  # clean-up the utility_code_pragmas
```
L1569  ⚪  (score=0)
```python
        'end'
```
L1570  ⚪  (score=0)
```python
    ]
```
L1571  ⚪  (score=0)
```python
```
L1572  ⚪  (score=0)
```python
    # h files can only have a much smaller list of sections
```
L1573  ⚪  (score=0)
```python
    h_code_layout = [
```
L1574  ⚪  (score=0)
```python
        'h_code',
```
L1575  ⚪  (score=0)
```python
        'utility_code_proto_before_types',
```
L1576  ⚪  (score=0)
```python
        'type_declarations',
```
L1577  ⚪  (score=0)
```python
        'utility_code_proto',
```
L1578  ⚪  (score=0)
```python
        'end'
```
L1579  ⚪  (score=0)
```python
    ]
```
L1580  ⚪  (score=0)
```python
```
L1581  ⚪  (score=0)
```python
    def __init__(self, writer, module_node, code_config, common_utility_include_dir=None):
```
L1582  ⚪  (score=0)
```python
        self.filename_table = {}
```
L1583  ⚪  (score=0)
```python
        self.filename_list = []
```
L1584  ⚪  (score=0)
```python
        self.input_file_contents = {}
```
L1585  ⚪  (score=0)
```python
        self.utility_codes = set()
```
L1586  ⚪  (score=0)
```python
        self.declared_cnames = {}
```
L1587  ⚪  (score=0)
```python
        self.in_utility_code_generation = False
```
L1588  ⚪  (score=0)
```python
        self.code_config = code_config
```
L1589  ⚪  (score=0)
```python
        self.common_utility_include_dir = common_utility_include_dir
```
L1590  ⚪  (score=0)
```python
        self.parts:dict[str, CCodeWriter] = {}
```
L1591  ⚪  (score=0)
```python
        self.module_node = module_node  # because some utility code generation needs it
```
L1592  ⚪  (score=0)
```python
                                        # (generating backwards-compatible Get/ReleaseBuffer
```
L1593  ⚪  (score=0)
```python
```
L1594  ⚪  (score=0)
```python
        self.const_cnames_used = {}
```
L1595  ⚪  (score=0)
```python
        self.string_const_index = {}
```
L1596  ⚪  (score=0)
```python
        self.dedup_const_index = {}
```
L1597  ⚪  (score=0)
```python
        self.pyunicode_ptr_const_index = {}
```
L1598  ⚪  (score=0)
```python
        self.codeobject_constants = []
```
L1599  ⚪  (score=0)
```python
        self.num_const_index = {}
```
L1600  ⚪  (score=0)
```python
        self.arg_default_constants = []
```
L1601  ⚪  (score=0)
```python
        self.const_array_counters = {}  # counts of differently prefixed arrays of constants
```
L1602  ⚪  (score=0)
```python
        self.cached_cmethods = {}
```
L1603  ⚪  (score=0)
```python
        self.initialised_constants = set()
```
L1604  ⚪  (score=0)
```python
        self.shared_utility_functions = []
```
L1605  ⚪  (score=0)
```python
```
L1606  ⚪  (score=0)
```python
        writer.set_global_state(self)
```
L1607  ⚪  (score=0)
```python
        self.rootwriter = writer
```
L1608  ⚪  (score=0)
```python
```
L1609  ⚪  (score=0)
```python
    def initialize_main_c_code(self):
```
L1610  ⚪  (score=0)
```python
        rootwriter = self.rootwriter
```
L1611  ⚪  (score=0)
```python
        for i, part in enumerate(self.code_layout):
```
L1612  ⚪  (score=0)
```python
            w = self.parts[part] = rootwriter.insertion_point()
```
L1613  ⚪  (score=0)
```python
            if i > 0:
```
L1614  ⚪  (score=0)
```python
                w.putln("/* #### Code section: %s ### */" % part)
```
L1615  ⚪  (score=0)
```python
```
L1616  ⚪  (score=0)
```python
        w = self.parts['cached_builtins']
```
L1617  ⚪  (score=0)
```python
        w.start_initcfunc(
```
L1618  ⚪  (score=0)
```python
            "int __Pyx_InitCachedBuiltins("
```
L1619  ⚪  (score=0)
```python
            f"{Naming.modulestatetype_cname} *{Naming.modulestatevalue_cname})")
```
L1620  ⚪  (score=0)
```python
        w.putln(f"CYTHON_UNUSED_VAR({Naming.modulestatevalue_cname});")
```
L1621  ⚪  (score=0)
```python
```
L1622  ⚪  (score=0)
```python
        w = self.parts['cached_constants']
```
L1623  ⚪  (score=0)
```python
        w.start_initcfunc(
```
L1624  ⚪  (score=0)
```python
            "int __Pyx_InitCachedConstants("
```
L1625  ⚪  (score=0)
```python
            f"{Naming.modulestatetype_cname} *{Naming.modulestatevalue_cname})",
```
L1626  ⚪  (score=0)
```python
            refnanny=True)
```
L1627  ⚪  (score=0)
```python
        w.putln(f"CYTHON_UNUSED_VAR({Naming.modulestatevalue_cname});")
```
L1628  ⚪  (score=0)
```python
        w.put_setup_refcount_context(StringEncoding.EncodedString("__Pyx_InitCachedConstants"))
```
L1629  ⚪  (score=0)
```python
```
L1630  ⚪  (score=0)
```python
        w = self.parts['init_globals']
```
L1631  ⚪  (score=0)
```python
        w.start_initcfunc("int __Pyx_InitGlobals(void)")
```
L1632  ⚪  (score=0)
```python
```
L1633  ⚪  (score=0)
```python
        w = self.parts['init_constants']
```
L1634  ⚪  (score=0)
```python
        w.start_initcfunc(
```
L1635  ⚪  (score=0)
```python
            "int __Pyx_InitConstants("
```
L1636  ⚪  (score=0)
```python
            f"{Naming.modulestatetype_cname} *{Naming.modulestatevalue_cname})")
```
L1637  ⚪  (score=0)
```python
        w.putln(f"CYTHON_UNUSED_VAR({Naming.modulestatevalue_cname});")
```
L1638  ⚪  (score=0)
```python
```
L1639  ⚪  (score=0)
```python
        if not Directives.generate_cleanup_code:
```
L1640  ⚪  (score=0)
```python
            del self.parts['cleanup_globals']
```
L1641  ⚪  (score=0)
```python
        else:
```
L1642  ⚪  (score=0)
```python
            w = self.parts['cleanup_globals']
```
L1643  ⚪  (score=0)
```python
            w.start_initcfunc(
```
L1644  ⚪  (score=0)
```python
                "void __Pyx_CleanupGlobals("
```
L1645  ⚪  (score=0)
```python
                f"{Naming.modulestatetype_cname} *{Naming.modulestatevalue_cname})")
```
L1646  ⚪  (score=0)
```python
            w.putln(f"CYTHON_UNUSED_VAR({Naming.modulestatevalue_cname});")
```
L1647  ⚪  (score=0)
```python
```
L1648  ⚪  (score=0)
```python
        code = self.parts['utility_code_proto']
```
L1649  ⚪  (score=0)
```python
        code.putln("")
```
L1650  ⚪  (score=0)
```python
        code.putln("/* --- Runtime support code (head) --- */")
```
L1651  ⚪  (score=0)
```python
```
L1652  ⚪  (score=0)
```python
        code = self.parts['utility_code_def']
```
L1653  ⚪  (score=0)
```python
        if self.code_config.emit_linenums:
```
L1654  ⚪  (score=0)
```python
            code.write('\n#line 1 "cython_utility"\n')
```
L1655  ⚪  (score=0)
```python
        code.putln("")
```
L1656  ⚪  (score=0)
```python
        code.putln("/* --- Runtime support code --- */")
```
L1657  ⚪  (score=0)
```python
```
L1658  ⚪  (score=0)
```python
    def initialize_main_h_code(self):
```
L1659  ⚪  (score=0)
```python
        rootwriter = self.rootwriter
```
L1660  ⚪  (score=0)
```python
        for part in self.h_code_layout:
```
L1661  ⚪  (score=0)
```python
            self.parts[part] = rootwriter.insertion_point()
```
L1662  ⚪  (score=0)
```python
```
L1663  ⚪  (score=0)
```python
    def finalize_main_c_code(self):
```
L1664  ⚪  (score=0)
```python
        self.close_global_decls()
```
L1665  ⚪  (score=0)
```python
```
L1666  ⚪  (score=0)
```python
        #
```
L1667  ⚪  (score=0)
```python
        # utility_code_def
```
L1668  ⚪  (score=0)
```python
        #
```
L1669  ⚪  (score=0)
```python
        code = self.parts['utility_code_def']
```
L1670  ⚪  (score=0)
```python
        util = TempitaUtilityCode.load_cached("TypeConversions", "TypeConversion.c")
```
L1671  ⚪  (score=0)
```python
        code.put(util.format_code(util.impl))
```
L1672  ⚪  (score=0)
```python
        code.putln("")
```
L1673  ⚪  (score=0)
```python
```
L1674  ⚪  (score=0)
```python
        #
```
L1675  ⚪  (score=0)
```python
        # utility code pragmas
```
L1676  ⚪  (score=0)
```python
        #
```
L1677  ⚪  (score=0)
```python
        code = self.parts['utility_code_pragmas']
```
L1678  ⚪  (score=0)
```python
        util = UtilityCode.load_cached("UtilityCodePragmas", "ModuleSetupCode.c")
```
L1679  ⚪  (score=0)
```python
        code.putln(util.format_code(util.impl))
```
L1680  ⚪  (score=0)
```python
        code.putln("")
```
L1681  ⚪  (score=0)
```python
        code = self.parts['utility_code_pragmas_end']
```
L1682  ⚪  (score=0)
```python
        util = UtilityCode.load_cached("UtilityCodePragmasEnd", "ModuleSetupCode.c")
```
L1683  ⚪  (score=0)
```python
        code.putln(util.format_code(util.impl))
```
L1684  ⚪  (score=0)
```python
        code.putln("")
```
L1685  ⚪  (score=0)
```python
```
L1686  ⚪  (score=0)
```python
    def __getitem__(self, key):
```
L1687  ⚪  (score=0)
```python
        return self.parts[key]
```
L1688  ⚪  (score=0)
```python
```
L1689  ⚪  (score=0)
```python
    #
```
L1690  ⚪  (score=0)
```python
    # Global constants, interned objects, etc.
```
L1691  ⚪  (score=0)
```python
    #
```
L1692  ⚪  (score=0)
```python
    def close_global_decls(self):
```
L1693  ⚪  (score=0)
```python
        # This is called when it is known that no more global declarations will
```
L1694  ⚪  (score=0)
```python
        # declared.
```
L1695  ⚪  (score=0)
```python
        self.generate_const_declarations()
```
L1696  ⚪  (score=0)
```python
```
L1697  ⚪  (score=0)
```python
        w = self.parts['cached_builtins']
```
L1698  ⚪  (score=0)
```python
        w.putln("return 0;")
```
L1699  ⚪  (score=0)
```python
        if w.label_used(w.error_label):
```
L1700  ⚪  (score=0)
```python
            w.put_label(w.error_label)
```
L1701  ⚪  (score=0)
```python
            w.putln("return -1;")
```
L1702  ⚪  (score=0)
```python
        w.putln("}")
```
L1703  ⚪  (score=0)
```python
        w.exit_cfunc_scope()
```
L1704  ⚪  (score=0)
```python
```
L1705  ⚪  (score=0)
```python
        w = self.parts['cached_constants']
```
L1706  ⚪  (score=0)
```python
        for const_type in ["tuple", "slice"]:
```
L1707  ⚪  (score=0)
```python
            if const_type in self.const_array_counters:
```
L1708  ⚪  (score=0)
```python
                self.immortalize_constants(
```
L1709  ⚪  (score=0)
```python
                    w.name_in_module_state(Naming.pyrex_prefix + const_type),
```
L1710  ⚪  (score=0)
```python
                    self.const_array_counters[const_type],
```
L1711  ⚪  (score=0)
```python
                    w)
```
L1712  ⚪  (score=0)
```python
        w.put_finish_refcount_context()
```
L1713  ⚪  (score=0)
```python
        w.putln("return 0;")
```
L1714  ⚪  (score=0)
```python
        if w.label_used(w.error_label):
```
L1715  ⚪  (score=0)
```python
            w.put_label(w.error_label)
```
L1716  ⚪  (score=0)
```python
            w.put_finish_refcount_context()
```
L1717  ⚪  (score=0)
```python
            w.putln("return -1;")
```
L1718  ⚪  (score=0)
```python
        w.putln("}")
```
L1719  ⚪  (score=0)
```python
        w.exit_cfunc_scope()
```
L1720  ⚪  (score=0)
```python
```
L1721  ⚪  (score=0)
```python
        for part in ['init_globals', 'init_constants']:
```
L1722  ⚪  (score=0)
```python
            w = self.parts[part]
```
L1723  ⚪  (score=0)
```python
            w.putln("return 0;")
```
L1724  ⚪  (score=0)
```python
            if w.label_used(w.error_label):
```
L1725  ⚪  (score=0)
```python
                w.put_label(w.error_label)
```
L1726  ⚪  (score=0)
```python
                w.putln("return -1;")
```
L1727  ⚪  (score=0)
```python
            w.putln("}")
```
L1728  ⚪  (score=0)
```python
            w.exit_cfunc_scope()
```
L1729  ⚪  (score=0)
```python
```
L1730  ⚪  (score=0)
```python
        if Directives.generate_cleanup_code:
```
L1731  ⚪  (score=0)
```python
            w = self.parts['cleanup_globals']
```
L1732  ⚪  (score=0)
```python
            w.putln("}")
```
L1733  ⚪  (score=0)
```python
            w.exit_cfunc_scope()
```
L1734  ⚪  (score=0)
```python
```
L1735  ⚪  (score=0)
```python
        if Directives.generate_cleanup_code:
```
L1736  ⚪  (score=0)
```python
            w = self.parts['cleanup_module']
```
L1737  ⚪  (score=0)
```python
            w.putln("}")
```
L1738  ⚪  (score=0)
```python
            w.exit_cfunc_scope()
```
L1739  ⚪  (score=0)
```python
```
L1740  ⚪  (score=0)
```python
    def put_pyobject_decl(self, entry):
```
L1741  ⚪  (score=0)
```python
        self['global_var'].putln("static PyObject *%s;" % entry.cname)
```
L1742  ⚪  (score=0)
```python
```
L1743  ⚪  (score=0)
```python
    # constant handling at code generation time
```
L1744  ⚪  (score=0)
```python
```
L1745  ⚪  (score=0)
```python
    def get_cached_constants_writer(self, target=None):
```
L1746  ⚪  (score=0)
```python
        if target is not None:
```
L1747  ⚪  (score=0)
```python
            if target in self.initialised_constants:
```
L1748  ⚪  (score=0)
```python
                # Return None on second/later calls to prevent duplicate creation code.
```
L1749  ⚪  (score=0)
```python
                return None
```
L1750  ⚪  (score=0)
```python
            self.initialised_constants.add(target)
```
L1751  ⚪  (score=0)
```python
        return self.parts['cached_constants']
```
L1752  ⚪  (score=0)
```python
```
L1753  ⚪  (score=0)
```python
    def get_int_const(self, str_value, longness=False):
```
L1754  ⚪  (score=0)
```python
        py_type = longness and 'long' or 'int'
```
L1755  ⚪  (score=0)
```python
        try:
```
L1756  ⚪  (score=0)
```python
            c = self.num_const_index[(str_value, py_type)]
```
L1757  ⚪  (score=0)
```python
        except KeyError:
```
L1758  ⚪  (score=0)
```python
            c = self.new_num_const(str_value, py_type)
```
L1759  ⚪  (score=0)
```python
        return c
```
L1760  ⚪  (score=0)
```python
```
L1761  ⚪  (score=0)
```python
    def get_float_const(self, str_value, value_code):
```
L1762  ⚪  (score=0)
```python
        try:
```
L1763  ⚪  (score=0)
```python
            c = self.num_const_index[(str_value, 'float')]
```
L1764  ⚪  (score=0)
```python
        except KeyError:
```
L1765  ⚪  (score=0)
```python
            c = self.new_num_const(str_value, 'float', value_code)
```
L1766  ⚪  (score=0)
```python
        return c
```
L1767  ⚪  (score=0)
```python
```
L1768  ⚪  (score=0)
```python
    def get_py_const(self, prefix, dedup_key=None):
```
L1769  ⚪  (score=0)
```python
        if dedup_key is not None:
```
L1770  ⚪  (score=0)
```python
            const = self.dedup_const_index.get(dedup_key)
```
L1771  ⚪  (score=0)
```python
            if const is not None:
```
L1772  ⚪  (score=0)
```python
                return const
```
L1773  ⚪  (score=0)
```python
        const = self.new_array_const_cname(prefix)
```
L1774  ⚪  (score=0)
```python
        if dedup_key is not None:
```
L1775  ⚪  (score=0)
```python
            self.dedup_const_index[dedup_key] = const
```
L1776  ⚪  (score=0)
```python
        return const
```
L1777  ⚪  (score=0)
```python
```
L1778  ⚪  (score=0)
```python
    def get_argument_default_const(self, type):
```
L1779  ⚪  (score=0)
```python
        cname = self.new_const_cname('')
```
L1780  ⚪  (score=0)
```python
        c = PyObjectConst(cname, type)
```
L1781  ⚪  (score=0)
```python
        self.arg_default_constants.append(c)
```
L1782  ⚪  (score=0)
```python
        # Argument default constants aren't currently cleaned up.
```
L1783  ⚪  (score=0)
```python
        # If that changes, it needs to account for the fact that they
```
L1784  ⚪  (score=0)
```python
        # aren't just Python objects
```
L1785  ⚪  (score=0)
```python
        return c
```
L1786  ⚪  (score=0)
```python
```
L1787  ⚪  (score=0)
```python
    def get_string_const(self, text, c_used=True):
```
L1788  ⚪  (score=0)
```python
        # return a C string constant, creating a new one if necessary
```
L1789  ⚪  (score=0)
```python
        if text.is_unicode:
```
L1790  ⚪  (score=0)
```python
            byte_string = text.utf8encode()
```
L1791  ⚪  (score=0)
```python
        else:
```
L1792  ⚪  (score=0)
```python
            byte_string = text.byteencode()
```
L1793  ⚪  (score=0)
```python
        try:
```
L1794  ⚪  (score=0)
```python
            c = self.string_const_index[byte_string]
```
L1795  ⚪  (score=0)
```python
        except KeyError:
```
L1796  ⚪  (score=0)
```python
            c = self.new_string_const(text, byte_string)
```
L1797  ⚪  (score=0)
```python
        if c_used:
```
L1798  ⚪  (score=0)
```python
            c.c_used = True
```
L1799  ⚪  (score=0)
```python
        return c
```
L1800  ⚪  (score=0)
```python
```
L1801  ⚪  (score=0)
```python
    def get_pyunicode_ptr_const(self, text):
```
L1802  ⚪  (score=0)
```python
        # return a Py_UNICODE[] constant, creating a new one if necessary
```
L1803  ⚪  (score=0)
```python
        assert text.is_unicode
```
L1804  ⚪  (score=0)
```python
        try:
```
L1805  ⚪  (score=0)
```python
            c = self.pyunicode_ptr_const_index[text]
```
L1806  ⚪  (score=0)
```python
        except KeyError:
```
L1807  ⚪  (score=0)
```python
            c = self.pyunicode_ptr_const_index[text] = self.new_const_cname()
```
L1808  ⚪  (score=0)
```python
        return c
```
L1809  ⚪  (score=0)
```python
```
L1810  ⚪  (score=0)
```python
    def get_py_string_const(self, text, identifier=None):
```
L1811  ⚪  (score=0)
```python
        # return a Python string constant, creating a new one if necessary
```
L1812  ⚪  (score=0)
```python
        c_string: StringConst = self.get_string_const(text, c_used=False)
```
L1813  ⚪  (score=0)
```python
        py_string = c_string.get_py_string_const(text.encoding, identifier)
```
L1814  ⚪  (score=0)
```python
        return py_string
```
L1815  ⚪  (score=0)
```python
```
L1816  ⚪  (score=0)
```python
    def get_py_codeobj_const(self, node):
```
L1817  ⚪  (score=0)
```python
        idx = len(self.codeobject_constants)
```
L1818  ⚪  (score=0)
```python
        name = f"{Naming.codeobjtab_cname}[{idx}]"
```
L1819  ⚪  (score=0)
```python
        self.codeobject_constants.append(node)
```
L1820  ⚪  (score=0)
```python
        return name
```
L1821  ⚪  (score=0)
```python
```
L1822  ⚪  (score=0)
```python
    def get_interned_identifier(self, text):
```
L1823  ⚪  (score=0)
```python
        return self.get_py_string_const(text, identifier=True)
```
L1824  ⚪  (score=0)
```python
```
L1825  ⚪  (score=0)
```python
    def new_string_const(self, text, byte_string):
```
L1826  ⚪  (score=0)
```python
        cname = self.new_string_const_cname(byte_string)
```
L1827  ⚪  (score=0)
```python
        c = StringConst(cname, text, byte_string)
```
L1828  ⚪  (score=0)
```python
        self.string_const_index[byte_string] = c
```
L1829  ⚪  (score=0)
```python
        return c
```
L1830  ⚪  (score=0)
```python
```
L1831  ⚪  (score=0)
```python
    def new_num_const(self, value, py_type, value_code=None):
```
L1832  ⚪  (score=0)
```python
        cname = self.new_num_const_cname(value, py_type)
```
L1833  ⚪  (score=0)
```python
        c = NumConst(cname, value, py_type, value_code)
```
L1834  ⚪  (score=0)
```python
        self.num_const_index[(value, py_type)] = c
```
L1835  ⚪  (score=0)
```python
        return c
```
L1836  ⚪  (score=0)
```python
```
L1837  ⚪  (score=0)
```python
    def new_string_const_cname(self, bytes_value):
```
L1838  ⚪  (score=0)
```python
        # Create a new globally-unique nice name for a C string constant.
```
L1839  ⚪  (score=0)
```python
        value = bytes_value.decode('ASCII', 'ignore')
```
L1840  ⚪  (score=0)
```python
        return self.new_const_cname(value=value)
```
L1841  ⚪  (score=0)
```python
```
L1842  ⚪  (score=0)
```python
    def unique_const_cname(self, format_str):  # type: (str) -> str
```
L1843  ⚪  (score=0)
```python
        used = self.const_cnames_used
```
L1844  ⚪  (score=0)
```python
        cname = value = format_str.format(sep='', counter='')
```
L1845  ⚪  (score=0)
```python
        while cname in used:
```
L1846  ⚪  (score=0)
```python
            counter = used[value] = used[value] + 1
```
L1847  ⚪  (score=0)
```python
            cname = format_str.format(sep='_', counter=counter)
```
L1848  ⚪  (score=0)
```python
        used[cname] = 1
```
L1849  ⚪  (score=0)
```python
        return cname
```
L1850  ⚪  (score=0)
```python
```
L1851  ⚪  (score=0)
```python
    def new_num_const_cname(self, value, py_type):  # type: (str, str) -> str
```
L1852  ⚪  (score=0)
```python
        if py_type == 'long':
```
L1853  ⚪  (score=0)
```python
            value += 'L'
```
L1854  ⚪  (score=0)
```python
            py_type = 'int'
```
L1855  ⚪  (score=0)
```python
        prefix = Naming.interned_prefixes[py_type]
```
L1856  ⚪  (score=0)
```python
```
L1857  ⚪  (score=0)
```python
        value = value.replace('.', '_').replace('+', '_').replace('-', 'neg_')
```
L1858  ⚪  (score=0)
```python
        if len(value) > 42:
```
L1859  ⚪  (score=0)
```python
            # update tests/run/large_integer_T5290.py in case the amount is changed
```
L1860  ⚪  (score=0)
```python
            cname = self.unique_const_cname(
```
L1861  ⚪  (score=0)
```python
                prefix + "large{counter}_" + value[:18] + "_xxx_" + value[-18:])
```
L1862  ⚪  (score=0)
```python
        else:
```
L1863  ⚪  (score=0)
```python
            cname = "%s%s" % (prefix, value)
```
L1864  ⚪  (score=0)
```python
        return cname
```
L1865  ⚪  (score=0)
```python
```
L1866  ⚪  (score=0)
```python
    def new_const_cname(self, prefix='', value=''):
```
L1867  ⚪  (score=0)
```python
        value = replace_identifier('_', value)[:32].strip('_')
```
L1868  ⚪  (score=0)
```python
        name_suffix = self.unique_const_cname(value + "{sep}{counter}")
```
L1869  ⚪  (score=0)
```python
        if prefix:
```
L1870  ⚪  (score=0)
```python
            prefix = Naming.interned_prefixes[prefix]
```
L1871  ⚪  (score=0)
```python
        else:
```
L1872  ⚪  (score=0)
```python
            prefix = Naming.const_prefix
```
L1873  ⚪  (score=0)
```python
        return "%s%s" % (prefix, name_suffix)
```
L1874  ⚪  (score=0)
```python
```
L1875  ⚪  (score=0)
```python
    def new_array_const_cname(self, prefix: str):
```
L1876  ⚪  (score=0)
```python
        count = self.const_array_counters.get(prefix, 0)
```
L1877  ⚪  (score=0)
```python
        self.const_array_counters[prefix] = count+1
```
L1878  ⚪  (score=0)
```python
        return f"{Naming.pyrex_prefix}{prefix}[{count}]"
```
L1879  ⚪  (score=0)
```python
```
L1880  ⚪  (score=0)
```python
    def get_cached_unbound_method(self, type_cname, method_name):
```
L1881  ⚪  (score=0)
```python
        key = (type_cname, method_name)
```
L1882  ⚪  (score=0)
```python
        try:
```
L1883  ⚪  (score=0)
```python
            cname = self.cached_cmethods[key]
```
L1884  ⚪  (score=0)
```python
        except KeyError:
```
L1885  ⚪  (score=0)
```python
            cname = self.cached_cmethods[key] = self.new_const_cname(
```
L1886  ⚪  (score=0)
```python
                'umethod', '%s_%s' % (type_cname, method_name))
```
L1887  ⚪  (score=0)
```python
        return cname
```
L1888  ⚪  (score=0)
```python
```
L1889  ⚪  (score=0)
```python
    def cached_unbound_method_call_code(self, modulestate_cname, obj_cname, type_cname, method_name, arg_cnames):
```
L1890  ⚪  (score=0)
```python
        # admittedly, not the best place to put this method, but it is reused by UtilityCode and ExprNodes ...
```
L1891  ⚪  (score=0)
```python
        utility_code_name = "CallUnboundCMethod%d" % len(arg_cnames)
```
L1892  ⚪  (score=0)
```python
        self.use_utility_code(UtilityCode.load_cached(utility_code_name, "ObjectHandling.c"))
```
L1893  ⚪  (score=0)
```python
        cache_cname = self.get_cached_unbound_method(type_cname, method_name)
```
L1894  ⚪  (score=0)
```python
        args = [obj_cname] + arg_cnames
```
L1895  ⚪  (score=0)
```python
        return "__Pyx_%s(&%s%s, %s)" % (
```
L1896  ⚪  (score=0)
```python
            utility_code_name,
```
L1897  ⚪  (score=0)
```python
            modulestate_cname,
```
L1898  ⚪  (score=0)
```python
            cache_cname,
```
L1899  ⚪  (score=0)
```python
            ', '.join(args),
```
L1900  ⚪  (score=0)
```python
        )
```
L1901  ⚪  (score=0)
```python
```
L1902  ⚪  (score=0)
```python
    def add_cached_builtin_decl(self, entry):
```
L1903  ⚪  (score=0)
```python
        if entry.is_builtin and entry.is_const:
```
L1904  ⚪  (score=0)
```python
            if self.should_declare(entry.cname, entry):
```
L1905  ⚪  (score=0)
```python
                self.put_pyobject_decl(entry)
```
L1906  ⚪  (score=0)
```python
                name = entry.name
```
L1907  ⚪  (score=0)
```python
                if name in renamed_py2_builtins_map:
```
L1908  ⚪  (score=0)
```python
                    name = renamed_py2_builtins_map[name]
```
L1909  ⚪  (score=0)
```python
                self.put_cached_builtin_init(
```
L1910  ⚪  (score=0)
```python
                    entry.pos, StringEncoding.EncodedString(name),
```
L1911  ⚪  (score=0)
```python
                    entry.cname)
```
L1912  ⚪  (score=0)
```python
```
L1913  ⚪  (score=0)
```python
    def put_cached_builtin_init(self, pos, name, cname):
```
L1914  ⚪  (score=0)
```python
        w = self.parts['cached_builtins']
```
L1915  ⚪  (score=0)
```python
        cname_in_modulestate = w.name_in_main_c_code_module_state(
```
L1916  ⚪  (score=0)
```python
            self.get_interned_identifier(name).cname)
```
L1917  ⚪  (score=0)
```python
        self.use_utility_code(
```
L1918  ⚪  (score=0)
```python
            UtilityCode.load_cached("GetBuiltinName", "ObjectHandling.c"))
```
L1919  ⚪  (score=0)
```python
        w.putln('%s = __Pyx_GetBuiltinName(%s); if (!%s) %s' % (
```
L1920  ⚪  (score=0)
```python
            cname,
```
L1921  ⚪  (score=0)
```python
            cname_in_modulestate,
```
L1922  ⚪  (score=0)
```python
            cname,
```
L1923  ⚪  (score=0)
```python
            w.error_goto(pos)))
```
L1924  ⚪  (score=0)
```python
```
L1925  ⚪  (score=0)
```python
    def generate_const_declarations(self):
```
L1926  ⚪  (score=0)
```python
        self.generate_cached_methods_decls()
```
L1927  ⚪  (score=0)
```python
        self.generate_object_constant_decls()
```
L1928  ⚪  (score=0)
```python
        self.generate_codeobject_constants()
```
L1929  ⚪  (score=0)
```python
        # generate code for string and numeric constants as late as possible
```
L1930  ⚪  (score=0)
```python
        # to allow new constants be to created by the earlier stages.
```
L1931  ⚪  (score=0)
```python
        # (although the constants themselves are written early)
```
L1932  ⚪  (score=0)
```python
        self.generate_string_constants()
```
L1933  ⚪  (score=0)
```python
        self.generate_num_constants()
```
L1934  ⚪  (score=0)
```python
```
L1935  ⚪  (score=0)
```python
    def _generate_module_array_traverse_and_clear(self, struct_attr_cname, count, may_have_refcycles=True):
```
L1936  ⚪  (score=0)
```python
        counter_type = 'int' if count < 2**15 else 'Py_ssize_t'
```
L1937  ⚪  (score=0)
```python
        visit_call = "Py_VISIT" if may_have_refcycles else "__Pyx_VISIT_CONST"
```
L1938  ⚪  (score=0)
```python
```
L1939  ⚪  (score=0)
```python
        writer = self.parts['module_state_traverse']
```
L1940  ⚪  (score=0)
```python
        writer.putln(f"for ({counter_type} i=0; i<{count}; ++i) {{ {visit_call}(traverse_module_state->{struct_attr_cname}[i]); }}")
```
L1941  ⚪  (score=0)
```python
```
L1942  ⚪  (score=0)
```python
        writer = self.parts['module_state_clear']
```
L1943  ⚪  (score=0)
```python
        writer.putln(f"for ({counter_type} i=0; i<{count}; ++i) {{ Py_CLEAR(clear_module_state->{struct_attr_cname}[i]); }}")
```
L1944  ⚪  (score=0)
```python
```
L1945  ⚪  (score=0)
```python
    def generate_object_constant_decls(self):
```
L1946  ⚪  (score=0)
```python
        consts = [(len(c.cname), c.cname, c)
```
L1947  ⚪  (score=0)
```python
                  for c in self.arg_default_constants]
```
L1948  ⚪  (score=0)
```python
        consts.sort()
```
L1949  ⚪  (score=0)
```python
        for _, cname, c in consts:
```
L1950  ⚪  (score=0)
```python
            self.parts['module_state'].putln("%s;" % c.type.declaration_code(cname))
```
L1951  ⚪  (score=0)
```python
            if not c.type.needs_refcounting:
```
L1952  ⚪  (score=0)
```python
                # Note that py_constants is used for all argument defaults
```
L1953  ⚪  (score=0)
```python
                # which aren't necessarily PyObjects, so aren't appropriate
```
L1954  ⚪  (score=0)
```python
                # to clear.
```
L1955  ⚪  (score=0)
```python
                continue
```
L1956  ⚪  (score=0)
```python
```
L1957  ⚪  (score=0)
```python
            self.parts['module_state_clear'].put_xdecref_clear(
```
L1958  ⚪  (score=0)
```python
                f"clear_module_state->{cname}",
```
L1959  ⚪  (score=0)
```python
                c.type,
```
L1960  ⚪  (score=0)
```python
                clear_before_decref=True,
```
L1961  ⚪  (score=0)
```python
                nanny=False,
```
L1962  ⚪  (score=0)
```python
            )
```
L1963  ⚪  (score=0)
```python
```
L1964  ⚪  (score=0)
```python
            if c.type.is_memoryviewslice:
```
L1965  ⚪  (score=0)
```python
                # TODO: Implement specific to type like CodeWriter.put_xdecref_clear()
```
L1966  ⚪  (score=0)
```python
                cname += "->memview"
```
L1967  ⚪  (score=0)
```python
```
L1968  ⚪  (score=0)
```python
            self.parts['module_state_traverse'].putln(
```
L1969  ⚪  (score=0)
```python
                f"Py_VISIT(traverse_module_state->{cname});")
```
L1970  ⚪  (score=0)
```python
```
L1971  ⚪  (score=0)
```python
        for prefix, count in sorted(self.const_array_counters.items()):
```
L1972  ⚪  (score=0)
```python
            struct_attr_cname = f"{Naming.pyrex_prefix}{prefix}"
```
L1973  ⚪  (score=0)
```python
            self.parts['module_state'].putln(f"PyObject *{struct_attr_cname}[{count}];")
```
L1974  ⚪  (score=0)
```python
```
L1975  ⚪  (score=0)
```python
            # The constant tuples/slices that we create can never participate in reference cycles.
```
L1976  ⚪  (score=0)
```python
            self._generate_module_array_traverse_and_clear(struct_attr_cname, count, may_have_refcycles=False)
```
L1977  ⚪  (score=0)
```python
```
L1978  ⚪  (score=0)
```python
            cleanup_level = cleanup_level_for_type_prefix(prefix)
```
L1979  ⚪  (score=0)
```python
            if cleanup_level is not None and cleanup_level <= Directives.generate_cleanup_code:
```
L1980  ⚪  (score=0)
```python
                part_writer = self.parts['cleanup_globals']
```
L1981  ⚪  (score=0)
```python
                part_writer.put(f"for (size_t i=0; i<{count}; ++i) ")
```
L1982  ⚪  (score=0)
```python
                part_writer.putln(
```
L1983  ⚪  (score=0)
```python
                    "{ Py_CLEAR(%s); }" %
```
L1984  ⚪  (score=0)
```python
                        part_writer.name_in_main_c_code_module_state(f"{struct_attr_cname}[i]")
```
L1985  ⚪  (score=0)
```python
                )
```
L1986  ⚪  (score=0)
```python
```
L1987  ⚪  (score=0)
```python
    def generate_cached_methods_decls(self):
```
L1988  ⚪  (score=0)
```python
        if not self.cached_cmethods:
```
L1989  ⚪  (score=0)
```python
            return
```
L1990  ⚪  (score=0)
```python
```
L1991  ⚪  (score=0)
```python
        decl = self.parts['module_state']
```
L1992  ⚪  (score=0)
```python
        init = self.parts['cached_builtins']
```
L1993  ⚪  (score=0)
```python
```
L1994  ⚪  (score=0)
```python
        init.putln("")
```
L1995  ⚪  (score=0)
```python
        init.putln("/* Cached unbound methods */")
```
L1996  ⚪  (score=0)
```python
```
L1997  ⚪  (score=0)
```python
        cnames = []
```
L1998  ⚪  (score=0)
```python
        for (type_cname, method_name), cname in sorted(self.cached_cmethods.items()):
```
L1999  ⚪  (score=0)
```python
            cnames.append(cname)
```
L2000  ⚪  (score=0)
```python
            method_name_cname = self.get_interned_identifier(StringEncoding.EncodedString(method_name)).cname
```
L2001  ⚪  (score=0)
```python
            decl.putln('__Pyx_CachedCFunction %s;' % (
```
L2002  ⚪  (score=0)
```python
                cname))
```
L2003  ⚪  (score=0)
```python
            # split type reference storage as it might not be static
```
L2004  ⚪  (score=0)
```python
            init.putln('%s.type = (PyObject*)%s;' % (
```
L2005  ⚪  (score=0)
```python
                init.name_in_main_c_code_module_state(cname), type_cname))
```
L2006  ⚪  (score=0)
```python
            # method name string isn't static in limited api
```
L2007  ⚪  (score=0)
```python
            init.putln(
```
L2008  ⚪  (score=0)
```python
                f'{init.name_in_main_c_code_module_state(cname)}.method_name = '
```
L2009  ⚪  (score=0)
```python
                f'&{init.name_in_main_c_code_module_state(method_name_cname)};')
```
L2010  ⚪  (score=0)
```python
```
L2011  ⚪  (score=0)
```python
        if Directives.generate_cleanup_code:
```
L2012  ⚪  (score=0)
```python
            cleanup = self.parts['cleanup_globals']
```
L2013  ⚪  (score=0)
```python
            for cname in cnames:
```
L2014  ⚪  (score=0)
```python
                cleanup.putln(f"Py_CLEAR({init.name_in_main_c_code_module_state(cname)}.method);")
```
L2015  ⚪  (score=0)
```python
```
L2016  ⚪  (score=0)
```python
    def generate_string_constants(self):
```
L2017  ⚪  (score=0)
```python
        c_consts = []
```
L2018  ⚪  (score=0)
```python
        py_bytes_consts = []
```
L2019  ⚪  (score=0)
```python
        py_unicode_consts = []
```
L2020  ⚪  (score=0)
```python
```
L2021  ⚪  (score=0)
```python
        # Split into buckets.
```
L2022  ⚪  (score=0)
```python
        for _, _, c in sorted([(len(c.cname), c.cname, c) for c in self.string_const_index.values()]):
```
L2023  ⚪  (score=0)
```python
            if c.c_used:
```
L2024  ⚪  (score=0)
```python
                c_consts.append((len(c.cname), c.cname, c.escaped_value))
```
L2025  ⚪  (score=0)
```python
            if c.py_strings:
```
L2026  ⚪  (score=0)
```python
                for py_string in c.py_strings.values():
```
L2027  ⚪  (score=0)
```python
                    text = c.text
```
L2028  ⚪  (score=0)
```python
                    if py_string.is_unicode and not isinstance(text, str):
```
L2029  ⚪  (score=0)
```python
                        text = StringEncoding.EncodedString(text.decode(py_string.encoding or 'UTF-8'))
```
L2030  ⚪  (score=0)
```python
```
L2031  ⚪  (score=0)
```python
                    (py_unicode_consts if py_string.is_unicode else py_bytes_consts).append((
```
L2032  ⚪  (score=0)
```python
                        py_string.intern and py_string.is_unicode,
```
L2033  ⚪  (score=0)
```python
                        py_string.cname,
```
L2034  ⚪  (score=0)
```python
                        text,
```
L2035  ⚪  (score=0)
```python
                    ))
```
L2036  ⚪  (score=0)
```python
```
L2037  ⚪  (score=0)
```python
        c_consts.sort()
```
L2038  ⚪  (score=0)
```python
        py_bytes_consts.sort()
```
L2039  ⚪  (score=0)
```python
        py_unicode_consts.sort()
```
L2040  ⚪  (score=0)
```python
```
L2041  ⚪  (score=0)
```python
        # Generate C string constants.
```
L2042  ⚪  (score=0)
```python
        decls_writer = self.parts['string_decls']
```
L2043  ⚪  (score=0)
```python
        for _, cname, escaped_value in c_consts:
```
L2044  ⚪  (score=0)
```python
            cliteral = StringEncoding.split_string_literal(escaped_value)
```
L2045  ⚪  (score=0)
```python
            decls_writer.putln(
```
L2046  ⚪  (score=0)
```python
                f'static const char {cname}[] = "{cliteral}";',
```
L2047  ⚪  (score=0)
```python
                safe=True,  # Braces in user strings are not for indentation.
```
L2048  ⚪  (score=0)
```python
            )
```
L2049  ⚪  (score=0)
```python
```
L2050  ⚪  (score=0)
```python
        # Generate legacy Py_UNICODE[] constants.
```
L2051  ⚪  (score=0)
```python
        for c, cname in sorted(self.pyunicode_ptr_const_index.items()):
```
L2052  ⚪  (score=0)
```python
            utf16_array, utf32_array = StringEncoding.encode_pyunicode_string(c)
```
L2053  ⚪  (score=0)
```python
            if utf16_array:
```
L2054  ⚪  (score=0)
```python
                # Narrow and wide representations differ
```
L2055  ⚪  (score=0)
```python
                decls_writer.putln("#ifdef Py_UNICODE_WIDE")
```
L2056  ⚪  (score=0)
```python
            decls_writer.putln("static Py_UNICODE %s[] = { %s };" % (cname, utf32_array))
```
L2057  ⚪  (score=0)
```python
            if utf16_array:
```
L2058  ⚪  (score=0)
```python
                decls_writer.putln("#else")
```
L2059  ⚪  (score=0)
```python
                decls_writer.putln("static Py_UNICODE %s[] = { %s };" % (cname, utf16_array))
```
L2060  ⚪  (score=0)
```python
                decls_writer.putln("#endif")
```
L2061  ⚪  (score=0)
```python
```
L2062  ⚪  (score=0)
```python
        # Generate stringtab and Python string constants.
```
L2063  ⚪  (score=0)
```python
        py_string_count = len(py_bytes_consts) + len(py_unicode_consts)
```
L2064  ⚪  (score=0)
```python
        # The actual storage lives in the module state struct ...
```
L2065  ⚪  (score=0)
```python
        self.parts['module_state'].putln(f"PyObject *{Naming.stringtab_cname}[{py_string_count}];")
```
L2066  ⚪  (score=0)
```python
        self._generate_module_array_traverse_and_clear(Naming.stringtab_cname, py_string_count, may_have_refcycles=False)
```
L2067  ⚪  (score=0)
```python
        # ... but we also expose a global ``PyObject **__pyx_string_tab`` alias so
```
L2068  ⚪  (score=0)
```python
        # that the ``__pyx_k*`` / ``__pyx_n*`` macros can use it in static
```
L2069  ⚪  (score=0)
```python
        # initialisers (fast-arg metadata etc.) without depending on the module
```
L2070  ⚪  (score=0)
```python
        # state helpers or their declaration order.
```
L2071  ⚪  (score=0)
```python
        self.parts['global_var'].putln(f"static PyObject **{Naming.stringtab_cname};")
```
L2072  ⚪  (score=0)
```python
```
L2073  ⚪  (score=0)
```python
        self.generate_pystring_constants(py_unicode_consts, py_bytes_consts)
```
L2074  ⚪  (score=0)
```python
```
L2075  ⚪  (score=0)
```python
    def generate_pystring_constants(self, text_strings: list, byte_strings: list):
```
L2076  ⚪  (score=0)
```python
        # Concatenate all strings into one byte sequence and build a length index array.
```
L2077  ⚪  (score=0)
```python
        defines = self.parts['constant_name_defines']
```
L2078  ⚪  (score=0)
```python
```
L2079  ⚪  (score=0)
```python
        bytes_values = []
```
L2080  ⚪  (score=0)
```python
        first_interned: cython.Py_ssize_t = -1
```
L2081  ⚪  (score=0)
```python
        stringtab_pos: cython.Py_ssize_t = 0
```
L2082  ⚪  (score=0)
```python
```
L2083  ⚪  (score=0)
```python
        # For (Unicode) text strings, the index stores the character lengths after UTF8 decoding.
```
L2084  ⚪  (score=0)
```python
        for i, (is_interned, cname, text) in enumerate(text_strings):
```
L2085  ⚪  (score=0)
```python
            bytes_values.append(text.encode('utf-8'))
```
L2086  ⚪  (score=0)
```python
            if first_interned == -1 and is_interned:
```
L2087  ⚪  (score=0)
```python
                first_interned = i
```
L2088  ⚪  (score=0)
```python
            defines.putln(f"#define {cname} {Naming.stringtab_cname}[{stringtab_pos}]")
```
L2089  ⚪  (score=0)
```python
            # Also expose the string-table index as a plain integer for
```
L2090  ⚪  (score=0)
```python
            # POD-only metadata (e.g. fast-arg __Pyx_ParamMeta tables).
```
L2091  ⚪  (score=0)
```python
            defines.putln(f"#define {cname}_IDX {stringtab_pos}u")
```
L2092  ⚪  (score=0)
```python
            stringtab_pos += 1
```
L2093  ⚪  (score=0)
```python
```
L2094  ⚪  (score=0)
```python
        stringtab_bytes_start: cython.Py_ssize_t = len(text_strings)
```
L2095  ⚪  (score=0)
```python
```
L2096  ⚪  (score=0)
```python
        # For bytes objects, the index stores the byte lengths, ignoring the initial Unicode string.
```
L2097  ⚪  (score=0)
```python
        for _, cname, text in byte_strings:
```
L2098  ⚪  (score=0)
```python
            bytes_values.append(text.byteencode() if text.encoding else text.utf8encode())
```
L2099  ⚪  (score=0)
```python
            defines.putln(f"#define {cname} {Naming.stringtab_cname}[{stringtab_pos}]")
```
L2100  ⚪  (score=0)
```python
            defines.putln(f"#define {cname}_IDX {stringtab_pos}u")
```
L2101  ⚪  (score=0)
```python
            stringtab_pos += 1
```
L2102  ⚪  (score=0)
```python
```
L2103  ⚪  (score=0)
```python
        index = list(map(len, bytes_values))
```
L2104  ⚪  (score=0)
```python
        concat_bytes = b''.join(bytes_values)
```
L2105  ⚪  (score=0)
```python
```
L2106  ⚪  (score=0)
```python
        w = self.parts['init_constants']
```
L2107  ⚪  (score=0)
```python
        w.putln("{")  # Start code block.
```
L2108  ⚪  (score=0)
```python
```
L2109  ⚪  (score=0)
```python
        # Store the index of string lengths.
```
L2110  ⚪  (score=0)
```python
        w.putln(
```
L2111  ⚪  (score=0)
```python
            "const struct { "
```
L2112  ⚪  (score=0)
```python
            f"const unsigned int length: {max(index).bit_length()}; "
```
L2113  ⚪  (score=0)
```python
            "} "
```
L2114  ⚪  (score=0)
```python
            f"index[] = {{{','.join(['{%d}' % length for length in index])}}};",
```
L2115  ⚪  (score=0)
```python
        )
```
L2116  ⚪  (score=0)
```python
```
L2117  ⚪  (score=0)
```python
        # Store and decompress the string data.
```
L2118  ⚪  (score=0)
```python
        self.use_utility_code(UtilityCode.load_cached("DecompressString", "StringTools.c"))
```
L2119  ⚪  (score=0)
```python
```
L2120  ⚪  (score=0)
```python
        has_if = False
```
L2121  ⚪  (score=0)
```python
        for algo_number, algo_name, compress in reversed(compression_algorithms):
```
L2122  ⚪  (score=0)
```python
            if compress is None:
```
L2123  ⚪  (score=0)
```python
                continue
```
L2124  ⚪  (score=0)
```python
            compressed_bytes = compress(concat_bytes)
```
L2125  ⚪  (score=0)
```python
            if len(compressed_bytes) >= len(concat_bytes) - 10:
```
L2126  ⚪  (score=0)
```python
                continue
```
L2127  ⚪  (score=0)
```python
```
L2128  ⚪  (score=0)
```python
            if algo_name == 'zlib':
```
L2129  ⚪  (score=0)
```python
                # Use zlib as fallback if the selected compression module is not available.
```
L2130  ⚪  (score=0)
```python
                assert algo_number == 1, f"Compression algorithm no. 1 must be 'zlib' to be used as fallback."
```
L2131  ⚪  (score=0)
```python
                guard = "(CYTHON_COMPRESS_STRINGS) != 0"
```
L2132  ⚪  (score=0)
```python
            elif algo_name == 'zstd':
```
L2133  ⚪  (score=0)
```python
                # 'compression.zstd' was added in Python 3.14.
```
L2134  ⚪  (score=0)
```python
                guard = f"(CYTHON_COMPRESS_STRINGS) == {algo_number} && __PYX_LIMITED_VERSION_HEX >= 0x030e0000"
```
L2135  ⚪  (score=0)
```python
            else:
```
L2136  ⚪  (score=0)
```python
                guard = f"(CYTHON_COMPRESS_STRINGS) == {algo_number}"
```
L2137  ⚪  (score=0)
```python
```
L2138  ⚪  (score=0)
```python
            w.putln(f"#{'if' if not has_if else 'elif'} {guard} /* compression: {algo_name} ({len(compressed_bytes)} bytes) */")
```
L2139  ⚪  (score=0)
```python
            has_if = True
```
L2140  ⚪  (score=0)
```python
            escaped_bytes = StringEncoding.split_string_literal(
```
L2141  ⚪  (score=0)
```python
                StringEncoding.escape_byte_string(compressed_bytes))
```
L2142  ⚪  (score=0)
```python
            w.putln(f'const char* const cstring = "{escaped_bytes}";', safe=True)
```
L2143  ⚪  (score=0)
```python
            w.putln(f'PyObject *data = __Pyx_DecompressString(cstring, {len(compressed_bytes)}, {algo_number});')
```
L2144  ⚪  (score=0)
```python
            w.putln(w.error_goto_if_null('data', self.module_pos))
```
L2145  ⚪  (score=0)
```python
```
L2146  ⚪  (score=0)
```python
            w.putln('const char* const bytes = __Pyx_PyBytes_AsString(data);')
```
L2147  ⚪  (score=0)
```python
            w.putln("#if !CYTHON_ASSUME_SAFE_MACROS")
```
L2148  ⚪  (score=0)
```python
            w.putln(f'if (likely(bytes)); else {{ Py_DECREF(data); {w.error_goto(self.module_pos)} }}')
```
L2149  ⚪  (score=0)
```python
            w.putln('#endif')
```
L2150  ⚪  (score=0)
```python
```
L2151  ⚪  (score=0)
```python
        if has_if:
```
L2152  ⚪  (score=0)
```python
            w.putln(f"#else /* compression: none ({len(concat_bytes)} bytes) */")
```
L2153  ⚪  (score=0)
```python
        escaped_bytes = StringEncoding.split_string_literal(
```
L2154  ⚪  (score=0)
```python
            StringEncoding.escape_byte_string(concat_bytes))
```
L2155  ⚪  (score=0)
```python
        w.putln(f'const char* const bytes = "{escaped_bytes}";', safe=True)
```
L2156  ⚪  (score=0)
```python
        w.putln('PyObject *data = NULL;')  # Always allow xdecref below.
```
L2157  ⚪  (score=0)
```python
        w.putln("CYTHON_UNUSED_VAR(__Pyx_DecompressString);")
```
L2158  ⚪  (score=0)
```python
        if has_if:
```
L2159  ⚪  (score=0)
```python
            w.putln("#endif")
```
L2160  ⚪  (score=0)
```python
```
L2161  ⚪  (score=0)
```python
        # Populate stringtab.
```
L2162  ⚪  (score=0)
```python
        # Make the module-state array accessible via the global ``__pyx_string_tab``
```
L2163  ⚪  (score=0)
```python
        # alias that the ``__pyx_k*`` / ``__pyx_n*`` macros use.
```
L2164  ⚪  (score=0)
```python
        w.putln(f"{Naming.stringtab_cname} = {w.name_in_main_c_code_module_state(Naming.stringtab_cname)};")
```
L2165  ⚪  (score=0)
```python
        w.putln(f"PyObject **stringtab = {Naming.stringtab_cname};")
```
L2166  ⚪  (score=0)
```python
        w.putln("Py_ssize_t pos = 0;")
```
L2167  ⚪  (score=0)
```python
```
L2168  ⚪  (score=0)
```python
        # Unpack Unicode strings.
```
L2169  ⚪  (score=0)
```python
        if stringtab_bytes_start > 0:
```
L2170  ⚪  (score=0)
```python
            # Note: We could decode the concatenated Unicode string in one go, but this has a drawback:
```
L2171  ⚪  (score=0)
```python
            # If most strings are ASCII/Latin-1 or at most BMP, then a single non-BMP string in the mix
```
L2172  ⚪  (score=0)
```python
            # will make all strings use 4 bytes of RAM per character during initialisation, until we finish
```
L2173  ⚪  (score=0)
```python
            # splitting the user substrings. In addition to using more memory, this might not even be faster
```
L2174  ⚪  (score=0)
```python
            # because it must copy Unicode slices between different character sizes.
```
L2175  ⚪  (score=0)
```python
            # We avoid this by repeatedly calling PyUnicode_DecodeUTF8() for each substring.
```
L2176  ⚪  (score=0)
```python
            w.putln(f"for ({'int' if stringtab_bytes_start < 2**15 else 'Py_ssize_t'} i = 0; i < {stringtab_bytes_start}; i++) {{")
```
L2177  ⚪  (score=0)
```python
            w.putln("Py_ssize_t bytes_length = index[i].length;")
```
L2178  ⚪  (score=0)
```python
```
L2179  ⚪  (score=0)
```python
            w.putln("PyObject *string = PyUnicode_DecodeUTF8(bytes + pos, bytes_length, NULL);")
```
L2180  ⚪  (score=0)
```python
            if first_interned >= 0:
```
L2181  ⚪  (score=0)
```python
                w.putln(f"if (likely(string) && i >= {first_interned}) PyUnicode_InternInPlace(&string);")
```
L2182  ⚪  (score=0)
```python
            w.putln("if (unlikely(!string)) {")
```
L2183  ⚪  (score=0)
```python
            w.putln("Py_XDECREF(data);")
```
L2184  ⚪  (score=0)
```python
            w.putln(w.error_goto(self.module_pos))
```
L2185  ⚪  (score=0)
```python
            w.putln('}')
```
L2186  ⚪  (score=0)
```python
```
L2187  ⚪  (score=0)
```python
            w.putln("stringtab[i] = string;")
```
L2188  ⚪  (score=0)
```python
            w.putln("pos += bytes_length;")
```
L2189  ⚪  (score=0)
```python
            w.putln("}")  # for()
```
L2190  ⚪  (score=0)
```python
```
L2191  ⚪  (score=0)
```python
        # Unpack byte strings.
```
L2192  ⚪  (score=0)
```python
        if stringtab_bytes_start < len(index):
```
L2193  ⚪  (score=0)
```python
            w.putln(f"for ({'int' if len(index) < 2**15 else 'Py_ssize_t'} i = {stringtab_bytes_start}; i < {len(index)}; i++) {{")
```
L2194  ⚪  (score=0)
```python
            w.putln("Py_ssize_t bytes_length = index[i].length;")
```
L2195  ⚪  (score=0)
```python
```
L2196  ⚪  (score=0)
```python
            w.putln("PyObject *string = PyBytes_FromStringAndSize(bytes + pos, bytes_length);")
```
L2197  ⚪  (score=0)
```python
            w.putln("stringtab[i] = string;")
```
L2198  ⚪  (score=0)
```python
            w.putln("pos += bytes_length;")
```
L2199  ⚪  (score=0)
```python
```
L2200  ⚪  (score=0)
```python
            w.putln("if (unlikely(!string)) {")
```
L2201  ⚪  (score=0)
```python
            w.putln("Py_XDECREF(data);")
```
L2202  ⚪  (score=0)
```python
            w.putln(w.error_goto(self.module_pos))
```
L2203  ⚪  (score=0)
```python
            w.putln('}')
```
L2204  ⚪  (score=0)
```python
```
L2205  ⚪  (score=0)
```python
            w.putln("}")  # for()
```
L2206  ⚪  (score=0)
```python
```
L2207  ⚪  (score=0)
```python
        w.putln("Py_XDECREF(data);")
```
L2208  ⚪  (score=0)
```python
```
L2209  ⚪  (score=0)
```python
        # Set up hash values.
```
L2210  ⚪  (score=0)
```python
        w.putln(f"for (Py_ssize_t i = 0; i < {len(index)}; i++) {{")
```
L2211  ⚪  (score=0)
```python
        w.putln("if (unlikely(PyObject_Hash(stringtab[i]) == -1)) {")
```
L2212  ⚪  (score=0)
```python
        w.putln(w.error_goto(self.module_pos))
```
L2213  ⚪  (score=0)
```python
        w.putln('}')
```
L2214  ⚪  (score=0)
```python
        w.putln('}')
```
L2215  ⚪  (score=0)
```python
```
L2216  ⚪  (score=0)
```python
        # Unicode strings are not trivially immortal but require certain rules.
```
L2217  ⚪  (score=0)
```python
        # See https://github.com/python/cpython/blob/920de7ccdcfa7284b6d23a124771b17c66dd3e4f/Objects/unicodeobject.c#L713-L739
```
L2218  ⚪  (score=0)
```python
        # But we can make bytes strings immortal.
```
L2219  ⚪  (score=0)
```python
        if stringtab_bytes_start < len(index):
```
L2220  ⚪  (score=0)
```python
            self.immortalize_constants(f"stringtab + {stringtab_bytes_start}", len(index) - stringtab_bytes_start, w)
```
L2221  ⚪  (score=0)
```python
```
L2222  ⚪  (score=0)
```python
        w.putln("}")  # close block
```
L2223  ⚪  (score=0)
```python
```
L2224  ⚪  (score=0)
```python
    def generate_codeobject_constants(self):
```
L2225  ⚪  (score=0)
```python
        w = self.parts['init_codeobjects']
```
L2226  ⚪  (score=0)
```python
        init_function = (
```
L2227  ⚪  (score=0)
```python
            f"int __Pyx_CreateCodeObjects({Naming.modulestatetype_cname} *{Naming.modulestatevalue_cname})"
```
L2228  ⚪  (score=0)
```python
        )
```
L2229  ⚪  (score=0)
```python
```
L2230  ⚪  (score=0)
```python
        if not self.codeobject_constants:
```
L2231  ⚪  (score=0)
```python
            w.start_initcfunc(init_function)
```
L2232  ⚪  (score=0)
```python
            w.putln(f"CYTHON_UNUSED_VAR({Naming.modulestatevalue_cname});")
```
L2233  ⚪  (score=0)
```python
            w.putln("return 0;")
```
L2234  ⚪  (score=0)
```python
            w.exit_cfunc_scope()
```
L2235  ⚪  (score=0)
```python
            w.putln("}")
```
L2236  ⚪  (score=0)
```python
            return
```
L2237  ⚪  (score=0)
```python
```
L2238  ⚪  (score=0)
```python
        # Create a downsized config struct and build code objects from it.
```
L2239  ⚪  (score=0)
```python
        max_flags = 0x3ff  # to be adapted when we start using new flags
```
L2240  ⚪  (score=0)
```python
        max_func_args = 1
```
L2241  ⚪  (score=0)
```python
        max_kwonly_args = 1
```
L2242  ⚪  (score=0)
```python
        max_posonly_args = 1
```
L2243  ⚪  (score=0)
```python
        max_vars = 1
```
L2244  ⚪  (score=0)
```python
        max_line = 1
```
L2245  ⚪  (score=0)
```python
        for node in self.codeobject_constants:
```
L2246  ⚪  (score=0)
```python
            def_node = node.def_node
```
L2247  ⚪  (score=0)
```python
            if not def_node.is_generator_expression:
```
L2248  ⚪  (score=0)
```python
                max_func_args = max(max_func_args, len(def_node.args) - def_node.num_kwonly_args)
```
L2249  ⚪  (score=0)
```python
                max_kwonly_args = max(max_kwonly_args, def_node.num_kwonly_args)
```
L2250  ⚪  (score=0)
```python
                max_posonly_args = max(max_posonly_args, def_node.num_posonly_args)
```
L2251  ⚪  (score=0)
```python
            max_vars = max(max_vars, len(node.varnames))
```
L2252  ⚪  (score=0)
```python
            max_line = max(max_line, def_node.pos[1])
```
L2253  ⚪  (score=0)
```python
```
L2254  ⚪  (score=0)
```python
        w.put(textwrap.dedent(f"""\
```
L2255  ⚪  (score=0)
```python
        typedef struct {{
```
L2256  ⚪  (score=0)
```python
            unsigned int argcount : {max_func_args.bit_length()};
```
L2257  ⚪  (score=0)
```python
            unsigned int num_posonly_args : {max_posonly_args.bit_length()};
```
L2258  ⚪  (score=0)
```python
            unsigned int num_kwonly_args : {max_kwonly_args.bit_length()};
```
L2259  ⚪  (score=0)
```python
            unsigned int nlocals : {max_vars.bit_length()};
```
L2260  ⚪  (score=0)
```python
            unsigned int flags : {max_flags.bit_length()};
```
L2261  ⚪  (score=0)
```python
            unsigned int first_line : {max_line.bit_length()};
```
L2262  ⚪  (score=0)
```python
        }} __Pyx_PyCode_New_function_description;
```
L2263  ⚪  (score=0)
```python
        """))
```
L2264  ⚪  (score=0)
```python
```
L2265  ⚪  (score=0)
```python
        self.use_utility_code(UtilityCode.load_cached("NewCodeObj", "ModuleSetupCode.c"))
```
L2266  ⚪  (score=0)
```python
```
L2267  ⚪  (score=0)
```python
        w.start_initcfunc(init_function)
```
L2268  ⚪  (score=0)
```python
```
L2269  ⚪  (score=0)
```python
        w.putln("PyObject* tuple_dedup_map = PyDict_New();")
```
L2270  ⚪  (score=0)
```python
        w.putln("if (unlikely(!tuple_dedup_map)) return -1;")
```
L2271  ⚪  (score=0)
```python
```
L2272  ⚪  (score=0)
```python
        for node in self.codeobject_constants:
```
L2273  ⚪  (score=0)
```python
            node.generate_codeobj(w, "bad")
```
L2274  ⚪  (score=0)
```python
```
L2275  ⚪  (score=0)
```python
        w.putln("Py_DECREF(tuple_dedup_map);")
```
L2276  ⚪  (score=0)
```python
        w.putln("return 0;")
```
L2277  ⚪  (score=0)
```python
```
L2278  ⚪  (score=0)
```python
        w.putln("bad:")
```
L2279  ⚪  (score=0)
```python
        w.putln("Py_DECREF(tuple_dedup_map);")
```
L2280  ⚪  (score=0)
```python
        w.putln("return -1;")
```
L2281  ⚪  (score=0)
```python
        w.exit_cfunc_scope()
```
L2282  ⚪  (score=0)
```python
        w.putln("}")
```
L2283  ⚪  (score=0)
```python
```
L2284  ⚪  (score=0)
```python
        code_object_count = len(self.codeobject_constants)
```
L2285  ⚪  (score=0)
```python
        self.parts['module_state'].putln(f"PyObject *{Naming.codeobjtab_cname}[{code_object_count}];")
```
L2286  ⚪  (score=0)
```python
        # The code objects that we generate only contain plain constants and can never participate in reference cycles.
```
L2287  ⚪  (score=0)
```python
        self._generate_module_array_traverse_and_clear(Naming.codeobjtab_cname, code_object_count, may_have_refcycles=False)
```
L2288  ⚪  (score=0)
```python
```
L2289  ⚪  (score=0)
```python
    def generate_num_constants(self):
```
L2290  ⚪  (score=0)
```python
        consts = [(c.py_type, len(c.value.lstrip('-')), c.value.lstrip('-'), c.value, c.value_code, c)
```
L2291  ⚪  (score=0)
```python
                  for c in self.num_const_index.values()]
```
L2292  ⚪  (score=0)
```python
        consts.sort()
```
L2293  ⚪  (score=0)
```python
        if not consts:
```
L2294  ⚪  (score=0)
```python
            return
```
L2295  ⚪  (score=0)
```python
```
L2296  ⚪  (score=0)
```python
        constant_count = len(consts)
```
L2297  ⚪  (score=0)
```python
        self.parts['module_state'].putln(f"PyObject *{Naming.numbertab_cname}[{constant_count}];")
```
L2298  ⚪  (score=0)
```python
        # Numeric constants can never participate in reference cycles.
```
L2299  ⚪  (score=0)
```python
        self._generate_module_array_traverse_and_clear(Naming.numbertab_cname, constant_count, may_have_refcycles=False)
```
L2300  ⚪  (score=0)
```python
```
L2301  ⚪  (score=0)
```python
        float_constants = []
```
L2302  ⚪  (score=0)
```python
        int_constants_by_bytesize = [[]]  # [[1 byte], [2 bytes], [4 bytes], [8 bytes]]
```
L2303  ⚪  (score=0)
```python
        large_constants = []
```
L2304  ⚪  (score=0)
```python
        int_constant_count = 0
```
L2305  ⚪  (score=0)
```python
        int_suffix = ''
```
L2306  ⚪  (score=0)
```python
```
L2307  ⚪  (score=0)
```python
        for py_type, _, _, value, value_code, c in consts:
```
L2308  ⚪  (score=0)
```python
            cname = c.cname
```
L2309  ⚪  (score=0)
```python
            if py_type == 'float':
```
L2310  ⚪  (score=0)
```python
                float_constants.append((cname, value_code))
```
L2311  ⚪  (score=0)
```python
            else:
```
L2312  ⚪  (score=0)
```python
                number_value = Utils.str_to_number(value)
```
L2313  ⚪  (score=0)
```python
                bit_length = number_value.bit_length()
```
L2314  ⚪  (score=0)
```python
                if bit_length <= 63:
```
L2315  ⚪  (score=0)
```python
                    while (bit_length + 8) // 8 > 1 << (len(int_constants_by_bytesize) - 1):
```
L2316  ⚪  (score=0)
```python
                        int_constants_by_bytesize.append([])
```
L2317  ⚪  (score=0)
```python
                        # Our <= 31-bit integer values pass happily as 'int32' without further modifiers,
```
L2318  ⚪  (score=0)
```python
                        # but MSVC misinterprets a negative '-2147483648' (== INT_MIN) and similar values as
```
L2319  ⚪  (score=0)
```python
                        # "that's 'uint32' just with a minus sign", where '-(2147483648)' == '2147483648'.
```
L2320  ⚪  (score=0)
```python
                        # See https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/compiler-warning-level-2-c4146?view=msvc-170
```
L2321  ⚪  (score=0)
```python
                        int_suffix = 'LL'[:len(int_constants_by_bytesize) - 2]
```
L2322  ⚪  (score=0)
```python
                    int_constant_count += 1
```
L2323  ⚪  (score=0)
```python
                    int_constants_by_bytesize[-1].append((cname, f"{number_value}{int_suffix}"))
```
L2324  ⚪  (score=0)
```python
                else:
```
L2325  ⚪  (score=0)
```python
                    large_constants.append((cname, number_value))
```
L2326  ⚪  (score=0)
```python
```
L2327  ⚪  (score=0)
```python
        w = self.parts['init_constants']
```
L2328  ⚪  (score=0)
```python
        defines = self.parts['constant_name_defines']
```
L2329  ⚪  (score=0)
```python
```
L2330  ⚪  (score=0)
```python
        def store_array(w, name: str, ctype: str, constants: list):
```
L2331  ⚪  (score=0)
```python
            c: tuple
```
L2332  ⚪  (score=0)
```python
            values = ','.join([c[1] for c in constants])
```
L2333  ⚪  (score=0)
```python
            w.putln(f"{ctype} const {name}[] = {{{values}}};")
```
L2334  ⚪  (score=0)
```python
```
L2335  ⚪  (score=0)
```python
        def generate_forloop_start(w, end: cython.Py_ssize_t):
```
L2336  ⚪  (score=0)
```python
            counter_type = 'int' if end < 2**15 else 'Py_ssize_t'
```
L2337  ⚪  (score=0)
```python
            w.putln(f"for ({counter_type} i = 0; i < {end}; i++) {{")
```
L2338  ⚪  (score=0)
```python
```
L2339  ⚪  (score=0)
```python
        def assign_constant(w, error_pos, rhs_code: str):
```
L2340  ⚪  (score=0)
```python
            w.putln(f"numbertab[i] = {rhs_code};")
```
L2341  ⚪  (score=0)
```python
            w.putln(w.error_goto_if_null("numbertab[i]", error_pos))
```
L2342  ⚪  (score=0)
```python
```
L2343  ⚪  (score=0)
```python
        def define_constants(defines, constants: list, start_offset: cython.Py_ssize_t = 0):
```
L2344  ⚪  (score=0)
```python
            i: cython.Py_ssize_t
```
L2345  ⚪  (score=0)
```python
            c: tuple
```
L2346  ⚪  (score=0)
```python
            numbertab_cname: str = Naming.numbertab_cname
```
L2347  ⚪  (score=0)
```python
            for i, c in enumerate(constants):
```
L2348  ⚪  (score=0)
```python
                cname: str = c[0]
```
L2349  ⚪  (score=0)
```python
                defines.putln(f"#define {cname} {numbertab_cname}[{start_offset + i}]")
```
L2350  ⚪  (score=0)
```python
```
L2351  ⚪  (score=0)
```python
        constant_offset: cython.Py_ssize_t = 0
```
L2352  ⚪  (score=0)
```python
```
L2353  ⚪  (score=0)
```python
        if float_constants:
```
L2354  ⚪  (score=0)
```python
            w.putln("{")
```
L2355  ⚪  (score=0)
```python
            w.putln(f"PyObject **numbertab = {w.name_in_main_c_code_module_state(Naming.numbertab_cname)};")
```
L2356  ⚪  (score=0)
```python
```
L2357  ⚪  (score=0)
```python
            store_array(w, "c_constants", 'double', float_constants)
```
L2358  ⚪  (score=0)
```python
            define_constants(defines, float_constants, constant_offset)
```
L2359  ⚪  (score=0)
```python
```
L2360  ⚪  (score=0)
```python
            generate_forloop_start(w, len(float_constants))
```
L2361  ⚪  (score=0)
```python
            assign_constant(w, self.module_pos, "PyFloat_FromDouble(c_constants[i])")
```
L2362  ⚪  (score=0)
```python
            w.putln("}")  # for()
```
L2363  ⚪  (score=0)
```python
```
L2364  ⚪  (score=0)
```python
            w.putln("}")
```
L2365  ⚪  (score=0)
```python
            constant_offset += len(float_constants)
```
L2366  ⚪  (score=0)
```python
```
L2367  ⚪  (score=0)
```python
        if int_constant_count > 0:
```
L2368  ⚪  (score=0)
```python
            w.putln("{")
```
L2369  ⚪  (score=0)
```python
            w.putln(f"PyObject **numbertab = {w.name_in_main_c_code_module_state(Naming.numbertab_cname)} + {constant_offset};")
```
L2370  ⚪  (score=0)
```python
```
L2371  ⚪  (score=0)
```python
            int_types = ['', 'int8_t', 'int16_t', 'int32_t', 'int64_t']
```
L2372  ⚪  (score=0)
```python
            array_access = "%s"
```
L2373  ⚪  (score=0)
```python
            int_constants_seen: cython.Py_ssize_t = 0
```
L2374  ⚪  (score=0)
```python
            byte_size: cython.int
```
L2375  ⚪  (score=0)
```python
            for byte_size, constants in enumerate(int_constants_by_bytesize, 1):
```
L2376  ⚪  (score=0)
```python
                if not constants:
```
L2377  ⚪  (score=0)
```python
                    continue
```
L2378  ⚪  (score=0)
```python
```
L2379  ⚪  (score=0)
```python
                array_name = f"cint_constants_{1 << (byte_size - 1)}"
```
L2380  ⚪  (score=0)
```python
                store_array(w, array_name, int_types[byte_size], constants)
```
L2381  ⚪  (score=0)
```python
                define_constants(defines, constants, constant_offset + int_constants_seen)
```
L2382  ⚪  (score=0)
```python
```
L2383  ⚪  (score=0)
```python
                read_item = f"{array_name}[i - {int_constants_seen}]"
```
L2384  ⚪  (score=0)
```python
                int_constants_seen += len(constants)
```
L2385  ⚪  (score=0)
```python
                array_access %= (
```
L2386  ⚪  (score=0)
```python
                    read_item if byte_size == len(int_constants_by_bytesize)  # last is simple access
```
L2387  ⚪  (score=0)
```python
                    else f"(i < {int_constants_seen} ? {read_item} : %s)"  # otherwise, access arrays step by step
```
L2388  ⚪  (score=0)
```python
                )
```
L2389  ⚪  (score=0)
```python
```
L2390  ⚪  (score=0)
```python
            generate_forloop_start(w, int_constant_count)
```
L2391  ⚪  (score=0)
```python
            capi_func = "PyLong_FromLong" if len(int_constants_by_bytesize) <= 3 else "PyLong_FromLongLong"
```
L2392  ⚪  (score=0)
```python
            assign_constant(w, self.module_pos, f"{capi_func}({array_access})")
```
L2393  ⚪  (score=0)
```python
            w.putln("}")  # for()
```
L2394  ⚪  (score=0)
```python
```
L2395  ⚪  (score=0)
```python
            w.putln("}")
```
L2396  ⚪  (score=0)
```python
            constant_offset += int_constant_count
```
L2397  ⚪  (score=0)
```python
```
L2398  ⚪  (score=0)
```python
        if large_constants:
```
L2399  ⚪  (score=0)
```python
            # We store large integer constants in a single '\0'-separated C string of base32 digits.
```
L2400  ⚪  (score=0)
```python
            def to_base32(number):
```
L2401  ⚪  (score=0)
```python
                is_neg: bool = number < 0
```
L2402  ⚪  (score=0)
```python
                if is_neg:
```
L2403  ⚪  (score=0)
```python
                    number = -number
```
L2404  ⚪  (score=0)
```python
```
L2405  ⚪  (score=0)
```python
                digits = bytearray()
```
L2406  ⚪  (score=0)
```python
                while number:
```
L2407  ⚪  (score=0)
```python
                    digit: cython.uint = number & 31
```
L2408  ⚪  (score=0)
```python
                    digit_char: cython.char = b'0123456789abcdefghijklmnopqrstuv'[digit]
```
L2409  ⚪  (score=0)
```python
                    digits.append(digit_char)
```
L2410  ⚪  (score=0)
```python
                    number >>= 5
```
L2411  ⚪  (score=0)
```python
                if not digits:
```
L2412  ⚪  (score=0)
```python
                    return b'0'
```
L2413  ⚪  (score=0)
```python
```
L2414  ⚪  (score=0)
```python
                if is_neg:
```
L2415  ⚪  (score=0)
```python
                    digits.append(ord(b'-'))
```
L2416  ⚪  (score=0)
```python
                digits.reverse()
```
L2417  ⚪  (score=0)
```python
                return digits
```
L2418  ⚪  (score=0)
```python
```
L2419  ⚪  (score=0)
```python
            w.putln("{")
```
L2420  ⚪  (score=0)
```python
            w.putln(f"PyObject **numbertab = {w.name_in_main_c_code_module_state(Naming.numbertab_cname)} + {constant_offset};")
```
L2421  ⚪  (score=0)
```python
            c_string = b'\\000'.join([to_base32(c[1]) for c in large_constants]).decode('ascii')
```
L2422  ⚪  (score=0)
```python
            w.putln(f'const char* c_constant = "{StringEncoding.split_string_literal(c_string)}";')
```
L2423  ⚪  (score=0)
```python
            define_constants(defines, large_constants, constant_offset)
```
L2424  ⚪  (score=0)
```python
```
L2425  ⚪  (score=0)
```python
            generate_forloop_start(w, len(large_constants))
```
L2426  ⚪  (score=0)
```python
            w.putln("char *end_pos;")
```
L2427  ⚪  (score=0)
```python
            assign_constant(w, self.module_pos, "PyLong_FromString(c_constant, &end_pos, 32)")
```
L2428  ⚪  (score=0)
```python
            w.putln("c_constant = end_pos + 1;")
```
L2429  ⚪  (score=0)
```python
            w.putln("}")  # for()
```
L2430  ⚪  (score=0)
```python
```
L2431  ⚪  (score=0)
```python
            w.putln("}")
```
L2432  ⚪  (score=0)
```python
```
L2433  ⚪  (score=0)
```python
        self.immortalize_constants(
```
L2434  ⚪  (score=0)
```python
            w.name_in_main_c_code_module_state(Naming.numbertab_cname),
```
L2435  ⚪  (score=0)
```python
            constant_count,
```
L2436  ⚪  (score=0)
```python
            w)
```
L2437  ⚪  (score=0)
```python
```
L2438  ⚪  (score=0)
```python
    @staticmethod
```
L2439  ⚪  (score=0)
```python
    def immortalize_constants(array_cname, constant_count, writer):
```
L2440  ⚪  (score=0)
```python
        writer.putln("#if CYTHON_IMMORTAL_CONSTANTS")
```
L2441  ⚪  (score=0)
```python
        writer.putln("{")
```
L2442  ⚪  (score=0)
```python
        writer.putln(f"PyObject **table = {array_cname};")
```
L2443  ⚪  (score=0)
```python
        writer.putln(f"for (Py_ssize_t i=0; i<{constant_count}; ++i) {{")
```
L2444  ⚪  (score=0)
```python
        writer.putln("#if CYTHON_COMPILING_IN_CPYTHON_FREETHREADING")
```
L2445  ⚪  (score=0)
```python
        writer.putln("Py_SET_REFCNT(table[i], _Py_IMMORTAL_REFCNT_LOCAL);")
```
L2446  ⚪  (score=0)
```python
        writer.putln("#else")
```
L2447  ⚪  (score=0)
```python
        writer.putln("Py_SET_REFCNT(table[i], _Py_IMMORTAL_INITIAL_REFCNT);")
```
L2448  ⚪  (score=0)
```python
        writer.putln("#endif")
```
L2449  ⚪  (score=0)
```python
        writer.putln("}")  # for()
```
L2450  ⚪  (score=0)
```python
        writer.putln("}")
```
L2451  ⚪  (score=0)
```python
        writer.putln("#endif")
```
L2452  ⚪  (score=0)
```python
```
L2453  ⚪  (score=0)
```python
    # The functions below are there in a transition phase only
```
L2454  ⚪  (score=0)
```python
    # and will be deprecated. They are called from Nodes.BlockNode.
```
L2455  ⚪  (score=0)
```python
    # The copy&paste duplication is intentional in order to be able
```
L2456  ⚪  (score=0)
```python
    # to see quickly how BlockNode worked, until this is replaced.
```
L2457  ⚪  (score=0)
```python
```
L2458  ⚪  (score=0)
```python
    def should_declare(self, cname, entry):
```
L2459  ⚪  (score=0)
```python
        if cname in self.declared_cnames:
```
L2460  ⚪  (score=0)
```python
            other = self.declared_cnames[cname]
```
L2461  ⚪  (score=0)
```python
            assert str(entry.type) == str(other.type)
```
L2462  ⚪  (score=0)
```python
            assert entry.init == other.init
```
L2463  ⚪  (score=0)
```python
            return False
```
L2464  ⚪  (score=0)
```python
        else:
```
L2465  ⚪  (score=0)
```python
            self.declared_cnames[cname] = entry
```
L2466  ⚪  (score=0)
```python
            return True
```
L2467  ⚪  (score=0)
```python
```
L2468  ⚪  (score=0)
```python
    #
```
L2469  ⚪  (score=0)
```python
    # File name state
```
L2470  ⚪  (score=0)
```python
    #
```
L2471  ⚪  (score=0)
```python
```
L2472  ⚪  (score=0)
```python
    def lookup_filename(self, source_desc):
```
L2473  ⚪  (score=0)
```python
        entry = source_desc.get_filenametable_entry()
```
L2474  ⚪  (score=0)
```python
        try:
```
L2475  ⚪  (score=0)
```python
            index = self.filename_table[entry]
```
L2476  ⚪  (score=0)
```python
        except KeyError:
```
L2477  ⚪  (score=0)
```python
            index = len(self.filename_list)
```
L2478  ⚪  (score=0)
```python
            self.filename_list.append(source_desc)
```
L2479  ⚪  (score=0)
```python
            self.filename_table[entry] = index
```
L2480  ⚪  (score=0)
```python
        return index
```
L2481  ⚪  (score=0)
```python
```
L2482  ⚪  (score=0)
```python
    def commented_file_contents(self, source_desc):
```
L2483  ⚪  (score=0)
```python
        try:
```
L2484  ⚪  (score=0)
```python
            return self.input_file_contents[source_desc]
```
L2485  ⚪  (score=0)
```python
        except KeyError:
```
L2486  ⚪  (score=0)
```python
            pass
```
L2487  ⚪  (score=0)
```python
        source_file = source_desc.get_lines(encoding='ASCII', error_handling='ignore')
```
L2488  ⚪  (score=0)
```python
        F = [' * ' + (
```
L2489  ⚪  (score=0)
```python
                line.replace(
```
L2490  ⚪  (score=0)
```python
                    '*/', '*[inserted by cython to avoid comment closer]/'
```
L2491  ⚪  (score=0)
```python
                ).replace(
```
L2492  ⚪  (score=0)
```python
                    '/*', '/[inserted by cython to avoid comment start]*'
```
L2493  ⚪  (score=0)
```python
                ) if '/' in line else line)
```
L2494  ⚪  (score=0)
```python
            for line in source_file
```
L2495  ⚪  (score=0)
```python
        ]
```
L2496  ⚪  (score=0)
```python
        if not F: F.append('')
```
L2497  ⚪  (score=0)
```python
        self.input_file_contents[source_desc] = F
```
L2498  ⚪  (score=0)
```python
        return F
```
L2499  ⚪  (score=0)
```python
```
L2500  ⚪  (score=0)
```python
    #
```
L2501  ⚪  (score=0)
```python
    # Utility code state
```
L2502  ⚪  (score=0)
```python
    #
```
L2503  ⚪  (score=0)
```python
```
L2504  ⚪  (score=0)
```python
    def use_utility_code(self, utility_code:"UtilityCode", used_by=None):
```
L2505  ⚪  (score=0)
```python
        """
```
L2506  ⚪  (score=0)
```python
        Adds code to the C file. utility_code should
```
L2507  ⚪  (score=0)
```python
        a) implement __eq__/__hash__ for the purpose of knowing whether the same
```
L2508  ⚪  (score=0)
```python
           code has already been included
```
L2509  ⚪  (score=0)
```python
        b) implement put_code, which takes a globalstate instance
```
L2510  ⚪  (score=0)
```python
```
L2511  ⚪  (score=0)
```python
        See UtilityCode.
```
L2512  ⚪  (score=0)
```python
        """
```
L2513  ⚪  (score=0)
```python
        if utility_code and utility_code not in self.utility_codes:
```
L2514  ⚪  (score=0)
```python
            self.utility_codes.add(utility_code)
```
L2515  ⚪  (score=0)
```python
            utility_code.put_code(self, used_by=used_by)
```
L2516  ⚪  (score=0)
```python
```
L2517  ⚪  (score=0)
```python
    def use_entry_utility_code(self, entry):
```
L2518  ⚪  (score=0)
```python
        if entry is None:
```
L2519  ⚪  (score=0)
```python
            return
```
L2520  ⚪  (score=0)
```python
        if entry.utility_code:
```
L2521  ⚪  (score=0)
```python
            self.use_utility_code(entry.utility_code)
```
L2522  ⚪  (score=0)
```python
        from . import PyrexTypes
```
L2523  ⚪  (score=0)
```python
        for tp in PyrexTypes.get_all_subtypes(entry.type):
```
L2524  ⚪  (score=0)
```python
            if hasattr(tp, "entry") and tp.entry is not entry:
```
L2525  ⚪  (score=0)
```python
                self.use_entry_utility_code(tp.entry)
```
L2526  ⚪  (score=0)
```python
```
L2527  ⚪  (score=0)
```python
```
L2528  ⚪  (score=0)
```python
def funccontext_property(func):
```
L2529  ⚪  (score=0)
```python
    name = func.__name__
```
L2530  ⚪  (score=0)
```python
    attribute_of = operator.attrgetter(name)
```
L2531  ⚪  (score=0)
```python
    def get(self):
```
L2532  ⚪  (score=0)
```python
        return attribute_of(self.funcstate)
```
L2533  ⚪  (score=0)
```python
    def set(self, value):
```
L2534  ⚪  (score=0)
```python
        setattr(self.funcstate, name, value)
```
L2535  ⚪  (score=0)
```python
    return property(get, set)
```
L2536  ⚪  (score=0)
```python
```
L2537  ⚪  (score=0)
```python
```
L2538  ⚪  (score=0)
```python
class CCodeConfig:
```
L2539  ⚪  (score=0)
```python
    # emit_linenums       boolean         write #line pragmas?
```
L2540  ⚪  (score=0)
```python
    # emit_code_comments  boolean         copy the original code into C comments?
```
L2541  ⚪  (score=0)
```python
    # c_line_in_traceback boolean         append the c file and line number to the traceback for exceptions?
```
L2542  ⚪  (score=0)
```python
```
L2543  ⚪  (score=0)
```python
    def __init__(self, emit_linenums=True, emit_code_comments=True, c_line_in_traceback=True):
```
L2544  ⚪  (score=0)
```python
        self.emit_code_comments = emit_code_comments
```
L2545  ⚪  (score=0)
```python
        self.emit_linenums = emit_linenums
```
L2546  ⚪  (score=0)
```python
        self.c_line_in_traceback = c_line_in_traceback
```
L2547  ⚪  (score=0)
```python
```
L2548  ⚪  (score=0)
```python
```
L2549  ⚪  (score=0)
```python
class CCodeWriter:
```
L2550  ⚪  (score=0)
```python
    """
```
L2551  ⚪  (score=0)
```python
    Utility class to output C code.
```
L2552  ⚪  (score=0)
```python
```
L2553  ⚪  (score=0)
```python
    When creating an insertion point one must care about the state that is
```
L2554  ⚪  (score=0)
```python
    kept:
```
L2555  ⚪  (score=0)
```python
    - formatting state (level, bol) is cloned and used in insertion points
```
L2556  ⚪  (score=0)
```python
      as well
```
L2557  ⚪  (score=0)
```python
    - labels, temps, exc_vars: One must construct a scope in which these can
```
L2558  ⚪  (score=0)
```python
      exist by calling enter_cfunc_scope/exit_cfunc_scope (these are for
```
L2559  ⚪  (score=0)
```python
      sanity checking and forward compatibility). Created insertion points
```
L2560  ⚪  (score=0)
```python
      looses this scope and cannot access it.
```
L2561  ⚪  (score=0)
```python
    - marker: Not copied to insertion point
```
L2562  ⚪  (score=0)
```python
    - filename_table, filename_list, input_file_contents: All codewriters
```
L2563  ⚪  (score=0)
```python
      coming from the same root share the same instances simultaneously.
```
L2564  ⚪  (score=0)
```python
    """
```
L2565  ⚪  (score=0)
```python
```
L2566  ⚪  (score=0)
```python
    # f                   file            output file
```
L2567  ⚪  (score=0)
```python
    # buffer              StringIOTree
```
L2568  ⚪  (score=0)
```python
```
L2569  ⚪  (score=0)
```python
    # level               int             indentation level
```
L2570  ⚪  (score=0)
```python
    # bol                 bool            beginning of line?
```
L2571  ⚪  (score=0)
```python
    # marker              string          comment to emit before next line
```
L2572  ⚪  (score=0)
```python
    # funcstate           FunctionState   contains state local to a C function used for code
```
L2573  ⚪  (score=0)
```python
    #                                     generation (labels and temps state etc.)
```
L2574  ⚪  (score=0)
```python
    # globalstate         GlobalState     contains state global for a C file (input file info,
```
L2575  ⚪  (score=0)
```python
    #                                     utility code, declared constants etc.)
```
L2576  ⚪  (score=0)
```python
    # pyclass_stack       list            used during recursive code generation to pass information
```
L2577  ⚪  (score=0)
```python
    #                                     about the current class one is in
```
L2578  ⚪  (score=0)
```python
    # code_config         CCodeConfig     configuration options for the C code writer
```
L2579  ⚪  (score=0)
```python
```
L2580  ⚪  (score=0)
```python
```
L2581  ⚪  (score=0)
```python
    def __init__(self, create_from=None, buffer=None, copy_formatting=False):
```
L2582  ⚪  (score=0)
```python
        if buffer is None: 
```
L2583  ⚪  (score=0)
```python
            buffer = StringIOTree()
```
L2584  ⚪  (score=0)
```python
        self.buffer = buffer
```
L2585  ⚪  (score=0)
```python
        self.last_pos = None
```
L2586  ⚪  (score=0)
```python
        self.last_marked_pos = None
```
L2587  ⚪  (score=0)
```python
        self.pyclass_stack = []
```
L2588  ⚪  (score=0)
```python
```
L2589  ⚪  (score=0)
```python
        self.funcstate = None
```
L2590  ⚪  (score=0)
```python
        self.globalstate = None
```
L2591  ⚪  (score=0)
```python
        self.code_config = None
```
L2592  ⚪  (score=0)
```python
        self.level = 0
```
L2593  ⚪  (score=0)
```python
        self.call_level = 0
```
L2594  ⚪  (score=0)
```python
        self.bol = 1
```
L2595  ⚪  (score=0)
```python
```
L2596  ⚪  (score=0)
```python
        if create_from is not None:
```
L2597  ⚪  (score=0)
```python
            # Use same global state
```
L2598  ⚪  (score=0)
```python
            self.set_global_state(create_from.globalstate)
```
L2599  ⚪  (score=0)
```python
            self.funcstate = create_from.funcstate
```
L2600  ⚪  (score=0)
```python
            # Clone formatting state
```
L2601  ⚪  (score=0)
```python
            if copy_formatting:
```
L2602  ⚪  (score=0)
```python
                self.level = create_from.level
```
L2603  ⚪  (score=0)
```python
                self.bol = create_from.bol
```
L2604  ⚪  (score=0)
```python
                self.call_level = create_from.call_level
```
L2605  ⚪  (score=0)
```python
            self.last_pos = create_from.last_pos
```
L2606  ⚪  (score=0)
```python
            self.last_marked_pos = create_from.last_marked_pos
```
L2607  ⚪  (score=0)
```python
```
L2608  ⚪  (score=0)
```python
    def create_new(self, create_from, buffer, copy_formatting):
```
L2609  ⚪  (score=0)
```python
        # polymorphic constructor -- very slightly more versatile
```
L2610  ⚪  (score=0)
```python
        # than using __class__
```
L2611  ⚪  (score=0)
```python
        result = CCodeWriter(create_from, buffer, copy_formatting)
```
L2612  ⚪  (score=0)
```python
        return result
```
L2613  ⚪  (score=0)
```python
```
L2614  ⚪  (score=0)
```python
    def set_global_state(self, global_state:"GlobalState"):
```
L2615  ⚪  (score=0)
```python
        assert self.globalstate is None  # prevent overwriting once it's set
```
L2616  ⚪  (score=0)
```python
        self.globalstate = global_state
```
L2617  ⚪  (score=0)
```python
        self.code_config = global_state.code_config
```
L2618  ⚪  (score=0)
```python
```
L2619  ⚪  (score=0)
```python
    def copyto(self, f):
```
L2620  ⚪  (score=0)
```python
        self.buffer.copyto(f)
```
L2621  ⚪  (score=0)
```python
```
L2622  ⚪  (score=0)
```python
    def getvalue(self):
```
L2623  ⚪  (score=0)
```python
        return self.buffer.getvalue()
```
L2624  ⚪  (score=0)
```python
```
L2625  ⚪  (score=0)
```python
    def write(self, s):
```
L2626  ⚪  (score=0)
```python
        if '\n' in s:
```
L2627  ⚪  (score=0)
```python
            self._write_lines(s)
```
L2628  ⚪  (score=0)
```python
        else:
```
L2629  ⚪  (score=0)
```python
            self._write_to_buffer(s)
```
L2630  ⚪  (score=0)
```python
```
L2631  ⚪  (score=0)
```python
    @cython.final
```
L2632  ⚪  (score=0)
```python
    def _write_lines(self, s):
```
L2633  ⚪  (score=0)
```python
        # Cygdb needs to know which Cython source line corresponds to which C line.
```
L2634  ⚪  (score=0)
```python
        # Therefore, we write this information into "self.buffer.markers" and then write it from there
```
L2635  ⚪  (score=0)
```python
        # into cython_debug/cython_debug_info_* (see ModuleNode._serialize_lineno_map).
```
L2636  ⚪  (score=0)
```python
        filename_line = self.last_marked_pos[:2] if self.last_marked_pos else (None, 0)
```
L2637  ⚪  (score=0)
```python
        self.buffer.markers.extend([filename_line] * s.count('\n'))
```
L2638  ⚪  (score=0)
```python
```
L2639  ⚪  (score=0)
```python
        self._write_to_buffer(s)
```
L2640  ⚪  (score=0)
```python
```
L2641  ⚪  (score=0)
```python
    def _write_to_buffer(self, s):
```
L2642  ⚪  (score=0)
```python
        self.buffer.write(s)
```
L2643  ⚪  (score=0)
```python
```
L2644  ⚪  (score=0)
```python
    def insertion_point(self):
```
L2645  ⚪  (score=0)
```python
        other = self.create_new(create_from=self, buffer=self.buffer.insertion_point(), copy_formatting=True)
```
L2646  ⚪  (score=0)
```python
        return other
```
L2647  ⚪  (score=0)
```python
```
L2648  ⚪  (score=0)
```python
    def new_writer(self):
```
L2649  ⚪  (score=0)
```python
        """
```
L2650  ⚪  (score=0)
```python
        Creates a new CCodeWriter connected to the same global state, which
```
L2651  ⚪  (score=0)
```python
        can later be inserted using insert.
```
L2652  ⚪  (score=0)
```python
        """
```
L2653  ⚪  (score=0)
```python
        return CCodeWriter(create_from=self)
```
L2654  ⚪  (score=0)
```python
```
L2655  ⚪  (score=0)
```python
    def insert(self, writer):
```
L2656  ⚪  (score=0)
```python
        """
```
L2657  ⚪  (score=0)
```python
        Inserts the contents of another code writer (created with
```
L2658  ⚪  (score=0)
```python
        the same global state) in the current location.
```
L2659  ⚪  (score=0)
```python
```
L2660  ⚪  (score=0)
```python
        It is ok to write to the inserted writer also after insertion.
```
L2661  ⚪  (score=0)
```python
        """
```
L2662  ⚪  (score=0)
```python
        assert writer.globalstate is self.globalstate
```
L2663  ⚪  (score=0)
```python
        self.buffer.insert(writer.buffer)
```
L2664  ⚪  (score=0)
```python
```
L2665  ⚪  (score=0)
```python
    # Properties delegated to function scope
```
L2666  ⚪  (score=0)
```python
    @funccontext_property
```
L2667  ⚪  (score=0)
```python
    def label_counter(self): pass
```
L2668  ⚪  (score=0)
```python
    @funccontext_property
```
L2669  ⚪  (score=0)
```python
    def return_label(self): pass
```
L2670  ⚪  (score=0)
```python
    @funccontext_property
```
L2671  ⚪  (score=0)
```python
    def error_label(self): pass
```
L2672  ⚪  (score=0)
```python
    @funccontext_property
```
L2673  ⚪  (score=0)
```python
    def labels_used(self): pass
```
L2674  ⚪  (score=0)
```python
    @funccontext_property
```
L2675  ⚪  (score=0)
```python
    def continue_label(self): pass
```
L2676  ⚪  (score=0)
```python
    @funccontext_property
```
L2677  ⚪  (score=0)
```python
    def break_label(self): pass
```
L2678  ⚪  (score=0)
```python
    @funccontext_property
```
L2679  ⚪  (score=0)
```python
    def return_from_error_cleanup_label(self): pass
```
L2680  ⚪  (score=0)
```python
    @funccontext_property
```
L2681  ⚪  (score=0)
```python
    def yield_labels(self): pass
```
L2682  ⚪  (score=0)
```python
```
L2683  ⚪  (score=0)
```python
    def label_interceptor(self, new_labels, orig_labels, skip_to_label=None, pos=None, trace=True):
```
L2684  ⚪  (score=0)
```python
        """
```
L2685  ⚪  (score=0)
```python
        Helper for generating multiple label interceptor code blocks.
```
L2686  ⚪  (score=0)
```python
```
L2687  ⚪  (score=0)
```python
        @param new_labels: the new labels that should be intercepted
```
L2688  ⚪  (score=0)
```python
        @param orig_labels: the original labels that we should dispatch to after the interception
```
L2689  ⚪  (score=0)
```python
        @param skip_to_label: a label to skip to before starting the code blocks
```
L2690  ⚪  (score=0)
```python
        @param pos: the node position to mark for each interceptor block
```
L2691  ⚪  (score=0)
```python
        @param trace: add a trace line for the pos marker or not
```
L2692  ⚪  (score=0)
```python
        """
```
L2693  ⚪  (score=0)
```python
        for label, orig_label in zip(new_labels, orig_labels):
```
L2694  ⚪  (score=0)
```python
            if not self.label_used(label):
```
L2695  ⚪  (score=0)
```python
                continue
```
L2696  ⚪  (score=0)
```python
            if skip_to_label:
```
L2697  ⚪  (score=0)
```python
                # jump over the whole interception block
```
L2698  ⚪  (score=0)
```python
                self.put_goto(skip_to_label)
```
L2699  ⚪  (score=0)
```python
                skip_to_label = None
```
L2700  ⚪  (score=0)
```python
```
L2701  ⚪  (score=0)
```python
            if pos is not None:
```
L2702  ⚪  (score=0)
```python
                self.mark_pos(pos, trace=trace)
```
L2703  ⚪  (score=0)
```python
            self.put_label(label)
```
L2704  ⚪  (score=0)
```python
            yield (label, orig_label)
```
L2705  ⚪  (score=0)
```python
            self.put_goto(orig_label)
```
L2706  ⚪  (score=0)
```python
```
L2707  ⚪  (score=0)
```python
    # Functions delegated to function scope
```
L2708  ⚪  (score=0)
```python
    def new_label(self, name=None):    return self.funcstate.new_label(name)
```
L2709  ⚪  (score=0)
```python
    def new_error_label(self, *args):  return self.funcstate.new_error_label(*args)
```
L2710  ⚪  (score=0)
```python
    def new_yield_label(self, *args):  return self.funcstate.new_yield_label(*args)
```
L2711  ⚪  (score=0)
```python
    def get_loop_labels(self):         return self.funcstate.get_loop_labels()
```
L2712  ⚪  (score=0)
```python
    def set_loop_labels(self, labels): return self.funcstate.set_loop_labels(labels)
```
L2713  ⚪  (score=0)
```python
    def new_loop_labels(self, *args):  return self.funcstate.new_loop_labels(*args)
```
L2714  ⚪  (score=0)
```python
    def get_all_labels(self):          return self.funcstate.get_all_labels()
```
L2715  ⚪  (score=0)
```python
    def set_all_labels(self, labels):  return self.funcstate.set_all_labels(labels)
```
L2716  ⚪  (score=0)
```python
    def all_new_labels(self):          return self.funcstate.all_new_labels()
```
L2717  ⚪  (score=0)
```python
    def use_label(self, lbl):          return self.funcstate.use_label(lbl)
```
L2718  ⚪  (score=0)
```python
    def label_used(self, lbl):         return self.funcstate.label_used(lbl)
```
L2719  ⚪  (score=0)
```python
```
L2720  ⚪  (score=0)
```python
```
L2721  ⚪  (score=0)
```python
    def enter_cfunc_scope(self, scope):
```
L2722  ⚪  (score=0)
```python
        self.funcstate = FunctionState(self, scope=scope)
```
L2723  ⚪  (score=0)
```python
```
L2724  ⚪  (score=0)
```python
    def exit_cfunc_scope(self):
```
L2725  ⚪  (score=0)
```python
        if self.funcstate is None:
```
L2726  ⚪  (score=0)
```python
            return
```
L2727  ⚪  (score=0)
```python
        self.funcstate.validate_exit()
```
L2728  ⚪  (score=0)
```python
        self.funcstate = None
```
L2729  ⚪  (score=0)
```python
```
L2730  ⚪  (score=0)
```python
    def start_initcfunc(self, signature, scope=None, refnanny=False):
```
L2731  ⚪  (score=0)
```python
        """
```
L2732  ⚪  (score=0)
```python
        Init code helper function to start a cfunc scope and generate
```
L2733  ⚪  (score=0)
```python
        the prototype and function header ("static SIG {") of the function.
```
L2734  ⚪  (score=0)
```python
        """
```
L2735  ⚪  (score=0)
```python
        proto = self.globalstate.parts['initfunc_declarations']
```
L2736  ⚪  (score=0)
```python
        proto.putln(f"static CYTHON_SMALL_CODE {signature}; /*proto*/")
```
L2737  ⚪  (score=0)
```python
        self.enter_cfunc_scope(scope)
```
L2738  ⚪  (score=0)
```python
        self.putln("")
```
L2739  ⚪  (score=0)
```python
        self.putln(f"static {signature} {{")
```
L2740  ⚪  (score=0)
```python
        if refnanny:
```
L2741  ⚪  (score=0)
```python
            self.put_declare_refcount_context()
```
L2742  ⚪  (score=0)
```python
```
L2743  ⚪  (score=0)
```python
    def start_slotfunc(self, class_scope, return_type, c_slot_name, args_signature, needs_funcstate=True, needs_prototype=False):
```
L2744  ⚪  (score=0)
```python
        # Slot functions currently live in the class scope as they don't have direct access to the module state.
```
L2745  ⚪  (score=0)
```python
        slotfunc_cname = class_scope.mangle_internal(c_slot_name)
```
L2746  ⚪  (score=0)
```python
        declaration = f"static {return_type.declaration_code(slotfunc_cname)}({args_signature})"
```
L2747  ⚪  (score=0)
```python
```
L2748  ⚪  (score=0)
```python
        if needs_prototype:
```
L2749  ⚪  (score=0)
```python
            self.globalstate['decls'].putln(declaration.replace("CYTHON_UNUSED ", "") + "; /*proto*/")
```
L2750  ⚪  (score=0)
```python
        if needs_funcstate:
```
L2751  ⚪  (score=0)
```python
            self.enter_cfunc_scope(class_scope)
```
L2752  ⚪  (score=0)
```python
        self.putln("")
```
L2753  ⚪  (score=0)
```python
        self.putln(declaration + " {")
```
L2754  ⚪  (score=0)
```python
```
L2755  ⚪  (score=0)
```python
    # constant handling
```
L2756  ⚪  (score=0)
```python
```
L2757  ⚪  (score=0)
```python
    def get_py_int(self, str_value, longness):
```
L2758  ⚪  (score=0)
```python
        return self.name_in_module_state(
```
L2759  ⚪  (score=0)
```python
            self.globalstate.get_int_const(str_value, longness).cname
```
L2760  ⚪  (score=0)
```python
        )
```
L2761  ⚪  (score=0)
```python
```
L2762  ⚪  (score=0)
```python
    def get_py_float(self, str_value, value_code):
```
L2763  ⚪  (score=0)
```python
        return self.name_in_module_state(
```
L2764  ⚪  (score=0)
```python
            self.globalstate.get_float_const(str_value, value_code).cname
```
L2765  ⚪  (score=0)
```python
        )
```
L2766  ⚪  (score=0)
```python
```
L2767  ⚪  (score=0)
```python
    def get_py_const(self, prefix, dedup_key=None):
```
L2768  ⚪  (score=0)
```python
        return self.name_in_module_state(
```
L2769  ⚪  (score=0)
```python
            self.globalstate.get_py_const(prefix, dedup_key)
```
L2770  ⚪  (score=0)
```python
        )
```
L2771  ⚪  (score=0)
```python
```
L2772  ⚪  (score=0)
```python
    def get_string_const(self, text):
```
L2773  ⚪  (score=0)
```python
        return self.globalstate.get_string_const(text).cname
```
L2774  ⚪  (score=0)
```python
```
L2775  ⚪  (score=0)
```python
    def get_pyunicode_ptr_const(self, text):
```
L2776  ⚪  (score=0)
```python
        return self.globalstate.get_pyunicode_ptr_const(text)
```
L2777  ⚪  (score=0)
```python
```
L2778  ⚪  (score=0)
```python
    def get_py_string_const(self, text, identifier=None):
```
L2779  ⚪  (score=0)
```python
        cname = self.globalstate.get_py_string_const(
```
L2780  ⚪  (score=0)
```python
            text, identifier).cname
```
L2781  ⚪  (score=0)
```python
        return self.name_in_module_state(cname)
```
L2782  ⚪  (score=0)
```python
```
L2783  ⚪  (score=0)
```python
    def get_py_codeobj_const(self, node):
```
L2784  ⚪  (score=0)
```python
        return self.name_in_module_state(self.globalstate.get_py_codeobj_const(node))
```
L2785  ⚪  (score=0)
```python
```
L2786  ⚪  (score=0)
```python
    def get_argument_default_const(self, type):
```
L2787  ⚪  (score=0)
```python
        return self.name_in_module_state(self.globalstate.get_argument_default_const(type).cname)
```
L2788  ⚪  (score=0)
```python
```
L2789  ⚪  (score=0)
```python
    def intern(self, text):
```
L2790  ⚪  (score=0)
```python
        return self.get_py_string_const(text)
```
L2791  ⚪  (score=0)
```python
```
L2792  ⚪  (score=0)
```python
    def intern_identifier(self, text):
```
L2793  ⚪  (score=0)
```python
        return self.get_py_string_const(text, identifier=True)
```
L2794  ⚪  (score=0)
```python
```
L2795  ⚪  (score=0)
```python
    def get_cached_constants_writer(self, target=None):
```
L2796  ⚪  (score=0)
```python
        return self.globalstate.get_cached_constants_writer(target)
```
L2797  ⚪  (score=0)
```python
```
L2798  ⚪  (score=0)
```python
    def name_in_module_state(self, cname):
```
L2799  ⚪  (score=0)
```python
        if self.funcstate.scope is None:
```
L2800  ⚪  (score=0)
```python
            # This is a mess. For example, within the codeobj generation
```
L2801  ⚪  (score=0)
```python
            # funcstate.scope is None while evaluating the strings, but not while
```
L2802  ⚪  (score=0)
```python
            # evaluating the code objects themselves. Right now it doesn't matter
```
L2803  ⚪  (score=0)
```python
            # because it all ends up going to the same place, but to actually turn
```
L2804  ⚪  (score=0)
```python
            # it into something useful this mess will need to be fixed.
```
L2805  ⚪  (score=0)
```python
            return self.name_in_main_c_code_module_state(cname)
```
L2806  ⚪  (score=0)
```python
        return self.funcstate.scope.name_in_module_state(cname)
```
L2807  ⚪  (score=0)
```python
```
L2808  ⚪  (score=0)
```python
    @staticmethod
```
L2809  ⚪  (score=0)
```python
    def name_in_main_c_code_module_state(cname):
```
L2810  ⚪  (score=0)
```python
        # The functions where this applies to have the modulestate passed
```
L2811  ⚪  (score=0)
```python
        # as an argument to them and so it's better use that argument than
```
L2812  ⚪  (score=0)
```python
        # to try to get it from a global variable.
```
L2813  ⚪  (score=0)
```python
        return f"{Naming.modulestatevalue_cname}->{cname}"
```
L2814  ⚪  (score=0)
```python
```
L2815  ⚪  (score=0)
```python
    @staticmethod
```
L2816  ⚪  (score=0)
```python
    def name_in_slot_module_state(cname):
```
L2817  ⚪  (score=0)
```python
        # TODO - eventually this will go through PyType_GetModuleByDef
```
L2818  ⚪  (score=0)
```python
        # in cases where it's supported.
```
L2819  ⚪  (score=0)
```python
        return f"{Naming.modulestateglobal_cname}->{cname}"
```
L2820  ⚪  (score=0)
```python
```
L2821  ⚪  (score=0)
```python
    def namespace_cname_in_module_state(self, scope):
```
L2822  ⚪  (score=0)
```python
        if scope.is_py_class_scope:
```
L2823  ⚪  (score=0)
```python
            return scope.namespace_cname
```
L2824  ⚪  (score=0)
```python
        else:
```
L2825  ⚪  (score=0)
```python
            return self.name_in_module_state(scope.namespace_cname)
```
L2826  ⚪  (score=0)
```python
```
L2827  ⚪  (score=0)
```python
    def typeptr_cname_in_module_state(self, type):
```
L2828  ⚪  (score=0)
```python
        if type.is_extension_type:
```
L2829  ⚪  (score=0)
```python
            return self.name_in_module_state(type.typeptr_cname)
```
L2830  ⚪  (score=0)
```python
        else:
```
L2831  ⚪  (score=0)
```python
            return type.typeptr_cname
```
L2832  ⚪  (score=0)
```python
```
L2833  ⚪  (score=0)
```python
    # code generation
```
L2834  ⚪  (score=0)
```python
```
L2835  ⚪  (score=0)
```python
    def putln(self, code="", safe=False):
```
L2836  ⚪  (score=0)
```python
        if self.last_pos and self.bol:
```
L2837  ⚪  (score=0)
```python
            self.emit_marker()
```
L2838  ⚪  (score=0)
```python
        if self.code_config.emit_linenums and self.last_marked_pos:
```
L2839  ⚪  (score=0)
```python
            source_desc, line, _ = self.last_marked_pos
```
L2840  ⚪  (score=0)
```python
            self._write_lines(f'\n#line {line} "{source_desc.get_escaped_description()}"\n')
```
L2841  ⚪  (score=0)
```python
        if code:
```
L2842  ⚪  (score=0)
```python
            if safe:
```
L2843  ⚪  (score=0)
```python
                self.put_safe(code)
```
L2844  ⚪  (score=0)
```python
            else:
```
L2845  ⚪  (score=0)
```python
                self.put(code)
```
L2846  ⚪  (score=0)
```python
        self._write_lines("\n")
```
L2847  ⚪  (score=0)
```python
        self.bol = 1
```
L2848  ⚪  (score=0)
```python
```
L2849  ⚪  (score=0)
```python
    def mark_pos(self, pos, trace=True):
```
L2850  ⚪  (score=0)
```python
        if pos is None:
```
L2851  ⚪  (score=0)
```python
            return
```
L2852  ⚪  (score=0)
```python
        if self.last_marked_pos and self.last_marked_pos[:2] == pos[:2]:
```
L2853  ⚪  (score=0)
```python
            return
```
L2854  ⚪  (score=0)
```python
        self.last_pos = (pos, trace)
```
L2855  ⚪  (score=0)
```python
```
L2856  ⚪  (score=0)
```python
    @cython.final
```
L2857  ⚪  (score=0)
```python
    def emit_marker(self):
```
L2858  ⚪  (score=0)
```python
        pos, trace = self.last_pos
```
L2859  ⚪  (score=0)
```python
        self.last_marked_pos = pos
```
L2860  ⚪  (score=0)
```python
        self.last_pos = None
```
L2861  ⚪  (score=0)
```python
        self._write_lines("\n")
```
L2862  ⚪  (score=0)
```python
        if self.code_config.emit_code_comments:
```
L2863  ⚪  (score=0)
```python
            self.indent()
```
L2864  ⚪  (score=0)
```python
            self._write_lines(self._build_marker(pos))
```
L2865  ⚪  (score=0)
```python
        if trace:
```
L2866  ⚪  (score=0)
```python
            self.write_trace_line(pos)
```
L2867  ⚪  (score=0)
```python
```
L2868  ⚪  (score=0)
```python
    @cython.final
```
L2869  ⚪  (score=0)
```python
    def write_trace_line(self, pos):
```
L2870  ⚪  (score=0)
```python
        if self.funcstate and self.funcstate.can_trace and self.globalstate.directives['linetrace']:
```
L2871  ⚪  (score=0)
```python
            self.indent()
```
L2872  ⚪  (score=0)
```python
            self._write_lines(
```
L2873  ⚪  (score=0)
```python
                f'__Pyx_TraceLine({pos[1]:d},{self.pos_to_offset(pos):d},{not self.funcstate.gil_owned:d},{self.error_goto(pos)})\n')
```
L2874  ⚪  (score=0)
```python
```
L2875  ⚪  (score=0)
```python
    @cython.final
```
L2876  ⚪  (score=0)
```python
    def _build_marker(self, pos):
```
L2877  ⚪  (score=0)
```python
        source_desc, line, col = pos
```
L2878  ⚪  (score=0)
```python
        assert isinstance(source_desc, SourceDescriptor)
```
L2879  ⚪  (score=0)
```python
        contents = self.globalstate.commented_file_contents(source_desc)
```
L2880  ⚪  (score=0)
```python
        lines = contents[max(0, line-3):line]  # line numbers start at 1
```
L2881  ⚪  (score=0)
```python
        lines[-1] += '             # <<<<<<<<<<<<<<'
```
L2882  ⚪  (score=0)
```python
        lines += contents[line:line+2]
```
L2883  ⚪  (score=0)
```python
        code = "\n".join(lines)
```
L2884  ⚪  (score=0)
```python
        return f'/* "{source_desc.get_escaped_description()}":{line:d}\n{code}\n*/\n'
```
L2885  ⚪  (score=0)
```python
```
L2886  ⚪  (score=0)
```python
    def put_safe(self, code):
```
L2887  ⚪  (score=0)
```python
        # put code, but ignore {}
```
L2888  ⚪  (score=0)
```python
        self.write(code)
```
L2889  ⚪  (score=0)
```python
        self.bol = 0
```
L2890  ⚪  (score=0)
```python
```
L2891  ⚪  (score=0)
```python
    @cython.final
```
L2892  ⚪  (score=0)
```python
    def put_or_include(self, code, name):
```
L2893  ⚪  (score=0)
```python
        include_dir = self.globalstate.common_utility_include_dir
```
L2894  ⚪  (score=0)
```python
        if include_dir and len(code) > 1024:
```
L2895  ⚪  (score=0)
```python
            hash = hashlib.sha256(code.encode('utf8')).hexdigest()
```
L2896  ⚪  (score=0)
```python
            include_file = f"{name}_{hash}.h"
```
L2897  ⚪  (score=0)
```python
            path = os.path.join(include_dir, include_file)
```
L2898  ⚪  (score=0)
```python
            if not os.path.exists(path):
```
L2899  ⚪  (score=0)
```python
                tmp_path = f'{path}.tmp{os.getpid()}'
```
L2900  ⚪  (score=0)
```python
                done = False
```
L2901  ⚪  (score=0)
```python
                try:
```
L2902  ⚪  (score=0)
```python
                    with Utils.open_new_file(tmp_path) as f:
```
L2903  ⚪  (score=0)
```python
                        f.write(code)
```
L2904  ⚪  (score=0)
```python
                    shutil.move(tmp_path, path)
```
L2905  ⚪  (score=0)
```python
                    done = True
```
L2906  ⚪  (score=0)
```python
                except (FileExistsError, PermissionError):
```
L2907  ⚪  (score=0)
```python
                    # If a different process created the file faster than us,
```
L2908  ⚪  (score=0)
```python
                    # renaming can fail on Windows.  It's ok if the file is there now.
```
L2909  ⚪  (score=0)
```python
                    if not os.path.exists(path):
```
L2910  ⚪  (score=0)
```python
                        raise
```
L2911  ⚪  (score=0)
```python
                finally:
```
L2912  ⚪  (score=0)
```python
                    if not done and os.path.exists(tmp_path):
```
L2913  ⚪  (score=0)
```python
                        os.unlink(tmp_path)
```
L2914  ⚪  (score=0)
```python
            # We use forward slashes in the include path to assure identical code generation
```
L2915  ⚪  (score=0)
```python
            # under Windows and Posix.  C/C++ compilers should still understand it.
```
L2916  ⚪  (score=0)
```python
            c_path = path.replace('\\', '/')
```
L2917  ⚪  (score=0)
```python
            code = f'#include "{c_path}"\n'
```
L2918  ⚪  (score=0)
```python
        self.put_multilines(code)
```
L2919  ⚪  (score=0)
```python
```
L2920  ⚪  (score=0)
```python
    @cython.final
```
L2921  ⚪  (score=0)
```python
    def put_multilines(self, code):
```
L2922  ⚪  (score=0)
```python
        # We assume that the code is consistently indented and just needs overall indenting.
```
L2923  ⚪  (score=0)
```python
        # We also don't need to indent the first line since "self.put()" will do it for us.
```
L2924  ⚪  (score=0)
```python
        if self.level and '\n' in code:
```
L2925  ⚪  (score=0)
```python
            code = ("  " * self.level).join(code.splitlines(keepends=True))
```
L2926  ⚪  (score=0)
```python
        self.put(code)
```
L2927  ⚪  (score=0)
```python
```
L2928  ⚪  (score=0)
```python
    def put(self, code):
```
L2929  ⚪  (score=0)
```python
        fix_indent = False
```
L2930  ⚪  (score=0)
```python
        dl: cython.Py_ssize_t = code.count("{") if "{" in code else 0
```
L2931  ⚪  (score=0)
```python
        if "}" in code:
```
L2932  ⚪  (score=0)
```python
            dl -= code.count("}")
```
L2933  ⚪  (score=0)
```python
            if dl < 0:
```
L2934  ⚪  (score=0)
```python
                self.level += dl
```
L2935  ⚪  (score=0)
```python
            elif dl == 0 and code[0] == "}":
```
L2936  ⚪  (score=0)
```python
                # special cases like "} else {" need a temporary dedent
```
L2937  ⚪  (score=0)
```python
                fix_indent = True
```
L2938  ⚪  (score=0)
```python
                self.level -= 1
```
L2939  ⚪  (score=0)
```python
        if self.bol:
```
L2940  ⚪  (score=0)
```python
            self.indent()
```
L2941  ⚪  (score=0)
```python
        self.write(code)
```
L2942  ⚪  (score=0)
```python
        self.bol = 0
```
L2943  ⚪  (score=0)
```python
        if dl > 0:
```
L2944  ⚪  (score=0)
```python
            self.level += dl
```
L2945  ⚪  (score=0)
```python
        elif fix_indent:
```
L2946  ⚪  (score=0)
```python
            self.level += 1
```
L2947  ⚪  (score=0)
```python
```
L2948  ⚪  (score=0)
```python
    def put_code_here(self, utility: UtilityCode):
```
L2949  ⚪  (score=0)
```python
        # Puts the impl section of the utility code directly to the current position.
```
L2950  ⚪  (score=0)
```python
        # Ensure we don't have a proto section (but do allow init and cleanup sections
```
L2951  ⚪  (score=0)
```python
        # because they might be useful in future).
```
L2952  ⚪  (score=0)
```python
        assert not utility.proto, utility.name
```
L2953  ⚪  (score=0)
```python
        utility._put_code_section(self, self.globalstate, "impl")
```
L2954  ⚪  (score=0)
```python
        utility._put_init_code_section(self.globalstate)
```
L2955  ⚪  (score=0)
```python
        if utility.cleanup and Directives.generate_cleanup_code:
```
L2956  ⚪  (score=0)
```python
            utility._put_code_section(
```
L2957  ⚪  (score=0)
```python
                self.globalstate['cleanup_globals'], self.globalstate, "cleanup")
```
L2958  ⚪  (score=0)
```python
```
L2959  ⚪  (score=0)
```python
    @cython.final
```
L2960  ⚪  (score=0)
```python
    def increase_indent(self):
```
L2961  ⚪  (score=0)
```python
        self.level += 1
```
L2962  ⚪  (score=0)
```python
```
L2963  ⚪  (score=0)
```python
    @cython.final
```
L2964  ⚪  (score=0)
```python
    def decrease_indent(self):
```
L2965  ⚪  (score=0)
```python
        self.level -= 1
```
L2966  ⚪  (score=0)
```python
```
L2967  ⚪  (score=0)
```python
    @cython.final
```
L2968  ⚪  (score=0)
```python
    def begin_block(self):
```
L2969  ⚪  (score=0)
```python
        self.putln("{")
```
L2970  ⚪  (score=0)
```python
        self.increase_indent()
```
L2971  ⚪  (score=0)
```python
```
L2972  ⚪  (score=0)
```python
    @cython.final
```
L2973  ⚪  (score=0)
```python
    def end_block(self):
```
L2974  ⚪  (score=0)
```python
        self.decrease_indent()
```
L2975  ⚪  (score=0)
```python
        self.putln("}")
```
L2976  ⚪  (score=0)
```python
```
L2977  ⚪  (score=0)
```python
    @cython.final
```
L2978  ⚪  (score=0)
```python
    def indent(self):
```
L2979  ⚪  (score=0)
```python
        self._write_to_buffer("  " * self.level)
```
L2980  ⚪  (score=0)
```python
```
L2981  ⚪  (score=0)
```python
    def get_py_version_hex(self, pyversion):
```
L2982  ⚪  (score=0)
```python
        return "0x%02X%02X%02X%02X" % (tuple(pyversion) + (0,0,0,0))[:4]
```
L2983  ⚪  (score=0)
```python
```
L2984  ⚪  (score=0)
```python
    def put_label(self, lbl):
```
L2985  ⚪  (score=0)
```python
        if (lbl in self.funcstate.labels_used
```
L2986  ⚪  (score=0)
```python
                or "argument_unpacking_done" in lbl
```
L2987  ⚪  (score=0)
```python
                or "vectorcall_argument_unpacking_done" in lbl):
```
L2988  ⚪  (score=0)
```python
            self.putln("%s:;" % lbl)
```
L2989  ⚪  (score=0)
```python
```
L2990  ⚪  (score=0)
```python
    def put_goto(self, lbl):
```
L2991  ⚪  (score=0)
```python
        self.funcstate.use_label(lbl)
```
L2992  ⚪  (score=0)
```python
        self.putln("goto %s;" % lbl)
```
L2993  ⚪  (score=0)
```python
```
L2994  ⚪  (score=0)
```python
    def put_var_declaration(self, entry, storage_class="",
```
L2995  ⚪  (score=0)
```python
                            dll_linkage=None, definition=True):
```
L2996  ⚪  (score=0)
```python
        #print "Code.put_var_declaration:", entry.name, "definition =", definition ###
```
L2997  ⚪  (score=0)
```python
        if entry.visibility == 'private' and not (definition or entry.defined_in_pxd):
```
L2998  ⚪  (score=0)
```python
            #print "...private and not definition, skipping", entry.cname ###
```
L2999  ⚪  (score=0)
```python
            return
```
L3000  ⚪  (score=0)
```python
        if entry.visibility == "private" and not entry.used:
```
L3001  ⚪  (score=0)
```python
            #print "...private and not used, skipping", entry.cname ###
```
L3002  ⚪  (score=0)
```python
            return
```
L3003  ⚪  (score=0)
```python
        if not entry.cf_used:
```
L3004  ⚪  (score=0)
```python
            self.put('CYTHON_UNUSED ')
```
L3005  ⚪  (score=0)
```python
        if storage_class:
```
L3006  ⚪  (score=0)
```python
            self.put("%s " % storage_class)
```
L3007  ⚪  (score=0)
```python
        if entry.is_cpp_optional:
```
L3008  ⚪  (score=0)
```python
            self.put(entry.type.cpp_optional_declaration_code(
```
L3009  ⚪  (score=0)
```python
                entry.cname, dll_linkage=dll_linkage))
```
L3010  ⚪  (score=0)
```python
        else:
```
L3011  ⚪  (score=0)
```python
            self.put(entry.type.declaration_code(
```
L3012  ⚪  (score=0)
```python
                entry.cname, dll_linkage=dll_linkage))
```
L3013  ⚪  (score=0)
```python
        if entry.init is not None:
```
L3014  ⚪  (score=0)
```python
            self.put_safe(" = %s" % entry.type.literal_code(entry.init))
```
L3015  ⚪  (score=0)
```python
        elif entry.type.is_pyobject:
```
L3016  ⚪  (score=0)
```python
            self.put(" = NULL")
```
L3017  ⚪  (score=0)
```python
        self.putln(";")
```
L3018  ⚪  (score=0)
```python
        self.globalstate.use_entry_utility_code(entry)
```
L3019  ⚪  (score=0)
```python
```
L3020  ⚪  (score=0)
```python
    def put_temp_declarations(self, func_context: FunctionState):
```
L3021  ⚪  (score=0)
```python
        for name, type, manage_ref, static in func_context.temps_allocated:
```
L3022  ⚪  (score=0)
```python
            if type.is_cpp_class and not type.is_fake_reference and func_context.scope.directives['cpp_locals']:
```
L3023  ⚪  (score=0)
```python
                decl = type.cpp_optional_declaration_code(name)
```
L3024  ⚪  (score=0)
```python
            else:
```
L3025  ⚪  (score=0)
```python
                decl = type.declaration_code(name)
```
L3026  ⚪  (score=0)
```python
            if type.is_pyobject:
```
L3027  ⚪  (score=0)
```python
                self.putln("%s = NULL;" % decl)
```
L3028  ⚪  (score=0)
```python
            elif type.is_memoryviewslice:
```
L3029  ⚪  (score=0)
```python
                self.putln("%s = %s;" % (decl, type.literal_code(type.default_value)))
```
L3030  ⚪  (score=0)
```python
            else:
```
L3031  ⚪  (score=0)
```python
                self.putln("%s%s;" % (static and "static " or "", decl))
```
L3032  ⚪  (score=0)
```python
```
L3033  ⚪  (score=0)
```python
        if func_context.should_declare_error_indicator:
```
L3034  ⚪  (score=0)
```python
            if self.funcstate.uses_error_indicator:
```
L3035  ⚪  (score=0)
```python
                unused = ''
```
L3036  ⚪  (score=0)
```python
            else:
```
L3037  ⚪  (score=0)
```python
                unused = 'CYTHON_UNUSED '
```
L3038  ⚪  (score=0)
```python
            # Initialize these variables to silence compiler warnings
```
L3039  ⚪  (score=0)
```python
            self.putln("%sint %s = 0;" % (unused, Naming.lineno_cname))
```
L3040  ⚪  (score=0)
```python
            self.putln("%sconst char *%s = NULL;" % (unused, Naming.filename_cname))
```
L3041  ⚪  (score=0)
```python
            self.putln("%sint %s = 0;" % (unused, Naming.clineno_cname))
```
L3042  ⚪  (score=0)
```python
```
L3043  ⚪  (score=0)
```python
    def put_generated_by(self):
```
L3044  ⚪  (score=0)
```python
        self.putln(Utils.GENERATED_BY_MARKER)
```
L3045  ⚪  (score=0)
```python
        self.putln("")
```
L3046  ⚪  (score=0)
```python
```
L3047  ⚪  (score=0)
```python
    def put_h_guard(self, guard):
```
L3048  ⚪  (score=0)
```python
        self.putln("#ifndef %s" % guard)
```
L3049  ⚪  (score=0)
```python
        self.putln("#define %s" % guard)
```
L3050  ⚪  (score=0)
```python
```
L3051  ⚪  (score=0)
```python
    def unlikely(self, cond):
```
L3052  ⚪  (score=0)
```python
        if Directives.gcc_branch_hints:
```
L3053  ⚪  (score=0)
```python
            return 'unlikely(%s)' % cond
```
L3054  ⚪  (score=0)
```python
        else:
```
L3055  ⚪  (score=0)
```python
            return cond
```
L3056  ⚪  (score=0)
```python
```
L3057  ⚪  (score=0)
```python
    def build_function_modifiers(self, modifiers, mapper=modifier_output_mapper):
```
L3058  ⚪  (score=0)
```python
        if not modifiers:
```
L3059  ⚪  (score=0)
```python
            return ''
```
L3060  ⚪  (score=0)
```python
        return '%s ' % ' '.join([mapper(m,m) for m in modifiers])
```
L3061  ⚪  (score=0)
```python
```
L3062  ⚪  (score=0)
```python
    # Python objects and reference counting
```
L3063  ⚪  (score=0)
```python
```
L3064  ⚪  (score=0)
```python
    def entry_as_pyobject(self, entry):
```
L3065  ⚪  (score=0)
```python
        type = entry.type
```
L3066  ⚪  (score=0)
```python
        if (not entry.is_self_arg and not entry.type.is_complete()
```
L3067  ⚪  (score=0)
```python
                or entry.type.is_extension_type):
```
L3068  ⚪  (score=0)
```python
            return "(PyObject *)" + entry.cname
```
L3069  ⚪  (score=0)
```python
        else:
```
L3070  ⚪  (score=0)
```python
            return entry.cname
```
L3071  ⚪  (score=0)
```python
```
L3072  ⚪  (score=0)
```python
    def as_pyobject(self, cname, type):
```
L3073  ⚪  (score=0)
```python
        from .PyrexTypes import py_object_type, typecast
```
L3074  ⚪  (score=0)
```python
        return typecast(py_object_type, type, cname)
```
L3075  ⚪  (score=0)
```python
```
L3076  ⚪  (score=0)
```python
    def put_gotref(self, cname, type):
```
L3077  ⚪  (score=0)
```python
        type.generate_gotref(self, cname)
```
L3078  ⚪  (score=0)
```python
```
L3079  ⚪  (score=0)
```python
    def put_giveref(self, cname, type):
```
L3080  ⚪  (score=0)
```python
        type.generate_giveref(self, cname)
```
L3081  ⚪  (score=0)
```python
```
L3082  ⚪  (score=0)
```python
    def put_xgiveref(self, cname, type):
```
L3083  ⚪  (score=0)
```python
        type.generate_xgiveref(self, cname)
```
L3084  ⚪  (score=0)
```python
```
L3085  ⚪  (score=0)
```python
    def put_xgotref(self, cname, type):
```
L3086  ⚪  (score=0)
```python
        type.generate_xgotref(self, cname)
```
L3087  ⚪  (score=0)
```python
```
L3088  ⚪  (score=0)
```python
    def put_incref(self, cname, type, nanny=True):
```
L3089  ⚪  (score=0)
```python
        # Note: original put_Memslice_Incref/Decref also added in some utility code
```
L3090  ⚪  (score=0)
```python
        # this is unnecessary since the relevant utility code is loaded anyway if a memoryview is used
```
L3091  ⚪  (score=0)
```python
        # and so has been removed. However, it's potentially a feature that might be useful here
```
L3092  ⚪  (score=0)
```python
        type.generate_incref(self, cname, nanny=nanny)
```
L3093  ⚪  (score=0)
```python
```
L3094  ⚪  (score=0)
```python
    def put_xincref(self, cname, type, nanny=True):
```
L3095  ⚪  (score=0)
```python
        type.generate_xincref(self, cname, nanny=nanny)
```
L3096  ⚪  (score=0)
```python
```
L3097  ⚪  (score=0)
```python
    def put_decref(self, cname, type, nanny=True, have_gil=True):
```
L3098  ⚪  (score=0)
```python
        type.generate_decref(self, cname, nanny=nanny, have_gil=have_gil)
```
L3099  ⚪  (score=0)
```python
```
L3100  ⚪  (score=0)
```python
    def put_xdecref(self, cname, type, nanny=True, have_gil=True):
```
L3101  ⚪  (score=0)
```python
        type.generate_xdecref(self, cname, nanny=nanny, have_gil=have_gil)
```
L3102  ⚪  (score=0)
```python
```
L3103  ⚪  (score=0)
```python
    def put_decref_clear(self, cname, type, clear_before_decref=False, nanny=True, have_gil=True):
```
L3104  ⚪  (score=0)
```python
        type.generate_decref_clear(self, cname, clear_before_decref=clear_before_decref,
```
L3105  ⚪  (score=0)
```python
                              nanny=nanny, have_gil=have_gil)
```
L3106  ⚪  (score=0)
```python
```
L3107  ⚪  (score=0)
```python
    def put_xdecref_clear(self, cname, type, clear_before_decref=False, nanny=True, have_gil=True):
```
L3108  ⚪  (score=0)
```python
        type.generate_xdecref_clear(self, cname, clear_before_decref=clear_before_decref,
```
L3109  ⚪  (score=0)
```python
                              nanny=nanny, have_gil=have_gil)
```
L3110  ⚪  (score=0)
```python
```
L3111  ⚪  (score=0)
```python
    def put_decref_set(self, cname, type, rhs_cname):
```
L3112  ⚪  (score=0)
```python
        type.generate_decref_set(self, cname, rhs_cname)
```
L3113  ⚪  (score=0)
```python
```
L3114  ⚪  (score=0)
```python
    def put_xdecref_set(self, cname, type, rhs_cname):
```
L3115  ⚪  (score=0)
```python
        type.generate_xdecref_set(self, cname, rhs_cname)
```
L3116  ⚪  (score=0)
```python
```
L3117  ⚪  (score=0)
```python
    def put_incref_memoryviewslice(self, slice_cname, type, have_gil):
```
L3118  ⚪  (score=0)
```python
        # TODO ideally this would just be merged into "put_incref"
```
L3119  ⚪  (score=0)
```python
        type.generate_incref_memoryviewslice(self, slice_cname, have_gil=have_gil)
```
L3120  ⚪  (score=0)
```python
```
L3121  ⚪  (score=0)
```python
    def put_var_incref_memoryviewslice(self, entry, have_gil):
```
L3122  ⚪  (score=0)
```python
        self.put_incref_memoryviewslice(entry.cname, entry.type, have_gil=have_gil)
```
L3123  ⚪  (score=0)
```python
```
L3124  ⚪  (score=0)
```python
    def put_var_gotref(self, entry):
```
L3125  ⚪  (score=0)
```python
        self.put_gotref(entry.cname, entry.type)
```
L3126  ⚪  (score=0)
```python
```
L3127  ⚪  (score=0)
```python
    def put_var_giveref(self, entry):
```
L3128  ⚪  (score=0)
```python
        self.put_giveref(entry.cname, entry.type)
```
L3129  ⚪  (score=0)
```python
```
L3130  ⚪  (score=0)
```python
    def put_var_xgotref(self, entry):
```
L3131  ⚪  (score=0)
```python
        self.put_xgotref(entry.cname, entry.type)
```
L3132  ⚪  (score=0)
```python
```
L3133  ⚪  (score=0)
```python
    def put_var_xgiveref(self, entry):
```
L3134  ⚪  (score=0)
```python
        self.put_xgiveref(entry.cname, entry.type)
```
L3135  ⚪  (score=0)
```python
```
L3136  ⚪  (score=0)
```python
    def put_var_incref(self, entry, **kwds):
```
L3137  ⚪  (score=0)
```python
        self.put_incref(entry.cname, entry.type, **kwds)
```
L3138  ⚪  (score=0)
```python
```
L3139  ⚪  (score=0)
```python
    def put_var_xincref(self, entry, **kwds):
```
L3140  ⚪  (score=0)
```python
        self.put_xincref(entry.cname, entry.type, **kwds)
```
L3141  ⚪  (score=0)
```python
```
L3142  ⚪  (score=0)
```python
    def put_var_decref(self, entry, **kwds):
```
L3143  ⚪  (score=0)
```python
        self.put_decref(entry.cname, entry.type, **kwds)
```
L3144  ⚪  (score=0)
```python
```
L3145  ⚪  (score=0)
```python
    def put_var_xdecref(self, entry, **kwds):
```
L3146  ⚪  (score=0)
```python
        self.put_xdecref(entry.cname, entry.type, **kwds)
```
L3147  ⚪  (score=0)
```python
```
L3148  ⚪  (score=0)
```python
    def put_var_decref_clear(self, entry, **kwds):
```
L3149  ⚪  (score=0)
```python
        self.put_decref_clear(entry.cname, entry.type, clear_before_decref=entry.in_closure, **kwds)
```
L3150  ⚪  (score=0)
```python
```
L3151  ⚪  (score=0)
```python
    def put_var_decref_set(self, entry, rhs_cname, **kwds):
```
L3152  ⚪  (score=0)
```python
        self.put_decref_set(entry.cname, entry.type, rhs_cname, **kwds)
```
L3153  ⚪  (score=0)
```python
```
L3154  ⚪  (score=0)
```python
    def put_var_xdecref_set(self, entry, rhs_cname, **kwds):
```
L3155  ⚪  (score=0)
```python
        self.put_xdecref_set(entry.cname, entry.type, rhs_cname, **kwds)
```
L3156  ⚪  (score=0)
```python
```
L3157  ⚪  (score=0)
```python
    def put_var_xdecref_clear(self, entry, **kwds):
```
L3158  ⚪  (score=0)
```python
        self.put_xdecref_clear(entry.cname, entry.type, clear_before_decref=entry.in_closure, **kwds)
```
L3159  ⚪  (score=0)
```python
```
L3160  ⚪  (score=0)
```python
    def put_var_decrefs(self, entries, used_only = 0):
```
L3161  ⚪  (score=0)
```python
        for entry in entries:
```
L3162  ⚪  (score=0)
```python
            if not used_only or entry.used:
```
L3163  ⚪  (score=0)
```python
                if entry.xdecref_cleanup:
```
L3164  ⚪  (score=0)
```python
                    self.put_var_xdecref(entry)
```
L3165  ⚪  (score=0)
```python
                else:
```
L3166  ⚪  (score=0)
```python
                    self.put_var_decref(entry)
```
L3167  ⚪  (score=0)
```python
```
L3168  ⚪  (score=0)
```python
    def put_var_xdecrefs(self, entries):
```
L3169  ⚪  (score=0)
```python
        for entry in entries:
```
L3170  ⚪  (score=0)
```python
            self.put_var_xdecref(entry)
```
L3171  ⚪  (score=0)
```python
```
L3172  ⚪  (score=0)
```python
    def put_var_xdecrefs_clear(self, entries):
```
L3173  ⚪  (score=0)
```python
        for entry in entries:
```
L3174  ⚪  (score=0)
```python
            self.put_var_xdecref_clear(entry)
```
L3175  ⚪  (score=0)
```python
```
L3176  ⚪  (score=0)
```python
    def put_make_object_deferred(self, cname):
```
L3177  ⚪  (score=0)
```python
        # Deferred reference counting is probably only worthwhile on global classes
```
L3178  ⚪  (score=0)
```python
        # that we expect to be long-term accessible.  So for now exclude it if not
```
L3179  ⚪  (score=0)
```python
        # at class or module scope.
```
L3180  ⚪  (score=0)
```python
        if (self.funcstate.scope.is_module_scope or
```
L3181  ⚪  (score=0)
```python
                self.funcstate.scope.is_c_class_scope or
```
L3182  ⚪  (score=0)
```python
                self.funcstate.scope.is_py_class_scope):
```
L3183  ⚪  (score=0)
```python
            self.putln("#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000")
```
L3184  ⚪  (score=0)
```python
            self.putln(f"PyUnstable_Object_EnableDeferredRefcount({cname});")
```
L3185  ⚪  (score=0)
```python
            self.putln("#endif")
```
L3186  ⚪  (score=0)
```python
```
L3187  ⚪  (score=0)
```python
    def put_init_to_py_none(self, cname, type, nanny=True):
```
L3188  ⚪  (score=0)
```python
        from .PyrexTypes import py_object_type, typecast
```
L3189  ⚪  (score=0)
```python
        py_none = typecast(type, py_object_type, "Py_None")
```
L3190  ⚪  (score=0)
```python
        if nanny:
```
L3191  ⚪  (score=0)
```python
            self.putln("%s = %s; __Pyx_INCREF(Py_None);" % (cname, py_none))
```
L3192  ⚪  (score=0)
```python
        else:
```
L3193  ⚪  (score=0)
```python
            self.putln("%s = %s; Py_INCREF(Py_None);" % (cname, py_none))
```
L3194  ⚪  (score=0)
```python
```
L3195  ⚪  (score=0)
```python
    def put_init_var_to_py_none(self, entry, template = "%s", nanny=True):
```
L3196  ⚪  (score=0)
```python
        code = template % entry.cname
```
L3197  ⚪  (score=0)
```python
        #if entry.type.is_extension_type:
```
L3198  ⚪  (score=0)
```python
        #    code = "((PyObject*)%s)" % code
```
L3199  ⚪  (score=0)
```python
        self.put_init_to_py_none(code, entry.type, nanny)
```
L3200  ⚪  (score=0)
```python
        if entry.in_closure:
```
L3201  ⚪  (score=0)
```python
            self.put_giveref('Py_None')
```
L3202  ⚪  (score=0)
```python
```
L3203  ⚪  (score=0)
```python
    def put_pymethoddef(self, entry, term, allow_skip=True, wrapper_code_writer=None):
```
L3204  ⚪  (score=0)
```python
        is_number_slot = False
```
L3205  ⚪  (score=0)
```python
        if entry.is_special or entry.name == '__getattribute__':
```
L3206  ⚪  (score=0)
```python
            from . import TypeSlots
```
L3207  ⚪  (score=0)
```python
            if entry.name not in special_py_methods:
```
L3208  ⚪  (score=0)
```python
                if TypeSlots.is_binop_number_slot(entry.name):
```
L3209  ⚪  (score=0)
```python
                    # It's useful if numeric binops are created with meth coexist
```
L3210  ⚪  (score=0)
```python
                    # so they can be called directly by looking up the name, skipping the
```
L3211  ⚪  (score=0)
```python
                    # dispatch wrapper that enables the reverse slots.  This is most useful
```
L3212  ⚪  (score=0)
```python
                    # when c_api_binop_methods is False, but there's no reason not to do it
```
L3213  ⚪  (score=0)
```python
                    # all the time
```
L3214  ⚪  (score=0)
```python
                    is_number_slot = True
```
L3215  ⚪  (score=0)
```python
                elif entry.name == '__getattr__' and not self.globalstate.directives['fast_getattr']:
```
L3216  ⚪  (score=0)
```python
                    pass
```
L3217  ⚪  (score=0)
```python
                # Python's typeobject.c will automatically fill in our slot
```
L3218  ⚪  (score=0)
```python
                # in add_operators() (called by PyType_Ready) with a value
```
L3219  ⚪  (score=0)
```python
                # that's better than ours.
```
L3220  ⚪  (score=0)
```python
                elif allow_skip:
```
L3221  ⚪  (score=0)
```python
                    return
```
L3222  ⚪  (score=0)
```python
```
L3223  ⚪  (score=0)
```python
        method_flags = entry.signature.method_flags()
```
L3224  ⚪  (score=0)
```python
        if not method_flags:
```
L3225  ⚪  (score=0)
```python
            return
```
L3226  ⚪  (score=0)
```python
        if entry.is_special:
```
L3227  ⚪  (score=0)
```python
            method_flags += [TypeSlots.method_coexist]
```
L3228  ⚪  (score=0)
```python
        func_ptr = wrapper_code_writer.put_pymethoddef_wrapper(entry) if wrapper_code_writer else entry.func_cname
```
L3229  ⚪  (score=0)
```python
        # Add required casts, but try not to shadow real warnings.
```
L3230  ⚪  (score=0)
```python
        cast = entry.signature.method_function_type()
```
L3231  ⚪  (score=0)
```python
        if cast != 'PyCFunction':
```
L3232  ⚪  (score=0)
```python
            func_ptr = '(void(*)(void))(%s)%s' % (cast, func_ptr)
```
L3233  ⚪  (score=0)
```python
        entry_name = entry.name.as_c_string_literal()
```
L3234  ⚪  (score=0)
```python
        if is_number_slot:
```
L3235  ⚪  (score=0)
```python
            # Unlike most special functions, binop numeric operator slots are actually generated here
```
L3236  ⚪  (score=0)
```python
            # (to ensure that they can be looked up). However, they're sometimes guarded by the preprocessor
```
L3237  ⚪  (score=0)
```python
            # so a bit of extra logic is needed
```
L3238  ⚪  (score=0)
```python
            slot = TypeSlots.get_slot_table(self.globalstate.directives).get_slot_by_method_name(entry.name)
```
L3239  ⚪  (score=0)
```python
            preproc_guard = slot.preprocessor_guard_code()
```
L3240  ⚪  (score=0)
```python
            if preproc_guard:
```
L3241  ⚪  (score=0)
```python
                self.putln(preproc_guard)
```
L3242  ⚪  (score=0)
```python
        self.putln(
```
L3243  ⚪  (score=0)
```python
            '{%s, (PyCFunction)%s, %s, %s}%s' % (
```
L3244  ⚪  (score=0)
```python
                entry_name,
```
L3245  ⚪  (score=0)
```python
                func_ptr,
```
L3246  ⚪  (score=0)
```python
                "|".join(method_flags),
```
L3247  ⚪  (score=0)
```python
                entry.doc_cname if entry.doc else '0',
```
L3248  ⚪  (score=0)
```python
                term))
```
L3249  ⚪  (score=0)
```python
        if is_number_slot and preproc_guard:
```
L3250  ⚪  (score=0)
```python
            self.putln("#endif")
```
L3251  ⚪  (score=0)
```python
```
L3252  ⚪  (score=0)
```python
    def put_pymethoddef_wrapper(self, entry):
```
L3253  ⚪  (score=0)
```python
        func_cname = entry.func_cname
```
L3254  ⚪  (score=0)
```python
        if entry.is_special:
```
L3255  ⚪  (score=0)
```python
            method_flags = entry.signature.method_flags() or []
```
L3256  ⚪  (score=0)
```python
            from .TypeSlots import method_noargs
```
L3257  ⚪  (score=0)
```python
            if method_noargs in method_flags:
```
L3258  ⚪  (score=0)
```python
                # Special NOARGS methods really take no arguments besides 'self', but PyCFunction expects one.
```
L3259  ⚪  (score=0)
```python
                func_cname = Naming.method_wrapper_prefix + func_cname
```
L3260  ⚪  (score=0)
```python
                self.putln("static PyObject *%s(PyObject *self, CYTHON_UNUSED PyObject *arg) {" % func_cname)
```
L3261  ⚪  (score=0)
```python
                func_call = "%s(self)" % entry.func_cname
```
L3262  ⚪  (score=0)
```python
                if entry.name == "__next__":
```
L3263  ⚪  (score=0)
```python
                    self.putln("PyObject *res = %s;" % func_call)
```
L3264  ⚪  (score=0)
```python
                    # tp_iternext can return NULL without an exception
```
L3265  ⚪  (score=0)
```python
                    self.putln("if (!res && !PyErr_Occurred()) { PyErr_SetNone(PyExc_StopIteration); }")
```
L3266  ⚪  (score=0)
```python
                    self.putln("return res;")
```
L3267  ⚪  (score=0)
```python
                else:
```
L3268  ⚪  (score=0)
```python
                    self.putln("return %s;" % func_call)
```
L3269  ⚪  (score=0)
```python
                self.putln("}")
```
L3270  ⚪  (score=0)
```python
        return func_cname
```
L3271  ⚪  (score=0)
```python
```
L3272  ⚪  (score=0)
```python
    # GIL methods
```
L3273  ⚪  (score=0)
```python
```
L3274  ⚪  (score=0)
```python
    def use_fast_gil_utility_code(self):
```
L3275  ⚪  (score=0)
```python
        if self.globalstate.directives['fast_gil']:
```
L3276  ⚪  (score=0)
```python
            self.globalstate.use_utility_code(UtilityCode.load_cached("FastGil", "ModuleSetupCode.c"))
```
L3277  ⚪  (score=0)
```python
        else:
```
L3278  ⚪  (score=0)
```python
            self.globalstate.use_utility_code(UtilityCode.load_cached("NoFastGil", "ModuleSetupCode.c"))
```
L3279  ⚪  (score=0)
```python
```
L3280  ⚪  (score=0)
```python
    def put_ensure_gil(self, declare_gilstate=True, variable=None):
```
L3281  ⚪  (score=0)
```python
        """
```
L3282  ⚪  (score=0)
```python
        Acquire the GIL. The generated code is safe even when no PyThreadState
```
L3283  ⚪  (score=0)
```python
        has been allocated for this thread (for threads not initialized by
```
L3284  ⚪  (score=0)
```python
        using the Python API). Additionally, the code generated by this method
```
L3285  ⚪  (score=0)
```python
        may be called recursively.
```
L3286  ⚪  (score=0)
```python
        """
```
L3287  ⚪  (score=0)
```python
        if self.globalstate.directives['subinterpreters_compatible'] != 'no':
```
L3288  ⚪  (score=0)
```python
            from .Errors import warning
```
L3289  ⚪  (score=0)
```python
            warning(
```
L3290  ⚪  (score=0)
```python
                self.last_marked_pos,
```
L3291  ⚪  (score=0)
```python
                "Acquiring the GIL is currently very unlikely to work correctly with subinterpreters.",
```
L3292  ⚪  (score=0)
```python
                2
```
L3293  ⚪  (score=0)
```python
            )
```
L3294  ⚪  (score=0)
```python
        self.globalstate.use_utility_code(
```
L3295  ⚪  (score=0)
```python
            UtilityCode.load_cached("ForceInitThreads", "ModuleSetupCode.c"))
```
L3296  ⚪  (score=0)
```python
        self.use_fast_gil_utility_code()
```
L3297  ⚪  (score=0)
```python
        if not variable:
```
L3298  ⚪  (score=0)
```python
            variable = '__pyx_gilstate_save'
```
L3299  ⚪  (score=0)
```python
            if declare_gilstate:
```
L3300  ⚪  (score=0)
```python
                self.put("PyGILState_STATE ")
```
L3301  ⚪  (score=0)
```python
        self.putln("%s = __Pyx_PyGILState_Ensure();" % variable)
```
L3302  ⚪  (score=0)
```python
```
L3303  ⚪  (score=0)
```python
    def put_release_ensured_gil(self, variable=None):
```
L3304  ⚪  (score=0)
```python
        """
```
L3305  ⚪  (score=0)
```python
        Releases the GIL, corresponds to `put_ensure_gil`.
```
L3306  ⚪  (score=0)
```python
        """
```
L3307  ⚪  (score=0)
```python
        self.use_fast_gil_utility_code()
```
L3308  ⚪  (score=0)
```python
        if not variable:
```
L3309  ⚪  (score=0)
```python
            variable = '__pyx_gilstate_save'
```
L3310  ⚪  (score=0)
```python
        self.putln("__Pyx_PyGILState_Release(%s);" % variable)
```
L3311  ⚪  (score=0)
```python
```
L3312  ⚪  (score=0)
```python
    def put_acquire_freethreading_lock(self):
```
L3313  ⚪  (score=0)
```python
        self.putln("#if CYTHON_COMPILING_IN_CPYTHON_FREETHREADING")
```
L3314  ⚪  (score=0)
```python
        self.putln(f"PyMutex_Lock(&{Naming.parallel_freethreading_mutex});")
```
L3315  ⚪  (score=0)
```python
        self.putln("#endif")
```
L3316  ⚪  (score=0)
```python
```
L3317  ⚪  (score=0)
```python
    def put_release_freethreading_lock(self):
```
L3318  ⚪  (score=0)
```python
        self.putln("#if CYTHON_COMPILING_IN_CPYTHON_FREETHREADING")
```
L3319  ⚪  (score=0)
```python
        self.putln(f"PyMutex_Unlock(&{Naming.parallel_freethreading_mutex});")
```
L3320  ⚪  (score=0)
```python
        self.putln("#endif")
```
L3321  ⚪  (score=0)
```python
```
L3322  ⚪  (score=0)
```python
    def put_acquire_gil(self, variable=None, unknown_gil_state=True):
```
L3323  ⚪  (score=0)
```python
        """
```
L3324  ⚪  (score=0)
```python
        Acquire the GIL. The thread's thread state must have been initialized
```
L3325  ⚪  (score=0)
```python
        by a previous `put_release_gil`
```
L3326  ⚪  (score=0)
```python
        """
```
L3327  ⚪  (score=0)
```python
        self.use_fast_gil_utility_code()
```
L3328  ⚪  (score=0)
```python
        self.putln("__Pyx_FastGIL_Forget();")
```
L3329  ⚪  (score=0)
```python
        if variable:
```
L3330  ⚪  (score=0)
```python
            self.putln('_save = %s;' % variable)
```
L3331  ⚪  (score=0)
```python
        if unknown_gil_state:
```
L3332  ⚪  (score=0)
```python
            func_name = "__Pyx_RestoreUnknownThread"
```
L3333  ⚪  (score=0)
```python
            self.globalstate.use_utility_code(
```
L3334  ⚪  (score=0)
```python
                UtilityCode.load_cached("ReleaseUnknownGil", "ModuleSetupCode.c"))
```
L3335  ⚪  (score=0)
```python
        else:
```
L3336  ⚪  (score=0)
```python
            func_name = "PyEval_RestoreThread"
```
L3337  ⚪  (score=0)
```python
        self.putln(f"{func_name}(_save);")
```
L3338  ⚪  (score=0)
```python
```
L3339  ⚪  (score=0)
```python
    def put_release_gil(self, variable=None, unknown_gil_state=True):
```
L3340  ⚪  (score=0)
```python
        "Release the GIL, corresponds to `put_acquire_gil`."
```
L3341  ⚪  (score=0)
```python
        self.use_fast_gil_utility_code()
```
L3342  ⚪  (score=0)
```python
        if unknown_gil_state:
```
L3343  ⚪  (score=0)
```python
            self.globalstate.use_utility_code(
```
L3344  ⚪  (score=0)
```python
                UtilityCode.load_cached("ReleaseUnknownGil", "ModuleSetupCode.c"))
```
L3345  ⚪  (score=0)
```python
            func_name = "__Pyx_SaveUnknownThread"
```
L3346  ⚪  (score=0)
```python
            result_type = "__Pyx_UnknownThreadState"
```
L3347  ⚪  (score=0)
```python
        else:
```
L3348  ⚪  (score=0)
```python
            func_name = "PyEval_SaveThread"
```
L3349  ⚪  (score=0)
```python
            result_type = "PyThreadState *"
```
L3350  ⚪  (score=0)
```python
        self.putln(f"{result_type} _save;")
```
L3351  ⚪  (score=0)
```python
        self.putln(f"_save = {func_name}();")
```
L3352  ⚪  (score=0)
```python
        if variable:
```
L3353  ⚪  (score=0)
```python
            self.putln('%s = _save;' % variable)
```
L3354  ⚪  (score=0)
```python
        self.putln("__Pyx_FastGIL_Remember();")
```
L3355  ⚪  (score=0)
```python
```
L3356  ⚪  (score=0)
```python
    def declare_gilstate(self):
```
L3357  ⚪  (score=0)
```python
        self.putln("PyGILState_STATE __pyx_gilstate_save;")
```
L3358  ⚪  (score=0)
```python
```
L3359  ⚪  (score=0)
```python
    # error handling
```
L3360  ⚪  (score=0)
```python
```
L3361  ⚪  (score=0)
```python
    def put_error_if_neg(self, pos, value):
```
L3362  ⚪  (score=0)
```python
        # TODO this path is almost _never_ taken, yet this macro makes is slower!
```
L3363  ⚪  (score=0)
```python
        # return self.putln("if (unlikely(%s < 0)) %s" % (value, self.error_goto(pos)))
```
L3364  ⚪  (score=0)
```python
        return self.putln("if (%s < (0)) %s" % (value, self.error_goto(pos)))
```
L3365  ⚪  (score=0)
```python
```
L3366  ⚪  (score=0)
```python
    def put_error_if_unbound(self, pos, entry, in_nogil_context=False, unbound_check_code=None):
```
L3367  ⚪  (score=0)
```python
        nogil_tag = "Nogil" if in_nogil_context else ""
```
L3368  ⚪  (score=0)
```python
        if entry.from_closure:
```
L3369  ⚪  (score=0)
```python
            func = "RaiseClosureNameError"
```
L3370  ⚪  (score=0)
```python
        elif entry.type.is_cpp_class and entry.is_cglobal:
```
L3371  ⚪  (score=0)
```python
            func = "RaiseCppGlobalNameError"
```
L3372  ⚪  (score=0)
```python
        elif entry.type.is_cpp_class and entry.is_variable and not entry.is_member and entry.scope.is_c_class_scope:
```
L3373  ⚪  (score=0)
```python
            # there doesn't seem to be a good way to detecting an instance-attribute of a C class
```
L3374  ⚪  (score=0)
```python
            # (is_member is only set for class attributes)
```
L3375  ⚪  (score=0)
```python
            func = "RaiseCppAttributeError"
```
L3376  ⚪  (score=0)
```python
        else:
```
L3377  ⚪  (score=0)
```python
            func = "RaiseUnboundLocalError"
```
L3378  ⚪  (score=0)
```python
```
L3379  ⚪  (score=0)
```python
        self.globalstate.use_utility_code(
```
L3380  ⚪  (score=0)
```python
                UtilityCode.load_cached(f"{func}{nogil_tag}", "ObjectHandling.c"))
```
L3381  ⚪  (score=0)
```python
```
L3382  ⚪  (score=0)
```python
        if not unbound_check_code:
```
L3383  ⚪  (score=0)
```python
            unbound_check_code = entry.type.check_for_null_code(entry.cname)
```
L3384  ⚪  (score=0)
```python
        self.putln('if (unlikely(!%s)) { %s(%s); %s }' % (
```
L3385  ⚪  (score=0)
```python
                                unbound_check_code,
```
L3386  ⚪  (score=0)
```python
                                f"__Pyx_{func}{nogil_tag}",
```
L3387  ⚪  (score=0)
```python
                                entry.name.as_c_string_literal(),
```
L3388  ⚪  (score=0)
```python
                                self.error_goto(pos)))
```
L3389  ⚪  (score=0)
```python
```
L3390  ⚪  (score=0)
```python
    def set_error_info(self, pos, used=False):
```
L3391  ⚪  (score=0)
```python
        self.funcstate.should_declare_error_indicator = True
```
L3392  ⚪  (score=0)
```python
        if used:
```
L3393  ⚪  (score=0)
```python
            self.funcstate.uses_error_indicator = True
```
L3394  ⚪  (score=0)
```python
        return "__PYX_MARK_ERR_POS(%s, %s)" % (
```
L3395  ⚪  (score=0)
```python
            self.lookup_filename(pos[0]),
```
L3396  ⚪  (score=0)
```python
            pos[1])
```
L3397  ⚪  (score=0)
```python
```
L3398  ⚪  (score=0)
```python
    def error_goto(self, pos, used=True):
```
L3399  ⚪  (score=0)
```python
        lbl = self.funcstate.error_label
```
L3400  ⚪  (score=0)
```python
        self.funcstate.use_label(lbl)
```
L3401  ⚪  (score=0)
```python
        if pos is None:
```
L3402  ⚪  (score=0)
```python
            return 'goto %s;' % lbl
```
L3403  ⚪  (score=0)
```python
        self.funcstate.should_declare_error_indicator = True
```
L3404  ⚪  (score=0)
```python
        if used:
```
L3405  ⚪  (score=0)
```python
            self.funcstate.uses_error_indicator = True
```
L3406  ⚪  (score=0)
```python
        return "__PYX_ERR(%s, %s, %s)" % (
```
L3407  ⚪  (score=0)
```python
            self.lookup_filename(pos[0]),
```
L3408  ⚪  (score=0)
```python
            pos[1],
```
L3409  ⚪  (score=0)
```python
            lbl)
```
L3410  ⚪  (score=0)
```python
```
L3411  ⚪  (score=0)
```python
    def error_goto_if(self, cond, pos):
```
L3412  ⚪  (score=0)
```python
        return "if (%s) %s" % (self.unlikely(cond), self.error_goto(pos))
```
L3413  ⚪  (score=0)
```python
```
L3414  ⚪  (score=0)
```python
    def error_goto_if_null(self, cname, pos):
```
L3415  ⚪  (score=0)
```python
        return self.error_goto_if("!%s" % cname, pos)
```
L3416  ⚪  (score=0)
```python
```
L3417  ⚪  (score=0)
```python
    def error_goto_if_neg(self, cname, pos):
```
L3418  ⚪  (score=0)
```python
        # Add extra parentheses to silence clang warnings about constant conditions.
```
L3419  ⚪  (score=0)
```python
        return self.error_goto_if("(%s < 0)" % cname, pos)
```
L3420  ⚪  (score=0)
```python
```
L3421  ⚪  (score=0)
```python
    def error_goto_if_PyErr(self, pos):
```
L3422  ⚪  (score=0)
```python
        return self.error_goto_if("PyErr_Occurred()", pos)
```
L3423  ⚪  (score=0)
```python
```
L3424  ⚪  (score=0)
```python
    def lookup_filename(self, filename):
```
L3425  ⚪  (score=0)
```python
        return self.globalstate.lookup_filename(filename)
```
L3426  ⚪  (score=0)
```python
```
L3427  ⚪  (score=0)
```python
    def put_declare_refcount_context(self):
```
L3428  ⚪  (score=0)
```python
        self.putln('__Pyx_RefNannyDeclarations')
```
L3429  ⚪  (score=0)
```python
```
L3430  ⚪  (score=0)
```python
    def put_setup_refcount_context(self, name, acquire_gil=False):
```
L3431  ⚪  (score=0)
```python
        name = name.as_c_string_literal()  # handle unicode names
```
L3432  ⚪  (score=0)
```python
        if acquire_gil:
```
L3433  ⚪  (score=0)
```python
            self.globalstate.use_utility_code(
```
L3434  ⚪  (score=0)
```python
                UtilityCode.load_cached("ForceInitThreads", "ModuleSetupCode.c"))
```
L3435  ⚪  (score=0)
```python
        self.putln('__Pyx_RefNannySetupContext(%s, %d);' % (name, acquire_gil and 1 or 0))
```
L3436  ⚪  (score=0)
```python
```
L3437  ⚪  (score=0)
```python
    def put_finish_refcount_context(self, nogil=False):
```
L3438  ⚪  (score=0)
```python
        self.putln("__Pyx_RefNannyFinishContextNogil()" if nogil else "__Pyx_RefNannyFinishContext();")
```
L3439  ⚪  (score=0)
```python
```
L3440  ⚪  (score=0)
```python
    def put_add_traceback(self, qualified_name, include_cline=True):
```
L3441  ⚪  (score=0)
```python
        """
```
L3442  ⚪  (score=0)
```python
        Build a Python traceback for propagating exceptions.
```
L3443  ⚪  (score=0)
```python
```
L3444  ⚪  (score=0)
```python
        qualified_name should be the qualified name of the function.
```
L3445  ⚪  (score=0)
```python
        """
```
L3446  ⚪  (score=0)
```python
        qualified_name = qualified_name.as_c_string_literal()  # handle unicode names
```
L3447  ⚪  (score=0)
```python
        format_tuple = (
```
L3448  ⚪  (score=0)
```python
            qualified_name,
```
L3449  ⚪  (score=0)
```python
            Naming.clineno_cname if include_cline else 0,
```
L3450  ⚪  (score=0)
```python
            Naming.lineno_cname,
```
L3451  ⚪  (score=0)
```python
            Naming.filename_cname,
```
L3452  ⚪  (score=0)
```python
        )
```
L3453  ⚪  (score=0)
```python
```
L3454  ⚪  (score=0)
```python
        self.funcstate.uses_error_indicator = True
```
L3455  ⚪  (score=0)
```python
        self.putln('__Pyx_AddTraceback(%s, %s, %s, %s);' % format_tuple)
```
L3456  ⚪  (score=0)
```python
```
L3457  ⚪  (score=0)
```python
    def put_unraisable(self, qualified_name, nogil=False):
```
L3458  ⚪  (score=0)
```python
        """
```
L3459  ⚪  (score=0)
```python
        Generate code to print a Python warning for an unraisable exception.
```
L3460  ⚪  (score=0)
```python
```
L3461  ⚪  (score=0)
```python
        qualified_name should be the qualified name of the function.
```
L3462  ⚪  (score=0)
```python
        """
```
L3463  ⚪  (score=0)
```python
        self.funcstate.uses_error_indicator = True
```
L3464  ⚪  (score=0)
```python
        self.putln('__Pyx_WriteUnraisable("%s", %s, %s, %s, %d, %d);' % (
```
L3465  ⚪  (score=0)
```python
            qualified_name,
```
L3466  ⚪  (score=0)
```python
            Naming.clineno_cname,
```
L3467  ⚪  (score=0)
```python
            Naming.lineno_cname,
```
L3468  ⚪  (score=0)
```python
            Naming.filename_cname,
```
L3469  ⚪  (score=0)
```python
            self.globalstate.directives['unraisable_tracebacks'],
```
L3470  ⚪  (score=0)
```python
            nogil,
```
L3471  ⚪  (score=0)
```python
        ))
```
L3472  ⚪  (score=0)
```python
        self.globalstate.use_utility_code(
```
L3473  ⚪  (score=0)
```python
            UtilityCode.load_cached("WriteUnraisableException", "Exceptions.c"))
```
L3474  ⚪  (score=0)
```python
```
L3475  ⚪  (score=0)
```python
    def is_tracing(self):
```
L3476  ⚪  (score=0)
```python
        return self.globalstate.directives['profile'] or self.globalstate.directives['linetrace']
```
L3477  ⚪  (score=0)
```python
```
L3478  ⚪  (score=0)
```python
    def pos_to_offset(self, pos):
```
L3479  ⚪  (score=0)
```python
        """
```
L3480  ⚪  (score=0)
```python
        Calculate a fake 'instruction offset' from a node position as 31 bit int (32 bit signed).
```
L3481  ⚪  (score=0)
```python
        """
```
L3482  ⚪  (score=0)
```python
        scope = self.funcstate.scope
```
L3483  ⚪  (score=0)
```python
        while scope and pos not in scope.node_positions_to_offset:
```
L3484  ⚪  (score=0)
```python
            scope = scope.parent_scope
```
L3485  ⚪  (score=0)
```python
        return scope.node_positions_to_offset[pos] if scope else 0
```
L3486  ⚪  (score=0)
```python
```
L3487  ⚪  (score=0)
```python
    def put_trace_declarations(self, is_generator=False):
```
L3488  ⚪  (score=0)
```python
        self.putln('__Pyx_TraceDeclarationsGen' if is_generator else '__Pyx_TraceDeclarationsFunc')
```
L3489  ⚪  (score=0)
```python
```
L3490  ⚪  (score=0)
```python
    def put_trace_frame_init(self, codeobj=None):
```
L3491  ⚪  (score=0)
```python
        if codeobj:
```
L3492  ⚪  (score=0)
```python
            self.putln('__Pyx_TraceFrameInit(%s)' % codeobj)
```
L3493  ⚪  (score=0)
```python
```
L3494  ⚪  (score=0)
```python
    def put_trace_start(self, name, pos, nogil=False, is_generator=False, is_cpdef_func=False):
```
L3495  ⚪  (score=0)
```python
        trace_func = "__Pyx_TraceStartGen" if is_generator else "__Pyx_TraceStartFunc"
```
L3496  ⚪  (score=0)
```python
        self.putln(
```
L3497  ⚪  (score=0)
```python
            f'{trace_func}('
```
L3498  ⚪  (score=0)
```python
            f'{name.as_c_string_literal()}, '
```
L3499  ⚪  (score=0)
```python
            f'{Naming.filetable_cname}[{self.lookup_filename(pos[0])}], '
```
L3500  ⚪  (score=0)
```python
            f'{pos[1]}, '
```
L3501  ⚪  (score=0)
```python
            f'{self.pos_to_offset(pos):d}, '
```
L3502  ⚪  (score=0)
```python
            f'{nogil:d}, '
```
L3503  ⚪  (score=0)
```python
            f'{Naming.skip_dispatch_cname if is_cpdef_func else "0"}, '
```
L3504  ⚪  (score=0)
```python
            f'{self.error_goto(pos)}'
```
L3505  ⚪  (score=0)
```python
            ');'
```
L3506  ⚪  (score=0)
```python
        )
```
L3507  ⚪  (score=0)
```python
```
L3508  ⚪  (score=0)
```python
    def put_trace_exit(self, nogil=False):
```
L3509  ⚪  (score=0)
```python
        self.putln(f"__Pyx_PyMonitoring_ExitScope({bool(nogil):d});")
```
L3510  ⚪  (score=0)
```python
```
L3511  ⚪  (score=0)
```python
    def put_trace_yield(self, retvalue_cname, pos):
```
L3512  ⚪  (score=0)
```python
        error_goto = self.error_goto(pos)
```
L3513  ⚪  (score=0)
```python
        self.putln(f"__Pyx_TraceYield({retvalue_cname}, {self.pos_to_offset(pos)}, {error_goto});")
```
L3514  ⚪  (score=0)
```python
```
L3515  ⚪  (score=0)
```python
    def put_trace_resume(self, pos):
```
L3516  ⚪  (score=0)
```python
        scope = self.funcstate.scope
```
L3517  ⚪  (score=0)
```python
        # pos[1] is probably not the first line, so try to find the first line of the generator function.
```
L3518  ⚪  (score=0)
```python
        first_line = scope.scope_class.pos[1] if scope.scope_class else pos[1]
```
L3519  ⚪  (score=0)
```python
        name = scope.name.as_c_string_literal()
```
L3520  ⚪  (score=0)
```python
        filename_index = self.lookup_filename(pos[0])
```
L3521  ⚪  (score=0)
```python
        error_goto = self.error_goto(pos)
```
L3522  ⚪  (score=0)
```python
        self.putln(
```
L3523  ⚪  (score=0)
```python
            '__Pyx_TraceResumeGen('
```
L3524  ⚪  (score=0)
```python
            f'{name}, '
```
L3525  ⚪  (score=0)
```python
            f'{Naming.filetable_cname}[{filename_index}], '
```
L3526  ⚪  (score=0)
```python
            f'{first_line}, '
```
L3527  ⚪  (score=0)
```python
            f'{self.pos_to_offset(pos)}, '
```
L3528  ⚪  (score=0)
```python
            f'{error_goto}'
```
L3529  ⚪  (score=0)
```python
            ');'
```
L3530  ⚪  (score=0)
```python
        )
```
L3531  ⚪  (score=0)
```python
```
L3532  ⚪  (score=0)
```python
    def put_trace_exception(self, pos, reraise=False, fresh=False):
```
L3533  ⚪  (score=0)
```python
        self.putln(f"__Pyx_TraceException({self.pos_to_offset(pos)}, {bool(reraise):d}, {bool(fresh):d});")
```
L3534  ⚪  (score=0)
```python
```
L3535  ⚪  (score=0)
```python
    def put_trace_exception_propagating(self):
```
L3536  ⚪  (score=0)
```python
        self.putln(f"__Pyx_TraceException({Naming.lineno_cname}, 0, 0);")
```
L3537  ⚪  (score=0)
```python
```
L3538  ⚪  (score=0)
```python
    def put_trace_exception_handled(self, pos):
```
L3539  ⚪  (score=0)
```python
        self.putln(f"__Pyx_TraceExceptionHandled({self.pos_to_offset(pos)});")
```
L3540  ⚪  (score=0)
```python
```
L3541  ⚪  (score=0)
```python
    def put_trace_unwind(self, pos, nogil=False):
```
L3542  ⚪  (score=0)
```python
        self.putln(f"__Pyx_TraceExceptionUnwind({self.pos_to_offset(pos)}, {bool(nogil):d});")
```
L3543  ⚪  (score=0)
```python
```
L3544  ⚪  (score=0)
```python
    def put_trace_stopiteration(self, pos, value):
```
L3545  ⚪  (score=0)
```python
        error_goto = self.error_goto(pos)
```
L3546  ⚪  (score=0)
```python
        self.putln(f"__Pyx_TraceStopIteration({value}, {self.pos_to_offset(pos)}, {error_goto});")
```
L3547  ⚪  (score=0)
```python
```
L3548  ⚪  (score=0)
```python
    def put_trace_return(self, retvalue_cname, pos, return_type=None, nogil=False):
```
L3549  ⚪  (score=0)
```python
        extra_arg = ""
```
L3550  ⚪  (score=0)
```python
        trace_func = "__Pyx_TraceReturnValue"
```
L3551  ⚪  (score=0)
```python
```
L3552  ⚪  (score=0)
```python
        if return_type is None:
```
L3553  ⚪  (score=0)
```python
            pass
```
L3554  ⚪  (score=0)
```python
        elif return_type.is_pyobject:
```
L3555  ⚪  (score=0)
```python
            retvalue_cname = return_type.as_pyobject(retvalue_cname)
```
L3556  ⚪  (score=0)
```python
        elif return_type.is_void:
```
L3557  ⚪  (score=0)
```python
            retvalue_cname = 'Py_None'
```
L3558  ⚪  (score=0)
```python
        elif return_type.is_string:
```
L3559  ⚪  (score=0)
```python
            # We don't know if the C string is 0-terminated, but we cannot convert if it's not.
```
L3560  ⚪  (score=0)
```python
            retvalue_cname = 'Py_None'
```
L3561  ⚪  (score=0)
```python
        elif return_type.to_py_function:
```
L3562  ⚪  (score=0)
```python
            trace_func = "__Pyx_TraceReturnCValue"
```
L3563  ⚪  (score=0)
```python
            extra_arg = f", {return_type.to_py_function}"
```
L3564  ⚪  (score=0)
```python
        else:
```
L3565  ⚪  (score=0)
```python
            # We don't have a Python visible return value but we still need to report that we returned.
```
L3566  ⚪  (score=0)
```python
            # 'None' may not be a misleading (it's false, for one), but it's hopefully better than nothing.
```
L3567  ⚪  (score=0)
```python
            retvalue_cname = 'Py_None'
```
L3568  ⚪  (score=0)
```python
```
L3569  ⚪  (score=0)
```python
        error_handling = self.error_goto(pos)
```
L3570  ⚪  (score=0)
```python
        self.putln(f"{trace_func}({retvalue_cname}{extra_arg}, {self.pos_to_offset(pos)}, {bool(nogil):d}, {error_handling});")
```
L3571  ⚪  (score=0)
```python
```
L3572  ⚪  (score=0)
```python
    def put_cpp_placement_new(self, target,
```
L3573  ⚪  (score=0)
```python
                              _utility_code=UtilityCode.load("DefaultPlacementNew", "CppSupport.cpp")):
```
L3574  ⚪  (score=0)
```python
        self.globalstate.use_utility_code(_utility_code)
```
L3575  ⚪  (score=0)
```python
        self.putln(f"__Pyx_default_placement_construct(&({target}));")
```
L3576  ⚪  (score=0)
```python
```
L3577  ⚪  (score=0)
```python
    def putln_openmp(self, string):
```
L3578  ⚪  (score=0)
```python
        self.putln("#ifdef _OPENMP")
```
L3579  ⚪  (score=0)
```python
        self.putln(string)
```
L3580  ⚪  (score=0)
```python
        self.putln("#endif /* _OPENMP */")
```
L3581  ⚪  (score=0)
```python
```
L3582  ⚪  (score=0)
```python
    def undef_builtin_expect(self, cond):
```
L3583  ⚪  (score=0)
```python
        """
```
L3584  ⚪  (score=0)
```python
        Redefine the macros likely() and unlikely to no-ops, depending on
```
L3585  ⚪  (score=0)
```python
        condition 'cond'
```
L3586  ⚪  (score=0)
```python
        """
```
L3587  ⚪  (score=0)
```python
        self.putln("#if %s" % cond)
```
L3588  ⚪  (score=0)
```python
        self.putln("    #undef likely")
```
L3589  ⚪  (score=0)
```python
        self.putln("    #undef unlikely")
```
L3590  ⚪  (score=0)
```python
        self.putln("    #define likely(x)   (x)")
```
L3591  ⚪  (score=0)
```python
        self.putln("    #define unlikely(x) (x)")
```
L3592  ⚪  (score=0)
```python
        self.putln("#endif")
```
L3593  ⚪  (score=0)
```python
```
L3594  ⚪  (score=0)
```python
    def redef_builtin_expect(self, cond):
```
L3595  ⚪  (score=0)
```python
        self.putln("#if %s" % cond)
```
L3596  ⚪  (score=0)
```python
        self.putln("    #undef likely")
```
L3597  ⚪  (score=0)
```python
        self.putln("    #undef unlikely")
```
L3598  ⚪  (score=0)
```python
        self.putln("    #define likely(x)   __builtin_expect(!!(x), 1)")
```
L3599  ⚪  (score=0)
```python
        self.putln("    #define unlikely(x) __builtin_expect(!!(x), 0)")
```
L3600  ⚪  (score=0)
```python
        self.putln("#endif")
```
L3601  ⚪  (score=0)
```python
```
L3602  ⚪  (score=0)
```python
```
L3603  ⚪  (score=0)
```python
class PyrexCodeWriter:
```
L3604  ⚪  (score=0)
```python
    # f                file      output file
```
L3605  ⚪  (score=0)
```python
    # level            int       indentation level
```
L3606  ⚪  (score=0)
```python
```
L3607  ⚪  (score=0)
```python
    def __init__(self, outfile_name):
```
L3608  ⚪  (score=0)
```python
        self.f = Utils.open_new_file(outfile_name)
```
L3609  ⚪  (score=0)
```python
        self.level = 0
```
L3610  ⚪  (score=0)
```python
```
L3611  ⚪  (score=0)
```python
    def putln(self, code):
```
L3612  ⚪  (score=0)
```python
        self.f.write("%s%s\n" % (" " * self.level, code))
```
L3613  ⚪  (score=0)
```python
```
L3614  ⚪  (score=0)
```python
    def indent(self):
```
L3615  ⚪  (score=0)
```python
        self.level += 1
```
L3616  ⚪  (score=0)
```python
```
L3617  ⚪  (score=0)
```python
    def dedent(self):
```
L3618  ⚪  (score=0)
```python
        self.level -= 1
```
L3619  ⚪  (score=0)
```python
```
L3620  ⚪  (score=0)
```python
```
L3621  ⚪  (score=0)
```python
class PyxCodeWriter:
```
L3622  ⚪  (score=0)
```python
    """
```
L3623  ⚪  (score=0)
```python
    Can be used for writing out some Cython code.
```
L3624  ⚪  (score=0)
```python
    """
```
L3625  ⚪  (score=0)
```python
```
L3626  ⚪  (score=0)
```python
    def __init__(self, buffer=None, indent_level=0, context=None, encoding='ascii'):
```
L3627  ⚪  (score=0)
```python
        self.buffer = buffer or StringIOTree()
```
L3628  ⚪  (score=0)
```python
        self.level = indent_level
```
L3629  ⚪  (score=0)
```python
        self.original_level = indent_level
```
L3630  ⚪  (score=0)
```python
        self.context = context
```
L3631  ⚪  (score=0)
```python
        self.encoding = encoding
```
L3632  ⚪  (score=0)
```python
        self._insertion_points = {}
```
L3633  ⚪  (score=0)
```python
```
L3634  ⚪  (score=0)
```python
    def indent(self, levels=1):
```
L3635  ⚪  (score=0)
```python
        self.level += levels
```
L3636  ⚪  (score=0)
```python
        return True
```
L3637  ⚪  (score=0)
```python
```
L3638  ⚪  (score=0)
```python
    def dedent(self, levels=1):
```
L3639  ⚪  (score=0)
```python
        self.level -= levels
```
L3640  ⚪  (score=0)
```python
```
L3641  ⚪  (score=0)
```python
    @contextmanager
```
L3642  ⚪  (score=0)
```python
    def indenter(self, line):
```
L3643  ⚪  (score=0)
```python
        """
```
L3644  ⚪  (score=0)
```python
        with pyx_code.indenter("for i in range(10):"):
```
L3645  ⚪  (score=0)
```python
            pyx_code.putln("print i")
```
L3646  ⚪  (score=0)
```python
        """
```
L3647  ⚪  (score=0)
```python
        self.putln(line)
```
L3648  ⚪  (score=0)
```python
        self.indent()
```
L3649  ⚪  (score=0)
```python
        yield
```
L3650  ⚪  (score=0)
```python
        self.dedent()
```
L3651  ⚪  (score=0)
```python
```
L3652  ⚪  (score=0)
```python
    def empty(self):
```
L3653  ⚪  (score=0)
```python
        return self.buffer.empty()
```
L3654  ⚪  (score=0)
```python
```
L3655  ⚪  (score=0)
```python
    def getvalue(self):
```
L3656  ⚪  (score=0)
```python
        result = self.buffer.getvalue()
```
L3657  ⚪  (score=0)
```python
        if isinstance(result, bytes):
```
L3658  ⚪  (score=0)
```python
            result = result.decode(self.encoding)
```
L3659  ⚪  (score=0)
```python
        return result
```
L3660  ⚪  (score=0)
```python
```
L3661  ⚪  (score=0)
```python
    def putln(self, line, context=None):
```
L3662  ⚪  (score=0)
```python
        if context is None:
```
L3663  ⚪  (score=0)
```python
            if self.context is not None:
```
L3664  ⚪  (score=0)
```python
                context = self.context
```
L3665  ⚪  (score=0)
```python
        if context is not None:
```
L3666  ⚪  (score=0)
```python
            line = sub_tempita(line, context)
```
L3667  ⚪  (score=0)
```python
        # Avoid indenting empty lines.
```
L3668  ⚪  (score=0)
```python
        self.buffer.write(f"{self.level * '    '}{line}\n" if line else "\n")
```
L3669  ⚪  (score=0)
```python
```
L3670  ⚪  (score=0)
```python
    def put_chunk(self, chunk, context=None):
```
L3671  ⚪  (score=0)
```python
        if context is None:
```
L3672  ⚪  (score=0)
```python
            if self.context is not None:
```
L3673  ⚪  (score=0)
```python
                context = self.context
```
L3674  ⚪  (score=0)
```python
        if context is not None:
```
L3675  ⚪  (score=0)
```python
            chunk = sub_tempita(chunk, context)
```
L3676  ⚪  (score=0)
```python
```
L3677  ⚪  (score=0)
```python
        chunk = _indent_chunk(chunk, self.level * 4)
```
L3678  ⚪  (score=0)
```python
        self.buffer.write(chunk)
```
L3679  ⚪  (score=0)
```python
```
L3680  ⚪  (score=0)
```python
    def insertion_point(self):
```
L3681  ⚪  (score=0)
```python
        return type(self)(self.buffer.insertion_point(), self.level, self.context)
```
L3682  ⚪  (score=0)
```python
```
L3683  ⚪  (score=0)
```python
    def reset(self):
```
L3684  ⚪  (score=0)
```python
        # resets the buffer so that nothing gets written. Most useful
```
L3685  ⚪  (score=0)
```python
        # for abandoning all work in a specific insertion point
```
L3686  ⚪  (score=0)
```python
        self.buffer.reset()
```
L3687  ⚪  (score=0)
```python
        self.level = self.original_level
```
L3688  ⚪  (score=0)
```python
```
L3689  ⚪  (score=0)
```python
    def named_insertion_point(self, name):
```
L3690  ⚪  (score=0)
```python
        self._insertion_points[name] = self.insertion_point()
```
L3691  ⚪  (score=0)
```python
```
L3692  ⚪  (score=0)
```python
    def __getitem__(self, name):
```
L3693  ⚪  (score=0)
```python
        return self._insertion_points[name]
```
L3694  ⚪  (score=0)
```python
```
L3695  ⚪  (score=0)
```python
```
L3696  ⚪  (score=0)
```python
@cython.final
```
L3697  ⚪  (score=0)
```python
@cython.ccall
```
L3698  ⚪  (score=0)
```python
def _indent_chunk(chunk: str, indentation_length: cython.int) -> str:
```
L3699  ⚪  (score=0)
```python
    """Normalise leading space to the intended indentation and strip empty lines.
```
L3700  ⚪  (score=0)
```python
    """
```
L3701  ⚪  (score=0)
```python
    assert '\t' not in chunk
```
L3702  ⚪  (score=0)
```python
    lines = chunk.splitlines(keepends=True)
```
L3703  ⚪  (score=0)
```python
    if not lines:
```
L3704  ⚪  (score=0)
```python
        return chunk
```
L3705  ⚪  (score=0)
```python
    last_line = lines[-1].rstrip(' ')
```
L3706  ⚪  (score=0)
```python
    if last_line:
```
L3707  ⚪  (score=0)
```python
        lines[-1] = last_line
```
L3708  ⚪  (score=0)
```python
    else:
```
L3709  ⚪  (score=0)
```python
        del lines[-1]
```
L3710  ⚪  (score=0)
```python
        if not lines:
```
L3711  ⚪  (score=0)
```python
            return '\n'
```
L3712  ⚪  (score=0)
```python
```
L3713  ⚪  (score=0)
```python
    # Count minimal (non-empty) indentation and strip empty lines.
```
L3714  ⚪  (score=0)
```python
    min_indentation: cython.int = len(chunk) + 1
```
L3715  ⚪  (score=0)
```python
    line_indentation: cython.int
```
L3716  ⚪  (score=0)
```python
    line: str
```
L3717  ⚪  (score=0)
```python
    i: cython.int
```
L3718  ⚪  (score=0)
```python
    for i, line in enumerate(lines):
```
L3719  ⚪  (score=0)
```python
        line_indentation = _count_indentation(line)
```
L3720  ⚪  (score=0)
```python
        if line_indentation + 1 == len(line):
```
L3721  ⚪  (score=0)
```python
            lines[i] = '\n'
```
L3722  ⚪  (score=0)
```python
        elif line_indentation < min_indentation:
```
L3723  ⚪  (score=0)
```python
            min_indentation = line_indentation
```
L3724  ⚪  (score=0)
```python
```
L3725  ⚪  (score=0)
```python
    if min_indentation > len(chunk):
```
L3726  ⚪  (score=0)
```python
        # All empty lines.
```
L3727  ⚪  (score=0)
```python
        min_indentation = 0
```
L3728  ⚪  (score=0)
```python
```
L3729  ⚪  (score=0)
```python
    if min_indentation < indentation_length:
```
L3730  ⚪  (score=0)
```python
        add_indent = ' ' * (indentation_length - min_indentation)
```
L3731  ⚪  (score=0)
```python
        lines = [
```
L3732  ⚪  (score=0)
```python
            add_indent + line if line != '\n' else '\n'
```
L3733  ⚪  (score=0)
```python
            for line in lines
```
L3734  ⚪  (score=0)
```python
        ]
```
L3735  ⚪  (score=0)
```python
    elif min_indentation > indentation_length:
```
L3736  ⚪  (score=0)
```python
        start: cython.int = min_indentation - indentation_length
```
L3737  ⚪  (score=0)
```python
        lines = [
```
L3738  ⚪  (score=0)
```python
            line[start:] if line != '\n' else '\n'
```
L3739  ⚪  (score=0)
```python
            for line in lines
```
L3740  ⚪  (score=0)
```python
        ]
```
L3741  ⚪  (score=0)
```python
```
L3742  ⚪  (score=0)
```python
    return ''.join(lines)
```
L3743  ⚪  (score=0)
```python
```
L3744  ⚪  (score=0)
```python
```
L3745  ⚪  (score=0)
```python
@cython.exceptval(-1)
```
L3746  ⚪  (score=0)
```python
@cython.cfunc
```
L3747  ⚪  (score=0)
```python
def _count_indentation(s: str) -> cython.int:
```
L3748  ⚪  (score=0)
```python
    i: cython.int = 0
```
L3749  ⚪  (score=0)
```python
    ch: cython.Py_UCS4
```
L3750  ⚪  (score=0)
```python
    for i, ch in enumerate(s):
```
L3751  ⚪  (score=0)
```python
        if ch != ' ':
```
L3752  ⚪  (score=0)
```python
            break
```
L3753  ⚪  (score=0)
```python
    return i
```
L3754  ⚪  (score=0)
```python
```
L3755  ⚪  (score=0)
```python
```
L3756  ⚪  (score=0)
```python
class ClosureTempAllocator:
```
L3757  ⚪  (score=0)
```python
    def __init__(self, klass):
```
L3758  ⚪  (score=0)
```python
        self.klass = klass
```
L3759  ⚪  (score=0)
```python
        self.temps_allocated = {}
```
L3760  ⚪  (score=0)
```python
        self.temps_free = {}
```
L3761  ⚪  (score=0)
```python
        self.temps_count = 0
```
L3762  ⚪  (score=0)
```python
```
L3763  ⚪  (score=0)
```python
    def reset(self):
```
L3764  ⚪  (score=0)
```python
        for type, cnames in self.temps_allocated.items():
```
L3765  ⚪  (score=0)
```python
            self.temps_free[type] = list(cnames)
```
L3766  ⚪  (score=0)
```python
```
L3767  ⚪  (score=0)
```python
    def allocate_temp(self, type):
```
L3768  ⚪  (score=0)
```python
        if type not in self.temps_allocated:
```
L3769  ⚪  (score=0)
```python
            self.temps_allocated[type] = []
```
L3770  ⚪  (score=0)
```python
            self.temps_free[type] = []
```
L3771  ⚪  (score=0)
```python
        elif self.temps_free[type]:
```
L3772  ⚪  (score=0)
```python
            return self.temps_free[type].pop(0)
```
L3773  ⚪  (score=0)
```python
        cname = '%s%d' % (Naming.codewriter_temp_prefix, self.temps_count)
```
L3774  ⚪  (score=0)
```python
        self.klass.declare_var(pos=None, name=cname, cname=cname, type=type, is_cdef=True)
```
L3775  ⚪  (score=0)
```python
        self.temps_allocated[type].append(cname)
```
L3776  ⚪  (score=0)
```python
        self.temps_count += 1
```
L3777  ⚪  (score=0)
```python
        return cname
```
