from http import HTTPStatus
from httpx import Response

from models.authentication import AdminAuthUser
from utils.clients.http.client import APIClient
from utils.constants.routes import APIRoutes


class AuthenticationClient(APIClient):

    def get_auth_token_api(self, payload: AdminAuthUser) -> Response:
        return self.client.post(f'{APIRoutes.AUTH_ADMIN_NEW}', json=payload.model_dump())

    def get_auth_token(self, payload: AdminAuthUser) -> str:

        response = self.get_auth_token_api(payload)
        json_response = response.json()

        assert response.status_code == HTTPStatus.OK
        assert json_response.get('session')
        return json_response['session']
