# Dependency Management System: Developer Guide

## 1. Introduction

The Dependency Management System offers a powerful solution for handling Python package dependencies across multiple source types, environments, and configuration formats. Unlike traditional dependency tools, it provides deep integration with Git repositories, local development workflows, and configuration synchronization.

### Purpose and Key Capabilities

This system solves several common challenges in Python dependency management:
- Managing dependencies from PyPI, Git repositories, and local paths with a unified interface
- Synchronizing between different configuration formats (requirements.txt, pyproject.toml)
- Supporting environment-specific dependency management
- Enabling seamless development workflows with editable installations

### When to Use This System

The Dependency Management System is particularly valuable when:
- Your project includes dependencies from multiple sources (not just PyPI)
- You need to maintain consistency across different configuration formats
- You work with multiple Python environments
- You develop packages that have their own dependencies

### Core Concepts and Terminology

Before diving into specific workflows, let's understand the fundamental concepts:

- **Dependency**: A Python package required by your project, represented by the `Dependency` class.
- **Source Types**: Where dependencies come from (PyPI, Git repositories, local paths).
- **Environment**: A Python execution context with its own package set.
- **Configuration Format**: How dependencies are declared (requirements.txt, pyproject.toml).

With these concepts in mind, let's get your system set up and start working with dependencies.

## 2. Getting Started

Setting up the Dependency Management System is straightforward. This section walks you through installation, basic configuration, and a simple example to validate your setup.

### Installation and Setup

First, install the base package:

```bash
pip install mbpy
```

Next, initialize your workspace environment:

```bash
# Create a workspace directory if you don't have one
mkdir -p my_workspace
cd my_workspace

# Initialize the workspace
mb init
```

This setup creates necessary configuration files and prepares your workspace for dependency management.

### Basic Usage Patterns

The typical workflow involves creating `Dependency` objects and performing operations on them:

```python
from mbpy.pkg.dependency import Dependency

# Create a dependency
requests_dep = Dependency("requests>=2.24.0")

# Install it
import asyncio
asyncio.run(requests_dep.install())

# Check its installed version
version = asyncio.run(requests_dep.installed_version())
print(f"Installed {requests_dep.name} version {version}")
```

### Quick Start Example

Let's put everything together in a quick example that demonstrates the core functionality:

```python
import asyncio
from mbpy.pkg.dependency import Dependency
from mbpy.pkg.mpip import sync_requirements_pyproject

async def main():
    # Create and install a PyPI package
    requests = Dependency("requests>=2.24.0")
    await requests.install()
    
    # Install a package with extras
    pandas = Dependency("pandas[excel,parquet]>=1.5.0")
    await pandas.install()
    
    # Install from a Git repository
    repo_pkg = Dependency("user/repo")
    await repo_pkg.install(editable=True)
    
    # Synchronize configuration files
    await sync_requirements_pyproject()
    
    print("Setup complete!")

if __name__ == "__main__":
    asyncio.run(main())
```

Now that you have a basic understanding of the system, let's explore the core workflows for different dependency types.

## 3. Core Workflows

The Dependency Management System handles different types of dependencies, each with its own workflow. This section covers the most common dependency sources and how to work with them effectively.

### Managing PyPI Packages

PyPI (Python Package Index) is the standard repository for Python packages. Working with PyPI packages is the most straightforward use case.

#### Installation, Upgrading, and Uninstallation

```python
import asyncio
from mbpy.pkg.dependency import Dependency

async def manage_pypi_packages():
    # Create a dependency with version specification
    numpy = Dependency("numpy>=1.20.0")
    
    # Install the package
    await numpy.install()
    
    # Upgrade to the latest version
    await numpy.install(upgrade=True)
    
    # Uninstall when no longer needed
    await numpy.uninstall()

asyncio.run(manage_pypi_packages())
```

#### Version Specification and Comparison

The system provides robust version handling:

```python
# Compare versions
numpy_older = Dependency("numpy>=1.19.0")
numpy_newer = Dependency("numpy>=1.20.0")

# Check if versions are compatible
if numpy_newer > numpy_older:
    print("Newer version detected")

# Verify installed version meets requirements
numpy_dep = Dependency("numpy>=1.20.0")
numpy_dep.require_version()  # Raises error if version requirement not met
```

These version handling capabilities make it easy to manage complex version constraints in your projects. Now, let's move on to Git repositories.

### Working with Git Repositories

Git repositories require special handling due to their asynchronous nature and the need for cloning operations.

