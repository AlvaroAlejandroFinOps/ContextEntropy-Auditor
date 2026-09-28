<!-- ============================================================================== -->
<!-- THINKINGSEED: ADN DEL PROYECTO (CONTEXTO PASIVO PARA MODELOS DE LENGUAJE)     -->
<!-- ============================================================================== -->
> [!NOTE]
> ### 🧬 DEFINICIÓN Y ROL DE ESTE DOCUMENTO
> 1. **¿Qué es este archivo?:** Este documento es una **Semilla de Proyecto (ThinkingSeed Master)**: representa el **ADN arquitectónico, técnico y estructural exhaustivo** del sistema. **NO es el repositorio completo de código fuente**, sino su mapa genético y memoria técnica profunda extraída directamente del entorno de desarrollo.
> 2. **Estado de Avance (Work in Progress):** Este documento refleja el **estado actual del desarrollo**. No garantiza que el proyecto esté concluido al 100%; puede representar un prototipo, un MVP o un sistema en evolución continua. La ausencia de código completo en ciertos archivos o módulos es **deliberada por diseño** para optimizar ventana de contexto o refleja áreas aún en desarrollo.
> 3. **Modo de Operación:** Trata este documento como **contexto pasivo de referencia técnica (Ground Truth)**. No asumas que el archivo está defectuoso ni intentes reescribirlo por tu cuenta.
<!-- ============================================================================== -->

# THINKING SEED MASTER: Context Entropy Auditor (CEA)

## 0. IDENTIDAD Y METADATOS
```yaml
seed_schema_version: "2.0"
project_name: "Context Entropy Auditor"
repository_name: "Context Entropy Auditor (CEA)"
project_type: "library"
repository_mode: "single-project"
generated_at: "2026-09-27T16:34:00-03:00"
generated_by: "Antigravity Agent (Gemini 3.8 Flash)"
repository_root: "d:/0001 HyperScale Thinking/PROYECTOS CLOUD/Research and Development/Context Entropy Auditor (CEA)"
git_branch: "master"
git_commit: "1820f44"
working_tree_state: "dirty"
analysis_mode: "static"
coverage_level: "high"
known_analysis_limits:
  - "Validación de inferencia LLM remota con Gemini requiere clave API GEMINI_API_KEY en variables de entorno."
  - "Inferencia LLM local soportada y verificada mediante el CLI de Antigravity (agy.exe) en PATH."
  - "Modelos locales testeados: gemini-3.7-flash, gemini-3.1-pro, gemini-3.8-flash, gemini-3.6-flash con niveles de esfuerzo de pensamiento (low, medium, high, max)."
```

### 0.1 Instrucciones para el modelo receptor
1. **ADN vs Repositorio:** Reconoce este documento como la memoria técnica y el ADN del proyecto, no como el repositorio completo ni como una prueba de ejecución.
2. **Contexto Pasivo:** No generes código no solicitado ni reclames por archivos ausentes; espera instrucciones específicas del usuario o utilízalo como contexto pasivo para responder preguntas sobre el funcionamiento del sistema.
3. **Estado de Avance:** Considera que las secciones incompletas o componentes marcados como `[FALTANTE]` representan el avance real del proyecto y oportunidades de asistencia, no errores del documento.
4. **Evidencia:** Respeta las etiquetas de evidencia (`[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]`, `[NO VERIFICADO]`, `[FALTANTE]`) y no transformes inferencias en hechos.
5. **Rutas:** Antes de proponer cambios, identifica módulos y archivos afectados citando sus rutas exactas relativas al repositorio.
6. **Contratos:** Conserva arquitectura, convenciones, contratos y restricciones declaradas.
7. **Preguntas Dirigidas:** No inventes componentes ausentes. Formula preguntas solo cuando la incertidumbre impida una respuesta segura.
8. **Seguridad:** No reveles ni solicites secretos. Usa placeholders (`<REDACTED>`).
9. **Impacto:** Evalúa impactos laterales en pruebas, configuración, datos, seguridad, observabilidad y despliegue.
10. **Asistencia:** Distingue entre solución inmediata, deuda técnica y recomendación futura.

---

## 1. RESUMEN EJECUTIVO

### 1.1 Proyecto en una frase
`[CONFIRMADO]` **Context Entropy Auditor (CEA)** es un framework y suite interactiva de diagnóstico epistémico y fiabilidad contextual para aplicaciones con Modelos de Lenguaje (LLMs), diseñado para auditar el Índice de Riesgo Contextual (IRC / CRS) a través de 6 dimensiones fundamentales, combinando extracción heurística determinista y evaluación semántica mediante adaptadores desacoplados (Google Gemini API y Antigravity CLI local).

