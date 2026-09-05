import pytest
from src.context_auditor.models import RecommendedAction
from src.context_auditor.policies import PolicyEngine, PolicyMode

def test_policy_audit_only():
    engine = PolicyEngine(mode=PolicyMode.AUDIT_ONLY)
    actions = [
        RecommendedAction(action="summarize", reason="too long", requires_policy_approval=False, destructive=False)
    ]
    processed = engine.process_actions(actions)
    assert len(processed) == 0

def test_policy_recommend():
    engine = PolicyEngine(mode=PolicyMode.RECOMMEND)
    actions = [
        RecommendedAction(action="summarize", reason="too long", requires_policy_approval=False, destructive=False),
        RecommendedAction(action="delete", reason="stale", requires_policy_approval=False, destructive=True)
    ]
    processed = engine.process_actions(actions)
    assert len(processed) == 2
    assert processed[0].requires_policy_approval == False
    assert processed[1].requires_policy_approval == True # Destructive actions automatically require approval

def test_policy_human_review():
    engine = PolicyEngine(mode=PolicyMode.HUMAN_REVIEW)
    actions = [
        RecommendedAction(action="summarize", reason="too long", requires_policy_approval=False, destructive=False)
    ]
    processed = engine.process_actions(actions)
    assert len(processed) == 1
    assert processed[0].requires_policy_approval == True # Human review forces approval on all