#### From GitHub and Other Git Hosts

```python
import asyncio
from mbpy.pkg.dependency import Dependency

async def work_with_git_repos():
    # GitHub shorthand format
    github_dep = Dependency("user/repo")
    await github_dep.install()
    
    # Full Git URL
    git_dep = Dependency("git+https://github.com/user/repo.git")
    await git_dep.install()
    
    # With branch or tag specification
    branch_dep = Dependency("git+https://github.com/user/repo.git@develop")
    await branch_dep.install()

asyncio.run(work_with_git_repos())
```

#### Development Workflow with Editable Installs

When actively developing a Git repository, use editable installs:

```python
async def git_development_workflow():
    # Clone and install in editable mode
    repo = Dependency("user/repo")
    await repo.install(editable=True)
    
    # The repository is cloned to your development workspace
    # Location: {workspace}/.dev/repo
    
    # Changes to the cloned repository will be immediately available
    # without reinstallation

asyncio.run(git_development_workflow())
```

Git repositories provide a way to use packages directly from source control. Next, let's look at local package development.

### Local Package Development

When developing packages locally, you'll often work with filesystem paths rather than remote repositories.

#### Directory Structure and Conventions

The system expects local packages to follow standard Python packaging conventions:

```
my_package/
├── pyproject.toml
├── setup.py (optional)
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── ...
├── tests/
└── ...
```

#### Development Mode Installation

Install local packages in development mode to reflect changes immediately:

```python
import asyncio
from mbpy.pkg.dependency import Dependency
from pathlib import Path

async def local_development():
    # Install current directory in editable mode
    current = Dependency(".", editable=True)
    await current.install()
    
    # Or specify a path
    pkg_path = Path("../another_package")
    path_pkg = Dependency(pkg_path)
    await path_pkg.install(editable=True)

asyncio.run(local_development())
```

Local package development integrates seamlessly with configuration management, which we'll explore next.

## 4. Configuration Management

Python projects typically use configuration files to declare dependencies. The Dependency Management System provides robust tools for maintaining these files.

### Understanding Configuration Files

Let's examine the structures of the main configuration file types the system supports.

#### pyproject.toml Structure

The modern Python project configuration format uses TOML syntax:

```toml
[project]
name = "my-project"
version = "0.1.0"
dependencies = [
    "requests>=2.24.0",
    "numpy>=1.20.0",
    "pandas[excel,parquet]>=1.5.0"
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0"
]
```

#### requirements.txt Format

The traditional dependency specification format uses plain text:

```
requests>=2.24.0
numpy>=1.20.0
pandas[excel,parquet]>=1.5.0
```

While these formats serve the same purpose, maintaining consistency between them can be challenging. That's where synchronization comes in.

### Synchronization Between Formats

The system provides tools to ensure your configuration files remain in sync.

#### Command-Line Interface

Synchronize files using the command-line interface:

```bash
# Default synchronization
mb sync

# With custom paths
mb sync --pyproject custom_pyproject.toml --requirements custom_requirements.txt

# Prefer requirements.txt as source of truth
mb sync --prefer-requirements
```

#### Programmatic API

For more control, use the programmatic API:

```python
import asyncio
from mbpy.pkg.mpip import sync_requirements_pyproject

async def sync_config_files():
    # Basic synchronization
    await sync_requirements_pyproject()
    
    # With custom paths and preferences
    await sync_requirements_pyproject(
        pyproject="custom_pyproject.toml",
        requirements="custom_requirements.txt",
        prefer_requirements=True
    )

asyncio.run(sync_config_files())
```

#### Conflict Resolution Strategies

When conflicts arise between configuration files, the system employs resolution strategies:

```python
# Define custom conflict resolution
def custom_preference(dep_a, dep_b):
    """Determine which dependency version to prefer."""
    # Prefer installed versions
    if dep_a.installed() and not dep_b.installed():
        return True
        
    # Prefer development versions for specific packages
    if dep_a.name in ["my-dev-package"]:
        return dep_a.source.startswith("git+")
        
    # Default to highest version
    return dep_a > dep_b

# Use custom resolution
from mbcore.collect import find_preferred
resolved_deps = find_preferred(deps_a, deps_b, is_preferred=custom_preference)
```

Configuration management often needs to account for different environments, which we'll explore next.

## 5. Environment Integration

Python projects frequently use multiple environments for different purposes. The Dependency Management System integrates with environment management tools.

