import allure
import httpx

from schemas.users_schemas import UpdateUserRequest
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
        self.get_user_response_data(response)
