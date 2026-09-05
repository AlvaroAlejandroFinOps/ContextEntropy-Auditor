# CEA — Fases de Entregables

Estructura de control para la implementación gradual del proyecto **Context Entropy Auditor**.

Cada fase contiene un `ENTREGABLES.md` que describe el objetivo, los artefactos producidos, el criterio de aceptación y el estado actual.

| Fase | Nombre | Versión | Estado |
|------|--------|---------|--------|
| Inc 0 | Fundación Epistémica | v0.1.0 | ✅ Completado |
| Inc 1 | Prompt Core | v0.1.0 | ✅ Completado |
| Inc 2 | Esquemas y Modelos | v0.2.0 | ✅ Completado |
| Inc 3 | Scoring Engine | v0.3.0 | ✅ Completado |
| Inc 4 | Señales Deterministas | v0.4.0 | ✅ Completado |
| Inc 5 | SDK + CLI | v0.5.0 | ✅ Completado |
| Inc 6 | Dataset + Evaluación | v0.6.0 | ✅ Completado |
| Inc 7 | Publicación Pública | v1.0.0 | ✅ Completado |

## Decisiones Adoptadas

1. **Estructura**: Se mantiene la estructura HyperScale corporativa. El paquete Python vive en `src/context_auditor/`.
2. **Idioma**: Código y API en inglés. Prompts y resultados en español e inglés.
3. **Proveedor LLM**: Gemini como adaptador inicial.
4. **Prompt original**: Archivado como referencia histórica en `prompts/v0-original.md`.
