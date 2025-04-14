datamodel-codegen \
    --input=/Users/sebastianperalta/simply/corp/projects/mbnew/mbpy/store/schemas/pyproject.json \
    --output-model-type=pydantic_v2.BaseModel \
    --input-file-type jsonschema \
    --snake-case-field \
    --use-default-kwarg \
    --use-field-description \
    --use-union-operator \
    --use-generic-container-types \
    --field-constraints \
    --enum-field-as-literal=all \
    --output=pyproject.py \
    --use-annotated \
    --use-standard-collections \
    --collapse-root-models \
    --disable-appending-item-suffix \
    --keep-model-order \
    --reuse-model \
    --target-python-version=3.10 \
    --use-schema-description



# datamodel-codegen \
#     --snake-case-field \
#     --use-default-kwarg \
#     --use-field-description \
#     --use-union-operator \
#     --use-generic-container-types \
#     --field-constraints \
#     --enum-field-as-literal=all \
#     --output-model-type=pydantic_v2.BaseModel \
#     --url=https://json.schemastore.org/pyproject.json  \
#     --input-file-type jsonschema \
#     --output=pyproject.py \
#     --use-annotated \
#     --use-standard-collections \
#     --collapse-root-models \
#     --disable-appending-item-suffix \
#     --keep-model-order \
#     --reuse-model \
#     --target-python-version=3.10 \
#     --use-schema-description