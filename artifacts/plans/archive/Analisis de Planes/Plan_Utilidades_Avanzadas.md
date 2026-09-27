# Plan de Avance Gradual: Utilidades Avanzadas en Producción

Este plan detalla la implementación escalonada de capacidades avanzadas para el Context Entropy Auditor (CEA) en entornos productivos.

## Fase 1: Auditoría de Sistemas RAG (Diagnóstico Estático)
*   **Objetivo:** Diagnosticar la contaminación por recuperación (Context Contamination).
*   **Acciones:**
    *   Implementar análisis de fragmentos inyectados por la BD vectorial.
    *   Evaluar la métrica de densidad de ruido vs. resolución de ambigüedad.
*   **Hito:** Capacidad de emitir reportes automatizados sobre la salud y relevancia del contexto RAG.

## Fase 2: Garbage Collection en Grafos Cognitivos (Optimización Activa)
*   **Objetivo:** Prevenir la saturación del KV Cache en flujos agénticos largos.
*   **Acciones:**
    *   Programar la ejecución de la sonda cada *N* turnos en segundo plano (background worker).
    *   Desarrollar lógica heurística para identificar y clasificar outputs de herramientas como "ruido".
    *   Implementar mecanismo de purga segura (Semantic Reset parcial) del historial de mensajes.
*   **Hito:** Reducción medible del consumo de tokens sin pérdida de contexto crítico.

## Fase 3: Enrutamiento Conversacional Adaptativo (Orquestación Dinámica)
*   **Objetivo:** Actuar como gatekeeper para derivar tareas según la entropía detectada.
*   **Acciones:**
    *   Conectar los umbrales del "Semáforo de Estado" a un nodo de enrutamiento (Router).
    *   Implementar triggers para "Semantic Reset" y transferencia de estado limpio.
    *   Habilitar la transición fluida de modelos ligeros a modelos de alta capacidad cuando la saturación es inminente.
*   **Hito:** Enrutamiento inteligente y dinámico basado en la salud del contexto (Capa L5).

## Fase 4: Evaluación Continua (CI/CD para LLMs)
*   **Objetivo:** Stress testing de System Prompts candidatos antes de pasar a producción.
*   **Acciones:**
    *   Desarrollar pipelines de inyección de historiales sintéticos densos.
    *   Automatizar la medición de la tasa de *Instruction Dominance*.
    *   Integración con herramientas CI/CD estándar (GitHub Actions, GitLab CI).
*   **Hito:** Pipeline de validación de prompts basado en resiliencia a la entropía y fatiga de atención.
