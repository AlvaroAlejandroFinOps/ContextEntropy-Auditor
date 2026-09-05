import json
import os
from jsonschema import validate, ValidationError
from typing import Dict, Any

def get_schema_path(schema_filename: str) -> str:
    """Returns the absolute path to a schema file."""
    # Assuming schemas are in the root schemas/ directory
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(base_dir, "schemas", schema_filename)

def validate_input(data: Dict[str, Any]) -> None:
    """
    Validates input data against audit-input.schema.json.
    Raises jsonschema.ValidationError if invalid.
    """
    schema_path = get_schema_path("audit-input.schema.json")
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    validate(instance=data, schema=schema)

def validate_result(data: Dict[str, Any]) -> None:
    """
    Validates output data against audit-result.schema.json.
    Raises jsonschema.ValidationError if invalid.
    """
    schema_path = get_schema_path("audit-result.schema.json")
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    validate(instance=data, schema=schema)
