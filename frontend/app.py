import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_URL = "http://127.0.0.1:8000"

st.title("Dashboard de Filmes")

# Função para obter filmes da API e converter em DataFrame
def get_filmes():
    response = requests.get(f"{API_URL}/filmes")
    filmes = response.json()
    # Transformar os dados em um DataFrame
    df = pd.DataFrame(filmes)
    return df

# Função para criar gráfico de barras com a quantidade nos rótulos
def plot_filmes_por_genero(df):
    genero_count = df['genero'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=genero_count.index, y=genero_count.values, ax=ax)
    for i in ax.containers:
        ax.bar_label(i, label_type='edge')
    ax.set_title("Quantidade de Filmes por Gênero")
    ax.set_ylabel("Quantidade")
    ax.set_xlabel("Gênero")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Obter os filmes e exibir na tabela e no gráfico
df_filmes = get_filmes()

# Gráfico de Barras
st.subheader("Gráfico de Filmes por Gênero")
plot_filmes_por_genero(df_filmes)

# Tabela com Paginação
st.subheader("Tabela de Filmes")
filmes_por_pagina = 10
total_paginas = (len(df_filmes) // filmes_por_pagina) + 1

# Adicionar um seletor de página
pagina = st.number_input("Página", min_value=1, max_value=total_paginas, value=1, step=1)
start = (pagina - 1) * filmes_por_pagina
end = start + filmes_por_pagina

st.table(df_filmes.iloc[start:end][["titulo", "genero"]])




