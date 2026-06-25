# Construye tu primer agente de IA con LangChain

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rtovardev/taller-langchain-agentes/blob/main/notebook/taller_langchain.ipynb)

Taller práctico de **EurusConf 2026 (Python Edition)**. En 90 minutos pasas de un modelo de lenguaje a un **agente que razona, usa herramientas y ejecuta tareas**, construido con Python y LangChain.

Ponente: **Ricardo Tovar** — AI Engineer en formación · Cofundador de [MART Automations](https://martautomations.com).

---

## El taller en 2 partes

1. **Parte 1 — en Google Colab** (no instalas nada): construyes un **agente investigador** y lo haces sólido (streaming + memoria + salida estructurada).
2. **Parte 2 — en VS Code**: llevas ese mismo agente a un **proyecto real** con `uv` y la estructura `src/`. Es lo que ves en este repo.

---

## Parte 1 — Google Colab

Haz clic en el botón **Open in Colab** de arriba. Corre la celda de Setup y pega tu API key cuando te la pida. Listo, no instalas nada.

**API key (gratis):** usamos **Gemini**. Saca tu key en [Google AI Studio](https://aistudio.google.com/apikey).

> **Opcional:** para mejores resultados (mejor tool-calling) puedes usar OpenAI u OpenRouter con unos créditos (aprox. $5). Ver `.env.example`.

---

## Parte 2 — del notebook al proyecto real (VS Code)

Aquí sacamos el agente del notebook y lo organizamos como un proyecto de verdad, usando **`uv`** (el gestor de paquetes moderno de Python).

### 1. Instala `uv` (una sola vez)

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clona, instala y configura

```bash
git clone https://github.com/rtovardev/taller-langchain-agentes.git
cd taller-langchain-agentes

uv sync                 # crea el entorno e instala todo (lee pyproject.toml)

cp .env.example .env    # y pega tu GOOGLE_API_KEY en .env
```

### 3. Corre el agente

```bash
uv run python main.py
```

Charlas con él en la terminal. Como tiene memoria, recuerda lo que le dijiste antes.

### La estructura

```
taller-langchain-agentes/
├── notebook/
│   └── taller_langchain.ipynb   # Parte 1 (Colab)
├── src/
│   └── agente/
│       ├── agent.py    # define el agente: create_agent + modelo + memoria
│       ├── tools.py    # las @tool (búsqueda web, hora, y las que agregues)
│       └── prompts.py  # el system prompt (el rol del agente)
├── main.py             # punto de entrada: agent.invoke en un loop
├── pyproject.toml      # dependencias (uv)
├── uv.lock             # versiones exactas
└── .env.example        # plantilla de variables (modelo + tokens)
```

### Del notebook al proyecto (1 a 1)

| En el notebook | En el proyecto |
|---|---|
| `@tool def ...` | `src/agente/tools.py` |
| `create_agent(...)` + memoria | `src/agente/agent.py` |
| el `system_prompt` | `src/agente/prompts.py` |
| `agent.invoke(...)` | `main.py` |
| la API key | `.env` |
| `%pip install ...` | `pyproject.toml` + `uv add ...` |

> ¿Quieres llevarlo a producción de verdad? El siguiente paso es **`langgraph.json`** + LangGraph Server/Studio para desplegarlo. Queda fuera del taller, pero ahí está el camino.

---

## 3 ideas para tu propio agente

Extiende el proyecto: agrega una `@tool` en `src/agente/tools.py`, súmala a la lista `tools`, y ajusta el `system_prompt`. Todas usan **token** (sin OAuth). Pon el token en tu `.env`.

### A — Tu productividad (Notion)

```python
import os, requests
from langchain_core.tools import tool

@tool
def agregar_a_notion(titulo: str) -> str:
    """Agrega una nota o tarea a tu base de datos de Notion."""
    resp = requests.post(
        "https://api.notion.com/v1/pages",
        headers={"Authorization": f"Bearer {os.getenv('NOTION_TOKEN')}",
                 "Notion-Version": "2022-06-28",
                 "Content-Type": "application/json"},
        json={"parent": {"database_id": os.getenv("NOTION_DATABASE_ID")},
              "properties": {"Name": {"title": [{"text": {"content": titulo}}]}}},
    )
    return "Agregado a Notion" if resp.ok else f"Error: {resp.text[:120]}"
```

### B — Tu lista de tareas (Todoist)

```python
import os, requests
from langchain_core.tools import tool

@tool
def agregar_a_todoist(tarea: str) -> str:
    """Agrega una tarea a tu Todoist."""
    resp = requests.post(
        "https://api.todoist.com/rest/v2/tasks",
        headers={"Authorization": f"Bearer {os.getenv('TODOIST_TOKEN')}"},
        json={"content": tarea},
    )
    return "Tarea agregada a Todoist" if resp.ok else f"Error: {resp.text[:120]}"
```

### C — Datos en vivo (API pública: clima)

```python
import os, requests
from langchain_core.tools import tool

@tool
def clima(ciudad: str) -> str:
    """Devuelve el clima actual de una ciudad."""
    resp = requests.get("https://api.openweathermap.org/data/2.5/weather",
        params={"q": ciudad, "appid": os.getenv("OPENWEATHER_API_KEY"),
                "units": "metric", "lang": "es"})
    if not resp.ok:
        return f"Error: {resp.text[:120]}"
    d = resp.json()
    return f"{ciudad}: {d['weather'][0]['description']}, {d['main']['temp']}C"
```

> Idea extra: un agente **investigador + scraping** que, además de buscar, entre a una página y extraiga la info (con `requests` + tu parser favorito).

---

## Requisitos previos

- Python 3.10+
- `uv` (para la Parte 2) — o `pip` si prefieres el camino clásico
- Git
- Bases de Python (variables y funciones). No necesitas experiencia previa en IA.

> ¿Sin `uv`? También puedes: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.
