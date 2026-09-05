from enum import Enum
from typing import List, Dict, Any
from src.context_auditor.models import RecommendedAction

class PolicyMode(str, Enum):
    AUDIT_ONLY = "audit_only"
    RECOMMEND = "recommend"
    HUMAN_REVIEW = "human_review"
    DRY_RUN = "dry_run"

class PolicyEngine:
    def __init__(self, mode: PolicyMode = PolicyMode.RECOMMEND):
        self.mode = mode

    def process_actions(self, candidate_actions: List[RecommendedAction]) -> List[RecommendedAction]:
        """
        Filters and modifies actions based on the active policy mode.
        """
        if self.mode == PolicyMode.AUDIT_ONLY:
            return [] # No actions are allowed

        processed_actions = []
        for action in candidate_actions:
            # If in recommend mode, we can pass them through, but if they are destructive, 
            # they automatically require policy approval.
            if action.destructive:
                action.requires_policy_approval = True
                
            if self.mode == PolicyMode.HUMAN_REVIEW:
                action.requires_policy_approval = True
                
            processed_actions.append(action)
            
        return processed_actions
