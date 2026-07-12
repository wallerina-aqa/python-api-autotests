from schemas.error_schemas import ErrorMessageResponse
from schemas.users_schemas import UserResponse
from services.base_api import BaseAPI


class UsersAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.USERS_API = f"{self.BASE_API}/users"
        self.ALREADY_EXISTS_ERROR_MESSAGE = "User already exists."

    def get_user_response_data(self, response):
        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            if self.STATUS_CODE in (401, 409):
                if self.STATUS_CODE == 401:
                    self.ERROR_MESSAGE = self.UNAUTHORIZED_ERROR_MESSAGE
                else:
                    self.ERROR_MESSAGE = self.ALREADY_EXISTS_ERROR_MESSAGE
                self.RESPONSE_DATA = ErrorMessageResponse(**response.json())
            else:
                self.RESPONSE_DATA = UserResponse(**response.json())
