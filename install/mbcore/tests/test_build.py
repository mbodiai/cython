import pytest
import shutil
import sys
import os
from pathlib import Path
import importlib.metadata
import importlib.util
import subprocess

# Adjust sys.path to ensure mbcore can be imported if tests are run from root
# This might be necessary depending on how pytest discovers/runs tests
mbcore_src_path = Path(__file__).parent.parent / 'src'
if str(mbcore_src_path) not in sys.path:
    sys.path.insert(0, str(mbcore_src_path))

# --- Robust import of functions to test ---
# Use importlib to load the module more reliably, especially in test environments

mbcore_build_path = Path(__file__).parent.parent / "src" / "mbcore" / "build.py"

def load_build_functions():
    try:
        spec = importlib.util.spec_from_file_location("mbcore.build", mbcore_build_path)
        if spec and spec.loader:
            mbcore_build = importlib.util.module_from_spec(spec)
            sys.modules["mbcore.build"] = mbcore_build # Add to sys.modules before loading
            spec.loader.exec_module(mbcore_build)
            # Return the required functions and global FLAGS
            return (
                getattr(mbcore_build, 'bundle_package', None),
                getattr(mbcore_build, 'setup_paths', None),
                getattr(mbcore_build, 'FLAGS', None),
                getattr(mbcore_build, '_main', None)
            )
        else:
            print(f"Could not create spec for {mbcore_build_path}")
            return None, None, None, None
    except Exception as e:
        print(f"Failed to import functions from {mbcore_build_path}: {e}")
        return None, None, None, None

bundle_package, setup_paths, FLAGS, _main = load_build_functions() # type: ignore

# Define dummy functions if import fails, so tests can be collected (but will likely fail)
if bundle_package is None:
    def bundle_package(package_name: str, packages_dir: Path) -> None:
        raise ImportError("bundle_package could not be imported")
if setup_paths is None:
    def setup_paths(**kwargs):
        raise ImportError("setup_paths could not be imported")
if FLAGS is None:
    FLAGS = {} # Ensure FLAGS is always a dict
if _main is None:
    def _main(*args, **kwargs):
        raise ImportError("_main could not be imported from mbcore.build")


# --- Test bundle_package ---

# Helper to find dist-info directory name
def get_dist_info_name(package_name):
    try:
        dist = importlib.metadata.distribution(package_name)
        # The metadata directory can be None, handle this case
        metadata_dir = dist.locate_file('') 
        if metadata_dir and Path(metadata_dir).name.endswith('.dist-info'):
             return Path(metadata_dir).name
        # Fallback if locate_file doesn't work as expected or name isn't dist-info
        # Look for directories matching pattern in the site-packages
        for path in sys.path:
             if 'site-packages' in path:
                  sp_dir = Path(path)
                  potential_dirs = list(sp_dir.glob(f'{package_name.replace("-", "_")}-*.dist-info'))
                  if potential_dirs:
                       return potential_dirs[0].name # Return the first match

    except importlib.metadata.PackageNotFoundError:
        return None

@pytest.mark.skipif(shutil.which('click') is None and get_dist_info_name('click') is None, reason="'click' package not found in environment")
def test_bundle_package_click(tmp_path):
    """Tests bundling the 'click' package into a temporary directory."""
    packages_dir = tmp_path / "bundled_packages"
    packages_dir.mkdir()

    package_name = "click"
    
    # Ensure the package exists before trying to bundle
    try:
        importlib.import_module(package_name)
    except ImportError:
        pytest.skip(f"{package_name} not installed, skipping bundle test")

    print(f"Attempting to bundle '{package_name}' into {packages_dir}")
    bundle_package(package_name, packages_dir)

    # Assertions
    bundled_click_dir = packages_dir / package_name
    assert bundled_click_dir.exists(), f"'{package_name}' directory was not created in {packages_dir}"
    assert bundled_click_dir.is_dir(), f"'{bundled_click_dir}' should be a directory"
    
    # Check for a key file within the bundled package
    click_init_file = bundled_click_dir / "__init__.py"
    assert click_init_file.exists(), f"'{click_init_file}' does not exist in bundled package"
    assert click_init_file.is_file(), f"'{click_init_file}' should be a file"

    # Check for the .dist-info directory
    # NOTE: The bundle_package function (as of reading its code) does not appear to copy
    # the .dist-info directory, although it might be intended. Commenting out this check.
    dist_info_name = get_dist_info_name(package_name)
    print(f"Expected dist-info name for {package_name}: {dist_info_name}")

    if dist_info_name:
        bundled_dist_info_dir = packages_dir / dist_info_name
        assert bundled_dist_info_dir.exists(), f"'{dist_info_name}' directory was not created in {packages_dir}"
        assert bundled_dist_info_dir.is_dir(), f"'{bundled_dist_info_dir}' should be a directory"
        
        # Check for a key file within dist-info
        metadata_file = bundled_dist_info_dir / "METADATA"
        assert metadata_file.exists(), f"'METADATA' file does not exist in {bundled_dist_info_dir}"
        assert metadata_file.is_file(), f"'METADATA' should be a file"
    else:
         # If we couldn't determine the dist-info name, we can't assert its presence.
         # This might happen in non-standard environments. Warn instead of failing.
         import warnings # Ensure warnings is imported if uncommenting
         warnings.warn(f"Could not determine .dist-info directory name for '{package_name}'. Cannot verify its bundling.")