### Environment Detection and Selection

The system can detect and work with different environment types.

#### Virtual Environments (venv)

Standard Python virtual environments:

```python
from mbpy.env import Env, getenv

# Get the active virtual environment
venv = getenv()
print(f"Active venv: {venv.name}")

# Create reference to a specific venv
custom_venv = Env(type="venv", name="my-venv", 
                  python="/path/to/venv/bin/python")
```

#### Conda Environments

Anaconda environments are detected and supported:

```python
# Detect active conda environment
conda_env = getenv()  # Automatically detects if conda is active
if conda_env.type == "conda":
    print(f"Active conda env: {conda_env.name}")
```

#### Custom Environments

For special cases, create custom environment definitions:

```python
from mbpy.env import Env
from pathlib import Path

# Define a custom environment
custom_env = Env(
    type="mb",  # Custom type
    name="production",
    python=Path("/usr/bin/python3"),
    ws=Path("/opt/project")
)
```

These environment utilities enable multi-environment projects.

### Multi-Environment Projects

Managing dependencies across multiple environments is a common requirement.

#### Environment-Specific Dependencies

Install dependencies in specific environments:

```python
import asyncio
from mbpy.pkg.dependency import Dependency
from mbpy.env import Env

async def environment_specific_install():
    # Create environment references
    dev_env = Env(type="venv", name="dev")
    prod_env = Env(type="venv", name="prod")
    
    # Development dependencies
    dev_deps = [
        Dependency("pytest"),
        Dependency("black")
    ]
    
    # Production dependencies
    prod_deps = [
        Dependency("gunicorn"),
        Dependency("uvicorn")
    ]
    
    # Install in specific environments
    for dep in dev_deps:
        await dep.install(env=dev_env)
        
    for dep in prod_deps:
        await dep.install(env=prod_env)

asyncio.run(environment_specific_install())
```

#### Cross-Environment Compatibility

Ensure packages work across environments:

```python
import asyncio
from mbpy.pkg.dependency import Dependency
from mbpy.env import detect_active_env

async def check_cross_compatibility():
    # Get all environments
    envs = detect_active_env()
    
    # Critical dependency
    dep = Dependency("critical-package>=2.0.0")
    
    # Check compatibility across environments
    for env in envs:
        try:
            # Try to verify version in each environment
            env_python = env.python
            installed_version = await dep.installed_version(env=env)
            
            if not installed_version:
                print(f"Warning: {dep.name} not installed in {env.name}")
            elif installed_version < "2.0.0":
                print(f"Warning: {dep.name} version {installed_version} in {env.name} is outdated")
            else:
                print(f"{dep.name} version {installed_version} in {env.name} is compatible")
        except Exception as e:
            print(f"Error checking {env.name}: {e}")

asyncio.run(check_cross_compatibility())
```

With environment integration covered, let's explore advanced features for more complex scenarios.

## 6. Advanced Features

The Dependency Management System offers advanced capabilities for complex projects and workflows.

### Dependency Groups and Organization

Organize dependencies into logical groups:

```python
import asyncio
from mbpy.pkg.mpip import modify_dependencies
from mbpy.pkg.dependency import Dependency

async def organize_dependencies():
    # Core dependencies
    core_deps = [
        Dependency("flask"),
        Dependency("sqlalchemy")
    ]
    
    # Development dependencies
    dev_deps = [
        Dependency("pytest"),
        Dependency("black")
    ]
    
    # Documentation dependencies
    docs_deps = [
        Dependency("sphinx"),
        Dependency("sphinx-rtd-theme")
    ]
    
    # Update configuration with groups
    await modify_dependencies(core_deps, action="install", group="dependencies")
    await modify_dependencies(dev_deps, action="install", group="dev-dependencies")
    await modify_dependencies(docs_deps, action="install", group="docs-dependencies")

asyncio.run(organize_dependencies())
```

### Conditional Dependencies

Specify environment-specific conditions:

```python
# Platform-specific dependencies
windows_dep = Dependency("pywin32; platform_system=='Windows'")
linux_dep = Dependency("python-prctl; platform_system=='Linux'")

# Python version-specific dependencies
py38_dep = Dependency("importlib-metadata; python_version<'3.8'")
```

### Repository Caching and Optimization

Optimize repository operations with caching:

