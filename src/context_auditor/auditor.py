import uuid
from typing import Dict, Any, Optional
from src.context_auditor.models import AuditInput, AuditResult, AuditScope, DimensionScores, Finding, RecommendedAction
from src.context_auditor.normalizers import normalize_input
from src.context_auditor.signals import extract_deterministic_signals
from src.context_auditor.scoring import compute_irc
from src.context_auditor.policies import PolicyEngine, PolicyMode
from src.context_auditor.adapters.base import BaseLLMAdapter
from src.context_auditor.validators import validate_result

class ContextAuditor:
    def __init__(self, llm_adapter: BaseLLMAdapter, policy_mode: PolicyMode = PolicyMode.RECOMMEND):
        self.llm_adapter = llm_adapter
        self.policy_engine = PolicyEngine(mode=policy_mode)
        
    def audit(self, raw_input: Dict[str, Any], task_requires_factual: bool = False) -> AuditResult:
        # 1. Normalize and parse input
        audit_input = normalize_input(raw_input)
        
        # 2. Extract deterministic signals
        signals = extract_deterministic_signals(audit_input)
        
        # 3. Ask LLM adapter to evaluate semantics based on context and signals
        llm_eval = self.llm_adapter.evaluate_context(audit_input, signals)
        
        # 4. Parse LLM responses into models
        dim_scores = DimensionScores(**llm_eval.get("dimension_scores", {}))
        confidence = llm_eval.get("confidence", 0.0)
        coverage = llm_eval.get("evidence_coverage", 0.0)
        
        # 5. Compute Risk Score (IRC) and Overall Status
        risk_score, overall_status, triggered_rules = compute_irc(
            dimensions=dim_scores,
            evidence_coverage=coverage,
            task_requires_factual=task_requires_factual
        )
        
        # 6. Apply Policies to Recommended Actions
        raw_actions = [RecommendedAction(**act) for act in llm_eval.get("recommended_actions", [])]
        filtered_actions = self.policy_engine.process_actions(raw_actions)
        
        findings = [Finding(**f) for f in llm_eval.get("findings", [])]
        
        # 7. Assemble final Audit Result
        result = AuditResult(
            schema_version="1.0.0",
            audit_version="0.1.0",
            audit_id=f"audit-{uuid.uuid4().hex[:8]}",
            overall_status=overall_status,
            risk_score=risk_score,
            confidence=confidence,
            evidence_coverage=coverage,
            scope=AuditScope(
                messages_observed=signals.get("message_count"),
                documents_observed=signals.get("document_count"),
                tool_outputs_observed=len(audit_input.tool_events)
            ),
            dimension_scores=dim_scores,
            findings=findings,
            recommended_actions=filtered_actions,
            triggered_rules=triggered_rules,
            limitations=llm_eval.get("limitations", [])
        )
        
        # Validate output matches schema
        validate_result(result.model_dump())
        
        return result