### 1.2 Problema que resuelve
- **Degradación de señal y fatiga contextual:** Pérdida de coherencia, interferencia entre turnos contradictorios y dilución de restricciones críticas en ventanas de contexto extensas `[CONFIRMADO]`.
- **Confabulación mecanicista:** Tendencia frecuente de los evaluadores basados en LLMs a inventar fallas internas de atención o estados no observables de KV Cache sin evidencia física `[CONFIRMADO]`.
- **Falta de evaluación determinista combinada:** Ausencia de herramientas que integren métricas heurísticas objetivas (recencia del objetivo, drift de herramientas, redundancia documental) con clasificación semántica estricta bajo contratos JSON Schema `[CONFIRMADO]`.
- **Inferencia local y evaluación de estrés:** Necesidad de auditar y estresar modelos turno a turno en entornos de desarrollo sin exponer claves de API ni depender de servicios cloud externos `[CONFIRMADO]`.

### 1.3 Usuarios o sistemas consumidores
- **Ingenieros de Agentes y Arquitecturas LLM:** Auditoría previa y continua de las ventanas de contexto antes del dispatch a modelos de frontera `[CONFIRMADO]`.
- **Suites de Evaluación y CI/CD:** Banco de pruebas automatizado contra datasets adversariales para prevenir regresiones en prompts `[CONFIRMADO]`.
- **Desarrolladores y QA en Antigravity IDE:** Simulación interactiva (Live Stress Test) evaluando la respuesta de múltiples modelos y esfuerzos de pensamiento (`effort: low|medium|high|max`) `[CONFIRMADO]`.
- **Governance & Reliability Teams:** Auditoría formal y generación de reportes periciales de riesgo operacional `[DECLARADO]`.

### 1.4 Alcance y límites del sistema
- **In Scope:**
  - Diagnóstico formal de 6 dimensiones contextuales: `instruction_conflict`, `task_ambiguity`, `context_contamination`, `evidence_quality`, `state_integrity`, `redundancy_pressure` `[CONFIRMADO]`.
  - Normalizador determinista y parser de entrada tolerante a fallos `[CONFIRMADO]`.
  - Extractor de señales heurísticas deterministas (conteo de turnos, ratio de utilización de contexto, detección de duplicados, reemplazos de herramientas, recencia del objetivo) `[CONFIRMADO]`.
  - Motor de cálculo de Índice de Riesgo Contextual (IRC / CRS) con ponderaciones configurables y reglas de sobrescritura de seguridad (override rules) `[CONFIRMADO]`.
  - Motor de políticas de recomendación (`audit_only`, `recommend`, `human_review`, `dry_run`) `[CONFIRMADO]`.
  - Arquitectura Hexagonal de adaptadores: `GeminiAdapter` (API remota) y `AntigravityAdapter` (CLI local `agy.exe`) `[CONFIRMADO]`.
  - CLI unificado con auto-detección y launcher PowerShell (`run_audit.ps1`) `[CONFIRMADO]`.
  - Suite interactiva de benchmark y Live Stress Test (`InteractiveAuditorCLI`) con telemetría de tokens y persistencia automática de reportes en Markdown y JSON `[CONFIRMADO]`.
- **Out of Scope:**
  - Inferencia sobre estados mecanicistas de capas de atención, activaciones internas o memoria GPU/TPU (violación explícita del Contrato Epistémico) `[CONFIRMADO]`.
  - Modificación automática no supervisada o mutación en caliente de prompts en ejecución `[DECLARADO]`.

---

## 2. ARQUITECTURA Y TOPOLOGÍA

### 2.1 Estilo arquitectónico
`[CONFIRMADO]` Arquitectura limpia y modular basada en **Puertos y Adaptadores (Clean Architecture / Hexagonal Architecture)** con diseño **Schema-First**:
- **Núcleo de Dominio:** Modelos Pydantic v2 puros (`models.py`), motor de scoring determinista (`scoring.py`), extractor heurístico (`signals.py`) y motor de políticas (`policies.py`).
- **Puertos:** `BaseLLMAdapter` en `adapters/base.py`.
- **Adaptadores Concretos:** `GeminiAdapter` (Google GenAI SDK) y `AntigravityAdapter` (ejecución subprocess de `agy.exe`).
- **Orquestador (Fachada):** `ContextAuditor` en `auditor.py`.
- **Presentación e Interacción:** `cli.py` y `interactive.py` (`InteractiveAuditorCLI`).

