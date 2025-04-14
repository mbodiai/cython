import json
from warnings import simplefilter

simplefilter(action="ignore", category=DeprecationWarning)
from jsonschema import validate, RefResolver

# Load the JSON schemas
from pathlib import Path

fp = Path(__file__).parent
mb = fp / "schemas" / "mb.json"
cpp = fp / "schemas" / "cpp.json"
unix = fp / "schemas" / "unix.json"
python = fp / "schemas" / "python.json"
with mb.open() as f:
    mb_schema = json.load(f)
with cpp.open() as f:
    cpp_schema = json.load(f)
with unix.open() as f:
    unix_schema = json.load(f)
with python.open() as f:
    python_schema = json.load(f)

# Create a resolver to handle dynamic references
store = {
    "mb.json": mb_schema,
    "cpp.json": cpp_schema,
    "unix.json": unix_schema,
    "python.json": python_schema,
}

resolver = RefResolver.from_schema(mb_schema, store=store)


# Define the validation logic
def validate_instance(instance, schema):
    try:
        validate(instance=instance, schema=schema, resolver=resolver)
        return "Validation successful"
    except Exception as e:
        return f"Validation error: {e}"


# Example instance to validate
instance = {
    "cpp": {
        "compiler": {
            "name": "g++",
            "version": "11.1.0",
        },
        "standard": "c++17",
        "buildOptions": {"warnings": "all", "optimization": "O3"},
    },
    "environment": {
        "PATH": "/usr/local/bin:/usr/bin:/bin",
        "HOME": "/home/user",
        "LANG": "en_US.UTF-8",
    },
    "python": {"version": "3.11", "packageManager": "pip", "virtualEnv": True},
    "project": {
        "name": "mb",
        "version": "1.0.0",
        "repository": "https://example.com/repo",
        "license": "MIT",
    },
    "build": {
        "buildDirectory": "/home/user/mb_build",
        "installDirectory": "/home/user/mb_output",
    },
}

# Validate the instance against the MB schema
result_valid = validate_instance(instance, mb_schema)

# Modify the instance to introduce an error and test validation
invalid_instance = instance.copy()
invalid_instance["python"]["version"] = "invalid_version"

result_invalid = validate_instance(invalid_instance, mb_schema)

print(result_valid)

assert result_valid == "Validation successful", (
    f"Expected {instance}, but got {result_valid}"
)

error = "Validation error: 'invalid_version' does not match"
assert result_invalid.startswith(error), f"Expected {error}, but got {result_invalid}"
