
# Provide a provisional version string *before* importing sub-modules
# to break circular import chains that expect ``Cython.__version__``
# to exist very early (e.g. ``Cython.Build.Cache``).
# It will be overwritten with the canonical value a few lines below.
__version__ = "0.0"

from .Shadow import *  # noqa: F403
from .Shadow import __version__ as __version__
# Ensure downstream modules have a non-None version string
cython_version = __version__

TYPE_CHECKING = False
if TYPE_CHECKING:
    # Don't import at runtime, only for type checking
    try:
        import IPython.core.interactiveshell
        from IPython.core.interactiveshell import InteractiveShell
    except ImportError:
        InteractiveShell = object # type: ignore
    from .Build.IpythonMagic import CythonMagics

def load_ipython_extension(ip) -> None:
    """Load the extension in IPython."""
    # Import dynamically to avoid hard dependency
    from .Build.IpythonMagic import CythonMagics  # pylint: disable=cyclic-import
    ip.register_magics(CythonMagics)