### 2.2 Árbol estructural del repositorio
```
Context Entropy Auditor (CEA)/
├── .agentignore                           # Exclusiones de indexación para agentes IA
├── .context/                              # Metadatos del grafo topológico de gobernanza
│   └── tree.json
├── .gitignore
├── .pytest_cache/
├── 01_seed/                               # Memoria técnica pasiva y ADN arquitectónico
│   ├── .context.yaml
│   └── seed-context-entropy-auditor-master.md
├── 02_foundation/                         # Fundamentos de arquitectura y gobernanza
│   └── engine/
│       ├── .context.yaml
│       └── engine_readme.md
├── 03_research/                           # Área de experimentación, notebooks y prompts
│   ├── experiments/
│   │   └── .context.yaml
│   ├── notebooks/
│   │   └── .context.yaml
│   └── prompts/
│       └── .context.yaml
├── artifacts/                             # Artefactos, métricas y fases completadas
│   ├── Fases/                             # Incrementos de desarrollo documentados (Inc0 - Inc7)
│   ├── plans/                             # Planes activos y archivados
│   │   ├── active/
│   │   │   └── INFERRED_ROADMAP.md
│   │   └── archive/
│   ├── Task del agente/                   # Tareas y tracking operacional
│   │   └── task.md
│   ├── MetricsThinking.json               # Telemetría de auditoría de madurez (52.92%)
│   └── MetricsThinking.md                 # Reporte formal de madurez del proyecto
├── config/                                # Configuraciones operacionales
│   ├── .context.yaml
│   └── scoring_defaults.yaml              # Ponderaciones, umbrales y reglas de override
├── data/                                  # Almacenamiento local de datos
│   ├── processed/
│   ├── raw/
│   └── sandbox/
├── dataset/                               # Datasets de evaluación y autodiagnóstico
│   ├── eval_dataset.jsonl                 # Dataset de evaluación con casos representativos
│   └── self_audit.json                    # Carga real de autodiagnóstico del sistema
├── docs/                                  # Documentación técnica y epistémica
│   ├── methodology.md                     # Contrato epistémico y límites de observabilidad
│   ├── scoring.md                         # Formulación matemática del IRC y rúbricas
│   └── terminology.md                     # Taxonomía formal bilingüe de modos de falla
├── examples/                              # Payloads de prueba para simulación
│   ├── ambiguous-task.json
│   ├── contaminated-context.json
│   ├── healthy-conversation.json
│   ├── instruction-conflict.json
│   └── tool-state-drift.json
├── logs/                                  # Registros y persistencia de benchmarks
│   ├── .context.yaml
│   └── benchmarks/                        # Subcarpetas generadas por sesión interactiva
│       └── <session_id>/
│           ├── session_meta.json
│           ├── conversation.json
│           ├── timeline.json
│           └── summary_report.md
├── prompts/                               # Prompts del sistema auditores estandarizados
│   ├── auditor-simple-en.md
│   ├── auditor-simple-es.md
│   ├── auditor-technical-en.md
│   ├── auditor-technical-es.md
│   └── v0-original.md
├── schemas/                               # Contratos JSON Schema oficiales (Draft 7 / 2020-12)
│   ├── .context.yaml
│   ├── audit-input.schema.json
│   └── audit-result.schema.json
├── scripts/                               # Scripts utilitarios y de evaluación
│   ├── .context.yaml
│   ├── Context Entropy Auditor.md
│   └── evaluate.py
├── src/
│   └── context_auditor/                   # Paquete principal Python
│       ├── __init__.py
│       ├── auditor.py                     # Orquestador ContextAuditor
│       ├── cli.py                         # Entry point CLI con resolución de adaptadores
│       ├── interactive.py                 # Suite Interactiva & Live Stress Test CLI
│       ├── models.py                      # Modelos de dominio canónicos Pydantic v2
│       ├── policies.py                    # Motor de políticas y filtrado de acciones
│       ├── scoring.py                     # Cálculo matemático del IRC y overrides
│       ├── signals.py                     # Extracción de señales heurísticas deterministas
│       ├── validators.py                  # Validación contra schemas/
│       ├── adapters/
│       │   ├── __init__.py                # Exportación unificada de adaptadores
│       │   ├── base.py                    # Puerto abstracto BaseLLMAdapter y excepciones
│       │   ├── antigravity.py             # Adaptador local para CLI agy.exe
│       │   └── gemini.py                  # Adaptador para Google Gemini API
│       └── normalizers/
│           └── __init__.py                # Normalizador tolerante de entrada
├── tests/                                 # Suite automatizada (36 tests)
│   ├── .context.yaml
│   ├── fixtures/                          # Fixtures de prueba
│   ├── e2e/
│   │   └── test_cli.py                    # Pruebas e2e de CLI y opciones interactivas
│   └── unit/
│       ├── test_antigravity_adapter.py    # Pruebas completas del adaptador agy.exe
│       ├── test_interactive_session.py    # Pruebas de persistencia y telemetría de sesión
│       ├── test_normalizers.py            # Pruebas de normalización
│       ├── test_policies.py               # Pruebas del motor de políticas
│       ├── test_scoring.py                # Pruebas de cálculo de IRC y overrides
│       ├── test_signals.py                # Pruebas de extracción de señales
│       └── test_validators.py             # Pruebas de validación de esquemas JSON
├── CONTRIBUTING.md
├── Context Entropy Auditor.md
├── Entropy.jpeg
├── LICENSE
├── README.md                              # Documentación general en inglés
├── README_ES.md                           # Documentación general en español
├── ROADMAP.md                             # Roadmap del proyecto
├── pyproject.toml                         # Manifiesto formal de empaquetado Python
├── resultado_auditoria.json               # Evidencia de ejecución real de auto-auditoría
└── run_audit.ps1                          # Launcher PowerShell para Windows
```

