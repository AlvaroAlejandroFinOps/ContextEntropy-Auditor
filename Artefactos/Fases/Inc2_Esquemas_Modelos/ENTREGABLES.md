# Incremento 2 — Esquemas y Modelos de Datos v0.2

## Objetivo
Convertir la salida del auditor en un contrato programático verificable con JSON Schema.

## Entregables

| Artefacto | Ruta | Estado |
|-----------|------|--------|
| Schema de entrada | `schemas/audit-input.schema.json` | ⏳ |
| Schema de resultado | `schemas/audit-result.schema.json` | ⏳ |
| Ejemplo: conversación saludable | `examples/healthy-conversation.json` | ⏳ |
| Ejemplo: tarea ambigua | `examples/ambiguous-task.json` | ⏳ |
| Ejemplo: contaminación contextual | `examples/contaminated-context.json` | ⏳ |
| Ejemplo: conflicto de instrucciones | `examples/instruction-conflict.json` | ⏳ |
| Ejemplo: deriva de herramientas | `examples/tool-state-drift.json` | ⏳ |
| Modelos tipados | `src/context_auditor/models.py` | ⏳ |
| Validadores | `src/context_auditor/validators.py` | ⏳ |
| Tests de validación | `tests/unit/test_validators.py` | ⏳ |

## Criterio de Aceptación
Toda salida se valida determinísticamente. Un JSON inválido falla con error descriptivo.

## Dependencias
- Inc 1 completado (prompts definen la estructura de salida esperada)
