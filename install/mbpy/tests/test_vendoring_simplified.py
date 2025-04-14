import os
import sys
import tempfile
import subprocess
from pathlib import Path
import pytest
import shutil
import time
import tomlkit

"""
Simplified integration test for vendoring functionality that focuses on:
1. Basic vendoring of a simple dependency
2. Verification that vendored copy works
3. Checking pyproject.toml path handling
"""


class TestVendoringSimplified:
    @pytest.fixture
    def test_env(self):
        """Create a minimal test environment with a package that needs vendoring"""
        # Create a temporary root directory
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)

            # Create the main workspace
            workspace = tmpdir_path / "workspace"
            workspace.mkdir()

            # Create a dev directory
            dev_dir = workspace / ".dev"
            dev_dir.mkdir()

            # Create a vendored directory
            vendored = workspace / "vendored"
            vendored.mkdir()

            # Create a dependency package
            dep_dir = tmpdir_path / "dependency"
            dep_dir.mkdir()
            (dep_dir / "__init__.py").write_text(
                "def hello():\n    return 'Hello from dependency'"
            )

            # Create a link in the dev directory
            (dev_dir / "testorg").mkdir()

            # Try to create symlink but handle if it fails (e.g., on Windows)
            try:
                os.symlink(dep_dir, dev_dir / "testorg" / "dependency")
            except OSError:
                # If symlink fails, just copy the directory
                shutil.copytree(dep_dir, dev_dir / "testorg" / "dependency")

            # Create a minimal pyproject.toml
            pyproject_content = f"""
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "test-project"
version = "0.1.0"
dependencies = [
    "dependency @ file:///{dep_dir.absolute()}"
]
"""
            with open(workspace / "pyproject.toml", "w") as f:
                f.write(pyproject_content)

            # Initialize Git repository to support vendoring
            orig_dir = os.getcwd()
            try:
                os.chdir(workspace)
                subprocess.run(["git", "init"], capture_output=True)
                subprocess.run(
                    ["git", "config", "user.email", "test@example.com"],
                    capture_output=True,
                )
                subprocess.run(
                    ["git", "config", "user.name", "Test User"], capture_output=True
                )
                subprocess.run(
                    [
                        "git",
                        "remote",
                        "add",
                        "origin",
                        "https://github.com/testorg/test-project.git",
                    ],
                    capture_output=True,
                )
                subprocess.run(["git", "add", "."], capture_output=True)
                subprocess.run(
                    ["git", "commit", "-m", "Initial commit"], capture_output=True
                )
            except Exception as e:
                print(f"Git setup error (non-critical): {e}")
            finally:
                os.chdir(orig_dir)

            yield {
                "workspace": workspace,
                "dependency": dep_dir,
                "dev_dir": dev_dir,
                "vendored": vendored,
            }

    @pytest.mark.asyncio
    async def test_basic_vendoring(self, test_env):
        """Test basic vendoring process using simplified setup."""
        # Extract paths
        workspace = test_env["workspace"]
        dep_dir = test_env["dependency"]
        dev_dir = test_env["dev_dir"]

        orig_dir = os.getcwd()

        try:
            os.chdir(workspace)
            # Re-enable touching the file to test the mtime check
            time.sleep(0.1)  # Small delay to ensure time difference
            (dep_dir / "__init__.py").touch()
            print(f"Touched dependency file: {dep_dir / '__init__.py'}")

            # Mock necessary environment functions
            # monkeypatch.setattr("mbpy.env.getws", lambda: workspace)
            # monkeypatch.setattr("mbpy.env.getdevws", lambda relative=False: dev_dir)
            # monkeypatch.setattr("mbpy.env.get_simple_org_repo", lambda ws=None: ("testorg", "test-project"))

            try:
                # ... (Setup SimplePyProject mock etc.) ...
                from mbpy.store.py.models.pyproject import PyProject

                class SimplePyProject:
                    def __init__(self):
                        self._project_data = {"dependencies": []}

                    @classmethod
                    def fromtoml(cls, path=None):
                        instance = cls()
                        instance._project_data = {
                            "dependencies": [
                                f"dependency @ file:///{dep_dir.absolute()}"
                            ]
                        }
                        return instance

                    @property
                    def project(self):
                        return self._project_data

                # monkeypatch.setattr("mbpy.store.py.models.pyproject.PyProject", SimplePyProject)
                # monkeypatch.setattr("mbpy.pkg.toml.find_toml", lambda path=None, cwd=None: workspace / "pyproject.toml")
                def mock_load_toml(path=None, cwd=None):
                    return {
                        "project": {
                            "dependencies": [
                                f"dependency @ file:///{dep_dir.absolute()}"
                            ]
                        }
                    }

                # monkeypatch.setattr("mbpy.pkg.toml.load_toml", mock_load_toml)

                # Import and run vendoring function
                from mbpy.git.check import ensure_vendored
                import asyncio

                print("Running vendoring process (no force_update)...")
                # Call without force_update to test the timestamp check
                await ensure_vendored(modify_main_pyproject=False)
                print("Vendoring process completed.")

                # Check if vendoring worked (Assertions remain the same)
                vendored_dir = workspace / "vendored"
                print(f"Checking vendored directory (exists: {vendored_dir.exists()})")
                print("Vendored directory contents:")
                vendored_items = list(vendored_dir.glob("**/*"))
                if vendored_dir.exists():
                    for item in vendored_items:
                        if item.name != ".last_vendored":
                            print(f"  - {item.relative_to(vendored_dir)}")
                assert vendored_dir.exists(), "Vendored directory doesn't exist"
                expected_vendored_dep_path1 = (
                    vendored_dir / dep_dir.name / "__init__.py"
                )
                expected_vendored_dep_path2 = (
                    vendored_dir / "testorg" / dep_dir.name / "__init__.py"
                )
                assert (
                    expected_vendored_dep_path1.exists()
                    or expected_vendored_dep_path2.exists()
                ), (
                    f"Vendored dependency __init__.py not found at expected locations: {expected_vendored_dep_path1} or {expected_vendored_dep_path2}"
                )
                print("Vendored dependency file found.")
                original_pyproject_content = (workspace / "pyproject.toml").read_text()
                assert f"file:///{dep_dir.absolute()}" in original_pyproject_content, (
                    "Original pyproject.toml was modified even though modify_main_pyproject was False"
                )

            except ImportError as e:
                pytest.skip(f"Failed to import vendoring modules: {e}")
            except Exception as e:
                pytest.fail(
                    f"Vendoring test failed with unexpected error: {type(e).__name__} - {e}"
                )

        finally:
            os.chdir(orig_dir)

    def test_vendoring_with_mb_command(self, test_env):
        """
        Test vendoring using the mb command line tool
        This test is skipped if mb command is not available
        """
        # Check if mb command is available
        try:
            result = subprocess.run(["mb", "--version"], capture_output=True, text=True)
            if result.returncode != 0:
                pytest.skip("mb command not available")
        except FileNotFoundError:
            pytest.skip("mb command not found")

        # Extract paths
        workspace = test_env["workspace"]
        orig_dir = os.getcwd()

        try:
            # Change to workspace directory
            os.chdir(workspace)

            # Run mb vendor command
            result = subprocess.run(
                ["mb", "pkg", "vendor"], capture_output=True, text=True
            )

            # Print output for debugging
            print(f"mb pkg vendor stdout: {result.stdout}")
            if result.stderr:
                print(f"mb pkg vendor stderr: {result.stderr}")

            # Check if command succeeded
            assert result.returncode == 0, (
                f"mb pkg vendor failed with code {result.returncode}"
            )

            # Check if vendoring created files
            vendored_dir = workspace / "vendored"
            assert vendored_dir.exists(), "Vendored directory doesn't exist"
            assert any(vendored_dir.glob("**/*")), "No files were vendored"

        finally:
            # Return to original directory
            os.chdir(orig_dir)
