import tempfile
import unittest
from pathlib import Path

# Import the dependency graph builder
from mbpy.pkg.graph import _build_dependency_graph


# Create a wrapper function to adapt the interface
def to_graph(files_list):
    """Wrapper to adapt _build_dependency_graph to work with lists of files
    instead of a directory path.

    Args:
        files_list: List of Path objects

    Returns:
        Dictionary mapping module names to their dependencies

    """
    if not files_list:
        return {}

    # Use the parent directory of the first file as the base directory
    if files_list:
        base_dir = files_list[0].parent
    else:
        return {}

    # Get a graph for the entire directory
    full_graph = _build_dependency_graph(base_dir)

    # Filter to only include the files in our list
    result = {}
    file_names = [f.name for f in files_list]

    for name in file_names:
        if name in full_graph:
            # Only include dependencies that are in our file list
            dependencies = [dep for dep in full_graph[name] if Path(dep).name in file_names]
            result[name] = dependencies

    return result


class TestToGraph(unittest.TestCase):
    def setUp(self):
        # Create temporary directory
        self.temp_dir = tempfile.mkdtemp()

        # Create test modules
        self.module_a = Path(self.temp_dir) / "module_a.py"
        self.module_b = Path(self.temp_dir) / "module_b.py"
        self.module_c = Path(self.temp_dir) / "module_c.py"

        # Write test content
        self.module_a.write_text("import module_b\nfrom module_c import func")
        self.module_b.write_text("import module_c")
        self.module_c.write_text("# Empty module")

        self.modules = [self.module_a, self.module_b, self.module_c]

    def tearDown(self):
        # Clean up temporary files
        for module in self.modules:
            if module.exists():
                module.unlink()
        if Path(self.temp_dir).exists():
            Path(self.temp_dir).rmdir()

    def test_empty_modules_list(self):
        """Test graph creation with empty modules list"""
        graph = to_graph([])
        self.assertEqual(graph, {})

    def test_module_with_no_dependencies(self):
        """Test graph creation with module having no dependencies"""
        graph = to_graph([self.module_c])
        self.assertEqual(graph, {self.module_c.name: []})

    def test_module_with_single_dependency(self):
        """Test graph creation with module having one dependency"""
        graph = to_graph([self.module_b])
        expected = {self.module_b.name: [Path("module_c.py")]}
        self.assertEqual(graph, expected)

    def test_module_with_multiple_dependencies(self):
        """Test graph creation with module having multiple dependencies"""
        graph = to_graph([self.module_a])
        expected = {self.module_a.name: [Path("module_b.py"), Path("module_c.py")]}
        self.assertEqual(graph, expected)

    def test_multiple_modules(self):
        """Test graph creation with multiple modules"""
        graph = to_graph(self.modules)
        expected = {
            self.module_a.name: [Path("module_b.py"), Path("module_c.py")],
            self.module_b.name: [Path("module_c.py")],
            self.module_c.name: [],
        }
        self.assertEqual(graph, expected)

    def test_nonexistent_dependency(self):
        """Test graph creation with nonexistent dependency"""
        module = Path(self.temp_dir) / "test_module.py"
        module.write_text("import nonexistent_module")
        try:
            graph = to_graph([module])
            self.assertEqual(graph, {module.name: []})
        finally:
            module.unlink()


if __name__ == "__main__":
    unittest.main()
