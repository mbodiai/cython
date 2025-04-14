# Data Model Code Generator Documentation

This module provides functionality for generating data models from various input formats. It includes utilities for parsing different file types and generating corresponding Python data models.

## Input File Types

The following input file types are supported:

```python
Auto = "auto"          # Automatically detect file type
OpenAPI = "openapi"    # OpenAPI specification
JsonSchema = "jsonschema"  # JSON Schema
Json = "json"          # JSON data
Yaml = "yaml"          # YAML data
Dict = "dict"          # Python dictionary
CSV = "csv"           # CSV data
GraphQL = "graphql"    # GraphQL schema
```

Raw data types that can be converted to JSON Schema:
- JSON
- YAML
- Dict
- CSV
- GraphQL

## Data Model Types

Supported output model types:

```python
class DataModelType(Enum):
    PydanticBaseModel = "pydantic.BaseModel"
    PydanticV2BaseModel = "pydantic_v2.BaseModel"
    DataclassesDataclass = "dataclasses.dataclass"
    TypingTypedDict = "typing.TypedDict"
    MsgspecStruct = "msgspec.Struct"
```

## Main Functions

### generate()

The main function for generating data models. Key parameters:

- `input_`: Source input (Path, string, URL, or mapping)
- `input_file_type`: Type of input file
- `output`: Output file path
- `output_model_type`: Target model type
- `validation`: Enable validation
- `field_constraints`: Enable field constraints
- `snake_case_field`: Convert field names to snake case
- `aliases`: Field name aliases mapping

### Error Handling

Custom exception classes:
- `Error`: Base error class
- `InvalidClassNameError`: Raised for invalid class names

### Utilities

- `get_first_file()`: Gets first file from a path
- `infer_input_type()`: Automatically detects input file type

## Examples

### Generate from JSON

```python
from datamodel_code_generator import generate, DataModelType

# Basic JSON to Pydantic model
json_data = """
{
    "name": "John Smith",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Boston"
    }
}
"""

generate(
    input_=json_data,
    input_file_type="json",
    output="person.py",
    output_model_type=DataModelType.PydanticBaseModel
)
```

### Generate from OpenAPI

```python
# Generate from OpenAPI spec with validation
generate(
    input_="api_spec.yaml",
    input_file_type="openapi",
    output="api_models.py",
    validation=True,
    field_constraints=True,
    snake_case_field=True
)
```

### Generate from CSV

```python
# Generate from CSV with custom aliases
generate(
    input_="data.csv",
    input_file_type="csv",
    output="models.py",
    aliases={"Original Name": "transformed_name"},
    snake_case_field=True
)
```

For detailed parameter descriptions and more examples, see the [official documentation](https://koxudaxi.github.io/datamodel-code-generator/).