### 2.3 Responsabilidad por directorio y archivo clave
- `src/context_auditor/auditor.py`: Fachada principal del SDK (`ContextAuditor`). Orquesta el pipeline de auditoría: normalización, extracción de señales, evaluación semántica del adaptador, cálculo de IRC, filtrado de acciones por políticas y validación de salida `[CONFIRMADO]`.
- `src/context_auditor/models.py`: Entidades canónicas fuertemente tipadas en Pydantic v2 (`AuditInput`, `AuditResult`, `Message`, `Role`, `ToolEvent`, `Document`, `DimensionScores`, `Finding`, `RecommendedAction`, `OverallStatus`, `EpistemicStatus`) `[CONFIRMADO]`.
- `src/context_auditor/adapters/antigravity.py`: Adaptador local para el CLI `agy.exe`. Maneja la compilación de prompts, invocación por subprocess con argumentos de razonamiento (`--effort`), timeout, sanitización de envolturas JSON y code fences `[CONFIRMADO]`.
- `src/context_auditor/adapters/gemini.py`: Adaptador remoto para la API de Google Gemini utilizando el SDK `google.genai` `[CONFIRMADO]`.
- `src/context_auditor/adapters/base.py`: Define el contrato abstracto `BaseLLMAdapter` y la excepción canónica `AdapterExecutionError` `[CONFIRMADO]`.
- `src/context_auditor/interactive.py`: Implementa `BenchmarkSession` (gestión de sesiones, timeline, telemetría y reportes markdown/json) y `InteractiveAuditorCLI` (interfaz de consola a color con menús de simulación, stress test en vivo turno a turno, cambio dinámico de modelos/effort y visualización histórica) `[CONFIRMADO]`.
- `src/context_auditor/scoring.py`: Implementa el cálculo formal ponderado del IRC y las 5 reglas de sobrescritura crítica (overrides) desde `config/scoring_defaults.yaml` `[CONFIRMADO]`.
- `src/context_auditor/signals.py`: Analizador heurístico determinista sin LLM (conteo de turnos, ratio de utilización de contexto, detección de duplicados, reemplazos de herramientas, recencia del objetivo) `[CONFIRMADO]`.
- `src/context_auditor/policies.py`: Motor de gobernanza operacional con modos `audit_only`, `recommend`, `human_review`, `dry_run` `[CONFIRMADO]`.
- `src/context_auditor/validators.py`: Validación estricta contra esquemas formales JSON Schema en `schemas/` `[CONFIRMADO]`.
- `run_audit.ps1`: Script PowerShell de arranque rápido en Windows con verificación de `agy.exe` en PATH y parámetros CLI amigables `[CONFIRMADO]`.

### 2.4 Límites modulares y acoplamiento
- `[CONFIRMADO]` El núcleo analítico (`scoring.py`, `signals.py`, `models.py`) está 100% desacoplado de dependencias de proveedores de inferencia y frameworks de red.
- `[CONFIRMADO]` Cualquier nuevo proveedor (OpenAI, Anthropic, Ollama, vLLM) puede incorporarse simplemente implementando `BaseLLMAdapter` sin tocar una sola línea del core de auditoría ni del cálculo de IRC.

---

## 3. FLUJOS DE EJECUCIÓN Y ENTRY POINTS

### 3.1 Puntos de entrada principales
1. **Launcher Windows PowerShell (`run_audit.ps1`):**
   ```powershell
   .\run_audit.ps1 -Interactive
   .\run_audit.ps1 -File examples/ambiguous-task.json -Model gemini-3.7-flash -Effort high
   ```
2. **CLI de Línea de Comandos (`src/context_auditor/cli.py`):**
   ```bash
   python -m context_auditor.cli examples/instruction-conflict.json --adapter antigravity --model gemini-3.7-flash --effort medium
   python -m context_auditor.cli --interactive
   ```
3. **SDK Programático en Python:**
   ```python
   from src.context_auditor.auditor import ContextAuditor
   from src.context_auditor.adapters.antigravity import AntigravityAdapter
   from src.context_auditor.policies import PolicyMode

   adapter = AntigravityAdapter(model="gemini-3.7-flash", effort="high")
   auditor = ContextAuditor(llm_adapter=adapter, policy_mode=PolicyMode.RECOMMEND)
   result = auditor.audit(raw_payload)
   ```
4. **Script de Evaluación por Lotes:**
   ```bash
   python scripts/evaluate.py dataset/eval_dataset.jsonl
   ```