# --- Test setup_paths (related to 'env vars'/FLAGS) ---

def test_setup_paths_defaults(tmp_path):
    """Tests setup_paths with default values, checking directory creation and FLAGS update."""
    root_dir = tmp_path / "test_project_defaults"
    root_dir.mkdir()
    
    # Create a dummy src dir and file for module detection
    src_dir = root_dir / "src" / "test_project_defaults"
    src_dir.mkdir(parents=True)
    (src_dir / "module1.py").touch()
    
    # Initialize FLAGS before potential modification by setup_paths
    global FLAGS
    if FLAGS is None: # Should not happen due to earlier fix, but good practice
        FLAGS = {} 
    initial_flags = FLAGS.copy() # Store initial state if needed

    # Use os.chdir temporarily because setup_paths uses relative paths from CWD by default
    original_cwd = Path.cwd()
    try:
        os.chdir(root_dir)
        flags = setup_paths(root_path=".") # Test with relative root
    finally:
        os.chdir(original_cwd)

    # Check directory creation
    assert (root_dir / "build").exists() and (root_dir / "build").is_dir()
    assert (root_dir / "install").exists() and (root_dir / "install").is_dir()
    assert (root_dir / "install" / "bin").exists() and (root_dir / "install" / "bin").is_dir()
    assert (root_dir / "install" / "lib").exists() and (root_dir / "install" / "lib").is_dir()
    
    # Check FLAGS update
    assert flags["ROOT_DIR"] == Path('.') # Check against the path stored by setup_paths
    # Check other paths relative to the actual resolved root_dir for clarity
    # Assert against the relative paths stored in FLAGS
    assert flags["SRC_DIR"] == Path('src') # Default src_dir should resolve to relative 'src'
    assert flags["BUILD_DIR"] == Path('build')
    assert flags["INSTALL_DIR"] == Path('install')
    assert flags["BIN_DIR"] == Path('install') / "bin"
    assert flags["LIB_DIR"] == Path('install') / "lib"
    assert flags["ENTRY_POINT"] == "main" # Default
    assert flags["FORCE"] is False # Default
    # Check if modules were detected
    assert isinstance(flags["MODULES"], list) 
    # Check if the detected module path stored in FLAGS is the expected relative path
    expected_relative_module_path = Path("src") / "test_project_defaults" / "module1.py"
    assert expected_relative_module_path in flags["MODULES"]
    
    # Verify python paths are set (these should still be absolute)
    assert flags["PYTHON_LIBRARY"].is_absolute() and flags["PYTHON_LIBRARY"].exists()
    assert flags["PYTHON_INCLUDE"].is_absolute() and flags["PYTHON_INCLUDE"].exists()

def test_setup_paths_custom(tmp_path):
    """Tests setup_paths with custom values, checking directory creation and FLAGS update."""
    root_dir = tmp_path / "test_project_custom"
    root_dir.mkdir()
    
    custom_src_name = "source"
    custom_build_name = "out_build"
    custom_install_name = "out_install"
    
    custom_src = root_dir / custom_src_name
    custom_src.mkdir()
    custom_module_file = custom_src / "custom_module.py"
    custom_module_file.touch()
    
    custom_build = root_dir / custom_build_name
    custom_install = root_dir / custom_install_name
    custom_entry = "app_entry"
    # Provide the module path relative to the root for the modules argument
    custom_modules_arg = [Path(custom_src_name) / "custom_module.py"]

    original_cwd = Path.cwd()
    try:
        os.chdir(root_dir)
        flags = setup_paths(
            root_path=".",
            src_dir=custom_src_name,
            build_dir=custom_build_name,
            install_dir=custom_install_name,
            entry=custom_entry,
            modules=custom_modules_arg, # Pass relative path
            force=True
        )
    finally:
        os.chdir(original_cwd)
        
    # Check directory creation (using absolute paths for checking filesystem)
    assert custom_build.exists() and custom_build.is_dir()
    assert custom_install.exists() and custom_install.is_dir()
    assert (custom_install / "bin").exists() and (custom_install / "bin").is_dir()
    assert (custom_install / "lib").exists() and (custom_install / "lib").is_dir()

    # Check FLAGS update (asserting against expected relative paths stored in FLAGS)
    assert flags["ROOT_DIR"] == Path('.') 
    assert flags["SRC_DIR"] == Path(custom_src_name)
    assert flags["BUILD_DIR"] == Path(custom_build_name)
    assert flags["INSTALL_DIR"] == Path(custom_install_name)
    assert flags["BIN_DIR"] == Path(custom_install_name) / "bin"
    assert flags["LIB_DIR"] == Path(custom_install_name) / "lib"
    assert flags["ENTRY_POINT"] == custom_entry
    assert flags["FORCE"] is True
    # Check module path stored in FLAGS is the relative one provided
    assert flags["MODULES"] == custom_modules_arg

