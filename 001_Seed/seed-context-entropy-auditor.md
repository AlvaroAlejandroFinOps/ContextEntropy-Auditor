# MASTER HYBRID SEED: Context Entropy Auditor (CEA)

> **Propósito:** Snapshot técnico, verificable y portable del proyecto Context Entropy Auditor (CEA).
> **Instrucción al Agente:** Snapshot generado bajo el estándar `ThinkingSeed_MasterHybrid.md` respetando estrictamente la evidencia empírica observada y la política de seguridad.

---

## 0. REGLAS DE GENERACIÓN (Epistemología y Seguridad)

*   **Etiquetas de Evidencia:**
    *   `[CONFIRMADO]`: Visto directamente en código, esquemas o archivos de configuración.
    *   `[INFERIDO]`: Deducción lógica basada en la estructura del proyecto o documentación.
    *   `[FALTANTE]`: Componentes, variables o integraciones esperadas que no existen aún en el repositorio.
*   **Política de Seguridad:** **PROHIBIDO** reproducir secretos, contraseñas, claves API, tokens o cadenas de conexión. Sustituir siempre por `<REDACTED>`.

---

## 1. CORE MANIFESTO

### 1.1 Objetivo Principal
Proporcionar un framework determinista y semántico de auditoría de fiabilidad del contexto para aplicaciones y agentes basados en Grandes Modelos de Lenguaje (LLMs), evaluando y mitigando la degradación epistémica y la entropía de contexto. `[CONFIRMADO]` (README.md, ROADMAP.md)

### 1.2 Problema que Resuelve
A medida que las ventanas de contexto se amplían, la acumulación de instrucciones contradictorias, deriva de estado de herramientas (tool state drift), contaminación de contexto anterior y presión por redundancia degrada la fiabilidad determinista de los LLMs. CEA actúa como un observador out-of-band que audita el estado del contexto antes de ejecutar acciones críticas. `[CONFIRMADO]` (README.md)

### 1.3 Patrón Arquitectónico
Pipeline de auditoría epistémicamente acotada estructurado en 3 fases: `[CONFIRMADO]` (README.md, `src/context_auditor/auditor.py`)
1. **Deterministic Signal Extraction:** Extracción matemática/determinista pura (hashes de duplicación, tasa de mensajes/documentos, integridad de IDs y estado de herramientas).
2. **Epistemically Bounded Semantic Evaluation:** Evaluación clasificatoria mediante un LLM secundario (ej. Gemini Adapter) restringido a límites epistémicos estrictos (`observed` vs `inferred`).
3. **Scoring & Policy Engine:** Cálculo del Índice de Riesgo y Contaminación (IRC), aplicación de reglas de anulación (override rules) y filtrado de acciones recomendadas mediante modos de política.

### 1.4 Stack Principal (Versiones y fuente)
*   **Lenguaje:** Python >= 3.9 `[CONFIRMADO]` (`pyproject.toml`)
*   **Data Validation & Modeling:** `pydantic >= 2.0.0` `[CONFIRMADO]` (`pyproject.toml`)
*   **Schema Enforcement:** `jsonschema >= 4.0.0` `[CONFIRMADO]` (`pyproject.toml`)
*   **Configuration:** `pyyaml >= 6.0` `[CONFIRMADO]` (`pyproject.toml`)
*   **Testing:** `pytest >= 7.0.0` `[CONFIRMADO]` (`pyproject.toml`)
*   **CLI Entry Point:** `context-auditor` (`src.context_auditor.cli:main`) `[CONFIRMADO]` (`pyproject.toml`)

---

## 2. REPOSITORY TOPOLOGY

