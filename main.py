"""Punto de entrada: charla con tu agente desde la terminal.

Ejecuta:  uv run python main.py
(Necesitas tu API key en .env — copia .env.example a .env.)
"""
from src.agente.agent import agent

# El thread_id agrupa la conversación: con el mismo id, el agente recuerda.
CONFIG = {"configurable": {"thread_id": "terminal"}}


def main():
    print("Agente investigador listo. Escribe 'salir' para terminar.\n")
    while True:
        try:
            pregunta = input("Tú: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if pregunta.lower() in {"salir", "exit", "quit"}:
            break
        if not pregunta:
            continue
        respuesta = agent.invoke(
            {"messages": [{"role": "user", "content": pregunta}]},
            CONFIG,
        )
        print("Agente:", respuesta["messages"][-1].content, "\n")


if __name__ == "__main__":
    main()
