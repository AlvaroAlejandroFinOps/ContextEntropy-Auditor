import os
import json
import pytest
from jsonschema import ValidationError
from src.context_auditor.validators import validate_input, validate_result

def get_example_path(filename: str) -> str:
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(base_dir, "examples", filename)

def test_validate_healthy_conversation_input():
    with open(get_example_path("healthy-conversation.json"), "r") as f:
        data = json.load(f)
    # Should not raise exception
    validate_input(data)

def test_validate_ambiguous_task_input():
    with open(get_example_path("ambiguous-task.json"), "r") as f:
        data = json.load(f)
    validate_input(data)

def test_validate_invalid_input():
    invalid_data = {
        "schema_version": "1.0.0"
        # Missing required 'messages'
    }
    with pytest.raises(ValidationError):
        validate_input(invalid_data)

def test_validate_invalid_role():
    invalid_data = {
        "schema_version": "1.0.0",
        "messages": [
            {
                "id": "msg-1",
                "role": "invalid_role",
                "content": "test"
            }
        ]
    }
    with pytest.raises(ValidationError):
        validate_input(invalid_data)

def test_validate_result_valid():
    valid_result = {
        "schema_version": "1.0.0",
        "audit_id": "audit-123",
        "overall_status": "stable",
        "risk_score": 15.0,
        "confidence": 0.9,
        "evidence_coverage": 1.0,
        "dimension_scores": {
            "instruction_conflict": 0,
            "task_ambiguity": 25,
            "context_contamination": 0,
            "evidence_quality": 0,
            "state_integrity": 0,
            "redundancy_pressure": 0
        },
        "findings": [
            {
                "finding_id": "f-1",
                "dimension": "task_ambiguity",
                "epistemic_status": "observed",
                "severity": 25,
                "evidence_refs": ["msg-2"],
                "explanation": "Minor ambiguity in request."
            }
        ],
        "limitations": ["No telemetry data available."]
    }
    validate_result(valid_result)

def test_validate_result_invalid_severity():
    invalid_result = {
        "schema_version": "1.0.0",
        "audit_id": "audit-123",
        "overall_status": "stable",
        "risk_score": 15.0,
        "confidence": 0.9,
        "evidence_coverage": 1.0,
        "dimension_scores": {
            "instruction_conflict": 10, # Invalid, must be 0, 25, 50, 75, 100
            "task_ambiguity": 25,
            "context_contamination": 0,
            "evidence_quality": 0,
            "state_integrity": 0,
            "redundancy_pressure": 0
        },
        "findings": [],
        "limitations": []
    }
    with pytest.raises(ValidationError):
        validate_result(invalid_result)
