# Incremento 6 — Dataset + Evaluación Inicial v0.6

## Objetivo
Demostrar que el scoring es evaluable, no solo un prompt.

## Entregables

| Artefacto | Ruta | Estado |
|-----------|------|--------|
| Casos etiquetados (30-50) | `datasets/context-regression/` | ⏳ |
| Métricas de evaluación | `evaluation/metrics.py` | ⏳ |
| Informe inicial | `evaluation/reports/` | ⏳ |
| Casos adversariales (10-15) | `tests/adversarial/` | ⏳ |
| CHANGELOG con ajustes | `CHANGELOG.md` | ⏳ |

## Criterio de Aceptación
Precisión/recall documentados por dimensión con ≥30 casos. Pesos ajustados con justificación trazable.

## Dependencias
- Inc 5 completado (SDK funcional para ejecutar evaluaciones)
