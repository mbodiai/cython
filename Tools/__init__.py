import os
import importlib.util
import importlib.machinery

def _load_extension(name):
    """Load the extension module with priority over .py files"""
    dirname = os.path.dirname(__file__)
    
    # Try to load .so file first
    ext_path = os.path.join(dirname, name + '.so')  # For Unix/Linux
    if not os.path.exists(ext_path):
        ext_path = os.path.join(dirname, name + '.pyd')  # For Windows
        
    if os.path.exists(ext_path):
        loader = importlib.machinery.ExtensionFileLoader(name, ext_path)
        spec = importlib.util.spec_from_loader(name, loader)
        module = importlib.util.module_from_spec(spec)
        loader.exec_module(module)
        return module
        
    # Fallback to regular import if .so/.pyd doesn't exist
    return importlib.import_module('.' + name, package=__package__)

# Import and expose the compiled modules
test_typing = _load_extension('test_typing')
