from enum import Enum
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime

# --- Input Models ---

class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"

class Message(BaseModel):
    id: str
    role: Role
    content: str
    timestamp: Optional[datetime] = None

class Document(BaseModel):
    id: str
    content: str
    source: Optional[str] = None
    confidence: Optional[float] = Field(None, ge=0.0, le=1.0)

class ToolEvent(BaseModel):
    id: str
    tool_name: str
    parameters: Dict[str, Any]
    result: str
    timestamp: Optional[datetime] = None

class AuditInput(BaseModel):
    schema_version: str = "1.0.0"
    messages: List[Message]
    documents: List[Document] = Field(default_factory=list)
    tool_events: List[ToolEvent] = Field(default_factory=list)
    runtime_telemetry: Dict[str, Any] = Field(default_factory=dict)
    audit_configuration: Dict[str, Any] = Field(default_factory=dict)

# --- Output Models ---

class OverallStatus(str, Enum):
    STABLE = "stable"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"

class EpistemicStatus(str, Enum):
    OBSERVED = "observed"
    INFERRED = "inferred"
    RUNTIME_MEASURED = "runtime_measured"
    UNKNOWN = "unknown"

class AuditScope(BaseModel):
    messages_observed: Optional[int] = None
    documents_observed: Optional[int] = None
    tool_outputs_observed: Optional[int] = None

class DimensionScores(BaseModel):
    instruction_conflict: int
    task_ambiguity: int
    context_contamination: int
    evidence_quality: int
    state_integrity: int
    redundancy_pressure: int

class Finding(BaseModel):
    finding_id: str
    dimension: str
    epistemic_status: EpistemicStatus
    severity: int
    evidence_refs: List[str]
    explanation: str
    confidence: Optional[float] = Field(None, ge=0.0, le=1.0)

class RecommendedAction(BaseModel):
    action: str
    target_refs: List[str] = Field(default_factory=list)
    reason: str
    requires_policy_approval: bool
    destructive: bool

class AuditResult(BaseModel):
    schema_version: str = "1.0.0"
    audit_version: Optional[str] = None
    audit_id: str
    overall_status: OverallStatus
    risk_score: float = Field(..., ge=0.0, le=100.0)
    confidence: float = Field(..., ge=0.0, le=1.0)
    evidence_coverage: float = Field(..., ge=0.0, le=1.0)
    scope: Optional[AuditScope] = None
    dimension_scores: DimensionScores
    findings: List[Finding]
    recommended_actions: List[RecommendedAction] = Field(default_factory=list)
    triggered_rules: List[str] = Field(default_factory=list)
    limitations: List[str]
