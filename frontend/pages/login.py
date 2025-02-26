import streamlit as st

st.title("Login")
usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    st.success("Login bem-sucedido!")