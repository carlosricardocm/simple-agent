"""
main.py -- Punto de entrada del agente.

Requiere una variable de entorno GEMINI_API_KEY (puede ir en un archivo .env).
Consíguela gratis en Google AI Studio: https://aistudio.google.com/apikey
"""

from google import genai
from dotenv import load_dotenv

from agent import Agent

load_dotenv()

MODEL = "gemini-3.7-flash"

print("Mi primer agente de IA (Gemini)")
print("Escribe 'salir' para terminar.\n")

client = genai.Client()
agent = Agent()

while True:                                   # bucle de conversación
    user_input = input("Tú: ").strip()

    if not user_input:
        continue
    if user_input.lower() in ("salir", "exit", "bye", "sayonara"):
        print("¡Hasta luego!")
        break

    agent.add_user_message(user_input)

    while True:                               # bucle del agente
        interaction = client.interactions.create(
            model=MODEL,
            store=False,                      # la memoria la llevamos nosotros
            system_instruction=Agent.SYSTEM_PROMPT,
            input=agent.history,
            tools=agent.tools,
        )

        if not agent.process_interaction(interaction):
            break                             # no pidió herramientas: ya terminó
