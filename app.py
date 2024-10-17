import streamlit as st
from langchain.llms import OpenAI
import os

# Carga la clave API desde las variables de entorno
openai_api_key = os.getenv("OPENAI_API_KEY")

# Imprimir la clave API (solo para depuración)
print("Clave API:", openai_api_key)

# Inicializa el modelo
llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
# Función para cargar archivos de texto
def load_texts(data_folder):
    texts = []
    for filename in os.listdir(data_folder):
        if filename.endswith(".txt"):
            with open(os.path.join(data_folder, filename), 'r') as file:
                texts.append(file.read())
    return texts

# Carga los textos desde la carpeta 'data'
data_folder = 'data'
knowledge_base = load_texts(data_folder)

# Configuración de la interfaz
st.title("Chatbot con Langchain y Streamlit")
user_input = st.text_input("Escribe tu mensaje:")

# Inicializa el modelo de lenguaje
if user_input:
    llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
    # Aquí puedes procesar el input y la base de conocimientos
    context = "\n".join(knowledge_base)  # Combina todos los textos en un solo contexto
    prompt = f"{context}\n\nUser: {user_input}\nChatbot:"
    response = llm(prompt)
    st.write(response)