```python
import asyncio
from mbpy.pkg.dependency import Dependency
from mbpy.env import git_devws, getws

async def optimize_repository_usage():
    repo_name = "frequently-used-repo"
    
    # Check if repository is already cloned
    dev_ws = getws() / ".dev"
    repo_path = dev_ws / repo_name
    
    if repo_path.exists():
        print(f"Using cached repository at {repo_path}")
        # Create dependency from existing path
        dep = Dependency(str(repo_path), editable=True)
    else:
        print(f"Cloning repository to {repo_path}")
        # Create and install from remote
        dep = Dependency(f"user/{repo_name}")
        await dep.install(editable=True)
    
    return dep

asyncio.run(optimize_repository_usage())
```

### IDE Integration (VSCode, PyCharm)

The system can update IDE configuration files:

```python
from mbpy.env import include_pyright_vscode
from pathlib import Path

# Add package to VSCode/PyRight path
package_path = Path("./my_package")
include_pyright_vscode(package_path)

# This updates:
# - .vscode/settings.json with the package path
# - pyproject.toml pyright configuration
```

These advanced features help manage complex project requirements. Next, let's address common challenges you might encounter.

## 7. Common Challenges and Solutions

While working with the Dependency Management System, you might encounter certain challenges. This section provides solutions to common issues.

### Git Repository Initialization Issues

When working with Git repositories, initialization problems can occur:

```python
import asyncio
from mbpy.pkg.dependency import Dependency

async def handle_git_initialization():
    # Problem: Empty source error
    # ValueError: Organization and repository not found in source:
    
    # Solution: Ensure source is set and initialization completes
    repo = Dependency("user/repo")
    
    if repo.git and not repo.source:
        # Ensure source is set
        repo.source = repo.original_source or "user/repo"
    
    # Wait for initialization to complete
    if hasattr(repo, '_tasks') and repo._tasks:
        await asyncio.gather(*repo._tasks.values())
    
    # Now installation should succeed
    await repo.install()

asyncio.run(handle_git_initialization())
```

### Dependency Resolution Conflicts

Version conflicts can arise between dependencies:

```python
import asyncio
from mbpy.pkg.dependency import Dependency

async def resolve_conflicts():
    # Problem: Conflicting version requirements
    
    # Solution: Use explicit versions for critical packages
    critical_deps = [
        Dependency("critical-package==2.1.0"),  # Pin exact version
        Dependency("compatible-package>=1.0.0,<2.0.0")  # Version range
    ]
    
    for dep in critical_deps:
        await dep.install()
        
    # Verify versions match expectations
    for dep in critical_deps:
        installed = await dep.installed_version()
        expected = dep.version.replace("==", "")
        if installed != expected and "==" in dep.version:
            print(f"Warning: {dep.name} version mismatch. Expected {expected}, got {installed}")

asyncio.run(resolve_conflicts())
```

### Environment Detection Problems

Environment detection can sometimes be unreliable:

```python
from mbpy.env import getenv, Env
import os

# Problem: Environment not correctly detected

# Solution: Set environment variables explicitly
os.environ["MB_WS"] = "/path/to/workspace"

# Or use explicit environment specification
explicit_env = Env(
    type="venv",
    name="my-explicit-env",
    python="/path/to/python",
    ws="/path/to/workspace"
)

# Use the explicit environment for operations
# await dependency.install(env=explicit_env)
```

### Format Parsing Edge Cases

Certain dependency formats can cause parsing issues:

```python
# Problem: Empty extras notation (package>=1.0.0[])

# Solution: Clean package names
def clean_package_name(name):
    if isinstance(name, str) and name.endswith('[]'):
        return name[:-2]
    return name

# Usage
from mbpy.pkg.dependency import Dependency
clean_dep = Dependency(clean_package_name("requests>=2.24.0[]"))
```

With these common challenges addressed, let's move on to the complete API reference.

## 8. API Reference

This section provides detailed information about the main classes and functions in the Dependency Management System.

### Dependency Class

The core class for dependency management.

#### Initialization Options

```python
class Dependency:
    """Handles Python package dependencies with smart version handling and installation."""
    
    def __init__(self, 
                 name: str | Path,                      # Package name or path
                 version: str | tuple = "",             # Version specification
                 extra_dependencies: str | list[str] = "", # Package extras
                 conditions: list[Condition] = [],      # Environment conditions
                 pypi_info: PyPackageInfo = None,       # PyPI metadata
                 editable: bool = False,                # Editable installation
                 upgrade: bool = False,                 # Upgrade flag
                 dependencies: list["Dependency"] = None, # Nested dependencies
                 group: str | None = None,              # Dependency group
                 git: bool | None = None,               # Git repository flag
                 at: bool | None = None,                # @ notation flag
                 env: Env | None = None,                # Target environment
                 author: str = "",                      # Repository author
                 source: str | Path = "")               # Installation source
```

