from abc import ABC, abstractmethod
from typing import Dict, Any
from src.context_auditor.models import AuditInput

class BaseLLMAdapter(ABC):
    @abstractmethod
    def evaluate_context(self, audit_input: AuditInput, signals: Dict[str, Any]) -> Dict[str, Any]:
        """
        Takes the context and deterministic signals, evaluates them using an LLM,
        and returns a dictionary containing 'dimension_scores', 'findings', 
        and 'recommended_actions' matching the CEA output schema.
        """
        pass