```
Context Entropy Auditor (CEA)/
├── 001_Seed/                               # Plantillas y snapshots de contexto técnico
│   ├── ThinkingSeed_MasterHybrid.md        # Estándar de especificación Seed [CONFIRMADO]
│   └── seed-context-entropy-auditor.md     # Snapshot de contexto activo (este archivo) [CONFIRMADO]
├── 01_Status/                              # Informes de estado y tracking de sprints [CONFIRMADO]
├── Artefactos/                             # Artefactos y documentación persistente de entregables [CONFIRMADO]
├── config/                                 # Configuraciones de evaluación y scoring
│   └── scoring_defaults.yaml               # Pesos, umbrales y reglas de anulación de scoring [CONFIRMADO]
├── data/                                   # Datos persistentes de ejecuciones/auditorías [CONFIRMADO]
├── dataset/                                # Datasets para evaluación y benchmark [CONFIRMADO]
├── docs/                                   # Especificaciones técnicas e investigación
│   ├── architecture/                       # Diagramas y documentos de diseño [CONFIRMADO]
│   ├── engineers_notes/                    # Notas técnicas de desarrollo [CONFIRMADO]
│   ├── technical_specs/                    # Especificaciones de protocolo y contratos [CONFIRMADO]
│   ├── methodology.md                      # Metodología de auditoría epistémica [CONFIRMADO]
│   ├── scoring.md                          # Formulación matemática del IRC [CONFIRMADO]
│   └── terminology.md                      # Glosario técnico y definiciones [CONFIRMADO]
├── Engine/                                 # Documentación del motor interno
│   └── EngineReadme.md                     # Visión general del motor de evaluación [CONFIRMADO]
├── examples/                               # Payloads JSON de prueba para validación CLI/SDK
│   ├── ambiguous-task.json                 # Caso de ambigüedad de tarea [CONFIRMADO]
│   ├── contaminated-context.json           # Caso de contaminación de contexto [CONFIRMADO]
│   ├── healthy-conversation.json           # Caso de contexto saludable [CONFIRMADO]
│   ├── instruction-conflict.json           # Caso de conflicto de instrucciones [CONFIRMADO]
│   └── tool-state-drift.json               # Caso de desincronización de herramientas [CONFIRMADO]
├── infrastructure/                         # Configuraciones de despliegue e infraestructura [CONFIRMADO]
├── logs/                                   # Logs de ejecución del sistema [CONFIRMADO]
├── Notebooks/                              # Notebooks de análisis y experimentación [CONFIRMADO]
├── prompts/                                # Prompts de evaluación epistémica (EN/ES)
│   ├── auditor-simple-en.md                # Versión ligera en inglés [CONFIRMADO]
│   ├── auditor-simple-es.md                # Versión ligera en español [CONFIRMADO]
│   ├── auditor-technical-en.md             # Versión técnica detallada en inglés [CONFIRMADO]
│   ├── auditor-technical-es.md             # Versión técnica detallada en español [CONFIRMADO]
│   └── v0-original.md                      # Prompt v0 de referencia inicial [CONFIRMADO]
├── schemas/                                # JSON Schemas para contrato I/O
│   ├── audit-input.schema.json             # Esquema de validación de entrada [CONFIRMADO]
│   └── audit-result.schema.json            # Esquema de validación de salida [CONFIRMADO]
├── scripts/                                # Scripts auxiliares y herramientas de desarrollo
│   ├── Context Entropy Auditor.md         # Notas de ejecución del script [CONFIRMADO]
│   └── evaluate.py                         # Script de evaluación de benchmarks [CONFIRMADO]
├── src/                                    # Código fuente principal de la aplicación
│   ├── context_auditor/                    # Paquete core
│   │   ├── adapters/                       # Adaptadores de modelos LLM (BaseLLMAdapter, Gemini) [CONFIRMADO]
│   │   ├── auditor.py                      # Clase principal ContextAuditor [CONFIRMADO]
│   │   ├── cli.py                          # CLI runner (`context-auditor`) [CONFIRMADO]
│   │   ├── models.py                       # Modelos de datos Pydantic [CONFIRMADO]
│   │   ├── normalizers.py                  # Normalizadores de payload [CONFIRMADO]
│   │   ├── policies.py                     # Motor de políticas y modos de acción [CONFIRMADO]
│   │   ├── scoring.py                      # Motor de puntuación e IRC [CONFIRMADO]
│   │   ├── signals.py                      # Extractor de señales deterministas [CONFIRMADO]
│   │   └── validators.py                   # Validadores JSonschema [CONFIRMADO]
│   ├── data_generation/                    # Generadores de dataset sintéticos [CONFIRMADO]
│   └── fabric_jobs/                        # Jobs de pipeline de datos en batch [CONFIRMADO]
├── tests/                                  # Suite de pruebas automatizadas
│   ├── e2e/                                # Pruebas End-to-End [CONFIRMADO]
│   ├── fixtures/                           # Fixtures de prueba [CONFIRMADO]
│   └── unit/                               # Pruebas unitarias [CONFIRMADO]
├── Tools/                                  # Herramientas de soporte del entorno [CONFIRMADO]
├── CONTRIBUTING.md                         # Guía de contribución al proyecto [CONFIRMADO]
├── LICENSE                                 # Licencia MIT [CONFIRMADO]
├── pyproject.toml                          # Manifiesto del proyecto Python [CONFIRMADO]
├── README.md                               # Documentación principal del repositorio [CONFIRMADO]
└── ROADMAP.md                              # Hoja de ruta del proyecto y versiones [CONFIRMADO]
```