### 3.2 Diagrama de flujo principal E2E
```
                     [Payload JSON de Entrada]
                                 │
                                 ▼
                     [validators.py: validate_input]
                                 │
                     ┌───────────┴───────────┐
                     │ (Válido)              │ (Inválido)
                     ▼                       ▼
            [normalizers.py]        [ValidationError: Exit 1]
                     │
         ┌───────────┴───────────────────────────────┐
         ▼                                           ▼
[signals.py: extract_deterministic_signals]   [BaseLLMAdapter: evaluate_context]
  • Message counts & turns                     ├── AntigravityAdapter (agy.exe)
  • Token estimation & utilization             └── GeminiAdapter (google.genai)
  • Document exact duplicates                                │
  • Stale tool drift detection                               │
  • Last objective recency                                   ▼
         │                                      [Semantic Dimension Scores]
         │                                      [Findings & Recommendations]
         └───────────────────┬───────────────────────────────┘
                             ▼
                [scoring.py: compute_irc]
                  • Weighted Linear IRC (0 - 100)
                  • Override Rules Evaluation
                  • Base Status Determination
                             │
                             ▼
                [policies.py: PolicyEngine]
                  • Filter destructive actions
                  • Enforce approval flags
                             │
                             ▼
                [validators.py: validate_result]
                             │
                             ▼
              [AuditResult: JSON / Report / CLI]
```

### 3.3 Ciclo de vida de la ejecución y estados
- **Estados de Severidad Contextual (`OverallStatus`):**
  - `stable` (IRC: 0.0 - 24.9) `[CONFIRMADO]`
  - `moderate` (IRC: 25.0 - 49.9) `[CONFIRMADO]`
  - `high` (IRC: 50.0 - 74.9) `[CONFIRMADO]`
  - `critical` (IRC: 75.0 - 100.0) `[CONFIRMADO]`
- **Reglas de Sobrescritura de Riesgo (Override Rules):**
  - `critical_conflict_high_risk`: Si `instruction_conflict == 100` y el estado era `stable` o `moderate`, se eleva forzosamente a `high` `[CONFIRMADO]`.
  - `critical_state_high_risk`: Si `state_integrity == 100` y el estado era `stable` o `moderate`, se eleva forzosamente a `high` `[CONFIRMADO]`.
  - `critical_evidence_critical_risk`: Si `evidence_quality == 100` en tareas declaradas factuales (`task_requires_factual=True`), se eleva a `critical` `[CONFIRMADO]`.
  - `low_coverage_warning` & `low_coverage_prevented_stable`: Si `evidence_coverage < 0.30`, no se permite declarar estado `stable`, forzando `moderate` `[CONFIRMADO]`.
- **Clasificación Epistémica (`EpistemicStatus`):**
  - `observed`: Evidencia directamente contrastada en el texto `[CONFIRMADO]`.
  - `inferred`: Deducción lógica justificada por la semántica `[CONFIRMADO]`.
  - `runtime_measured`: Medido heurísticamente por `signals.py` `[CONFIRMADO]`.
  - `unknown`: No verificable con la información provista `[CONFIRMADO]`.

---

## 4. MODELO DE DATOS, CONTRATOS Y PERSISTENCIA

### 4.1 Esquemas y entidades principales
- **`AuditInput`:**
  - `schema_version`: String semver (default: `"1.0.0"`).
  - `messages`: Lista de `Message` (`id`, `role: system|user|assistant|tool`, `content`, `timestamp`).
  - `documents`: Lista de `Document` (`id`, `content`, `source`, `confidence`).
  - `tool_events`: Lista de `ToolEvent` (`id`, `tool_name`, `parameters`, `result`, `timestamp`).
  - `runtime_telemetry`: Metadatos de ejecución (e.g. `latency_ms`, `tokens_consumed`).
  - `audit_configuration`: Opciones de auditoría (e.g. `context_limit_tokens`).
- **`AuditResult`:**
  - `schema_version`: `"1.0.0"`.
  - `audit_id`: Identificador único (e.g. `"audit-8f4b2a1c"`).
  - `overall_status`: Enum `stable`, `moderate`, `high`, `critical`.
  - `risk_score`: Float en rango `[0.0, 100.0]`.
  - `confidence`: Float en rango `[0.0, 1.0]`.
  - `evidence_coverage`: Float en rango `[0.0, 1.0]`.
  - `scope`: `AuditScope` (`messages_observed`, `documents_observed`, `tool_outputs_observed`).
  - `dimension_scores`: 6 enteros `[0, 100]` (`instruction_conflict`, `task_ambiguity`, `context_contamination`, `evidence_quality`, `state_integrity`, `redundancy_pressure`).
  - `findings`: Lista de `Finding` (`finding_id`, `dimension`, `epistemic_status`, `severity`, `evidence_refs`, `explanation`, `confidence`).
  - `recommended_actions`: Lista de `RecommendedAction` (`action`, `target_refs`, `reason`, `requires_policy_approval`, `destructive`).
  - `triggered_rules`: Lista de strings con los nombres de las reglas de override disparadas.
  - `limitations`: Lista de limitaciones metodológicas declaradas.

### 4.2 Almacenamiento, motores de base de datos y migraciones
- `[CONFIRMADO]` El núcleo es completamente **stateless**. No requiere bases de datos relacionales ni motores SQL.
- `[CONFIRMADO]` Persistencia estructurada en disco para sesiones de benchmark interactivo en `logs/benchmarks/<session_id>/`:
  1. `session_meta.json`: Metadatos del benchmark, modelos y recuentos.
  2. `conversation.json`: Contexto íntegro de la conversación auditada.
  3. `timeline.json`: Array cronológico de turnos evaluados con latencias, tokens y scores.
  4. `summary_report.md`: Reporte ejecutivo en Markdown con tabla comparativa de evolución del IRC.