# Remove the closing tag below if it exists
# </rewritten_file>

# --- Test Standalone Executable Build ---

# Check if a C++ compiler is available (basic check)
def has_compiler():
    return shutil.which('g++') is not None or shutil.which('clang++') is not None

@pytest.mark.skipif(not has_compiler(), reason="Requires g++ or clang++ compiler in PATH")
@pytest.mark.skipif(shutil.which('click') is None and get_dist_info_name('click') is None, reason="'click' package not found in environment")
def test_build_standalone_executable(tmp_path):
    """Tests building a standalone executable by invoking the mbuild command."""
    project_root = tmp_path / "my_app"
    relative_src_dir = Path("src") / "my_app" # Relative path within project
    src_dir = project_root / relative_src_dir
    src_dir.mkdir(parents=True)

    # Create dummy __init__.py
    (src_dir / "__init__.py").touch()

    # Create main entry point with a dependency
    main_py_content = """
import click
import sys

def main():
    # Add check for frozen executable environment
    is_frozen = getattr(sys, 'frozen', False)
    if is_frozen:
        print("Hello from frozen executable!")
    else:
        print("Hello from script!")
    
    # Use the dependency
    try:
        click.echo("Click dependency worked!")
    except Exception as e:
        print(f"Error using click: {e}")
        sys.exit(1) # Exit if dependency fails

if __name__ == "__main__":
    main()
"""
    main_py_rel_path = relative_src_dir / "main.py"
    main_py_abs_path = project_root / main_py_rel_path
    main_py_abs_path.write_text(main_py_content)

    # Define expected output paths (relative to project_root)
    install_dir_rel = Path("install") # Default install dir
    bin_dir_rel = install_dir_rel / "bin"
    executable_name = main_py_rel_path.stem # Should be 'main'
    executable_rel_path = bin_dir_rel / executable_name
    executable_abs_path = project_root / executable_rel_path

    # Command to run mbuild
    # We need to ensure mbcore.build is runnable via python -m
    # This might require adjusting PYTHONPATH or running from the correct directory
    # For simplicity, assume running from the root of the *mbcore* project allows finding it.
    mbuild_cmd = [
        sys.executable, # Use the same python interpreter running pytest
        "-m", "mbcore.build",
        "--embed",
        "--force",
        "--root", str(project_root), # Root of the *test* project
        "--entry", str(main_py_rel_path), # Entry point relative to test project root
        "--install-dir", str(install_dir_rel), # Explicitly set install dir relative to root
        str(main_py_rel_path) # Module to build, relative to test project root
    ]

    print(f"Running mbuild command: {' '.join(mbuild_cmd)}")
    
    # Run the build process as a subprocess
    # Run from the main workspace directory so mbcore can be found
    workspace_root = Path(__file__).parent.parent.parent # Assuming tests/test_build.py location
    
    # Set PYTHONPATH for the subprocess to find sibling packages (like mbpy)
    env = os.environ.copy()
    env["PYTHONPATH"] = str(workspace_root) + os.pathsep + env.get("PYTHONPATH", "")
    
    build_process = subprocess.run(
        mbuild_cmd, 
        capture_output=True, 
        text=True, 
        cwd=workspace_root, # Run from workspace root
        env=env, # Pass the modified environment with PYTHONPATH
        check=False # Don't check yet, assert based on output/files
    )

    print("mbuild stdout:", build_process.stdout)
    print("mbuild stderr:", build_process.stderr)
    assert build_process.returncode == 0, f"mbuild command failed with exit code {build_process.returncode}"

    # Assertions: Check if executable exists and is runnable
    print(f"Checking for executable at: {executable_abs_path}")
    assert executable_abs_path.exists(), f"Executable '{executable_name}' not found in {executable_abs_path.parent}"
    assert executable_abs_path.is_file(), f"'{executable_abs_path}' is not a file"
    assert os.access(executable_abs_path, os.X_OK), f"Executable '{executable_abs_path}' is not executable"

    # Run the created executable and check output
    print(f"Running executable: {executable_abs_path}")
    run_executable_process = subprocess.run(
        [str(executable_abs_path)], 
        capture_output=True, 
        text=True, 
        check=True
    )
    
    print("Executable stdout:", run_executable_process.stdout)
    print("Executable stderr:", run_executable_process.stderr)
    assert "Hello from frozen executable!" in run_executable_process.stdout
    assert "Click dependency worked!" in run_executable_process.stdout

# Remove the closing tag below if it exists
# </rewritten_file> 