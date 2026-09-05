# Context Entropy Auditor — Scoring Model

> All weights and thresholds in this document are **provisional** until calibrated against a labeled dataset.

---

## 1. Metric Name

| Language | Full Name | Abbreviation |
|----------|-----------|--------------|
| English | Context Risk Score | CRS |
| Spanish | Índice de Riesgo Contextual | IRC |

Do not use `entropy_score` as a technical metric name. The word "entropy" may appear in the brand but not in a variable that implies an undefined mathematical measurement.

---

## 2. Dimensions

CEA evaluates six dimensions in its MVP:

### 2.1 `instruction_conflict`

**Definition**: Conflict between simultaneously active instructions.

| Score | Criteria |
|-------|----------|
| 0 | No conflicting instructions detected. All active instructions are compatible. |
| 25 | Minor tension between instructions (e.g., stylistic preferences that slightly overlap) but no functional impact on task execution. |
| 50 | Moderate conflict: two instructions give contradictory guidance on a specific aspect (e.g., format, scope, tone) but the task can still be completed with reasonable interpretation. |
| 75 | High conflict: instructions produce incompatible requirements. Precedence is difficult to determine without human clarification. Task outcome is materially uncertain. |
| 100 | Confirmed failure: instructions are mutually exclusive and block task completion. Evidence shows the model followed one instruction while violating another. |

### 2.2 `task_ambiguity`

**Definition**: Absence or ambiguity of objective, scope, format, reference, or success criteria.

| Score | Criteria |
|-------|----------|
| 0 | Task is clearly defined with explicit objective, scope, format, and success criteria. |
| 25 | Minor ambiguity in one aspect (e.g., format not specified) but intent is clear from context. |
| 50 | Moderate ambiguity: multiple aspects are underspecified. The task can be interpreted in 2-3 plausible ways. |
| 75 | High ambiguity: the task objective itself is unclear. Key references are unresolved. Multiple equally plausible interpretations exist. |
| 100 | No discernible task objective. The user's intent cannot be determined from available context. |

### 2.3 `context_contamination`

**Definition**: Harmful persistence of data, objectives, rules, or constraints from previous sub-tasks that impair the current task.

| Score | Criteria |
|-------|----------|
| 0 | No evidence of previous context interfering with the current task. |
| 25 | Residual data from a previous task is present but does not observably affect the current response. |
| 50 | Previous objectives or rules are visibly influencing the current task. The response addresses aspects that are no longer relevant. |
| 75 | Strong contamination: the response applies rules, formats, or constraints from a previous task that directly conflict with the current request. |
| 100 | The response is primarily executing a previous task rather than the current one. The current user intent is effectively overridden. |

### 2.4 `evidence_quality`

**Definition**: Relevance, sufficiency, consistency, currency, and provenance of documents or fragments.

| Score | Criteria |
|-------|----------|
| 0 | All evidence is relevant, sufficient, consistent, current, and has clear provenance. |
| 25 | Minor gaps: some evidence lacks provenance metadata or is slightly dated but remains functionally adequate. |
| 50 | Moderate issues: evidence is partially relevant or inconsistent. Key claims lack supporting documents. Some fragments are of uncertain provenance. |
| 75 | High risk: evidence contradicts itself across sources. Critical claims rely on a single unverified fragment. Significant portions are outdated or irrelevant. |
| 100 | Evidence is absent, fabricated, contradictory on critical points, or entirely irrelevant to the task. Factual claims cannot be supported. |

### 2.5 `state_integrity`

**Definition**: Correct utilization of current results and state preservation in tool or agent interactions.

| Score | Criteria |
|-------|----------|
| 0 | All tool/agent results are current, correctly referenced, and state is consistent. |
| 25 | Minor staleness: one result could be refreshed but the impact is negligible. |
| 50 | Moderate drift: a tool result has been superseded by a newer one but the outdated version is still being referenced. State handoff has minor gaps. |
| 75 | High risk: decisions are based on stale or contradicted tool results. State between agent steps is inconsistent. Redundant tool calls indicate loss of tracking. |
| 100 | Critical failure: actions were taken based on an error-state tool result, or state was silently dropped between agent steps causing observable incorrect behavior. |

