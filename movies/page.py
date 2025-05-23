import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from datetime import datetime
from movies.service import MovieService
from genres.service import GenreService
from actors.service import ActorService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Lista de Filmes')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum filme encontrado.')

    st.title('Cadastrar novo Filme')
    title = st.text_input('Título do filme')

    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    resume = st.text_area('Resumo')

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actors_name = {actor['name']: actor['id'] for actor in actors}
    selected_actor_name = st.multiselect('Ator/Atriz', list(actors_name.keys()))
    selected_actors_ids = [actors_name[name] for name in selected_actor_name]

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genres_name = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', list(genres_name.keys()))

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            resume=resume,
            actors=selected_actors_ids,
            genre=genres_name[selected_genre_name],
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar novo filme, verifique os campos e tente novamente.')
