# Context Entropy Auditor — Methodology

> An evidence-based context reliability framework for LLM applications.
> Un framework de confiabilidad contextual basado en evidencia para aplicaciones con modelos de lenguaje.

---

## 1. Purpose

Context Entropy Auditor (CEA) examines the context available to a language model interaction, identifies observable risks, links every diagnostic finding to evidence, quantifies risk, confidence and coverage, and delivers recommendations that people or systems can apply in a controlled manner.

The system answers questions such as:

- Is the current task sufficiently defined?
- Are there incompatible active instructions?
- Do previous data, objectives or constraints persist and harm the current task?
- Do incorporated documents provide relevant, sufficient and traceable evidence?
- Are tool results still current?
- Is there avoidable redundancy, contradiction or contextual pressure?
- Should the conversation continue, request clarification, compact, selectively reconstruct context, escalate, or route to human review?
- What observable evidence supports each finding?

---

## 2. Epistemic Contract

Every diagnostic assertion produced by CEA must be classified into exactly one of these categories:

| Status | Definition | Example |
|--------|-----------|---------|
| `observed` | Appears directly in messages, documents, metadata, or visible events. | "Message msg_12 contradicts instruction in system_prompt line 4." |
| `inferred` | Plausible explanation supported by observable evidence. Must cite the evidence. | "The task likely shifted at turn 8 based on the change in user vocabulary and references." |
| `runtime_measured` | Comes from external telemetry supplied by the runtime (e.g., token counts from the provider API). | "Token usage reported by API: 127,400 / 128,000." |
| `unknown` | Available information is insufficient to determine. | "Evidence coverage is 0.35; cannot assess state_integrity with confidence." |

### Rules

1. Every finding must include `evidence_refs` — stable references to elements in the normalized input.
2. Every inference must include a `confidence` score and cite the evidence that supports it.
3. If evidence is insufficient, return `unknown` or do not generate the finding. **Never fill gaps with invented mechanistic explanations.**
4. Citations must reference stable IDs present in the normalized input.
5. Severity values must belong to the allowed rubric set (`0`, `25`, `50`, `75`, `100`).

---

## 3. What CEA Does NOT Claim

The project must never assert that it:

- Observes attention weights or attention heads.
- Inspects logits, activations, or residual streams.
- Directly measures neural degradation.
- Detects the physical state of the KV Cache through text analysis.
- Demonstrates internal causal mechanisms of the model.
- Measures mathematical entropy of the context or the model, unless a formal, independently defined metric exists in the future.
- Can purge the KV Cache via a prompt.
- Can guarantee by itself the safety or correctness of an application.

If the runtime provides authorized external telemetry, CEA may report it as a **runtime measurement**, clearly separated from observations and semantic inferences.

---

## 4. Separation of Responsibilities

CEA strictly separates its processing into six layers:

```
┌─────────────────────────────────────────────┐
│  1. Normalization                           │
│     Transform heterogeneous inputs into     │
│     a common model.                         │
├─────────────────────────────────────────────┤
│  2. Deterministic Signals                   │
│     Compute verifiable facts without an LLM.│
├─────────────────────────────────────────────┤
│  3. Semantic Evaluation                     │
│     Analyze ambiguity, relevance, conflict, │
│     coherence via LLM.                      │
├─────────────────────────────────────────────┤
│  4. Scoring                                 │
│     Compute reproducible scores.            │
├─────────────────────────────────────────────┤
│  5. Policies                                │
│     Decide which actions are permitted.     │
├─────────────────────────────────────────────┤
│  6. Presentation                            │
│     Adapt output for people or integrations.│
└─────────────────────────────────────────────┘
```

**The evaluator recommends. The policy engine decides.** No probabilistic output may directly execute a destructive action.

---

## 5. Audited Content Is Untrusted Data

All content under audit — messages, documents, tool results, RAG fragments — must be treated as untrusted data. The evaluator must not obey instructions embedded in audited content. The boundary between auditor instructions and audited content must always be explicit.

---

## 6. Capabilities and Non-Capabilities

### What CEA can do

- Identify observable risks in the available context.
- Quantify risk, confidence and evidence coverage per dimension.
- Reference specific evidence for each finding.
- Recommend controlled actions (continue, clarify, summarize, reconstruct, escalate).
- Operate in manual (prompt), programmatic (SDK/CLI), and organizational modes.
- Validate outputs against versioned schemas.
- Compare audits across runs.

### What CEA cannot do

- Access model internals (weights, attention, logits, KV Cache state).
- Guarantee absence of hallucination or error.
- Replace human judgment for safety-critical decisions.
- Automatically execute destructive actions without policy approval.
- Measure mathematical entropy of text or model states.

---

## 7. Metaphorical Use of "Entropy"

The term "entropy" in the project name **Context Entropy Auditor** is an operational metaphor. It refers to observable disorder, noise, and degradation in the context — not to Shannon entropy, thermodynamic entropy, or any formal information-theoretic measure.

This distinction must be stated in the README, methodology documentation, and any public-facing material.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2025-09-05 | Initial methodology document. Derived from master plan §1-§3. |
