import requests
import streamlit as st
from login.service import logout


class ReviewRepository:

    def __init__(self):
        self.__base_url = 'https://akeenathon.pythonanywhere.com/api/v1/'
        self.__reviews_url = f'{self.__base_url}reviews/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_reviews(self):
        response = requests.get(
            self.__reviews_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API, status code: {response.status_code}')

    def create_review(self, review):
        response = requests.post(
            self.__reviews_url,
            headers=self.__headers,
            data=review,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao criar review, status code: {response.status_code}')
