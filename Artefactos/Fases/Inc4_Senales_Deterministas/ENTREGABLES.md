# Incremento 4 — Señales Deterministas + Normalizador v0.4

## Objetivo
Extraer métricas objetivas del contexto sin necesidad de LLM.

## Entregables

| Artefacto | Ruta | Estado |
|-----------|------|--------|
| Normalizadores | `src/context_auditor/normalizers/` | ⏳ |
| Extractor de señales | `src/context_auditor/signals.py` | ⏳ |
| Tests normalizadores | `tests/unit/test_normalizers.py` | ⏳ |
| Tests señales | `tests/unit/test_signals.py` | ⏳ |
| Fixtures (10) | `tests/fixtures/` | ⏳ |

## Señales Deterministas Iniciales
- Conteo de mensajes/turnos
- Tokens estimados (tiktoken)
- Proporción de contexto utilizado
- Documentos/fuentes distintas
- Duplicación exacta
- IDs repetidos o ausentes
- Resultados de herramientas reemplazados
- Antigüedad del último objetivo explícito

## Criterio de Aceptación
Las señales se calculan sobre JSON normalizado y producen resultados idénticos en cada ejecución.

## Dependencias
- Inc 2 (schemas) + Inc 3 (scoring)
