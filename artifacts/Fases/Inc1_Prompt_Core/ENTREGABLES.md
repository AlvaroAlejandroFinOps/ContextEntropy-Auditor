# Incremento 1 — Prompt Core v0.1

## Objetivo
Producir un prompt corregido, epistemológicamente seguro y usable manualmente en español e inglés.

## Entregables

| Artefacto | Ruta | Estado |
|-----------|------|--------|
| Prompt simple español | `prompts/auditor-simple-es.md` | ⏳ |
| Prompt simple inglés | `prompts/auditor-simple-en.md` | ⏳ |
| Prompt técnico español | `prompts/auditor-technical-es.md` | ⏳ |
| Prompt técnico inglés | `prompts/auditor-technical-en.md` | ⏳ |

## Cambios Clave vs. Prompt v0
1. Eliminar "deja de responder normalmente"
2. Reemplazar "token exacto" por rangos observables
3. Sustituir `Trajectory Lock-in` → `observable_error_propagation`
4. Reclasificar `Lost-in-the-Middle` como riesgo potencial
5. Introducir IRC, confianza, cobertura
6. Clasificación epistémica obligatoria (observed/inferred/runtime_measured/unknown)
7. Campo `limitations` obligatorio en salida

## Criterio de Aceptación
El prompt produce hallazgos con evidence_refs y reconoce explícitamente la falta de información.

## Dependencias
- Inc 0 completado (metodología y rúbricas definidas)
