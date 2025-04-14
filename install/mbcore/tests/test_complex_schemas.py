
import numpy as np
import pytest

pytest.skip("skipping test_complex_schemas", allow_module_level=True)


@pytest.fixture
def complex_schema():
    return {
        "type": "object",
        "properties": {
            "person": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "maxLength": 50},
                    "age": {"type": "integer", "minimum": 0},
                    "address": {
                        "type": "object",
                        "properties": {
                            "street": {"type": "string"},
                            "city": {"type": "string"},
                            "coordinates": {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2},
                        },
                    },
                    "hobbies": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {"name": {"type": "string"}, "years": {"type": "integer"}},
                        },
                    },
                },
            },
            "metadata": {"type": "object", "patternProperties": {"^[a-z]+$": {"type": "string"}}},
        },
    }


@pytest.fixture
def test_data():
    return [
        {
            "person": {
                "name": "Alice",
                "age": 30,
                "address": {"street": "123 Main St", "city": "Techville", "coordinates": [34.0522, -118.2437]},
                "hobbies": [{"name": "Programming", "years": 10}, {"name": "Hiking", "years": 5}],
            },
            "metadata": {"version": "1.0", "status": "active"},
        },
    ]


def test_complex_schema_handling(tmp_path, complex_schema, test_data):
    # Setup paths
    file_path = tmp_path / "complex_array.npy"

    # Initialize SchemaArray
    sa = SchemaArray(complex_schema, file_path=file_path)

    # Test creation from JSON
    sa.from_json(test_data)

    # Verify array structure
    assert sa.array.shape == (1,), "Array should have 1 entry"
    person_dtype = sa.dtype["person"]
    assert person_dtype.names == ("name", "age", "address", "hobbies"), "Person dtype mismatch"

    # Verify nested structure
    address_dtype = person_dtype["address"]
    assert address_dtype.names == ("street", "city", "coordinates"), "Address dtype mismatch"
    assert address_dtype["coordinates"].shape == (2,), "Coordinates should be fixed-size array"

    # Test object array handling - check item structure directly
    entry = sa.array[0]
    hobby = entry["person"]["hobbies"][0]

    # Verify hobbies are structured with correct fields
    assert hasattr(hobby, "dtype"), "Hobby should be a structured type"
    assert "name" in hobby.dtype.names, "Hobby missing name field"
    assert "years" in hobby.dtype.names, "Hobby missing years field"

    # Verify array content
    assert hobby["name"] == "Programming", "Hobby name mismatch"
    assert hobby["years"] == 10, "Hobby years mismatch"

    # Verify array length
    assert len(entry["person"]["hobbies"]) == 2, "Hobbies array length mismatch"

    # Test save/load cycle
    sa.save()
    sa_loaded = SchemaArray(complex_schema, file_path=file_path)
    sa_loaded.load()

    # Verify loaded data
    loaded_entry = sa_loaded.array[0]
    assert loaded_entry["person"]["name"] == "Alice", "Loaded name mismatch"
    assert np.allclose(loaded_entry["person"]["address"]["coordinates"], [34.0522, -118.2437], atol=1e-4), (
        "Coordinates mismatch"
    )

    # Verify memory mapping
    if sa._can_mmap:
        assert isinstance(sa_loaded._array, np.memmap), "Should be memory-mapped"
    else:
        assert isinstance(sa_loaded._array, np.recarray), "Should be regular array"


def test_pattern_properties(complex_schema, test_data):
    sa = SchemaArray(complex_schema)
    sa.from_json(test_data)

    # Get metadata field dtype
    metadata_dtype = sa.dtype["metadata"]

    # Add null check before iteration
    assert metadata_dtype.names is not None, "Metadata should be structured type"
    pattern_fields = [name for name in metadata_dtype.names if name.startswith("_pattern_")]
    assert len(pattern_fields) == 1, "Should have one pattern property field"

    # Verify pattern data storage
    entry = sa.array[0]
    pattern_data = entry["metadata"][pattern_fields[0]]
    assert pattern_data["version"] == "1.0", "Pattern property value mismatch"
    assert pattern_data["status"] == "active", "Pattern property value mismatch"
