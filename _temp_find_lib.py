import sys, sysconfig, os, ctypes.util
from pathlib import Path

DEBUG=True

def check_path(path):
    p = Path(path)
    return str(p.resolve()) if p.exists() else None

shared_lib = None
lib_name = sysconfig.get_config_var('LDLIBRARY') or ''
lib_dir = sysconfig.get_config_var('LIBDIR') or ''

print(f"Sysconfig LDLIBRARY: {lib_name}")
print(f"Sysconfig LIBDIR: {lib_dir}")

# Try finding library via sysconfig path first
if lib_name and lib_dir:
    shared_lib = check_path(Path(lib_dir) / lib_name)
    if DEBUG: print(f"Checking sysconfig path: {Path(lib_dir) / lib_name} -> {shared_lib}")

# Try ctypes.util.find_library
if not shared_lib:
    ctypes_lib_name = f"python{sys.version_info[0]}.{sys.version_info[1]}"
    found = ctypes.util.find_library(ctypes_lib_name)
    if DEBUG: print(f"Checking ctypes.util.find_library({ctypes_lib_name!r}): {found}")
    if found:
        shared_lib = check_path(found)
        if DEBUG: print(f"Resolved ctypes path: {shared_lib}")

# Search common candidate directories
if not shared_lib and lib_name:
    candidate_dirs = [
        Path(getattr(sys, 'base_prefix', sys.prefix)) / 'lib',
        Path(sys.prefix) / 'lib',
        Path('/usr/lib'),
        Path('/usr/local/lib'),
        Path('/opt/homebrew/lib'),
    ]
    if DEBUG: print(f"Checking candidate dirs for {lib_name}...")
    for d in candidate_dirs:
        if not d.is_dir(): continue
        candidate = d / lib_name
        if DEBUG: print(f"  Checking candidate: {candidate}")
        if candidate.exists():
            shared_lib = str(candidate.resolve())
            if DEBUG: print(f"  Found candidate: {shared_lib}")
            break

print(f"\nFinal resolved shared library: {shared_lib}")