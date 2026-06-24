# Construye tu primer agente de IA con LangChain

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rtovardev/taller-langchain-agentes/blob/main/notebook/taller_langchain.ipynb)

Taller práctico de **EurusConf 2026 (Python Edition)**. En 90 minutos pasas de un modelo de lenguaje a un **agente que razona, usa herramientas y ejecuta tareas**, construido con Python y LangChain.

Ponente: **Ricardo Tovar** — AI Engineer en formación · Cofundador de [MART Automations](https://martautomations.com).

## Qué vas a construir

Tres prácticas, cada una sobre la anterior:

1. **Tu primer agente** — `create_agent`, herramientas y salida estructurada.
2. **Tu agente investigador web** — búsqueda en internet + memoria.
3. **Tu agente de valor** — lo construyes tú, conectado a un servicio real (Notion, Todoist o una API pública).

## Cómo seguir el taller

Tienes dos caminos. **Recomendado: VS Code.** Respaldo sin instalar nada: **Google Colab** (botón de arriba).

### Opción A — VS Code (local)

```bash
# 1. Clona el repo
git clone https://github.com/rtovardev/taller-langchain-agentes.git
cd taller-langchain-agentes

# 2. Crea un entorno e instala dependencias
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Copia el ejemplo de variables de entorno y pon tu API key
cp .env.example .env
# edita .env y pega tu GOOGLE_API_KEY
```

Abre `notebook/taller_langchain.ipynb` en VS Code (con las extensiones **Python** y **Jupyter**) y ejecuta las celdas.

### Opción B — Google Colab (sin instalar nada)

Haz clic en el botón **Open in Colab** de arriba. Corre la celda de setup y pega tu API key cuando te la pida.

## API key (proveedor del modelo)

Por defecto usamos **Gemini (gratis)**. Saca tu key en [Google AI Studio](https://aistudio.google.com/apikey) y ponla en `.env` como `GOOGLE_API_KEY`.

**Opcional:** si quieres mejores resultados y experimentar con modelos más potentes (mejor tool-calling), puedes usar OpenAI u OpenRouter con unos créditos (aprox. $5). Ver `.env.example`.

## Requisitos previos

- Python 3.10+
- VS Code con extensiones Python y Jupyter (para la opción A)
- Git
- Bases de Python (variables y funciones). No necesitas experiencia previa en IA.

## Estructura

```
taller-langchain-agentes/
├── notebook/
│   └── taller_langchain.ipynb   # el taller completo
├── requirements.txt
├── .env.example
└── README.md
```
