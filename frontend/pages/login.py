import streamlit as st
from auth import register_user, login_user, is_admin

st.title("Login")

# Inputs de login
usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

# Botão de Login
if st.button("Entrar"):
    if login_user(usuario, senha):
        st.session_state.logged_in = True
        st.session_state.username = usuario
        st.success("Login bem-sucedido!")
        st.experimental_set_query_params(page="app")
    else:
        st.error("Nome de usuário ou senha incorretos.")

# Inputs de registro
st.subheader("Registrar")
novo_usuario = st.text_input("Novo Usuário")
nova_senha = st.text_input("Nova Senha", type="password")
confirmar_senha = st.text_input("Confirmar Senha", type="password")

# Botão de Registro
if st.button("Registrar"):
    if nova_senha == confirmar_senha:
        if register_user(novo_usuario, nova_senha):
            st.success("Usuário registrado com sucesso!")
        else:
            st.error("Nome de usuário já existe.")
    else:
        st.error("As senhas não correspondem.")
