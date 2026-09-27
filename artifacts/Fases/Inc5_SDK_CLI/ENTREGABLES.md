# Incremento 5 — SDK Mínimo + CLI v0.5

## Objetivo
Un desarrollador puede auditar un JSON desde código Python o terminal.

## Entregables

| Artefacto | Ruta | Estado |
|-----------|------|--------|
| Clase Auditor | `src/context_auditor/auditor.py` | ⏳ |
| CLI (Typer) | `src/context_auditor/cli.py` | ⏳ |
| Adaptador Gemini | `src/context_auditor/providers/gemini.py` | ⏳ |
| Empaquetado | `pyproject.toml` | ⏳ |
| README público | `README.md` | ⏳ |
| Tests integración | `tests/integration/test_auditor.py` | ⏳ |

## Comandos
```bash
context-auditor inspect conversation.json
context-auditor validate audit-result.json
context-auditor compare baseline.json candidate.json
```

## Criterio de Aceptación
`pip install -e .` funciona, el CLI audita un JSON de ejemplo y produce un resultado válido según schema.

## Dependencias
- Inc 4 completado (señales + normalizadores)
