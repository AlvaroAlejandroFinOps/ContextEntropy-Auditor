import pytest
from src.context_auditor.models import DimensionScores, OverallStatus
from src.context_auditor.scoring import compute_irc

def test_compute_irc_perfect_score():
    dimensions = DimensionScores(
        instruction_conflict=0,
        task_ambiguity=0,
        context_contamination=0,
        evidence_quality=0,
        state_integrity=0,
        redundancy_pressure=0
    )
    score, status, rules = compute_irc(dimensions, evidence_coverage=1.0)
    assert score == 0.0
    assert status == OverallStatus.STABLE
    assert len(rules) == 0

def test_compute_irc_moderate():
    dimensions = DimensionScores(
        instruction_conflict=25,
        task_ambiguity=50,
        context_contamination=25,
        evidence_quality=25,
        state_integrity=0,
        redundancy_pressure=75
    )
    score, status, rules = compute_irc(dimensions, evidence_coverage=1.0)
    # 25*0.2 + 50*0.2 + 25*0.2 + 25*0.15 + 0*0.15 + 75*0.10 = 5 + 10 + 5 + 3.75 + 0 + 7.5 = 31.25
    assert score == 31.25
    assert status == OverallStatus.MODERATE

def test_override_instruction_conflict():
    dimensions = DimensionScores(
        instruction_conflict=100, # 20 points
        task_ambiguity=0,
        context_contamination=0,
        evidence_quality=0,
        state_integrity=0,
        redundancy_pressure=0
    )
    score, status, rules = compute_irc(dimensions, evidence_coverage=1.0)
    assert score == 20.0 # Naturally this would be STABLE
    assert status == OverallStatus.HIGH # But override elevates it
    assert "critical_conflict_high_risk" in rules

def test_override_evidence_quality_factual():
    dimensions = DimensionScores(
        instruction_conflict=0,
        task_ambiguity=0,
        context_contamination=0,
        evidence_quality=100, # 15 points
        state_integrity=0,
        redundancy_pressure=0
    )
    score, status, rules = compute_irc(dimensions, evidence_coverage=1.0, task_requires_factual=True)
    assert score == 15.0
    assert status == OverallStatus.CRITICAL
    assert "critical_evidence_critical_risk" in rules

def test_override_low_coverage():
    dimensions = DimensionScores(
        instruction_conflict=0,
        task_ambiguity=0,
        context_contamination=0,
        evidence_quality=0,
        state_integrity=0,
        redundancy_pressure=0
    )
    score, status, rules = compute_irc(dimensions, evidence_coverage=0.20)
    assert score == 0.0
    assert status == OverallStatus.MODERATE
    assert "low_coverage_warning" in rules
    assert "low_coverage_prevented_stable" in rules
