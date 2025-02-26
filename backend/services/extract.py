import requests

API_KEY = 'c90c917f98d91bd0c1fd096a6b77ab58'
URL_TMDB = "https://api.themoviedb.org/3/movie/popular"

def get_filmes_populares():
    """ Obtém os filmes populares do TMDB """
    try:
        params = {"api_key": API_KEY, "language": "pt-BR", "page": 1}
        response = requests.get(URL_TMDB, params=params, timeout=10)
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar filmes do TMDB: {e}")
        return []