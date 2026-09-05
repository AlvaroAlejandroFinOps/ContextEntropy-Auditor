# Contributing to Context Entropy Auditor (CEA)

We welcome contributions from researchers and engineers dedicated to advancing LLM reliability and alignment.

## Epistemic Rules for Contributors

When submitting Pull Requests, especially those affecting the `prompts/` or `src/context_auditor/scoring.py` files, please ensure your changes adhere to the foundational epistemic boundaries of this project:

1. **No Mechanistic Confabulation:** Do not introduce prompts or logic that assume the auditor can read the internal state (weights, attention) of the target LLM.
2. **Evidence-Based Findings:** Any new dimension or scoring rule must be traceable to deterministic signals or observable semantic contradictions in the text.
3. **Deterministic Fallbacks:** When semantic evaluation is ambiguous, the system must default to its deterministic normalizers and signals.

## Development Setup

1. Fork and clone the repository.
2. Install the development dependencies: `pip install -e ".[dev]"`
3. Run the global test suite before committing: `pytest tests/`

Thank you for contributing to safer, more reliable AI systems.
