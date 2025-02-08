from os.path import isdir
from sys import argv

if len(argv) == 2 and argv[1] == 'repl':
    # don't want to use __main__ only for repl yet, maybe we want to use it for
    # something else. So just use the keyword ``repl`` for now.
    pass
elif len(argv) > 1 and argv[1] == 'linter':
    """
    This is a pre-alpha API. You're not supposed to use it at all, except for
    testing. It will very likely change.
    """
    import sys

    import jedi

    if '--debug' in sys.argv:
        jedi.set_debug_function()

    for path in sys.argv[2:]:
        if path.startswith('--'):
            continue
        if isdir(path):
            import fnmatch
            import os

            paths = []
            for root, _dirnames, filenames in os.walk(path):
                for filename in fnmatch.filter(filenames, '*.py'):
                    paths.append(os.path.join(root, filename))
        else:
            paths = [path]

        try:
            for path in paths:
                for _error in jedi.Script(path=path)._analysis():
                    pass
        except Exception:
            if '--pdb' in sys.argv:
                import pdb
                pdb.post_mortem()
            else:
                raise