### 2.1 Diferenciaciones Clave
*   `src/context_auditor/`: Contiene el paquete ejecutable del motor de auditoría (CLI y SDK). `[CONFIRMADO]`
*   `schemas/` vs `src/context_auditor/models.py`: `schemas/` define los esquemas JSON canónicos independientes de lenguaje (`audit-input.schema.json` y `audit-result.schema.json`), mientras que `models.py` define las clases Pydantic v2 correspondientes para Python. `[CONFIRMADO]`
*   `config/scoring_defaults.yaml`: Define los parámetros configurables de peso y umbrales por defecto consumidos por `scoring.py`. `[CONFIRMADO]`

---

## 3. EXECUTION FLOW

### 3.1 Flujo E2E (Pipeline de Auditoría)

```mermaid
flowchart TD
    A[Raw Input Payload JSON] --> B[normalize_input()]
    B --> C[AuditInput Model]
    C --> D[extract_deterministic_signals()]
    D --> E[BaseLLMAdapter.evaluate_context()]
    E --> F[DimensionScores & Findings]
    F --> G[compute_irc()]
    G --> H[Risk Score IRC & Overall Status]
    H --> I[PolicyEngine.process_actions()]
    I --> J[Filtered RecommendedActions]
    J --> K[validate_result()]
    K --> L[AuditResult JSON / Model]
```

### 3.2 Entry Points
1.  **CLI Interface:** `context-auditor <input.json> [--factual] [--policy MODE]` `[CONFIRMADO]` (`pyproject.toml`, `src/context_auditor/cli.py`)
2.  **SDK Programático:**
    ```python
    from src.context_auditor.auditor import ContextAuditor
    from src.context_auditor.policies import PolicyMode

    auditor = ContextAuditor(llm_adapter=adapter, policy_mode=PolicyMode.RECOMMEND)
    result = auditor.audit(raw_input_dict, task_requires_factual=False)
    ```
    `[CONFIRMADO]` (`src/context_auditor/auditor.py`)

### 3.3 Datos: Origen, Transformación y Persistencia
*   **Origen:** Mensajes del sistema/usuario, llamadas a herramientas, resultados de herramientas y documentos RAG formateados según `audit-input.schema.json`. `[CONFIRMADO]` (`schemas/audit-input.schema.json`)
*   **Transformación:**
    1. Signals deterministas: cálculo de conteos, hashes de duplicidad e integridad. `[CONFIRMADO]` (`signals.py`)
    2. Clasificación semántica: extracción de puntuaciones en 6 dimensiones (0-100), evidencia (`observed`/`inferred`) y recomendaciones. `[CONFIRMADO]` (`auditor.py`)
    3. Puntuación agregada: suma ponderada + reglas de anulación `override_rules` (p. ej. `state_integrity == 100` fuerza `status = high/critical`). `[CONFIRMADO]` (`scoring.py`, `scoring_defaults.yaml`)
*   **Persistencia:** La auditoría produce un `AuditResult` serializable a JSON conforme a `audit-result.schema.json`. `[CONFIRMADO]` (`validators.py`)

---

## 4. CURRENT STATE & RULES

