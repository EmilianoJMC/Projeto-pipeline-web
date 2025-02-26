import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Dashboard de Filmes")

if st.button("Listar Filmes"):
    response = requests.get(f"{API_URL}/filmes")
    st.write(response.json())

titulo = st.text_input("Título do Filme")
genero = st.text_input("Gênero")

if st.button("Adicionar Filme"):
    response = requests.post(f"{API_URL}/filmes", params={"titulo": titulo, "genero": genero})
    st.write(response.json())