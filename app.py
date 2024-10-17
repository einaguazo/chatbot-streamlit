import streamlit as st
from langchain.llms import OpenAI

# Configuración de la interfaz
st.title("Chatbot con Langchain y Streamlit")
user_input = st.text_input("Escribe tu mensaje:")

# Inicializa el modelo de lenguaje
if user_input:
    llm = OpenAI(model_name="text-davinci-003")  # Cambia según el modelo que uses
    response = llm(user_input)
    st.write(response)
