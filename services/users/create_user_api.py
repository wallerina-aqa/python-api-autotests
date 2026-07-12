import allure
import httpx

from schemas.users_schemas import CreateUserRequest
from services.users.users_api import UsersAPI


class CreateUserAPI(UsersAPI):
    def __init__(self):
        super().__init__()
        self.CREATE_USER_API = self.USERS_API
        self.TIMEOUT = 20

    @allure.step("Send POST request to create new user")
    def send_request(self, new_user_data, validate=True):
        if validate:
            new_user_data = CreateUserRequest(**new_user_data).model_dump()

        response = httpx.post(
            self.CREATE_USER_API, json=new_user_data, timeout=self.TIMEOUT
        )
        self.STATUS_CODE = response.status_code
        self.get_user_response_data(response)
