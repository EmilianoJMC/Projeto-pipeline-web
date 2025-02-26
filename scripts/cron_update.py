import schedule
import time
import requests

def atualizar_dados():
    try:
        novo_filme = {
            "titulo": "Matrix",
            "genero": "Ficção Científica"
        }
        print("Tentando conectar ao servidor...")
        response = requests.get("http://127.0.0.1:8000/")
        print("Conexão bem-sucedida:", response.status_code)
        print("Enviando requisição POST para adicionar filme...")
        response = requests.post("http://127.0.0.1:8000/filmes", json=novo_filme, timeout=10)
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)
        response.raise_for_status()
        print("Filme adicionado:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Erro ao adicionar filme: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

schedule.every(5).minutes.do(atualizar_dados)

while True:
    schedule.run_pending()
    print("Executando tarefa...")
    time.sleep(60)