### 2.6 `redundancy_pressure`

**Definition**: Duplication, superseded information, dispensable traces, and observable contextual pressure.

| Score | Criteria |
|-------|----------|
| 0 | Context is lean. No significant duplication or dispensable content. |
| 25 | Minor duplication or a few dispensable traces that do not impair the response. |
| 50 | Moderate pressure: significant duplication exists. Superseded results are still present. Context could be meaningfully reduced without information loss. |
| 75 | High pressure: context is dominated by redundant or superseded content. The relevant signal is diluted. Response quality may be affected. |
| 100 | Context is overwhelmingly redundant or filled with dispensable content. The model's response shows signs of being affected by contextual noise (e.g., citing superseded data, repeating patterns from duplicated content). |

---

## 3. Renamed / Removed Dimensions

| Original (v0 Prompt) | New Name | Reason |
|---|---|---|
| `Trajectory Lock-in` | `observable_error_propagation` | The original term implied causal access to autoregressive decoding mechanics. The new name focuses on observable reuse of incorrect assumptions in subsequent decisions. |
| `Lost-in-the-Middle` | *(absorbed into `redundancy_pressure`)* | Cannot be confirmed as a causal mechanism via text analysis. Treated as a potential risk associated with contextual pressure, never as an observed causal failure. |
| `Instruction Dominance` | *(absorbed into `instruction_conflict`)* | Subsumed: over-triggering of system instructions is a form of instruction conflict. |
| `Coreference Resolution Failure` | *(absorbed into `task_ambiguity`)* | Ambiguous references are a symptom of task ambiguity, not a separate mechanistic dimension. |

---

## 4. Scoring Formula (Provisional)

```
IRC = 0.20 × instruction_conflict
    + 0.20 × task_ambiguity
    + 0.20 × context_contamination
    + 0.15 × evidence_quality
    + 0.15 × state_integrity
    + 0.10 × redundancy_pressure
```

These weights are **provisional**. They must be:
- Declared in configuration (not hardcoded).
- Versioned.
- Subject to calibration against a labeled dataset.
- Never presented as scientifically determined.

---

## 5. Overall Status Thresholds (Provisional)

| IRC Range | Status | Label (EN) | Label (ES) |
|-----------|--------|------------|------------|
| 0–24 | `stable` | Stable | Estable |
| 25–49 | `moderate` | Moderate Risk | Riesgo Moderado |
| 50–74 | `high` | High Risk | Riesgo Alto |
| 75–100 | `critical` | Critical Risk | Riesgo Crítico |

These thresholds are **provisional** until calibration is completed.

---

## 6. Override Rules

A weighted average must not conceal critical failures. The following rules override the computed status:

```
IF instruction_conflict == 100:
    minimum_status = "high"

IF state_integrity == 100:
    minimum_status = "high"

IF evidence_quality == 100 AND task requires factual claims:
    minimum_status = "critical"

IF evidence_coverage < 0.30:
    do not declare global stability without an explicit warning
```

Override rules must be:
- Configurable.
- Traceable (the output must explain which rule was triggered).
- Versioned alongside weights and thresholds.

---

## 7. The Risk–Confidence–Coverage Triple

CEA never returns an isolated score. Every audit result must include:

| Field | Definition |
|-------|-----------|
| `risk_score` | Aggregated severity of observable risks (IRC). Range: 0–100. |
| `confidence` | How well-supported the classification is by available evidence. Range: 0.0–1.0. |
| `evidence_coverage` | Proportion of the relevant conversation flow visible to the auditor. Range: 0.0–1.0. |

**Low coverage ≠ low risk.** When coverage is limited, this must be stated explicitly.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2025-09-05 | Initial scoring model. 6 dimensions, provisional weights, override rules. |
