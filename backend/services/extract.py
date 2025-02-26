import requests

# Substitua pela sua chave de API
api_key = 'c90c917f98d91bd0c1fd096a6b77ab58'

# URL para acessar a API do TMDB
url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=pt-BR&page=1"

def get_filmes_populares():
    response = requests.get(url)
    return response.json()