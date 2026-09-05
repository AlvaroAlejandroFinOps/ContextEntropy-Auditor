# Plan de Avance Gradual: Optimización Profesional para Lanzamiento en GitHub

Este plan estructura la transformación del prompt CEA en una herramienta programática de grado profesional, lista para ser publicada open-source.

## Fase 1: Consolidación del Core (Versionado de Límite Epistémico)
*   **Objetivo:** Establecer la "Supresión de Confabulación Mecanicista" como núcleo inamovible.
*   **Acciones:**
    *   Extraer el bloque core del prompt a un submódulo independiente.
    *   Implementar un sistema de versionado semántico estricto (SemVer) para este bloque lógico.
    *   Documentar prohibiciones explícitas sobre la modificación de esta restricción en el README.
*   **Hito:** Núcleo epistémico protegido, aislado y versionado independientemente.

## Fase 2: Inyección de Metadatos del Sistema (Conciencia de Contexto)
*   **Objetivo:** Dotar al modelo de parámetros duros para evitar alucinaciones diagnósticas.
*   **Acciones:**
    *   Diseñar un motor de plantillas ligero (ej. Jinja2 o f-strings en Python) para el prompt base.
    *   Inyectar variables dinámicas en tiempo real antes de inferencia: `[TOKENS_ACTUALES]`, `[LLAMADAS_HERRAMIENTAS]`, `[TURNO_ACTUAL]`.
*   **Hito:** Mejora empírica en la precisión del diagnóstico gracias al anclaje paramétrico del LLM.

## Fase 3: Forzar Salida Estructurada (JSON Schema)
*   **Objetivo:** Hacer que la herramienta sea cien por ciento consumible por código (Programática).
*   **Acciones:**
    *   Definir un JSON Schema estricto que reemplace la salida visual en Markdown.
    *   Configurar campos fuertemente tipados: `semaforo_estado` (enum), `severidad_dimensiones` (array de objetos), `plan_accion_recomendado`.
    *   Validar la salida del LLM contra el esquema usando librerías como Pydantic.
*   **Hito:** Integración fluida en flujos de orquestación complejos sin necesidad de parseo manual por regex.

## Fase 4: Empaquetado como SDK / Wrapper
*   **Objetivo:** Proveer una interfaz de usuario para desarrolladores (DX) impecable e intuitiva.
*   **Acciones:**
    *   Desarrollar una clase constructora principal en Python (ej. `IOPScanner` o `ContextEntropyAuditor`).
    *   Abstraer la inyección invisible del prompt del auditor en el array de mensajes de la API.
    *   Exponer métodos analíticos asíncronos de alto nivel: `.get_entropy_score()`, `.get_recommended_pruning()`.
    *   Configurar pip package (setup.py, pyproject.toml) y publicar en PyPI.
*   **Hito:** Herramienta distribuible, instalable vía `pip install context-entropy-auditor` e integrable en escasas líneas de código.
