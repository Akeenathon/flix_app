import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genres_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de Gêneros')
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=genres_df,
            reload_data=True,
            key='genres_grid',
        )
    else:
        st.warning('Nenhum gênero encontrado.')

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        new_genre = genres_service.create_genre(
            name=name
        )
        if new_genre:
            st.success(f'Gênero "{name}" cadastrado com sucesso!')
            st.rerun()
        else:
            st.error('Erro ao cadastrar o gênero. Verifique os campos e tente novamente.')
