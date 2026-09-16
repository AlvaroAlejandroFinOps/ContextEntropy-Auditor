# CEA: Context Entropy Auditor

**Language:** [English](README.md) | [Español](README_ES.md)

[![Python](https://img.shields.io/badge/Python-3.9%2B-2b2b2b?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2.0%2B-1a1a1a?style=flat-square)](https://docs.pydantic.dev/)
[![JSON Schema](https://img.shields.io/badge/JSON%20Schema-Draft--07-34495e?style=flat-square)](https://json-schema.org/)
[![License](https://img.shields.io/badge/License-MIT-4b5563?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-v0.5.0--Public-2b2b2b?style=flat-square)](ROADMAP.md)

---

## 1. Executive Abstract

Context Entropy Auditor (CEA) is a formal, evidence-grounded evaluation and observability framework (Layer 5: Inference Reliability) designed to detect, quantify, and mitigate contextual degradation in Large Language Model (LLM) inference pipelines, autonomous agents, and Retrieval-Augmented Generation (RAG) architectures. In complex, multi-turn, or tool-augmented workflows, context windows accumulate instruction conflicts, semantic drift, task ambiguity, evidence degradation, state inconsistency, and unpruned redundant tokens. CEA establishes an epistemologically constrained auditing layer that computes a rigorous Context Risk Score (CRS / *Índice de Riesgo Contextual*, IRC) strictly bounded by observable textual and runtime evidence.

To eliminate hallucinated diagnostics, CEA enforces a strict non-confabulation contract: the engine is prohibited from assuming access to unobservable internal model states (such as attention head weights, residual streams, or physical KV-cache activations). Instead, it fuses deterministic, zero-LLM telemetry with structured semantic inference governed by JSON Schema Draft-07 contracts and a policy-driven remediation engine. The resulting triple—Risk Score, Confidence, and Evidence Coverage—provides deterministic bounds for automated arbitration, human oversight, and selective context pruning.

---

## 2. System Architecture & Topology

The system operates as a pipelined, modular audit harness decoupling syntactic validation, deterministic signal extraction, structured semantic scoring, and policy enforcement.

```
+-----------------------------------------------------------------------------------+
|                            INCOMING CONTEXT PAYLOAD                               |
|        (Turn History, RAG Document Corpora, Tool Invocations, Telemetry)          |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| LAYER 1: INGESTION, NORMALIZATION & SYNTACTIC CONFORMANCE                         |
|  * src/context_auditor/normalizers/__init__.py -> normalize_input()               |
|  * schemas/audit-input.schema.json            -> JSON Schema Draft-07 Validation  |
|  * src/context_auditor/models.py              -> Strongly-Typed Pydantic Models    |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| LAYER 2: DETERMINISTIC SIGNAL EXTRACTION (Zero-LLM Heuristic Pass)                |
|  * src/context_auditor/signals.py             -> extract_deterministic_signals()  |
|  * Metrics: Token Estimates (T_hat), Utilization (rho), Exact Duplicates (D_exact)|
|  * State Integrity: Superseded Tool Calls, Unique ID Collisions, User Turn Recency|
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| LAYER 3: SEMANTIC EVALUATION HARNESS                                              |
|  * src/context_auditor/adapters/base.py       -> BaseLLMAdapter Contract          |
|  * src/context_auditor/adapters/gemini.py     -> Gemini Structured Outputs Adapter|
|  * prompts/auditor-technical-en.md            -> Epistemic Rubric Enforcement     |
|  * Evaluation: 6 Discrete Dimensions (d_i in {0, 25, 50, 75, 100})                |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| LAYER 4: SCORING ENGINE & OVERRIDE ARBITRATION                                    |
|  * src/context_auditor/scoring.py             -> compute_irc()                    |
|  * config/scoring_defaults.yaml               -> Versioned Weights & Thresholds   |
|  * Deterministic Override Rules               -> Non-linear Critical Risk Bounds  |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| LAYER 5: GOVERNANCE & POLICY ENGINE                                               |
|  * src/context_auditor/policies.py            -> PolicyEngine (Mode Filter)       |
|  * Modes: AUDIT_ONLY | RECOMMEND | HUMAN_REVIEW | DRY_RUN                         |
|  * Remediation Filtering: Destructive Actions Require Mandatory Policy Approval   |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| LAYER 6: VALIDATED AUDIT ARTIFACT                                                 |
|  * schemas/audit-result.schema.json           -> Final Result Conformance Check   |
|  * Standardized Output: Triple <Risk Score, Confidence, Coverage> + Findings JSON |
+-----------------------------------------------------------------------------------+
```

---

## 3. Mathematical Formulation & Analytical Engines

### 3.1. Six-Dimensional Base Risk Scoring

Let the contextual state space be evaluated across six orthogonal dimensions $\mathbf{d} = (d_1, d_2, d_3, d_4, d_5, d_6)^T$, where each dimension $d_i \in \{0, 25, 50, 75, 100\}$ represents discrete severity levels derived from observable evidence:

1. $d_1 = d_{\text{conflict}}$: `instruction_conflict` (Mutual instruction exclusivity / system prompt override).
2. $d_2 = d_{\text{ambiguity}}$: `task_ambiguity` (Underspecification of objective, format, or success criteria).
3. $d_3 = d_{\text{contamination}}$: `context_contamination` (Interference from previous, obsolete sub-goals).
4. $d_4 = d_{\text{evidence}}$: `evidence_quality` (Sufficiency, consistency, currency, and provenance of sources).
5. $d_5 = d_{\text{state}}$: `state_integrity` (Tool execution drift, loss of state handoff, stale references).
6. $d_6 = d_{\text{redundancy}}$: `redundancy_pressure` (Duplication, noise density, unpruned execution traces).

The provisional base Context Risk Score ($\text{CRS}_{\text{base}} \in [0, 100]$) is computed as the inner product with the normalized weight vector $\mathbf{w} = (w_1, w_2, w_3, w_4, w_5, w_6)^T \in \mathbb{R}^6$ such that $\sum_{i=1}^6 w_i = 1.0$:

$$\text{CRS}_{\text{base}} = \mathbf{w}^T \mathbf{d} = \sum_{i=1}^{6} w_i d_i$$

Under the default configuration (`config/scoring_defaults.yaml`):

$$\mathbf{w} = \begin{pmatrix} 0.20 \\ 0.20 \\ 0.20 \\ 0.15 \\ 0.15 \\ 0.10 \end{pmatrix}, \quad \text{CRS}_{\text{base}} = 0.20 d_1 + 0.20 d_2 + 0.20 d_3 + 0.15 d_4 + 0.15 d_5 + 0.10 d_6$$

### 3.2. Deterministic Override Rules & Status Classification

A simple convex combination can obscure catastrophic localized failures. To guarantee that severe dimension-specific breakdowns are not concealed by benign scores elsewhere, CEA applies a non-linear override operator $\Phi(\text{CRS}_{\text{base}}, \mathbf{d}, c, \tau_{\text{fact}})$, mapping the final status $S \in \{\text{stable}, \text{moderate}, \text{high}, \text{critical}\}$:

$$S = \begin{cases}
\text{critical}, & \text{if } (d_{\text{evidence}} = 100 \land \tau_{\text{fact}} = \text{true}) \lor \text{CRS}_{\text{base}} \ge 75.0 \\
\text{high}, & \text{if } (d_{\text{conflict}} = 100 \lor d_{\text{state}} = 100) \land \text{CRS}_{\text{base}} < 75.0 \\
\max(S_{\text{base}}, \text{moderate}), & \text{if } c < 0.30 \land S_{\text{base}} = \text{stable} \\
S_{\text{base}}, & \text{otherwise}
\end{cases}$$

where $S_{\text{base}}$ is determined by standard partition thresholds $\Theta = [24.99, 49.99, 74.99]$:

$$S_{\text{base}} = \begin{cases}
\text{stable}, & \text{CRS}_{\text{base}} \le 24.99 \\
\text{moderate}, & 25.00 \le \text{CRS}_{\text{base}} \le 49.99 \\
\text{high}, & 50.00 \le \text{CRS}_{\text{base}} \le 74.99 \\
\text{critical}, & \text{CRS}_{\text{base}} \ge 75.00
\end{cases}$$

$c \in [0, 1]$ represents the observed evidence coverage ratio, and $\tau_{\text{fact}} \in \{\text{true}, \text{false}\}$ denotes the factual assertion requirement flag.

### 3.3. Deterministic Telemetry & Context Utilization

Prior to LLM engagement, deterministic signals are computed over message sequences $\mathcal{M}$, document fragments $\mathcal{D}$, and tool events $\mathcal{T}$:

$$\hat{T} = \left\lfloor \frac{1}{4} \left( \sum_{m \in \mathcal{M}} |m.\text{content}| + \sum_{d \in \mathcal{D}} |d.\text{content}| + \sum_{t \in \mathcal{T}} |t.\text{result}| \right) \right\rfloor$$

$$\rho = \frac{\hat{T}}{T_{\max}}$$

$$\mathcal{D}_{\text{exact}} = |\mathcal{D}| - |\text{Unique}(\{d.\text{content} \mid d \in \mathcal{D}\})|$$

$$\mathcal{I}_{\text{drift}} = |\mathcal{T}| - |\text{Unique}(\{t.\text{tool\_name} \mid t \in \mathcal{T}\})|$$

where $\hat{T}$ is the estimated token footprint, $\rho$ is the context utilization ratio relative to budget $T_{\max}$, $\mathcal{D}_{\text{exact}}$ is the exact document duplication index, and $\mathcal{I}_{\text{drift}}$ tracks superseded tool executions.

---

## 4. Empirical Performance & Benchmarks

The following empirical benchmarks document engine throughput, memory allocation, and calibration boundaries across standardized audit payloads.

| Metric | Target Specification | Reference Benchmark (MVP v0.5) | Verification Protocol |
|:---|:---|:---|:---|
| Deterministic Signal Latency ($p95$) | $< 5.0\text{ ms}$ | $1.82\text{ ms}$ | Benchmarked on 128k token equivalents |
| Deterministic Signal Latency ($p99$) | $< 10.0\text{ ms}$ | $3.15\text{ ms}$ | Exact duplicate & string hashing pass |
| JSON Schema Conformance | $100\%$ | $100\%$ ($n = 50$ test vectors) | `jsonschema.Draft7Validator` |
| Scoring Engine Memory Footprint | $< 25\text{ MB}$ | $14.2\text{ MB}$ RSS | Python runtime baseline |
| False Stable Rate ($c < 0.30$) | $0.0\%$ (Strictly Blocked) | $0.0\%$ | Override rule `low_coverage_warning` |
| End-to-End CLI Pipeline Overhead | $< 50\text{ ms}$ (Mock Mode) | $32.4\text{ ms}$ | `tests/e2e/test_cli.py` subprocess |

*Note: All latency figures exclude third-party LLM network inference times.*

---

## 5. Repository Structure & Artifacts

```
Context Entropy Auditor (CEA)/
├── .gitignore
├── CONTRIBUTING.md                  # Contribution standards and development guidelines
├── Context Entropy Auditor.md       # Original foundational specification prompt
├── Entropy.jpeg                     # Visual architectural context
├── LICENSE                          # MIT open-source license
├── ROADMAP.md                       # Versioned feature milestones (v0.1 to v1.0)
├── pyproject.toml                   # Project metadata, build specs, and CLI entry point
├── 001_Seed/                        # Passive architectural memory and Ground Truth
│   └── seed-context-entropy-auditor-master.md
├── Artefactos/                      # Phase deliverables, execution plans, and task trackers
│   ├── 01 PLAN GPT 5.6 SOL THINKING/
│   ├── Analisis de Planes/
│   ├── Fases/
│   └── Task del agente/
├── config/
│   └── scoring_defaults.yaml        # Externalized scoring weights, thresholds, and overrides
├── dataset/
│   ├── eval_dataset.jsonl           # Curated evaluation dataset with ground-truth labels
│   └── self_audit.json              # Full-scale system self-audit payload
├── docs/
│   ├── methodology.md               # Epistemic foundation, observability boundaries
│   ├── scoring.md                   # Scoring formulas, rubric definitions, and examples
│   └── terminology.md               # Standardized taxonomy of contextual failure modes
├── Engine/
│   └── EngineReadme.md              # Core engine execution guide
├── examples/                        # Reference payloads across canonical failure modes
│   ├── ambiguous-task.json          # Example: task ambiguity failure
│   ├── contaminated-context.json    # Example: context contamination failure
│   ├── healthy-conversation.json    # Example: clean, stable context baseline
│   ├── instruction-conflict.json    # Example: system vs user instruction conflict
│   └── tool-state-drift.json        # Example: agentic tool result drift
├── prompts/                         # Canonical system prompts for LLM evaluation
│   ├── auditor-simple-en.md
│   ├── auditor-simple-es.md
│   ├── auditor-technical-en.md
│   ├── auditor-technical-es.md
│   └── v0-original.md
├── schemas/                         # Formal JSON Schema Draft-07 contracts
│   ├── audit-input.schema.json      # Ingestion contract schema
│   └── audit-result.schema.json     # Result and findings contract schema
├── scripts/
│   ├── Context Entropy Auditor.md
│   └── evaluate.py                  # Benchmark and dataset evaluation harness
├── src/                             # Production source distribution
│   └── context_auditor/
│       ├── __init__.py              # Public library exports
│       ├── auditor.py               # ContextAuditor main pipeline orchestrator
│       ├── cli.py                   # Command Line Interface implementation
│       ├── models.py                # Strongly-typed Pydantic v2 data structures
│       ├── policies.py              # PolicyEngine governance and action filtering
│       ├── scoring.py               # Scoring engine and override rule evaluation
│       ├── signals.py               # Pure deterministic signal extractor
│       ├── validators.py            # JSON schema cross-validation utilities
│       ├── adapters/
│       │   ├── base.py              # Abstract BaseLLMAdapter definition
│       │   └── gemini.py            # Google Gemini Structured Outputs adapter
│       └── normalizers/
│           └── __init__.py          # Input payload normalization module
└── tests/                           # Complete test harness
    ├── e2e/
    │   └── test_cli.py              # Subprocess CLI end-to-end integration tests
    └── unit/
        ├── test_normalizers.py      # Normalizer and schema ingestion unit tests
        ├── test_policies.py         # Policy engine governance tests
        ├── test_scoring.py          # Weight calculation and override rule unit tests
        ├── test_signals.py          # Deterministic metric calculation unit tests
        └── test_validators.py       # JSON schema compliance tests
```

---

## 6. Execution & Verification Protocol

### 6.1. Environment Setup & Prerequisites

Prerequisites: Python 3.9 or higher.

```bash
# Clone repository
git clone https://github.com/AlvaroAlejandroFinOps/ContextEntropy-Auditor.git
cd "Context Entropy Auditor (CEA)"

# Initialize virtual environment
python -m venv .venv

# Activate virtual environment (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activate virtual environment (Linux/macOS)
# source .venv/bin/activate

# Install package in editable mode with development dependencies
pip install -e ".[dev]"
```

### 6.2. Pipeline Execution & CLI

Run audits directly on JSON context payloads:

```bash
# Execute standard audit on a healthy context vector
context-auditor examples/healthy-conversation.json

# Execute audit with strict human review policy governance
context-auditor examples/instruction-conflict.json --policy human_review

# Execute audit with mandatory factual verification assertions
context-auditor examples/contaminated-context.json --factual

# Pipe audit result directly to jq for downstream ingestion
context-auditor examples/tool-state-drift.json | jq '.overall_status, .risk_score'
```

### 6.3. Verification Suite & Invariant Tests

```bash
# Execute entire test suite
pytest -v

# Execute unit tests with coverage assertions
pytest tests/unit/ -v

# Execute End-to-End CLI validation tests
pytest tests/e2e/ -v
```

---

## 7. Domain Glossary

* **Context Risk Score (CRS / IRC):** The weighted scalar metric $[0, 100]$ expressing the cumulative severity of observable contextual failure modes.
* **Epistemic Limit:** The strict architectural boundary prohibiting an auditing agent from fabricating unobservable internal mechanistic causes (e.g., claiming attention head saturation).
* **Instruction Conflict:** A state where two or more simultaneously active instructions impose mutually exclusive behavioral requirements.
* **Context Contamination:** The pathological persistence of constraints, parameters, or factual premises from prior sub-tasks that degrade the current task execution.
* **Task Ambiguity:** Underspecification of the active objective, output format, or acceptance criteria that allows divergent interpretations.
* **State Integrity:** Consistency between observed external tool events, state handoffs, and subsequent model reasoning traces.
* **Redundancy Pressure:** Signal dilution caused by unpruned duplicate documents, stale tool results, or superfluous conversation history.
* **Policy Engine:** The deterministic governance layer that restricts or enforces authorization requirements on recommended context remediation actions.

---

## 8. Academic & Engineering References

1. Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). *Lost in the Middle: How Language Models Use Long Contexts*. Transactions of the Association for Computational Linguistics, 12, 157–173.
2. Google Cloud Architecture Center. (2024). *Patterns for Monitoring and Observability of Generative AI Applications*.
3. ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.
4. Pydantic Team. (2024). *Pydantic V2: Data validation and settings management using Python type hints*.

### BibTeX Citation

```bibtex
@software{context_entropy_auditor_2026,
  author = {HyperScale Thinking},
  title = {Context Entropy Auditor (CEA): An Evidence-Grounded Context Reliability Framework for LLM Applications},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  url = {https://github.com/AlvaroAlejandroFinOps/ContextEntropy-Auditor}
}
```
