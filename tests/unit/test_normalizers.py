import pytest
from src.context_auditor.normalizers import normalize_input
from pydantic import ValidationError as PydanticValidationError
from jsonschema import ValidationError as JsonSchemaValidationError

def test_normalize_valid_input():
    raw_data = {
        "schema_version": "1.0.0",
        "messages": [
            {"id": "1", "role": "user", "content": "hello"}
        ]
    }
    audit_input = normalize_input(raw_data)
    assert len(audit_input.messages) == 1
    assert audit_input.messages[0].role == "user"

def test_normalize_invalid_schema():
    raw_data = {
        "schema_version": "1.0.0"
        # missing messages
    }
    with pytest.raises(JsonSchemaValidationError):
        normalize_input(raw_data)
