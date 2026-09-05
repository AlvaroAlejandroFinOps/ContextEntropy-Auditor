![alt text](Entropy.jpeg)
# Context Entropy Auditor (CEA) by Hyperscale Thinking
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](pyproject.toml)
[![Language: English](https://img.shields.io/badge/Language-English-orange.svg)](README.md)
[![Versión en Español](https://img.shields.io/badge/Idioma-Español-green.svg)](README_ES.md)

## Abstract

As Large Language Models (LLMs) process increasingly vast and complex context windows, the probability of epistemic degradation—where instructions conflict, tool states drift, and context becomes contaminated—scales exponentially. The Context Entropy Auditor (CEA) is a deterministic and semantic framework designed to measure, evaluate, and mitigate context degradation in LLM-driven applications. By enforcing strict epistemic boundaries (observed vs. inferred data) and isolating deterministic signals from semantic evaluation, CEA provides a quantifiable Index of Risk and Contamination (IRC) that dictates whether an agent's context is stable enough to proceed with a given task.

---

## 1. Introduction

Modern LLM applications, particularly autonomous agents, operate over prolonged sessions. As the session advances, the context window accumulates system prompts, user instructions, retrieved documents (RAG), and tool outputs. This accumulation inevitably leads to "Context Entropy," a state where contradictory instructions, stale tool data, and irrelevant noise compromise the model's ability to act deterministically and safely.

The Context Entropy Auditor acts as a strict, out-of-band observer. It does not generate content for the end-user; rather, it audits the state of the conversation and memory before a critical action is taken, determining if the context is safe, ambiguous, or critically contaminated.

## 2. Architectural Vanguard

The architecture of CEA represents a paradigm shift in LLM evaluation, moving away from subjective "vibes-based" grading toward rigorous epistemic auditing. The system is divided into three distinct operational areas.

### 2.1. Deterministic Signal Extraction
**Technical Vanguard:** Before any LLM evaluation occurs, CEA extracts absolute, mathematical truths from the input payload. This includes exact hash-based document duplication rates, context limit utilization ratios, ID integrity, and superseded tool state detection.
**Plain Language:** Before asking an AI to judge the situation, the system does raw math. It counts how many messages there are, checks if any documents are exactly duplicated, and sees if the AI is ignoring new tool results in favor of old ones. This gives us undeniable facts about the conversation's health.

### 2.2. Epistemically Bounded Semantic Evaluation
**Technical Vanguard:** CEA utilizes a secondary LLM (e.g., Gemini) strictly as a semantic classifier constrained by rigid epistemic rules. The LLM cannot claim to know the internal weights or attention mechanisms of the primary model. It is forced to classify findings strictly as `observed` (explicitly present in text) or `inferred` (deduced from textual contradictions). The evaluation spans six dimensions: Instruction Conflict, Task Ambiguity, Context Contamination, Evidence Quality, State Integrity, and Redundancy Pressure.
**Plain Language:** We use a second AI to read the conversation and look for logical conflicts or confusing instructions. However, we force this AI to stick to the facts—it can only report what is actually written in the text, preventing it from hallucinating or guessing what the main AI "might" be thinking.

### 2.3. The Scoring & Policy Engine
**Technical Vanguard:** A deterministic rules engine calculates the Index of Risk and Contamination (IRC). It applies pre-configured weights to the semantic dimensions and executes override policies (e.g., if State Integrity hits 100 on a factual task, the status is immediately flagged as Critical, regardless of the overall average). The Policy Engine then filters recommended actions, ensuring destructive actions (like deleting memory) require explicit system policy approval.
**Plain Language:** The system takes the math (Area 1) and the semantic review (Area 2) and calculates a final risk score. If it spots a critical danger—like the AI relying on entirely false documents for a factual task—it immediately pulls the alarm, regardless of how good the rest of the conversation looks. It also blocks the AI from taking dangerous actions automatically.

---

## 3. Installation and Usage

CEA is built as a modern Python package requiring Python 3.9 or higher.

### Installation

```bash
# Clone the repository
git clone https://github.com/hyperscale/context-entropy-auditor.git
cd context-entropy-auditor

# Install the package and its dependencies
pip install -e .
```

### Command Line Interface (CLI)

The auditor can be invoked directly from the terminal against a JSON payload that conforms to the `audit-input.schema.json` specification.

```bash
# Basic evaluation recommending actions
context-auditor examples/healthy-conversation.json

# Evaluation requiring strict factual checks and human review policy
context-auditor examples/contaminated-context.json --factual --policy human_review
```

---

## 4. Technical Glossary

* **Context Entropy:** The measure of disorder, contradiction, and irrelevant noise within an LLM's context window. High entropy correlates directly with a loss of deterministic reliability.
* **Epistemic Boundary:** The strict delineation between what an auditor can definitively know (textual presence) and what it cannot know (the internal cognitive or mechanical state of the target LLM).
* **IRC (Index of Risk and Contamination):** A weighted scalar value (0-100) representing the overall danger of executing a task given the current context state.
* **Instruction Conflict:** A state where two or more directives within the context mutually exclude one another (e.g., a system prompt demanding brevity and a user prompt demanding a lengthy essay).
* **Context Contamination:** The persistence of rules, constraints, or personas from previous, resolved tasks that inappropriately leak into and affect the current, unrelated task.
* **State Integrity:** The coherence of tool use and memory. A loss of state integrity occurs when the model hallucinates tool outputs, ignores recent tool results, or relies on deprecated data.
* **Redundancy Pressure:** The computational and attentional strain caused by identical or highly similar information being repeated throughout the context window, diluting the weight of novel instructions.
* **Policy Engine:** The deterministic module responsible for intercepting mitigation recommendations and enforcing execution constraints (e.g., requiring human review for destructive memory operations).
