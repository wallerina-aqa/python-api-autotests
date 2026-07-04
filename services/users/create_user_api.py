import allure
import httpx

from schemas.error_schemas import ErrorMessageResponse
from schemas.users_schemas import CreateUserRequest, UserResponse
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

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            if self.STATUS_CODE == 409:
                self.ERROR_MESSAGE = self.ALREADY_EXISTS_ERROR_MESSAGE
                self.RESPONSE_DATA = ErrorMessageResponse(**response.json())
            else:
                self.RESPONSE_DATA = UserResponse(**response.json())
