import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from actors.service import ActorService
from datetime import datetime


NATIONALITIES = {
    'AFG': 'Afeganistão',
    'ALB': 'Albânia',
    'DEU': 'Alemanha',
    'AND': 'Andorra',
    'AGO': 'Angola',
    'ARG': 'Argentina',
    'ARM': 'Armênia',
    'AUS': 'Austrália',
    'AUT': 'Áustria',
    'AZE': 'Azerbaijão',
    'BHS': 'Bahamas',
    'BHR': 'Bahrein',
    'BGD': 'Bangladesh',
    'BRB': 'Barbados',
    'BEL': 'Bélgica',
    'BLZ': 'Belize',
    'BEN': 'Benim',
    'BLR': 'Bielorrússia',
    'BOL': 'Bolívia',
    'BIH': 'Bósnia e Herzegovina',
    'BWA': 'Botsuana',
    'BRA': 'Brasil',
    'BRN': 'Brunei',
    'BGR': 'Bulgária',
    'BFA': 'Burkina Faso',
    'BDI': 'Burundi',
    'BTN': 'Butão',
    'CPV': 'Cabo Verde',
    'CMR': 'Camarões',
    'KHM': 'Camboja',
    'CAN': 'Canadá',
    'QAT': 'Catar',
    'KAZ': 'Cazaquistão',
    'TCD': 'Chade',
    'CHL': 'Chile',
    'CHN': 'China',
    'CYP': 'Chipre',
    'COL': 'Colômbia',
    'COM': 'Comores',
    'COG': 'Congo',
    'PRK': 'Coreia do Norte',
    'KOR': 'Coreia do Sul',
    'CIV': 'Costa do Marfim',
    'CRI': 'Costa Rica',
    'HRV': 'Croácia',
    'CUB': 'Cuba',
    'DNK': 'Dinamarca',
    'DJI': 'Djibuti',
    'DMA': 'Dominica',
    'EGY': 'Egito',
    'SLV': 'El Salvador',
    'ARE': 'Emirados Árabes Unidos',
    'ECU': 'Equador',
    'ERI': 'Eritreia',
    'SVK': 'Eslováquia',
    'SVN': 'Eslovênia',
    'ESP': 'Espanha',
    'USA': 'Estados Unidos',
    'EST': 'Estônia',
    'ETH': 'Etiópia',
    'FJI': 'Fiji',
    'PHL': 'Filipinas',
    'FIN': 'Finlândia',
    'FRA': 'França',
    'GAB': 'Gabão',
    'GMB': 'Gâmbia',
    'GHA': 'Gana',
    'GEO': 'Geórgia',
    'GRD': 'Granada',
    'GRC': 'Grécia',
    'GTM': 'Guatemala',
    'GUY': 'Guiana',
    'GIN': 'Guiné',
    'GNB': 'Guiné-Bissau',
    'GNQ': 'Guiné Equatorial',
    'HTI': 'Haiti',
    'NLD': 'Holanda',
    'HND': 'Honduras',
    'HUN': 'Hungria',
    'YEM': 'Iêmen',
    'IND': 'Índia'
}


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Atores e Atrizes')
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid'
        )
    else:
        st.warning('Nenhum Ator/Atriz encontrado.')

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do ator/atriz')
    birthday = st.date_input(
        label='Data de nascimento',
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nationality = st.selectbox(
        label='Nacionalidade',
        options=list(NATIONALITIES.keys()),
        format_func=lambda sigla: NATIONALITIES[sigla],
    )
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o(a) Ator/Atriz, verifique os campos e tente novamente.')
