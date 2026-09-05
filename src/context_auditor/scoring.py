import os
import yaml
from typing import Dict, Any, Tuple
from src.context_auditor.models import DimensionScores, OverallStatus

def load_scoring_config() -> Dict[str, Any]:
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config_path = os.path.join(base_dir, "config", "scoring_defaults.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def compute_base_status(score: float, thresholds: Dict[str, float]) -> OverallStatus:
    if score <= thresholds["stable"]:
        return OverallStatus.STABLE
    elif score <= thresholds["moderate"]:
        return OverallStatus.MODERATE
    elif score <= thresholds["high"]:
        return OverallStatus.HIGH
    else:
        return OverallStatus.CRITICAL

def compute_irc(
    dimensions: DimensionScores, 
    evidence_coverage: float, 
    task_requires_factual: bool = False
) -> Tuple[float, OverallStatus, list[str]]:
    
    config = load_scoring_config()
    weights = config["weights"]
    
    # 1. Compute base score
    raw_score = (
        dimensions.instruction_conflict * weights["instruction_conflict"] +
        dimensions.task_ambiguity * weights["task_ambiguity"] +
        dimensions.context_contamination * weights["context_contamination"] +
        dimensions.evidence_quality * weights["evidence_quality"] +
        dimensions.state_integrity * weights["state_integrity"] +
        dimensions.redundancy_pressure * weights["redundancy_pressure"]
    )
    
    # 2. Determine base status
    status = compute_base_status(raw_score, config["thresholds"])
    triggered_rules = []

    # 3. Apply override rules
    rules = config.get("override_rules", {})
    
    # Rule: Critical Conflict
    if dimensions.instruction_conflict == 100:
        if status in [OverallStatus.STABLE, OverallStatus.MODERATE]:
            status = OverallStatus.HIGH
            triggered_rules.append("critical_conflict_high_risk")

    # Rule: Critical State Integrity
    if dimensions.state_integrity == 100:
        if status in [OverallStatus.STABLE, OverallStatus.MODERATE]:
            status = OverallStatus.HIGH
            triggered_rules.append("critical_state_high_risk")

    # Rule: Critical Evidence Quality on Factual Tasks
    if dimensions.evidence_quality == 100 and task_requires_factual:
        status = OverallStatus.CRITICAL
        triggered_rules.append("critical_evidence_critical_risk")

    # Rule: Low Coverage Warning
    if evidence_coverage < 0.30:
        triggered_rules.append("low_coverage_warning")
        # Ensure we don't declare stability blindly
        if status == OverallStatus.STABLE:
            triggered_rules.append("low_coverage_prevented_stable")
            status = OverallStatus.MODERATE

    return round(raw_score, 2), status, triggered_rules
