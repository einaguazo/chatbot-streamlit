import streamlit as st
from langchain.llms import OpenAI
import os

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
    llm = OpenAI(model_name="text-davinci-003")  # Cambia según el modelo que uses
    # Aquí puedes procesar el input y la base de conocimientos
    context = "\n".join(knowledge_base)  # Combina todos los textos en un solo contexto
    prompt = f"{context}\n\nUser: {user_input}\nChatbot:"
    response = llm(prompt)
    st.write(response)
