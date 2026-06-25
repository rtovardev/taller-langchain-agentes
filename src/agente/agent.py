"""Define el agente: modelo + herramientas + system prompt + memoria.

Es el mismo `create_agent` del notebook, ahora viviendo en su propio archivo.
"""
import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from .tools import tools
from .prompts import SYSTEM_PROMPT

load_dotenv()  # lee las variables de .env


def get_model():
    """Elige el modelo según el .env (Gemini por defecto)."""
    provider = os.getenv("MODEL_PROVIDER", "google_genai")
    model_name = os.getenv("MODEL_NAME", "gemini-2.0-flash")
    if provider == "openrouter":  # OpenRouter usa la API compatible con OpenAI
        return init_chat_model(
            f"openai:{model_name}",
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )
    return init_chat_model(f"{provider}:{model_name}")


def build_agent():
    """Arma el agente investigador con memoria."""
    return create_agent(
        model=get_model(),
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=InMemorySaver(),  # memoria en proceso (se reinicia al cerrar)
    )


agent = build_agent()
