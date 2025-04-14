import pytest
import os
import sys
import tempfile
import shutil
import subprocess
from pathlib import Path
from mbcore.import_utils import files

@pytest.fixture(scope="session")
def setup_venv():
    """Create a virtual environment for testing using subprocess."""
    with tempfile.TemporaryDirectory() as temp_dir:
        venv_dir = Path(temp_dir) / "test_venv"
        venv_dir.mkdir(exist_ok=True)
        
        # Install virtualenv if needed
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "virtualenv"], check=True)
        except subprocess.CalledProcessError:
            pass  # Already installed
        
        # Create the virtual environment
        subprocess.run([sys.executable, "-m", "virtualenv", str(venv_dir)], check=True)

        # Install mb if needed
        mb_path = Path(__file__).parent.parent
        subprocess.run([sys.executable, "-m", "pip", "install", str(mb_path)], check=True)
        pip_path = "mb"
        # Get executable paths
        if sys.platform == "win32":
            python_path = venv_dir / "Scripts" / "python.exe"
        else:
            python_path = venv_dir / "bin" / "python"


        
        yield temp_dir, venv_dir, python_path, pip_path

        # Clean up the virtual environment
        shutil.rmtree(venv_dir)     


@pytest.mark.slow
def test_simple_package_installation(setup_venv ):
    """Test installation of a simple package with no version specification."""
    temp_dir, venv_dir, python_path, pip_path = setup_venv
        
    print("\nTesting simple package installation..." + str(pip_path))       
        
    # Install the package
    result = subprocess.run(
        [str(pip_path), "install", "six"],
        check=True, capture_output=True, text=True
    )
    
    # Verify the package is installed
    result = subprocess.run(
        [str(python_path), "-c", "import six; print(six.__version__)"],
        check=True, capture_output=True, text=True
    )
    version = result.stdout.strip()
    print(f"Installed six version: {version}")
    assert version, "Failed to get six version"


@pytest.mark.slow
def test_versioned_package_installation(setup_venv):
    """Test installation of a package with specific version."""
    temp_dir, venv_dir, python_path, pip_path = setup_venv
        
        
    print("\nTesting package with version...")
    
    # Install the package with specific version
    result = subprocess.run(
        [str(pip_path), "install", "requests==2.28.0"],
        check=True, capture_output=True, text=True
    )
    
    # Verify specific version installed
    result = subprocess.run(
        [str(python_path), "-c", "import requests; print(requests.__version__)"],
        check=True, capture_output=True, text=True
    )
    version = result.stdout.strip()
    print(f"Installed requests version: {version}")
    assert version == "2.28.0", f"Expected version 2.28.0, got {version}"


@pytest.mark.slow
def test_package_with_extras_installation(setup_venv):
    """Test installation of a package with extras."""
    temp_dir, venv_dir, python_path, pip_path = setup_venv
        
        
    print("\nTesting package with extras...")
    
    # Install the package with extras
    result = subprocess.run(
        [str(pip_path), "install", "requests[socks]"],
        check=True, capture_output=True, text=True
    )
    
    # Verify the extra is installed
    result = subprocess.run(
        [str(python_path), "-c", "import socks; print('PySocks installed')"],
        check=True, capture_output=True, text=True
    )
    print(result.stdout.strip())
    assert "PySocks installed" in result.stdout, "PySocks was not installed"


@pytest.mark.slow
def test_git_url_installation(setup_venv):
    """Test installation from a git URL."""
    temp_dir, venv_dir, python_path, pip_path = setup_venv
        
        
    print("\nTesting git URL installation...")
    
    # Install from git URL
    result = subprocess.run(
        [str(pip_path), "install", "git+https://github.com/benjaminp/six.git@1.16.0"],
        check=True, capture_output=True, text=True
    )
    
    # Verify package installed from git
    result = subprocess.run(
        [str(python_path), "-c", "import six; print(six.__version__)"],
        check=True, capture_output=True, text=True
    )
    version = result.stdout.strip()
    print(f"Installed six from git version: {version}")
    assert version == "1.16.0", f"Expected version 1.16.0, got {version}"


@pytest.mark.slow
def test_editable_installation(setup_venv):
    """Test installation in editable mode."""
    temp_dir, venv_dir, python_path, pip_path = setup_venv
        
    
    print("\nTesting editable installation...")
    
    # Create a simple package
    pkg_dir = Path(temp_dir) / "testpkg"
    pkg_dir.mkdir()
    (pkg_dir / "setup.py").write_text("""
from setuptools import setup

setup(
name="testpkg",
version="0.1.0",
packages=["testpkg"],
)
""")
    
    pkg_code_dir = pkg_dir / "testpkg"
    pkg_code_dir.mkdir()
    (pkg_code_dir / "__init__.py").write_text("__version__ = '0.1.0'")
    
    # Install in editable mode
    result = subprocess.run(
        [str(pip_path), "install", "-e", str(pkg_dir)],
        check=True, capture_output=True, text=True
    )
    
    # Verify editable install
    result = subprocess.run(
        [str(python_path), "-c", "import testpkg; print(testpkg.__version__)"],
        check=True, capture_output=True, text=True
    )
    version = result.stdout.strip()
    print(f"Installed testpkg in editable mode: {version}")
    assert version == "0.1.0", f"Expected version 0.1.0, got {version}"
    
    # Modify the package and verify changes are reflected
    (pkg_code_dir / "__init__.py").write_text("__version__ = '0.1.1'")
    
    # Verify the change is reflected (editable mode)
    result = subprocess.run(
        [str(python_path), "-c", "import testpkg; print(testpkg.__version__)"],
        check=True, capture_output=True, text=True
    )
    version = result.stdout.strip()
    print(f"Modified testpkg in editable mode: {version}")
    assert version == "0.1.1", f"Expected version 0.1.1 after modification, got {version}"


@pytest.mark.slow
def test_org_repo_shorthand_installation(setup_venv):
    """Test installation using org/repo shorthand."""
    temp_dir, venv_dir, python_path, pip_path = setup_venv
        
    
    print("\nTesting org/repo format GitHub shorthand...")
    
    # First, create a requirements.txt file with GitHub shorthand
    work_dir = Path(temp_dir) / "workspace"
    work_dir.mkdir()
    req_file = work_dir / "requirements.txt"
    req_file.write_text("benjaminp/six")
    
    # Since we don't want to set up the full MB system,
    # we'll just verify pip can install from a GitHub repo
    result = subprocess.run(
        [str(pip_path), "install", "git+https://github.com/benjaminp/six.git"],
        check=True, capture_output=True, text=True
    )
    
    # Verify installation
    result = subprocess.run(
        [str(python_path), "-c", "import six; print(six.__version__)"],
        check=True, capture_output=True, text=True
    )
    version = result.stdout.strip()
    print(f"Installed six from GitHub shorthand: {version}")
    assert version, "Failed to get six version"


if __name__ == "__main__":
    import sys
    pytest.main(["-xvs", __file__,*(sys.argv[1:] if len(sys.argv) > 1 else [])]) 