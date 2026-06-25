"""Las herramientas del agente.

Una herramienta es una función con la que el agente actúa sobre el mundo.
Pueden ser tuyas (con `@tool`) o venir de una librería (como la búsqueda web).
"""
from datetime import datetime

from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun


@tool
def hora_actual() -> str:
    """Devuelve la fecha y hora actual."""
    return datetime.now().strftime("%Y-%m-%d %H:%M")


# Búsqueda en la web (no necesita API key)
buscar_web = DuckDuckGoSearchRun()

# La lista que recibe el agente. Agrega aquí las tuyas.
tools = [buscar_web, hora_actual]
