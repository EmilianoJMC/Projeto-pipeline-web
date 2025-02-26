import schedule
import time
import requests

API_KEY = "c90c917f98d91bd0c1fd096a6b77ab58"
URL_TMDB = "https://api.themoviedb.org/3/movie/popular"
URL_FASTAPI = "http://127.0.0.1:8000/filmes"

# Mapeamento de IDs de gêneros para nomes de gêneros
GENRE_MAP = {
    28: "Ação",
    12: "Aventura",
    16: "Animação",
    35: "Comédia",
    80: "Crime",
    99: "Documentário",
    18: "Drama",
    10751: "Família",
    14: "Fantasia",
    36: "História",
    27: "Terror",
    10402: "Música",
    9648: "Mistério",
    10749: "Romance",
    878: "Ficção Científica",
    10770: "Cinema TV",
    53: "Thriller",
    10752: "Guerra",
    37: "Faroeste"
}

def buscar_filmes_tmdb():
    """ Obtém os filmes populares do TMDB """
    try:
        params = {"api_key": API_KEY, "language": "pt-BR", "page": 1}
        response = requests.get(URL_TMDB, params=params, timeout=10)
        response.raise_for_status()
        filmes = response.json().get("results", [])
        return filmes
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar filmes do TMDB: {e}")
        return []

def enviar_filmes_para_api(filmes):
    """ Envia os filmes para o backend do FastAPI """
    for filme in filmes:
        genero_id = filme["genre_ids"][0] if filme["genre_ids"] else None
        genero_nome = GENRE_MAP.get(genero_id, "Desconhecido")
        dados_filme = {
            "titulo": filme["title"],
            "genero": genero_nome
        }
        try:
            print(f"Enviando filme: {dados_filme}")
            response = requests.post(URL_FASTAPI, json=dados_filme, timeout=10)
            print("Status Code:", response.status_code)
            print("Response Body:", response.text)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar filme: {e}")

def atualizar_dados():
    """ Função principal que busca os filmes do TMDB e os envia para a API """
    print("🔄 Iniciando atualização de dados...")
    filmes = buscar_filmes_tmdb()
    if filmes:
        enviar_filmes_para_api(filmes)
    else:
        print("⚠️ Nenhum filme foi encontrado no TMDB.")

# Agendando para rodar a cada 5 minutos
schedule.every(1).minutes.do(atualizar_dados)

print("⏳ Serviço agendado para rodar a cada 5 minutos...")

while True:
    schedule.run_pending()
    time.sleep(60)
