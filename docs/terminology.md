# Context Entropy Auditor — Terminology / Terminología

Bilingual glossary of key terms used across the project.
Glosario bilingüe de términos clave utilizados en el proyecto.

---

## Core Concepts / Conceptos Fundamentales

| English | Spanish | Definition |
|---------|---------|-----------|
| Context Entropy Auditor (CEA) | Auditor de Entropía Contextual | The project and framework. "Entropy" is used as an operational metaphor, not a mathematical measure. |
| Context Risk Score (CRS) | Índice de Riesgo Contextual (IRC) | The aggregated risk score computed from all dimension scores. Range: 0–100. Provisional until calibrated. |
| Epistemic Contract | Contrato Epistémico | The binding agreement that every finding must be classified as `observed`, `inferred`, `runtime_measured`, or `unknown`. |
| Evidence Coverage | Cobertura de Evidencia | The proportion of the relevant conversation flow visible to the auditor. Range: 0.0–1.0. |
| Confidence | Confianza | How well-supported the classification is by available evidence. Range: 0.0–1.0. |

---

## Epistemic Categories / Categorías Epistémicas

| English | Spanish | Definition |
|---------|---------|-----------|
| Observed | Observado | Appears directly in messages, documents, metadata, or visible events. |
| Inferred | Inferido | Plausible explanation supported by observable evidence. Must cite evidence and include confidence. |
| Runtime Measured | Medición del Runtime | Data supplied by external telemetry from the runtime (e.g., provider API token counts). |
| Unknown | Desconocido | Available information is insufficient to determine. |

---

## Dimensions / Dimensiones

| English | Spanish | Abbreviation |
|---------|---------|-------------|
| Instruction Conflict | Conflicto de Instrucciones | `instruction_conflict` |
| Task Ambiguity | Ambigüedad de Tarea | `task_ambiguity` |
| Context Contamination | Contaminación Contextual | `context_contamination` |
| Evidence Quality | Calidad de Evidencia | `evidence_quality` |
| State Integrity | Integridad del Estado | `state_integrity` |
| Redundancy Pressure | Presión de Redundancia | `redundancy_pressure` |

---

## Scoring / Puntuación

| English | Spanish | Definition |
|---------|---------|-----------|
| Dimension Score | Puntuación por Dimensión | Risk score for a single dimension. Values: 0, 25, 50, 75, 100. |
| Override Rule | Regla de Sobrescritura | A rule that elevates the overall status when a critical threshold is reached, regardless of the weighted average. |
| Overall Status | Estado General | The final risk classification: stable / moderate / high / critical. |
| Provisional | Provisional | Label applied to weights, thresholds, and calibration status until validated against a labeled dataset. |

---

## Severity Scale / Escala de Severidad

| Value | English | Spanish |
|-------|---------|---------|
| 0 | No evidence of risk | Sin evidencia de riesgo |
| 25 | Weak or localized signal, no visible relevant impact | Señal débil o localizada, sin impacto visible relevante |
| 50 | Moderate risk, possible or partial impact | Riesgo moderado, con impacto posible o parcial |
| 75 | High risk, visible impact or hard-to-determine precedence | Riesgo alto, con impacto visible o precedencia difícil de determinar |
| 100 | Confirmed failure, task blocked or result materially affected | Fallo confirmado, bloqueo de la tarea o resultado materialmente afectado |

---

## Architecture / Arquitectura

| English | Spanish | Definition |
|---------|---------|-----------|
| Normalizer | Normalizador | Transforms heterogeneous inputs (messages, documents, tool events) into a common model. |
| Deterministic Signals | Señales Deterministas | Verifiable facts computed without an LLM (token counts, duplication, ID checks). |
| Semantic Evaluator | Evaluador Semántico | LLM-powered analysis of ambiguity, conflict, relevance, and coherence. |
| Scoring Engine | Motor de Puntuación | Computes reproducible scores from dimension evaluations. |
| Policy Engine | Motor de Políticas | Converts recommendations into controlled decisions according to the active mode. |
| Presenter | Presentador | Adapts the canonical result for different audiences (human, Markdown, JSON, CLI). |

---

## Policy Modes / Modos de Política

| Mode | Spanish | Definition |
|------|---------|-----------|
| `audit_only` | Solo auditoría | Diagnose and report. No actions executed. |
| `recommend` | Recomendar | Diagnose and propose actions. No automatic execution. |
| `human_review` | Revisión humana | Require human approval for selected actions. |
| `dry_run` | Simulación | Simulate the policy and log what would have happened. |
| `auto_recover` | Recuperación automática | *Reserved for a future phase. Disabled by default.* |

---

## Actions / Acciones

| English | Spanish | Definition |
|---------|---------|-----------|
| Continue | Continuar | Proceed with the current context. |
| Request Clarification | Solicitar Aclaración | Ask the user to disambiguate the task. |
| Reinforce Task Anchor | Reforzar Ancla de Tarea | Re-state the current objective to counteract contamination. |
| Summarize | Resumir | Compress specific elements to reduce contextual pressure. |
| Mark Superseded | Marcar como Reemplazado | Flag elements that have been replaced by newer versions. |
| Selective Context Reconstruction | Reconstrucción Selectiva del Contexto | Rebuild context preserving only essential state and evidence. |
| Retrieve Additional Evidence | Recuperar Evidencia Adicional | Fetch missing documents or data to improve coverage. |
| Route to Human Review | Enviar a Revisión Humana | Escalate to a human decision-maker. |
| Escalate Model | Escalar Modelo | Recommend switching to a more capable model (recommendation only). |

---

## Deprecated Terms / Términos Deprecados

| Deprecated Term | Replaced By | Reason |
|----------------|-------------|--------|
| `Trajectory Lock-in` | `observable_error_propagation` | Implied causal access to autoregressive decoding. |
| `Lost-in-the-Middle` | Absorbed into `redundancy_pressure` | Cannot be confirmed as a mechanism via text analysis. |
| `entropy_score` | `risk_score` / IRC / CRS | Implied mathematical entropy measurement. |
| `Conversational Attractor` | *(Descriptive language in findings)* | Mechanistic metaphor; use observable descriptions instead. |
| `Semantic Reset` | `Selective Context Reconstruction` | "Reset" implies KV Cache purging capability. |
| `RSD (Ratio de Señal-a-Distractor)` | *(Integrated into `redundancy_pressure`)* | Informal metric; formalized within the redundancy dimension. |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2025-09-05 | Initial glossary. 60+ terms across 9 categories. |
