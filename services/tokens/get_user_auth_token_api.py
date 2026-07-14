import allure
import httpx

from schemas.auth_schemas import GetUserAuthTokenResponseSchema
from schemas.error_schemas import ErrorMessageResponseSchema
from services.tokens.tokens_api import TokensAPI


class GetUserAuthTokenAPI(TokensAPI):
    def __init__(self):
        super().__init__()
        self.GET_USER_AUTH_TOKEN_API = f"{self.TOKENS_API}/auth"
        self.TIMEOUT = 10
        self.ACCESS_TOKEN = None

    @allure.step("Send POST request to get user auth tokens")
    def send_request(self, username, password):
        user_data = {"username": username, "password": password}
        response = httpx.post(
            self.GET_USER_AUTH_TOKEN_API, data=user_data, timeout=self.TIMEOUT
        )
        self.STATUS_CODE = response.status_code

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            if self.STATUS_CODE == 401:
                self.ERROR_MESSAGE = self.UNAUTHORIZED_ERROR_MESSAGE
                self.RESPONSE_DATA = ErrorMessageResponseSchema(**response.json())
            else:
                self.RESPONSE_DATA = GetUserAuthTokenResponseSchema(**response.json())
                self.ACCESS_TOKEN = self.RESPONSE_DATA.access_token
