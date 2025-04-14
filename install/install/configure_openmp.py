import platform
import os
from pathlib import Path

def configure_openmp():
    is_arm = platform.machine() == 'arm64'
    base_path = '/opt/homebrew' if is_arm else '/usr/local'
    
    # Find libomp installation
    if is_arm:
        omp_root = Path(base_path) / 'opt' / 'libomp'
    else:
        omp_root = Path(base_path) / 'opt' / 'libomp'
    
    return {
        'include_path': str(omp_root / 'include'),
        'lib_path': str(omp_root / 'lib')
    }

if __name__ == '__main__':
    paths = configure_openmp()
    print(f"Add these to your Cython magic:")
    print(f"# distutils: include_dirs={paths['include_path']}")
    print(f"# distutils: extra_link_args=-L{paths['lib_path']} -lomp")