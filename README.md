# Construye tu primer agente de IA con LangChain

**EurusConf 2026 · Python Edition · 27 de junio de 2026 · Ricardo Tovar**

Construir un agente investigador y entender herramientas, memoria, streaming y salida estructurada.

## Recursos

| Archivo | Uso |
|---|---|
| [taller_langchain.ipynb](taller_langchain.ipynb) | Notebook generado desde la fuente original del taller. |
| [resumen.pdf](resumen.pdf) | Ideas principales y ruta de repaso. |
| [brief-taller.pdf](brief-taller.pdf) | Objetivo, contenido, práctica, requisitos y siguiente paso. |
| [AVISO-DE-USO.md](AVISO-DE-USO.md) | Permisos y límites de uso. |

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rtovardev/taller-langchain-agentes/blob/main/taller_langchain.ipynb)

## Lo que vimos

- Modelo, herramienta y ciclo de ejecución de un agente.
- create_agent de LangChain y relación con LangGraph.
- Búsqueda web, streaming, memoria y salida estructurada.
- Paso del notebook a un proyecto local con uv y src/.

## Cómo empezar

1. Abre el notebook en Colab y guarda una copia en Drive.
2. Revisa los requisitos del brief; si una celda usa una API, proporciona tu propia clave sin guardarla en el notebook.
3. Haz el ejercicio y comprueba el resultado con los criterios del resumen.

## Continuación en un proyecto local

El Colab cubre la primera parte. Para practicar la transición a un proyecto propio:

1. Crea una carpeta vacía y ejecuta `uv init`.
2. Añade las dependencias que usa tu versión del notebook con `uv add`.
3. Mueve el `system_prompt`, las herramientas y la construcción del agente a módulos separados dentro de `src/agente/`.
4. Crea un `main.py` que invoque el agente con una pregunta conocida.
5. Guarda las claves como variables de entorno; no las subas al repositorio.
6. Prueba una pregunta normal y otra ambigua. Registra qué esperabas y qué respondió el agente.

Puedes extender el investigador con lectura de una página, conectar un servicio de tareas con permiso explícito o consultar una API pública. Empieza con una sola herramienta y un caso de aceptación verificable.

## Uso de los materiales

El acceso público permite la consulta y el estudio personal en los términos de [AVISO-DE-USO.md](AVISO-DE-USO.md). La reutilización en cursos, charlas o publicaciones requiere autorización expresa.
