from typing import Dict, Any
from src.context_auditor.models import AuditInput
from src.context_auditor.validators import validate_input

def normalize_input(raw_data: Dict[str, Any]) -> AuditInput:
    """
    Validates the raw dictionary against the JSON schema and converts it 
    into a strongly typed AuditInput Pydantic model.
    """
    # 1. Schema Validation (Raises ValidationError if invalid)
    validate_input(raw_data)
    
    # 2. Pydantic Parsing (Raises ValidationError if types don't match)
    return AuditInput(**raw_data)
