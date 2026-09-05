# Context Entropy Auditor — Roadmap

> An evidence-based context reliability framework for LLM applications.

All weights, thresholds, and calibration claims are **provisional** until validated.

---

## Release Plan

| Version | Name | Status | Description |
|---------|------|--------|-------------|
| `v0.1-alpha` | Prompt Core | ⏳ Planned | Revised prompt, methodology, scoring model, epistemic contract. |
| `v0.2-alpha` | Schemas & Models | ⏳ Planned | JSON Schemas for input/output, typed models, validators, 5 examples. |
| `v0.3-beta` | Scoring Engine | ⏳ Planned | Reproducible scoring engine, policy modes, override rules. |
| `v0.4-beta` | Deterministic Signals | ⏳ Planned | Input normalizers, signal extractors, fixtures. |
| `v0.5-public` | SDK & CLI | ⏳ Planned | Python SDK, CLI (`inspect`, `validate`, `compare`), Gemini adapter. |
| `v0.6` | Dataset & Evaluation | ⏳ Planned | 30-50 labeled cases, evaluation metrics, adversarial tests. |
| `v0.7` | Public Repository | ⏳ Planned | LICENSE, CONTRIBUTING, SECURITY, CI/CD, release notes. |
| `v0.8` | RAG Auditor | 🔮 Future | RAG pipeline evaluation: retrieval, reranking, grounding, citation quality. |
| `v0.9` | Agentic State Auditor | 🔮 Future | Multi-step agent state evaluation, tool chain integrity. |
| `v1.0` | Stable Release | 🔮 Future | Stable schema, calibrated scoring, multi-vendor support, bilinugal documentation. |

---

## What Is NOT on the Near-Term Roadmap

These capabilities are explicitly deferred:

- **`auto_recover` policy mode** — Disabled by default until safety is demonstrated.
- **Organizational mode** — Corporate policies, tenancy, permissions.
- **Adaptive routing** — Automatic model escalation.
- **Adaptive compaction** — Automatic context reduction.
- **Advanced telemetry** — KV Cache metrics, attention analysis.
- **Dashboard / UI** — Visualization interface.
- **Multi-vendor integrations** — Beyond initial Gemini adapter.

---

## Principles

1. **Publish methodological rigor before functional breadth.**
2. **Every metric is provisional until calibrated against labeled data.**
3. **No destructive action without policy approval.**
4. **"Entropy" is a brand metaphor, not a mathematical claim.**

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2025-09-05 | Initial roadmap. |
