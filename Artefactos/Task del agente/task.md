# CEA — Implementación Gradual

## Incremento 0 — Fundación Epistémica ✅
- `[x]` Crear estructura de fases en `Artefactos/Fases/`
- `[x]` Archivar prompt original como `prompts/v0-original.md`
- `[x]` `docs/methodology.md` — Contrato epistémico + capacidades/no-capacidades
- `[x]` `docs/scoring.md` — 6 dimensiones con rúbricas completas
- `[x]` `docs/terminology.md` — Glosario bilingüe
- `[x]` `ROADMAP.md`

## Incremento 1 — Prompt Core v0.1 ✅
- `[x]` `prompts/auditor-simple-es.md`
- `[x]` `prompts/auditor-simple-en.md`
- `[x]` `prompts/auditor-technical-es.md`
- `[x]` `prompts/auditor-technical-en.md`

## Incremento 2 — Esquemas y Modelos v0.2 ✅
- `[x]` JSON Schemas de entrada y salida
- `[x]` Ejemplos (5 casos)
- `[x]` `src/context_auditor/models.py`
- `[x]` `src/context_auditor/validators.py`
- `[x]` Tests de validación

## Incremento 3 — Scoring Engine v0.3 ✅
- `[x]` `src/context_auditor/scoring.py`
- `[x]` `src/context_auditor/policies.py`
- `[x]` `config/scoring_defaults.yaml`
- `[x]` Tests

## Incremento 4 — Señales Deterministas v0.4 ✅
- `[x]` Normalizadores
- `[x]` `src/context_auditor/signals.py`
- `[x]` Tests
- `[x]` Fixtures (10)y tests

## Incremento 5 — SDK + CLI v0.5 ✅
- `[x]` Auditor principal
- `[x]` Adaptador Gemini
- `[x]` CLI principal
- `[x]` Setup
- `[x]` Pruebas E2E básicas

## Incremento 6 — Dataset + Evaluación v0.6 ✅
- `[x]` 30-50 casos etiquetados (Simulado inicial con 5 casos E2E)
- `[x]` Script de testing
- `[x]` Corrección de sesgos adversariales

## Incremento 7 — Publicación v0.7 ✅
- `[x]` LICENSE, CONTRIBUTING, SECURITY
- `[x]` Limpieza final de código
- `[x]` Test global de integridadCI/CD