#### Core Methods

```python
# Installation methods
async def install(self, executable=None, editable=None, upgrade=None, 
                  group=None, progress_tid=None) -> Self:
    """Install the dependency using pip."""

async def uninstall(self, env=None) -> Self:
    """Uninstall the dependency."""

# Version methods
async def installed_version(self) -> str:
    """Get the installed version of the package."""

def require_version(self) -> None:
    """Verify installed version meets requirements."""

# String representation
async def to_string(self, requirements=False, editable=None, project=False) -> str:
    """Generate string representation for different contexts."""

# Git repository handling
async def clone(self) -> None:
    """Clone a git repository and update dependency information."""
```

#### Properties and Attributes

```python
# Package identification
self.name       # Normalized package name
self.base       # Base package name without extras or version
self.extras     # List of package extras
self.extras_str # Formatted extras string (e.g., "[extra1,extra2]")

# Version information
self.version      # Version object
self.version_str  # Version string
self.version_info # Parsed version components

# Source information
self.source      # Installation source
self.git         # Git repository flag
self.editable    # Editable installation flag
self.author      # Repository author (for Git)

# Environment integration
self.env         # Target environment
self.conditions  # Environment conditions
```

### Environment Management

Functions and classes for environment handling.

```python
# Environment detection
def getenv(env_str=None) -> Env:
    """Get the appropriate environment."""

def getws(root=None) -> Path:
    """Get the workspace root directory."""

def getdevws(root=None) -> Path:
    """Get the development workspace directory."""

# Environment class
class Env:
    """Represents a Python environment."""
    
    def __init__(self, type="mb", name="", python=Path(sys.executable),
                 ws=Path(os.getenv("MB_WS", "")), 
                 devws=Path(os.getenv("MB_DEV_WS", ""))):
        """Initialize environment with type and paths."""
```

### Configuration Utilities

Functions for managing configuration files.

```python
# Synchronization functions
async def sync_requirements_pyproject(pyproject="pyproject.toml", 
                                     requirements="requirements.txt",
                                     prefer_requirements=False,
                                     upgrade=False) -> None:
    """Synchronize requirements.txt and pyproject.toml."""

async def modify_pyproject(packages=None, action="install", env=None,
                          group=None, pyproject_path="pyproject.toml") -> TOMLDocument:
    """Modify pyproject.toml with dependencies."""

async def modify_dependencies(incoming, action, group="dependencies",
                             env=None, commit=True) -> tuple[list[Dependency], TOMLDocument]:
    """Update dependencies in configuration files."""
```

This API reference provides a foundation for understanding the system's capabilities. Next, let's look at best practices for using it effectively.

## 9. Best Practices

Following these best practices will help you use the Dependency Management System effectively and avoid common pitfalls.

### Dependency Organization Strategies

Organize dependencies to improve maintainability:

```python
# Group dependencies by purpose
core_dependencies = [
    Dependency("flask"),       # Web framework
    Dependency("sqlalchemy"),  # Database ORM
    Dependency("pydantic")     # Data validation
]

dev_dependencies = [
    Dependency("pytest"),      # Testing
    Dependency("black"),       # Formatting
    Dependency("pylint")       # Linting
]

# Document dependency purposes with comments
docs_dependencies = [
    Dependency("sphinx"),             # Documentation generator
    Dependency("sphinx-rtd-theme"),   # Documentation theme
    Dependency("sphinx-autodoc-typehints")  # Type hint support
]

# Separate optional features
optional_dependencies = {
    "aws": [Dependency("boto3")],             # AWS integration
    "azure": [Dependency("azure-storage-blob")]  # Azure integration
}
```

### Version Management

Adopt a consistent versioning strategy:

```python
# Pin versions for stability in production
production_deps = [
    Dependency("critical-package==1.2.3"),  # Exact version for stability
]

# Use ranges for flexibility in development
development_deps = [
    Dependency("dev-tool>=2.0.0,<3.0.0"),  # Compatible versions
]

# Minimum versions for basic compatibility
compatibility_deps = [
    Dependency("common-lib>=1.0.0"),  # At least this version
]
```

### Error Handling Patterns

Implement robust error handling:

