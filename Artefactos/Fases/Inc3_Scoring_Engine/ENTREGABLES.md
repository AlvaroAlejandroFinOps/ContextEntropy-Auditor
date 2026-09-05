# Incremento 3 — Scoring Engine v0.3

## Objetivo
Motor de puntuación reproducible, separado del LLM, con pesos configurables y reglas de sobrescritura.

## Entregables

| Artefacto | Ruta | Estado |
|-----------|------|--------|
| Motor de scoring | `src/context_auditor/scoring.py` | ⏳ |
| Motor de políticas | `src/context_auditor/policies.py` | ⏳ |
| Config de pesos | `config/scoring_defaults.yaml` | ⏳ |
| Tests de scoring | `tests/unit/test_scoring.py` | ⏳ |
| Tests de políticas | `tests/unit/test_policies.py` | ⏳ |

## Fórmula
```
IRC = 0.20*instruction_conflict + 0.20*task_ambiguity + 0.20*context_contamination
    + 0.15*evidence_quality + 0.15*state_integrity + 0.10*redundancy_pressure
```

## Criterio de Aceptación
Dado un JSON de scores por dimensión, el motor calcula IRC, aplica sobrescrituras y produce resultado reproducible sin LLM.

## Dependencias
- Inc 2 completado (modelos tipados disponibles)
