import os
import openai

# Configura la clave API desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Verifica que la clave API esté configurada
if openai.api_key is None:
    raise ValueError("La clave API de OpenAI no está configurada correctamente.")

# Realiza una solicitud al modelo gpt-3.5-turbo
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "Hola, ¿cómo estás?"}
    ],
    max_tokens=150
)

# Imprime la respuesta del modelo
print(response['choices'][0]['message']['content'])
