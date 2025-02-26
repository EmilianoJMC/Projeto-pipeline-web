import streamlit as st
import hashlib
import json
import os

# Caminho para o arquivo de dados dos usuários
USER_DB_PATH = "users_db.json"

# Função para carregar dados dos usuários do arquivo JSON
def load_users():
    if os.path.exists(USER_DB_PATH):
        with open(USER_DB_PATH, 'r') as file:
            return json.load(file)
    return {}

# Função para salvar dados dos usuários no arquivo JSON
def save_users(users_db):
    with open(USER_DB_PATH, 'w') as file:
        json.dump(users_db, file)

# Carregar usuários do arquivo
users_db = load_users()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    if username in users_db:
        return False
    users_db[username] = {"password": hash_password(password), "role": "user"}
    save_users(users_db)  # Salvar usuários após registrar
    return True

def login_user(username, password):
    if username in users_db and users_db[username]["password"] == hash_password(password):
        return True
    return False

def is_admin(username):
    return users_db.get(username, {}).get("role") == "admin"