### 4.1 Foco Actual y Estado de Madurez
*   **Versión Actual en pyproject.toml:** `0.5.0` `[CONFIRMADO]` (`pyproject.toml`)
*   **Fase del Proyecto:** Alpha / Public SDK & CLI Foundation (`v0.5-public` en roadmap). `[CONFIRMADO]` (`ROADMAP.md`)
*   **Foco Activo:** Calibración de reglas de anulación, soporte para adaptadores de proveedores (Gemini) e integración con conjuntos de prueba de evaluación. `[CONFIRMADO]` (`ROADMAP.md`)

### 4.2 Reglas de Código y Convenciones
*   **Principio Epistémico:** Delineación estricta entre datos observados (presentes en texto) e inferidos (deducciones lógicas). `[CONFIRMADO]` (`README.md`)
*   **Validación de Modelos:** Uso prioritario de Pydantic v2 en `models.py` y validación estricta contra esquemas JSON en `validators.py`. `[CONFIRMADO]` (`src/context_auditor/validators.py`)
*   **Seguridad por Defecto:** Las acciones destructivas (ej. purgar contexto o memoria) requieren explícitamente aprobación de política (`requires_policy_approval = True`). `[CONFIRMADO]` (`policies.py`)

### 4.3 Convenciones de Directorios
*   Código ejecutable bajo `src/context_auditor/`. `[CONFIRMADO]`
*   Esquemas JSON canónicos en `schemas/`. `[CONFIRMADO]`
*   Casos de prueba de payloads en `examples/`. `[CONFIRMADO]`
*   Prompts en `prompts/` categorizados por idioma y nivel de complejidad (`simple`/`technical`). `[CONFIRMADO]`

---

## 5. ECOSYSTEM CONTEXT

*   **Iniciativa:** HyperScale Thinking — Research and Development. `[CONFIRMADO]` (`pyproject.toml`)
*   **Integraciones Objetivo:** Frameworks de agentes LLM, orquestadores RAG y capas de guardrails/seguridad agentica. `[CONFIRMADO]` (`README.md`)
*   **Adaptadores de LLM:** `BaseLLMAdapter` extensible (implementación inicial orientada a Google Gemini API). `[CONFIRMADO]` (`auditor.py`, `ROADMAP.md`)

---

## 6. CONFIGURATION REFERENCE

| Variable / Parámetro | Tipo | Default | Efecto | Sensible (Sí/No) |
| :--- | :--- | :--- | :--- | :--- |
| `weights.instruction_conflict` | float | `0.20` | Peso de la dimensión de conflicto de instrucciones en IRC | No `[CONFIRMADO]` (`scoring_defaults.yaml`) |
| `weights.task_ambiguity` | float | `0.20` | Peso de la dimensión de ambigüedad de tarea en IRC | No `[CONFIRMADO]` (`scoring_defaults.yaml`) |
| `weights.context_contamination` | float | `0.20` | Peso de la dimensión de contaminación de contexto | No `[CONFIRMADO]` (`scoring_defaults.yaml`) |
| `weights.evidence_quality` | float | `0.15` | Peso de la dimensión de calidad de evidencia | No `[CONFIRMADO]` (`scoring_defaults.yaml`) |
| `weights.state_integrity` | float | `0.15` | Peso de la dimensión de integridad de estado | No `[CONFIRMADO]` (`scoring_defaults.yaml`) |
| `weights.redundancy_pressure` | float | `0.10` | Peso de la dimensión de presión por redundancia | No `[CONFIRMADO]` (`scoring_defaults.yaml`) |
| `thresholds.stable` | float | `24.99` | Umbral superior para estado `stable` | No `[CONFIRMADO]` (`scoring_defaults.yaml`) |
| `thresholds.moderate` | float | `49.99` | Umbral superior para estado `moderate` | No `[CONFIRMADO]` (`scoring_defaults.yaml`) |
| `thresholds.high` | float | `74.99` | Umbral superior para estado `high` | No `[CONFIRMADO]` (`scoring_defaults.yaml`) |
| `thresholds.critical` | float | `100.0` | Umbral superior para estado `critical` | No `[CONFIRMADO]` (`scoring_defaults.yaml`) |
| `policy_mode` | Enum | `PolicyMode.RECOMMEND` | Modo del motor de políticas (`audit_only`, `recommend`, `human_review`, `dry_run`) | No `[CONFIRMADO]` (`policies.py`) |
| `GEMINI_API_KEY` | string | `None` | Key para invocación de Gemini Adapter | **Sí** (`<REDACTED>`) `[INFERIDO]` |

