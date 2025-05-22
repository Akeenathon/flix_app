import requests


class Auth:

    def __init__(self):
        self.__base_url = 'https://akeenathon.pythonanywhere.com/api/v1/'  # link da API (flix_api)
        self.__auth_url = f'{self.__base_url}authentication/token/'

    def get_token(self, username, password):
        """
        Método para autenticar o usuário e obter o token de acesso.
        :username: Nome de usuário
        :password: Senha do usuário
        :return: Token de acesso
        """
        auth_payload = {
            'username': username,
            'password': password
        }
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Falha na autenticação. status code: {auth_response.status_code}'}