```python
import asyncio
from mbpy.pkg.dependency import Dependency

async def robust_installation(dependencies):
    """Install dependencies with robust error handling."""
    results = []
    
    for dep in dependencies:
        try:
            # Try installation
            await dep.install()
            results.append({"name": dep.name, "status": "success"})
        except Exception as e:
            # Handle specific error types
            if "404" in str(e):
                print(f"Package {dep.name} not found")
                results.append({"name": dep.name, "status": "not_found", "error": str(e)})
            elif "already satisfied" in str(e):
                print(f"Package {dep.name} already installed")
                results.append({"name": dep.name, "status": "already_installed"})
            else:
                # General error handling
                print(f"Error installing {dep.name}: {e}")
                results.append({"name": dep.name, "status": "error", "error": str(e)})
                
            # Optional retry logic
            if "ConnectionError" in str(e):
                print(f"Connection error, retrying {dep.name}...")
                try:
                    await asyncio.sleep(1)  # Backoff
                    await dep.install()
                    results[-1] = {"name": dep.name, "status": "success_retry"}
                except Exception as retry_e:
                    print(f"Retry failed: {retry_e}")
    
    return results
```

### Performance Optimization

Optimize performance for larger projects:

```python
import asyncio
from mbpy.pkg.dependency import Dependency

async def optimized_installation(dependencies):
    """Optimize installation performance."""
    # Prepare all installation tasks
    tasks = []
    
    for dep in dependencies:
        # Create task but don't await it yet
        task = asyncio.create_task(dep.install())
        tasks.append((dep, task))
    
    # Wait for all tasks to complete
    for dep, task in tasks:
        try:
            await task
            print(f"Installed {dep.name}")
        except Exception as e:
            print(f"Error installing {dep.name}: {e}")
```

These best practices help ensure your dependency management is robust and maintainable. Finally, let's cover migration and compatibility information.

## 10. Migration and Compatibility

As the Dependency Management System evolves, you may need to migrate between versions or integrate with other tools.

### Upgrading from Previous Versions

When upgrading to a new version of the system:

```python
# Check current version
from mbpy import __version__
print(f"Current version: {__version__}")

# Migration from version 1.x to 2.x
if __version__.startswith("2."):
    # New dependency format (example)
    from mbpy.pkg.dependency import Dependency
    
    # In 2.x, editable is a parameter, not a flag in the string
    # Old: dep = Dependency("-e .")
    # New:
    dep = Dependency(".", editable=True)
    
    # In 2.x, Git repos use author/repo format
    # Old: dep = Dependency("git+https://github.com/user/repo.git")
    # New:
    dep = Dependency("user/repo")
```

### Compatibility with Other Tools

The system can work alongside other Python tools:

```python
# Integration with poetry
# Export dependencies to poetry format
async def export_to_poetry():
    import tomlkit
    from mbpy.pkg.dependency import Dependency
    from mbpy.pkg.mpip import get_project_deps
    
    # Get current dependencies
    deps = get_project_deps()
    
    # Create poetry pyproject.toml
    poetry_toml = tomlkit.document()
    poetry_toml["tool"] = {"poetry": {"dependencies": {}}}
    
    # Convert dependencies to poetry format
    for dep in deps:
        if isinstance(dep, str):
            dep = Dependency(dep)
        
        if dep.extras:
            extras_str = ", ".join(dep.extras)
            poetry_toml["tool"]["poetry"]["dependencies"][dep.name] = {
                "version": dep.version,
                "extras": [e.strip() for e in extras_str.split(",")]
            }
        else:
            poetry_toml["tool"]["poetry"]["dependencies"][dep.name] = dep.version
    
    # Write poetry file
    with open("poetry_pyproject.toml", "w") as f:
        f.write(tomlkit.dumps(poetry_toml))
```

### Future Development Roadmap

The Dependency Management System continues to evolve with planned enhancements:

- **Enhanced Security Features**: Vulnerability scanning integration
- **Improved Performance**: Optimized caching and parallel operations
- **Container Integration**: Support for containerized environments
- **Dependency Graph Visualization**: Interactive dependency tree exploration
- **Plugin System**: Extensibility for custom source types and operations

By staying informed about these developments, you can leverage the full capabilities of the system as it grows.

This completes our comprehensive guide to the Dependency Management System. By following the patterns and practices described here, you can effectively manage dependencies across different sources, environments, and configuration formats, creating more maintainable and robust Python projects.