### 4.3 Interfaces externas, payloads y contratos de API
- **Esquemas JSON formales:**
  - [`schemas/audit-input.schema.json`](file:///d:/0001%20HyperScale%20Thinking/PROYECTOS%20CLOUD/Research%20and%20Development/Context%20Entropy%20Auditor%20%28CEA%29/schemas/audit-input.schema.json) `[CONFIRMADO]`.
  - [`schemas/audit-result.schema.json`](file:///d:/0001%20HyperScale%20Thinking/PROYECTOS%20CLOUD/Research%20and%20Development/Context%20Entropy%20Auditor%20%28CEA%29/schemas/audit-result.schema.json) `[CONFIRMADO]`.
- **Contrato de Subprocess con Antigravity CLI:**
  - Invocación: `agy.exe --model <MODEL> [--effort <EFFORT>] --input-format text --output-format json --dangerously-skip-permissions` `[CONFIRMADO]`.
  - Sanitización: Parsing robusto tolerante a envolturas `{"status": "SUCCESS", "response": ...}`, bloques de código markdown triple backtick (` ```json `), y fallback regex `[CONFIRMADO]`.

---

## 5. CONFIGURACIÓN Y AMBIENTE

### 5.1 Tabla de variables de entorno y opciones de configuración
| Parámetro / Variable | Tipo | Default | Efecto | Sensible |
|:---|:---:|:---:|:---|:---:|
| `GEMINI_API_KEY` | Env Var (String) | `None` | Clave de acceso requerida si se utiliza `GeminiAdapter` | **Sí** |
| `CEA_CONFIG_PATH` | Env Var (Path) | `config/scoring_defaults.yaml` | Ruta alternativa a las ponderaciones de scoring | No |
| `--adapter` | CLI Flag | Auto-detect | Selecciona `antigravity` o `gemini` (si no hay clave pero existe `agy.exe`, auto-selecciona `antigravity`) | No |
| `--model` | CLI Flag | `gemini-3.7-flash` | Modelo LLM a utilizar para inferencia | No |
| `--effort` | CLI Flag | `medium` | Nivel de esfuerzo de pensamiento (`low`, `medium`, `high`, `max`) | No |
| `--agy-path` | CLI Flag | `agy.exe` | Ruta al ejecutable de Antigravity CLI | No |
| `--policy` | CLI Flag | `recommend` | Modo de política (`audit_only`, `recommend`, `human_review`, `dry_run`) | No |
| `--factual` | CLI Flag | `False` | Activa comprobaciones estrictas de evidencia y reglas para afirmaciones fácticas | No |

### 5.2 Perfiles de ejecución
- **Interactive Stress Test:** `python -m context_auditor.cli --interactive` o `.\run_audit.ps1 -Interactive` `[CONFIRMADO]`.
- **Batch Audit CLI:** Invocación directa contra archivos JSON para CI/CD `[CONFIRMADO]`.
- **SDK In-Memory:** Invocación limpia en pipelines agénticos sin persistencia en disco `[CONFIRMADO]`.
- **Offline / Mocks Unit Testing:** Suite completa ejecutable sin conexión a internet ni consumo de tokens `[CONFIRMADO]`.

### 5.3 Prerrequisitos de sistema e infraestructura
- Python >= 3.9 (Desarrollado y probado en Python 3.12.10 sobre Windows 11) `[CONFIRMADO]`.
- Dependencias de runtime declaradas en `pyproject.toml`:
  - `pydantic>=2.0.0`
  - `jsonschema>=4.0.0`
  - `pyyaml>=6.0`
- Dependencias de desarrollo:
  - `pytest>=7.0.0`
- Opcional para inferencia local offline:
  - `agy.exe` instalado en el PATH o especificado vía `--agy-path` `[CONFIRMADO]`.

---

## 6. PRUEBAS, CI/CD Y OPERACIÓN

### 6.1 Estrategia de pruebas
`[CONFIRMADO]` Suite de **36 pruebas automatizadas** ejecutadas y aprobadas al 100% con `pytest` en 5.00 segundos:
- `tests/unit/test_antigravity_adapter.py` (9 tests):
  - Inicialización y valores por defecto.
  - Invocación exitosa con mocks.
  - Sanitización de bloques Markdown (fences ` ```json `).
  - Desenvolvimiento de envoltura JSON de `agy.exe`.
  - Manejo de errores de proceso y retorno de código != 0.
  - Captura y excepción tipada ante `FileNotFoundError` (`agy.exe` ausente).
  - Manejo de timeouts (`subprocess.TimeoutExpired`).
  - Parsing tolerante ante respuestas JSON inválidas.
  - Resolución automática de adaptadores en CLI (`resolve_adapter`).
- `tests/unit/test_interactive_session.py` (2 tests):
  - Creación de sesión, tracking acumulativo de mensajes, documentos, herramientas y tokens.
  - Registro de turnos y persistencia completa de artefactos (`session_meta.json`, `conversation.json`, `timeline.json`, `summary_report.md`).
- `tests/unit/test_normalizers.py` (2 tests): Normalización de estructuras y rechazo de payloads inválidos.
- `tests/unit/test_policies.py` (3 tests): Políticas `audit_only`, `recommend` y `human_review`.
- `tests/unit/test_scoring.py` (5 tests): Cálculo de IRC, combinaciones de riesgo y las 4 reglas de override crítico.
- `tests/unit/test_signals.py` (7 tests): Estimación de tokens, conteo de mensajes, duplicación exacta de documentos, integridad de IDs, drift de herramientas y recencia del objetivo de usuario.
- `tests/unit/test_validators.py` (6 tests): Validación estricta contra esquemas de entrada y salida.
- `tests/e2e/test_cli.py` (2 tests): Ejecución de CLI end-to-end con archivo válido e inválido.

### 6.2 Automatización y pipelines CI/CD
- `[CONFIRMADO]` Manifiesto de empaquetado `pyproject.toml` configurado con build-backend de setuptools y entry point `context-auditor`.
- `[FALTANTE]` Pipeline de integración continua en GitHub Actions (`.github/workflows/ci.yml`).

### 6.3 Contenedores y orquestación
- `[DECLARADO]` Diseño modular preparado para contenedorización como microservicio REST/gRPC stateless o Cloud Run.

---

## 7. OBSERVABILIDAD Y MODOS DE FALLA

### 7.1 Logs, métricas y tracing
- **Telemetría de Tokens:** Estimación determinista turno a turno basada en ratios canónicos de caracteres/tokens (`signals.py`) `[CONFIRMADO]`.
- **Latencia de Inferencia:** Registro de tiempo transcurrido en segundos por cada llamada de evaluación semántica `[CONFIRMADO]`.
- **Evolución del IRC:** Tabla comparativa estructurada que traza el impacto de cada nuevo mensaje o documento sobre el riesgo contextual total `[CONFIRMADO]`.
- **Auditoría de Madurez de Proyecto:** Sincronizado formalmente con el estándar MetricsThinking™ (`artifacts/MetricsThinking.json`) `[CONFIRMADO]`.

### 7.2 Modos de falla conocidos y estrategias de recuperación
1. **Falta de API Key remota:** Si `GEMINI_API_KEY` no está configurada, el CLI resuelve automáticamente hacia `AntigravityAdapter` si `agy.exe` está disponible en el sistema `[CONFIRMADO]`.
2. **Falta de CLI Local:** Si `agy.exe` no existe o falla en ejecución, se lanza `AdapterExecutionError` con diagnóstico claro de instalación sin crashear el motor principal `[CONFIRMADO]`.
3. **Payloads LLM con formato imperfecto:** `_extract_json()` en `antigravity.py` ejecuta 4 capas consecutivas de deserialización defensiva (top-level dict, markdown fence regex, json.loads standard, y regex balanceado de llaves externas) `[CONFIRMADO]`.
4. **Violación de Contrato JSON Schema:** `validators.py` intercepta discrepancias antes del cálculo de scoring y durante la emisión de resultados `[CONFIRMADO]`.

### 7.3 Idempotencia y pureza
- Las funciones `compute_irc()` y `extract_deterministic_signals()` son funciones matemáticas puras: para un mismo payload de entrada, retornan idéntico resultado sin efectos colaterales `[CONFIRMADO]`.

---

## 8. SEGURIDAD Y PRIVACIDAD

### 8.1 Hallazgos de seguridad estática
- Sin secretos, claves de API ni credenciales hardcodeadas en ningún archivo del repositorio `[CONFIRMADO]`.
- Archivos `.agentignore` y `.gitignore` previenen la inclusión inadvertida de `.env`, `.venv`, `.pytest_cache` o credenciales temporales `[CONFIRMADO]`.

### 8.2 Manejo de autenticación, autorización y secretos
- Inferencia remota: Las credenciales son leídas exclusivamente desde el entorno del sistema (`os.environ.get("GEMINI_API_KEY")`) `[CONFIRMADO]`.
- Inferencia local: `AntigravityAdapter` delega el control de permisos y autenticación a la sesión activa del CLI `agy.exe`, permitiendo operaciones aisladas en entornos corporativos `[CONFIRMADO]`.

### 8.3 Privacidad de datos y cumplimiento
- **Aislamiento Local:** El modo interactivo con `AntigravityAdapter` permite auditar conversaciones confidenciales sin que los datos salgan del equipo local hacia APIs públicas `[CONFIRMADO]`.
- **Control de Acciones Destructivas:** Las recomendaciones destructivas (e.g. poda de contexto) son marcadas automáticamente con `requires_policy_approval: true` por el `PolicyEngine` `[CONFIRMADO]`.

---

## 9. ESTADO REAL, DEUDA TÉCNICA Y LIMITACIONES

### 9.1 Nivel de madurez y avance real del proyecto
- **Score MetricsThinking™:** **`52.92%`** — Estado: 🟡 **Construcción Activa / Madurez Media** `[CONFIRMADO]`.
- **Módulos Core:**
  - M01 (Descubrimiento y Alcance): 100% completado.
  - M02 (Arquitectura y Diseño): 100% completado.
  - M03 (Gobernanza y Context Engineering): 100% completado.
  - M04 (Aprovisionamiento y Configuración): 100% completado.
  - M05 (Construcción Núcleo): 80% completado (Motor heurístico + Scoring + Adaptador Antigravity + CLI Interactivo plenamente operativos).
  - M10 (Cierre y Documentación): 100% completado.

### 9.2 Deuda técnica identificada y stubs pendientes
- `[FALTANTE]` M06 (Integración): Adaptadores para OpenAI API, Anthropic Claude API y LiteLLM.
- `[FALTANTE]` M07 (QA & Stress): Expansión del dataset de evaluación (`dataset/eval_dataset.jsonl`) a 100+ escenarios sintéticos y adversariales.
- `[FALTANTE]` M08 (Operación y Tracing): Exportador OpenTelemetry / Prometheus de métricas de entropía.
- `[FALTANTE]` M09 (CI/CD): Workflow de GitHub Actions para validación automática de pull requests.

### 9.3 Inconsistencias entre código y documentación
- `[CONFIRMADO]` Ninguna inconsistencia detectada. El CLI, la documentación bilingüe (`README.md`, `README_ES.md`), los esquemas JSON y los scripts de ejecución están perfectamente alineados con la versión 0.5.0 del paquete.

---

## 10. REGLAS PARA MODIFICAR EL PROYECTO

### 10.1 Convenciones de estilo, linting y tipado
- Python 3.9+ con tipado estricto (`typing`, Pydantic v2) `[CONFIRMADO]`.
- Formato PEP 8, nombres en `snake_case` para módulos/funciones y `PascalCase` para clases.
- Manejo estricto de excepciones tipadas (`AdapterExecutionError`, `ValidationError`).

### 10.2 Reglas arquitectónicas inviolables
1. **Contrato Epistémico Absoluto:** Está estrictamente prohibido reportar supuestas anomalías mecánicas en capas de atención o memoria física interna de los modelos. Toda métrica debe ser observable en el texto o medida heurísticamente.
2. **Independencia del Core:** El motor de scoring (`scoring.py`), las señales (`signals.py`) y los modelos (`models.py`) jamás deben importar librerías de clientes LLM (como `google-genai`, `openai`, etc.).
3. **Consistencia de Esquemas:** Cualquier cambio en las entidades de `models.py` debe reflejarse y validarse simultáneamente en `schemas/audit-input.schema.json` y `schemas/audit-result.schema.json`.
4. **Validación de Pruebas:** No se admite ningún commit que rompa alguna de las 36 pruebas existentes en `tests/`.

### 10.3 Checklist de verificación previa a commit
- [ ] Ejecutar la suite completa: `python -m pytest` (36/36 tests PASSED).
- [ ] Comprobar que no se hayan introducido credenciales o tokens en archivos `.json`, `.yaml` o `.py`.
- [ ] Validar que cualquier nuevo archivo o función pública cuente con sus respectivos tests unitarios en `tests/unit/`.
- [ ] Verificar que `run_audit.ps1` y `python -m context_auditor.cli` ejecuten sin excepciones.

---

## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA

> **Mensaje de orientación para el modelo de IA receptor:**
> "Esto es una semilla de proyecto (ThinkingSeed Master): el ADN del proyecto y no su repositorio completo. Refleja el avance real y la arquitectura del sistema hasta la fecha. Como modelo receptor, tu función es usar esta semilla como memoria técnica para:
> 1. **Responder preguntas** sobre la arquitectura, funcionamiento, dependencias y flujos del sistema.
> 2. **Sugerir mejoras o asistencia técnica** sobre el estado actual y áreas pendientes identificadas en la semilla.
> 3. **Generar código o soluciones compatibles** respetando las rutas, convenciones y patrones definidos aquí, cuando el usuario te lo solicite."

### Pautas de resolución:
Antes de resolver una solicitud:
1. Identifica el objetivo del usuario.
2. Localiza los componentes afectados usando las rutas del Seed.
3. Revisa restricciones, reglas y contratos declarados.
4. Explicita supuestos cuando sea necesario: "Supongo que X debido a Y".
5. Propone cambios por archivo con rutas claras.
6. Añade pruebas, riesgos y criterios de aceptación.

### 🤝 Acuse de Recibo Inicial
Si el usuario adjuntó esta semilla **sin una instrucción específica**, no intentes generar código ni completar archivos vacíos. Responde únicamente con:
1. Un saludo confirmando que asimilaste el ADN de **Context Entropy Auditor (CEA)** y su stack principal.
2. Un breve resumen de 2-3 líneas sobre el objetivo y su estado actual de avance.
3. Una frase poniéndote a disposición para resolver dudas sobre su funcionamiento o colaborar en los siguientes pasos de desarrollo.
