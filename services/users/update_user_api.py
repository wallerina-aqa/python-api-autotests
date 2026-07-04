import allure
import httpx

from schemas.error_schemas import ErrorMessageResponse
from schemas.users_schemas import UpdateUserRequest, UserResponse
from services.users.users_api import UsersAPI


class UpdateUserAPI(UsersAPI):
    def __init__(self):
        super().__init__()
        self.UPDATE_USER_API = self.USERS_API
        self.TIMEOUT = 20

    @allure.step("Send PUT request to fully update user")
    def send_request(self, user_data_to_update, access_token=None, validate=True):
        headers = {"Authorization": f"Bearer {access_token}"}
        if validate:
            user_data_to_update = UpdateUserRequest(**user_data_to_update).model_dump(
                exclude_none=True
            )

        response = httpx.put(
            self.UPDATE_USER_API,
            headers=headers,
            json=user_data_to_update,
            timeout=self.TIMEOUT,
        )
        self.STATUS_CODE = response.status_code

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            if self.STATUS_CODE == 401:
                self.ERROR_MESSAGE = self.UNAUTHORIZED_ERROR_MESSAGE
                self.RESPONSE_DATA = ErrorMessageResponse(**response.json())
            else:
                self.RESPONSE_DATA = UserResponse(**response.json())
