# Void cython.* directives (for case insensitive operating systems).
from .Shadow import *  # noqa: F403
from .Shadow import __version__


def load_ipython_extension(ip) -> "CythonMagics":
    """Load the extension in IPython."""
    from .Build.IpythonMagic import CythonMagics  # pylint: disable=cyclic-import
    ip.register_magics(CythonMagics)
