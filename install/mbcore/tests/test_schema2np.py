import tempfile

import numpy as np
import pytest


@pytest.skip("skipping schema2np tests", allow_module_level=True)
@pytest.fixture
def simple_schema():
    return {
        "type": "object",
        "properties": {"id": {"type": "integer"}, "name": {"type": "string"}, "value": {"type": "number"}},
    }


@pytest.fixture
def complex_schema():
    return {
        "wrapped": {
            "type": "array",
            "items": {
                "__key__": {"type": "str"},
                "__url__": {"type": "str"},
                "data.pickle": {
                    "type": "object",
                    "properties": {
                        "image_list": {"type": "array", "items": {"type": "str"}},
                        "steps": {
                            "type": "array",
                            "items": {
                                "action": {
                                    "type": "object",
                                    "properties": {
                                        "actions": {"type": "array", "items": {"type": "float"}},
                                        "rel_actions_gripper": {"type": "array", "items": {"type": "float"}},
                                        "rel_actions_world": {"type": "array", "items": {"type": "float"}},
                                        "terminate_episode": {"type": "float"},
                                    },
                                },
                                "is_first": {"type": "bool"},
                                "is_last": {"type": "bool"},
                                "is_terminal": {"type": "bool"},
                                "observation": {
                                    "type": "object",
                                    "properties": {
                                        "depth_gripper": {
                                            "type": "object",
                                            "properties": {
                                                "bytes": {"type": "bytes"},
                                                "path": {"type": "NoneType"},
                                            },
                                        },
                                        "depth_static": {
                                            "type": "object",
                                            "properties": {
                                                "bytes": {"type": "bytes"},
                                                "path": {"type": "NoneType"},
                                            },
                                        },
                                        "natural_language_embedding": {"type": "array", "items": {"type": "float"}},
                                        "natural_language_instruction": {"type": "str"},
                                        "rgb_gripper": {
                                            "type": "object",
                                            "properties": {
                                                "bytes": {"type": "bytes"},
                                                "path": {"type": "NoneType"},
                                            },
                                        },
                                        "rgb_static": {
                                            "type": "object",
                                            "properties": {
                                                "bytes": {"type": "bytes"},
                                                "path": {"type": "NoneType"},
                                            },
                                        },
                                        "robot_obs": {"type": "array", "items": {"type": "float"}},
                                        "structured_language_instruction": {"type": "str"},
                                    },
                                },
                                "reward": {"type": "float"},
                            },
                        },
                    },
                },
            },
        },
    }


@pytest.fixture
def sample_data():
    return [{"id": 1, "name": "test1", "value": 1.1}, {"id": 2, "name": "test2", "value": 2.2}]


def test_schema_array_init(simple_schema):
    # Test initialization without file path
    sa = SchemaArray(simple_schema)
    assert sa.schema == simple_schema
    assert sa.file_path is None
    assert sa._array is None

    # Test initialization with file path
    with tempfile.NamedTemporaryFile() as tf:
        sa = SchemaArray(simple_schema, tf.name)
        assert sa.file_path == tf.name


def test_schema_array_create(simple_schema):
    sa = SchemaArray(simple_schema)

    # Test creating array with default shape
    arr = sa.create()
    assert isinstance(arr, np.recarray)
    assert len(arr) == 0

    # Test creating array with specific shape
    arr = sa.create(2)
    assert len(arr) == 2

    # Test memory mapping
    with tempfile.NamedTemporaryFile() as tf:
        sa = SchemaArray(simple_schema, tf.name)
        arr = sa.create(2)
        assert isinstance(arr, np.recarray)
        assert isinstance(sa._array, np.memmap)


def test_schema_array_from_json(simple_schema, sample_data):
    sa = SchemaArray(simple_schema)
    arr = sa.from_json(sample_data)

    assert len(arr) == 2
    assert arr[0].id == 1
    assert arr[0].name == "test1"
    assert arr[0].value == 1.1
    assert arr[1].id == 2
    assert arr[1].name == "test2"
    assert arr[1].value == 2.2


def test_schema_array_save_load(simple_schema, sample_data):
    with tempfile.NamedTemporaryFile() as tf:
        # Create and save array
        sa1 = SchemaArray(simple_schema)
        arr1 = sa1.from_json(sample_data)
        sa1.save(tf.name)

        # Load array in new SchemaArray instance
        sa2 = SchemaArray(simple_schema)
        arr2 = np.load(tf.name, allow_pickle=True).view(np.recarray)

        # Verify data matches
        np.testing.assert_array_equal(arr1, arr2)


def test_schema_array_memmap(simple_schema, sample_data):
    with tempfile.NamedTemporaryFile() as tf:
        # Create memory-mapped array
        sa = SchemaArray(simple_schema, tf.name)
        arr = sa.create(len(sample_data))

        # Populate data
        for i, item in enumerate(sample_data):
            arr[i].id = item["id"]
            arr[i].name = item["name"]
            arr[i].value = item["value"]

        # Flush changes
        sa.save()

        # Load and verify
        sa2 = SchemaArray(simple_schema, tf.name)
        arr2 = sa2.load()
        np.testing.assert_array_equal(arr, arr2)


def test_schema_array_property(simple_schema, sample_data):
    sa = SchemaArray(simple_schema)

    # Test array property creates new array
    arr1 = sa.array
    assert isinstance(arr1, np.recarray)
    assert len(arr1) == 0

    # Test array property returns existing array
    arr2 = sa.array
    assert arr1 is arr2

    # Test with file path
    with tempfile.NamedTemporaryFile() as tf:
        sa = SchemaArray(simple_schema, tf.name)
        arr1 = sa.from_json(sample_data)
        sa.save()

        # New instance should load existing file
        sa2 = SchemaArray(simple_schema, tf.name)
        arr2 = sa2.array
        np.testing.assert_array_equal(arr1, arr2)


def test_schema_array_errors(simple_schema):
    sa = SchemaArray(simple_schema)

    # Test save without array
    with pytest.raises(ValueError, match="No array has been created or loaded"):
        sa.save("test.npy")

    # Test save without file path
    sa.create(1)
    with pytest.raises(ValueError, match="No file path specified"):
        sa.save()

    # Test load without file path
    with pytest.raises(ValueError, match="No file path specified"):
        sa.load()


if __name__ == "__main__":
    pytest.main([__file__])
