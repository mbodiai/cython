"""Register hooks for the plugin."""
try:
    from hatchling.plugin import hookimpl
except ImportError:
    try:
        from setuptools.sandbox import Distribution
    except ImportError:
        from setuptools.dist import Distribution

from mbpy.pkg.plugin import BuildScriptsHook


@hookimpl
def hatch_register_build_hook():
    """Get the hook implementation."""
    return BuildScriptsHook
