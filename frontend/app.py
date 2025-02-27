import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from auth import is_admin
import io

API_URL = "http://127.0.0.1:8000"

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.experimental_set_query_params(page="login")
    st.warning("Por favor, faça login para continuar.")
else:
    st.title("Dashboard de Filmes")

    # Função para obter filmes da API e converter em DataFrame
    def get_filmes():
        response = requests.get(f"{API_URL}/filmes")
        filmes = response.json()
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

    # Função para exportar dados para Excel
    def to_excel(df):
        output = io.BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='Filmes')
        writer.close()
        processed_data = output.getvalue()
        return processed_data

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

    # Adicionar botão para exportar dados para Excel
    if st.button("Download"):
        df_xlsx = to_excel(df_filmes)
        st.download_button(label='📥 Baixar Excel',
                           data=df_xlsx,
                           file_name='filmes.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')    

    # Verificar se o usuário é administrador
    if is_admin(st.session_state.username):
        st.subheader("Administração")
        st.write("Aqui você pode adicionar funcionalidades de administração.")