---

## 7. SEGURIDAD, RIESGOS Y FAILURE MODES

### 7.1 Security Findings
*   **Acciones Destructivas:** El motor de políticas previene la ejecución automática de acciones marcadas como `destructive` sin autorización de política explicita. `[CONFIRMADO]` (`policies.py`)
*   **Gestión de Secretos:** No existen contraseñas ni claves hardcodeadas en el código base. `[CONFIRMADO]`

### 7.2 Failure Modes
1.  **Fallo de Adaptador LLM:** Si la API del LLM clasificador no responde o retorna un formato inválido, la evaluación de fallback detiene el proceso lanzando una excepción de validación o retornando un error de esquema. `[CONFIRMADO]` (`auditor.py`)
2.  **Entrada Inválida:** Si el payload JSON no cumple con `audit-input.schema.json`, `normalize_input` / `validators.py` rechazan la solicitud antes de consumir cuotas de LLM. `[CONFIRMADO]` (`auditor.py`)
3.  **Regla de Anulación Crítica (Override Rule):** Si la integridad de estado o la calidad de evidencia factual colapsan (`state_integrity == 100` o `evidence_quality == 100` en tareas factuales), el estatus del contexto se eleva automáticamente a `critical` anulando el promedio ponderado. `[CONFIRMADO]` (`scoring_defaults.yaml`, `scoring.py`)

### 7.3 Riesgos Técnicos
*   **Calibración Provisional:** Todos los pesos y umbrales son provisionales hasta su validación empírica con datasets etiquetados de producción. `[CONFIRMADO]` (`ROADMAP.md`)
*   **Latencia de Auditoría:** La evaluación semántica introduce una llamada a LLM adicional fuera de banda antes de permitir la ejecución de la tarea. `[INFERIDO]`

---

## 8. ESTRATEGIA DE PRUEBAS (SECCIÓN OPCIONAL)

*   **Pruebas Unitarias (`tests/unit/`):** Cobertura de señales deterministas, cálculo de IRC, validación de esquemas y reglas de política. `[CONFIRMADO]`
*   **Pruebas E2E (`tests/e2e/`):** Evaluación completa de payloads contenidos en `examples/` (`healthy-conversation.json`, `contaminated-context.json`, `tool-state-drift.json`, `instruction-conflict.json`, `ambiguous-task.json`). `[CONFIRMADO]`
*   **Comando de Ejecución:**
    ```bash
    pytest tests/
    ```
    `[CONFIRMADO]` (`pyproject.toml`)

---

## 9. CONTEXT HANDOFF

Este documento es la fuente primaria de contexto técnico portable para el proyecto **Context Entropy Auditor (CEA)**.

**Archivos Principales de Referencia:**
*   [pyproject.toml](file:///d:/0001%20HyperScale%20Thinking/PROYECTOS%20CLOUD/Research%20and%20Development/Context%20Entropy%20Auditor%20%28CEA%29/pyproject.toml)
*   [README.md](file:///d:/0001%20HyperScale%20Thinking/PROYECTOS%20CLOUD/Research%20and%20Development/Context%20Entropy%20Auditor%20%28CEA%29/README.md)
*   [ROADMAP.md](file:///d:/0001%20HyperScale%20Thinking/PROYECTOS%20CLOUD/Research%20and%20Development/Context%20Entropy%20Auditor%20%28CEA%29/ROADMAP.md)
*   [auditor.py](file:///d:/0001%20HyperScale%20Thinking/PROYECTOS%20CLOUD/Research%20and%20Development/Context%20Entropy%20Auditor%20%28CEA%29/src/context_auditor/auditor.py)
*   [scoring_defaults.yaml](file:///d:/0001%20HyperScale%20Thinking/PROYECTOS%20CLOUD/Research%20and%20Development/Context%20Entropy%20Auditor%20%28CEA%29/config/scoring_defaults.yaml)
