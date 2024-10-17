import os
from langchain.llms import OpenAI

# Carga la clave API desde las variables de entorno
openai_api_key = os.getenv("OPENAI_API_KEY")

# Imprimir la clave API (solo para depuración)
print("Clave API:", openai_api_key)

# Inicializa el modelo
llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
