import os
import openai
from langchain.llms import OpenAI

# Cargar la clave de API desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Verificar que la clave de API se está cargando correctamente
if openai.api_key is None:
    raise ValueError("La clave API de OpenAI no está configurada correctamente.")

# Inicializa el modelo usando la biblioteca de OpenAI directamente
response = openai.Completion.create(
    engine="gpt-3.5-turbo",  # O usa "text-davinci-003" si prefieres
    prompt="Hola, ¿cómo puedo ayudarte?",
    max_tokens=150
)

# Imprime la respuesta del modelo
print(response.choices[0].text)
