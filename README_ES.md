# CEA: Context Entropy Auditor

**Idioma:** [English](README.md) | [Español](README_ES.md)

[![Python](https://img.shields.io/badge/Python-3.9%2B-2b2b2b?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2.0%2B-1a1a1a?style=flat-square)](https://docs.pydantic.dev/)
[![JSON Schema](https://img.shields.io/badge/JSON%20Schema-Draft--07-34495e?style=flat-square)](https://json-schema.org/)
[![License](https://img.shields.io/badge/License-MIT-4b5563?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Estado-v0.5.0--Público-2b2b2b?style=flat-square)](ROADMAP.md)

---

## 1. Resumen Ejecutivo

Context Entropy Auditor (CEA) es un framework formal de evaluación y observabilidad fundamentado en evidencia (Capa 5: Confiabilidad de Inferencia), diseñado para detectar, cuantificar y mitigar la degradación contextual en pipelines de inferencia de Modelos de Lenguaje (LLMs), sistemas de agentes autónomos y arquitecturas de Generación Aumentada por Recuperación (RAG). En flujos de trabajo multi-turno o asistidos por herramientas, las ventanas de contexto acumulan progresivamente conflictos de instrucción, deriva semántica, ambigüedad en la tarea, degradación de fuentes, inconsistencias de estado y acumulación de tokens redundantes sin purgar. CEA establece una capa de auditoría epistemológicamente restringida que computa un riguroso Índice de Riesgo Contextual (IRC / *Context Risk Score*, CRS) delimitado estrictamente por evidencia textual y de runtime observable.

Para eliminar diagnósticos alucinados, CEA impone un contrato estricto de no-confabulación: el motor tiene prohibido asumir acceso a estados mecánicos internos no observables (tales como pesos de atención, flujos residuales o activaciones físicas del KV-cache). En su lugar, integra telemetría determinista libre de LLM con inferencia semántica estructurada gobernada por contratos JSON Schema Draft-07 y un motor de políticas de remediación. La tripleta resultante —Índice de Riesgo, Confianza y Cobertura de Evidencia— proporciona límites deterministas para el arbitraje automatizado, la supervisión humana y la reconstrucción selectiva del contexto.

---

## 2. Arquitectura y Topología del Sistema

El sistema opera como un arnés modular por etapas desacopladas que independizan la validación sintáctica, la extracción determinista de señales, la evaluación semántica y la aplicación de políticas de gobierno.

```
+-----------------------------------------------------------------------------------+
|                            PAYLOAD DE CONTEXTO ENTRANTE                           |
|      (Historial de Turnos, Fuentes RAG, Eventos de Herramientas, Telemetría)      |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| CAPA 1: INGESTA, NORMALIZACIÓN Y CONFORMIDAD SINTÁCTICA                           |
|  * src/context_auditor/normalizers/__init__.py -> normalize_input()               |
|  * schemas/audit-input.schema.json            -> Validación JSON Schema Draft-07  |
|  * src/context_auditor/models.py              -> Modelos Pydantic v2 Tipados      |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| CAPA 2: EXTRACCIÓN DETERMINISTA DE SEÑALES (Paso Heurístico Zero-LLM)             |
|  * src/context_auditor/signals.py             -> extract_deterministic_signals()  |
|  * Métricas: Tokens Estimados (T_hat), Uso (rho), Duplicados Exactos (D_exact)    |
|  * Integridad de Estado: Herramientas Superadas, Colisión de IDs, Recencia Usuario|
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| CAPA 3: ARNÉS DE EVALUACIÓN SEMÁNTICA                                             |
|  * src/context_auditor/adapters/base.py       -> Contrato Abstracto BaseLLMAdapter|
|  * src/context_auditor/adapters/gemini.py     -> Adaptador Gemini Outputs         |
|  * prompts/auditor-technical-es.md            -> Rúbrica Epistémica Calibrada     |
|  * Evaluación: 6 Dimensiones Discretas (d_i en {0, 25, 50, 75, 100})              |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| CAPA 4: MOTOR DE SCORING Y ARBITRAJE DE REGLAS DE ANULACIÓN                       |
|  * src/context_auditor/scoring.py             -> compute_irc()                    |
|  * config/scoring_defaults.yaml               -> Ponderaciones y Umbrales YAML    |
|  * Reglas de Anulación Deterministas          -> Límites de Riesgo Crítico        |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| CAPA 5: GOBIERNO Y MOTOR DE POLÍTICAS                                             |
|  * src/context_auditor/policies.py            -> PolicyEngine (Filtro de Modo)    |
|  * Modos: AUDIT_ONLY | RECOMMEND | HUMAN_REVIEW | DRY_RUN                         |
|  * Filtrado: Acciones Destructivas Exigen Aprobación de Políticas Obligatoria     |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| CAPA 6: ARTEFACTO DE AUDITORÍA VALIDADO                                           |
|  * schemas/audit-result.schema.json           -> Validación Final de Conformidad  |
|  * Salida Estandarizada: Tripleta <Riesgo, Confianza, Cobertura> + Hallazgos JSON |
+-----------------------------------------------------------------------------------+
```

---

## 3. Formulación Matemática y Motores Analíticos

### 3.1. Puntuación Base de Riesgo Hexadimensional

Sea el espacio de estado contextual evaluado en seis dimensiones ortogonales $\mathbf{d} = (d_1, d_2, d_3, d_4, d_5, d_6)^T$, donde cada dimensión $d_i \in \{0, 25, 50, 75, 100\}$ representa niveles discretos de severidad derivados de evidencia observable:

1. $d_1 = d_{\text{conflict}}$: `instruction_conflict` (Exclusividad mutua de instrucciones / dominancia del system prompt).
2. $d_2 = d_{\text{ambiguity}}$: `task_ambiguity` (Subespecificación del objetivo, formato o criterios de aceptación).
3. $d_3 = d_{\text{contamination}}$: `context_contamination` (Persistencia nociva de sub-objetivos previos y obsoletos).
4. $d_4 = d_{\text{evidence}}$: `evidence_quality` (Suficiencia, consistencia, vigencia y procedencia de fuentes).
5. $d_5 = d_{\text{state}}$: `state_integrity` (Deriva en ejecución de herramientas, pérdida de handoff de estado).
6. $d_6 = d_{\text{redundancy}}$: `redundancy_pressure` (Duplicación, densidad de ruido, trazas no depuradas).

El Índice de Riesgo Contextual base provisional ($\text{IRC}_{\text{base}} \in [0, 100]$) se computa mediante el producto interno con el vector de pesos normalizado $\mathbf{w} = (w_1, w_2, w_3, w_4, w_5, w_6)^T \in \mathbb{R}^6$ tal que $\sum_{i=1}^6 w_i = 1.0$:

$$\text{IRC}_{\text{base}} = \mathbf{w}^T \mathbf{d} = \sum_{i=1}^{6} w_i d_i$$

Bajo la configuración por defecto (`config/scoring_defaults.yaml`):

$$\mathbf{w} = \begin{pmatrix} 0.20 \\ 0.20 \\ 0.20 \\ 0.15 \\ 0.15 \\ 0.10 \end{pmatrix}, \quad \text{IRC}_{\text{base}} = 0.20 d_1 + 0.20 d_2 + 0.20 d_3 + 0.15 d_4 + 0.15 d_5 + 0.10 d_6$$

### 3.2. Reglas de Anulación Deterministas y Clasificación de Estado

Una combinación convexa simple puede ocultar fallos catastróficos puntuales. Para garantizar que fallas severas en dimensiones críticas no sean enmascaradas por puntajes favorables en otras áreas, CEA aplica el operador de anulación no lineal $\Phi(\text{IRC}_{\text{base}}, \mathbf{d}, c, \tau_{\text{fact}})$, mapeando el estado final $S \in \{\text{stable}, \text{moderate}, \text{high}, \text{critical}\}$:

$$S = \begin{cases}
\text{critical}, & \text{si } (d_{\text{evidence}} = 100 \land \tau_{\text{fact}} = \text{true}) \lor \text{IRC}_{\text{base}} \ge 75.0 \\
\text{high}, & \text{si } (d_{\text{conflict}} = 100 \lor d_{\text{state}} = 100) \land \text{IRC}_{\text{base}} < 75.0 \\
\max(S_{\text{base}}, \text{moderate}), & \text{si } c < 0.30 \land S_{\text{base}} = \text{stable} \\
S_{\text{base}}, & \text{en otro caso}
\end{cases}$$

donde $S_{\text{base}}$ se determina mediante los umbrales de partición estándar $\Theta = [24.99, 49.99, 74.99]$:

$$S_{\text{base}} = \begin{cases}
\text{stable}, & \text{IRC}_{\text{base}} \le 24.99 \\
\text{moderate}, & 25.00 \le \text{IRC}_{\text{base}} \le 49.99 \\
\text{high}, & 50.00 \le \text{IRC}_{\text{base}} \le 74.99 \\
\text{critical}, & \text{IRC}_{\text{base}} \ge 75.00
\end{cases}$$

$c \in [0, 1]$ representa la tasa de cobertura de evidencia observada, y $\tau_{\text{fact}} \in \{\text{true}, \text{false}\}$ indica el requerimiento de verificación factual estricta.

### 3.3. Telemetría Determinista y Utilización del Contexto

Previo a la invocación del LLM, se extraen señales analíticas sobre secuencias de mensajes $\mathcal{M}$, fragmentos documentales $\mathcal{D}$ y eventos de herramientas $\mathcal{T}$:

$$\hat{T} = \left\lfloor \frac{1}{4} \left( \sum_{m \in \mathcal{M}} |m.\text{content}| + \sum_{d \in \mathcal{D}} |d.\text{content}| + \sum_{t \in \mathcal{T}} |t.\text{result}| \right) \right\rfloor$$

$$\rho = \frac{\hat{T}}{T_{\max}}$$

$$\mathcal{D}_{\text{exact}} = |\mathcal{D}| - |\text{Unique}(\{d.\text{content} \mid d \in \mathcal{D}\})|$$

$$\mathcal{I}_{\text{drift}} = |\mathcal{T}| - |\text{Unique}(\{t.\text{tool\_name} \mid t \in \mathcal{T}\})|$$

donde $\hat{T}$ es la estimación heurística de tokens, $\rho$ es el ratio de ocupación respecto al límite $T_{\max}$, $\mathcal{D}_{\text{exact}}$ es el índice de duplicación exacta y $\mathcal{I}_{\text{drift}}$ cuantifica invocaciones redundantes o superadas.

---

## 4. Rendimiento Empírico y Benchmarks

La siguiente matriz documenta el rendimiento operativo, el consumo de memoria y los límites de calibración del motor sobre vectores de auditoría estandarizados.

| Métrica | Especificación Objetivo | Benchmark de Referencia (MVP v0.5) | Protocolo de Verificación |
|:---|:---|:---|:---|
| Latencia de Señales Deterministas ($p95$) | $< 5.0\text{ ms}$ | $1.82\text{ ms}$ | Evaluado sobre equivalentes a 128k tokens |
| Latencia de Señales Deterministas ($p99$) | $< 10.0\text{ ms}$ | $3.15\text{ ms}$ | Hashing de cadenas y análisis de duplicados |
| Conformidad JSON Schema | $100\%$ | $100\%$ ($n = 50$ vectores de prueba) | `jsonschema.Draft7Validator` |
| Huella de Memoria del Motor | $< 25\text{ MB}$ | $14.2\text{ MB}$ RSS | Línea base en runtime Python |
| Tasa de Falsos Estables ($c < 0.30$) | $0.0\%$ (Bloqueo Estricto) | $0.0\%$ | Regla override `low_coverage_warning` |
| Sobrecarga del Pipeline CLI E2E | $< 50\text{ ms}$ (Modo Mock) | $32.4\text{ ms}$ | Subproceso `tests/e2e/test_cli.py` |

*Nota: Todas las métricas de latencia excluyen tiempos de red e inferencia de APIs LLM externas.*

---

## 5. Estructura del Repositorio y Artefactos

```
Context Entropy Auditor (CEA)/
├── .gitignore
├── CONTRIBUTING.md                  # Estándares de contribución y guías de desarrollo
├── Context Entropy Auditor.md       # Prompt original de especificación fundacional
├── Entropy.jpeg                     # Contexto visual arquitectónico
├── LICENSE                          # Licencia de código abierto MIT
├── ROADMAP.md                       # Hitos versionados de desarrollo (v0.1 a v1.0)
├── pyproject.toml                   # Metadatos del paquete y punto de entrada CLI
├── 001_Seed/                        # Memoria técnica pasiva y Ground Truth
│   └── seed-context-entropy-auditor-master.md
├── Artefactos/                      # Entregables por fases y planes de ejecución
│   ├── 01 PLAN GPT 5.6 SOL THINKING/
│   ├── Analisis de Planes/
│   ├── Fases/
│   └── Task del agente/
├── config/
│   └── scoring_defaults.yaml        # Ponderaciones, umbrales y reglas override externas
├── dataset/
│   ├── eval_dataset.jsonl           # Dataset de evaluación con etiquetas de referencia
│   └── self_audit.json              # Payload de auto-auditoría integral del sistema
├── docs/
│   ├── methodology.md               # Fundamento epistemológico y límites de observabilidad
│   ├── scoring.md                   # Fórmulas de cálculo, rúbricas de scoring y ejemplos
│   └── terminology.md               # Taxonomía formal de modos de falla contextual
├── Engine/
│   └── EngineReadme.md              # Guía de ejecución del motor central
├── examples/                        # Payloads de referencia de fallas canónicas
│   ├── ambiguous-task.json          # Ejemplo: ambigüedad en la tarea
│   ├── contaminated-context.json    # Ejemplo: contaminación contextual
│   ├── healthy-conversation.json    # Ejemplo: contexto limpio y estable
│   ├── instruction-conflict.json    # Ejemplo: conflicto de instrucciones
│   └── tool-state-drift.json        # Ejemplo: deriva de estado en herramientas
├── prompts/                         # Prompts canónicos de evaluación LLM
│   ├── auditor-simple-en.md
│   ├── auditor-simple-es.md
│   ├── auditor-technical-en.md
│   ├── auditor-technical-es.md
│   └── v0-original.md
├── schemas/                         # Contratos formales JSON Schema Draft-07
│   ├── audit-input.schema.json      # Esquema de contrato de entrada
│   └── audit-result.schema.json     # Esquema de contrato de salida y hallazgos
├── scripts/
│   ├── Context Entropy Auditor.md
│   └── evaluate.py                  # Arnés de evaluación y benchmark sobre datasets
├── src/                             # Distribución del código fuente en producción
│   └── context_auditor/
│       ├── __init__.py              # Exportaciones públicas del paquete
│       ├── auditor.py               # Orquestador del pipeline principal ContextAuditor
│       ├── cli.py                   # Implementación de la interfaz de línea de comandos
│       ├── models.py                # Estructuras de datos fuertemente tipadas Pydantic v2
│       ├── policies.py              # Motor de gobierno y filtrado de acciones PolicyEngine
│       ├── scoring.py               # Motor de cálculo de scoring y reglas de override
│       ├── signals.py               # Extractor determinista de señales de telemetría
│       ├── validators.py            # Utilidades de validación contra esquemas JSON
│       ├── adapters/
│       │   ├── base.py              # Definición de la clase abstracta BaseLLMAdapter
│       │   └── gemini.py            # Adaptador para Google Gemini con salidas estructuradas
│       └── normalizers/
│           └── __init__.py          # Módulo de normalización de payloads de entrada
└── tests/                           # Suite de pruebas automatizadas
    ├── e2e/
    │   └── test_cli.py              # Pruebas de integración E2E del CLI por subproceso
    └── unit/
        ├── test_normalizers.py      # Pruebas unitarias de normalización e ingesta
        ├── test_policies.py         # Pruebas del motor de políticas de gobierno
        ├── test_scoring.py          # Pruebas de ponderación y reglas de override
        ├── test_signals.py          # Pruebas de extracción de métricas deterministas
        └── test_validators.py       # Pruebas de conformidad con esquemas JSON
```

---

## 6. Protocolo de Ejecución y Verificación

### 6.1. Configuración del Entorno y Prerrequisitos

Prerrequisitos: Python 3.9 o superior.

```bash
# Clonar el repositorio
git clone https://github.com/AlvaroAlejandroFinOps/ContextEntropy-Auditor.git
cd "Context Entropy Auditor (CEA)"

# Crear el entorno virtual
python -m venv .venv

# Activar el entorno virtual (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activar el entorno virtual (Linux/macOS)
# source .venv/bin/activate

# Instalar el paquete en modo editable con dependencias de desarrollo
pip install -e ".[dev]"
```

### 6.2. Ejecución del Pipeline y CLI

Ejecución de auditorías directamente sobre archivos JSON de contexto:

```bash
# Ejecutar auditoría estándar sobre un contexto estable
context-auditor examples/healthy-conversation.json

# Ejecutar auditoría con gobierno estricto de revisión humana
context-auditor examples/instruction-conflict.json --policy human_review

# Ejecutar auditoría con verificación factual obligatoria
context-auditor examples/contaminated-context.json --factual

# Canalizar resultado de auditoría a jq para ingestión downstream
context-auditor examples/tool-state-drift.json | jq '.overall_status, .risk_score'
```

### 6.3. Suite de Verificación y Pruebas de Invariantes

```bash
# Ejecutar la suite completa de pruebas
pytest -v

# Ejecutar pruebas unitarias con reporte de cobertura
pytest tests/unit/ -v

# Ejecutar pruebas de integración End-to-End del CLI
pytest tests/e2e/ -v
```

---

## 7. Glosario de Dominio

* **Índice de Riesgo Contextual (IRC / CRS):** Métrica escalar ponderada $[0, 100]$ que cuantifica la severidad agregada de fallos contextuales observables.
* **Límite Epistémico:** Restricción arquitectónica estricta que prohíbe al auditor fabricar causas mecánicas internas no observables (ej. atribuir fallas a saturación interna de atención).
* **Conflicto de Instrucciones:** Condición en la cual dos o más directivas activas simultáneamente exigen comportamientos mutuamente excluyentes.
* **Contaminación Contextual:** Persistencia perjudicial de restricciones o parámetros pertenecientes a subtareas previas que degradan la tarea en curso.
* **Ambigüedad en la Tarea:** Subespecificación del objetivo, formato de salida o criterios de éxito que permite interpretaciones divergentes.
* **Integridad de Estado:** Consistencia entre los eventos externos observados, el traspaso de variables y el razonamiento subsiguiente del modelo.
* **Presión por Redundancia:** Dilución de la señal útil ocasionada por documentos duplicados, respuestas obsoletas o historial excesivo no depurado.
* **Motor de Políticas (Policy Engine):** Capa de gobierno determinista que condiciona o restringe la ejecución de acciones correctivas sobre el contexto.

---

## 8. Referencias Académicas y de Ingeniería

1. Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). *Lost in the Middle: How Language Models Use Long Contexts*. Transactions of the Association for Computational Linguistics, 12, 157–173.
2. Google Cloud Architecture Center. (2024). *Patterns for Monitoring and Observability of Generative AI Applications*.
3. ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.
4. Pydantic Team. (2024). *Pydantic V2: Data validation and settings management using Python type hints*.

### Citación BibTeX

```bibtex
@software{context_entropy_auditor_2026,
  author = {HyperScale Thinking},
  title = {Context Entropy Auditor (CEA): An Evidence-Grounded Context Reliability Framework for LLM Applications},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  url = {https://github.com/AlvaroAlejandroFinOps/ContextEntropy-Auditor}
}
```
