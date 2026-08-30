import allure
import httpx

from schemas.users_schemas import GetUsersResponseSchema
from services.users.users_api import UsersAPI


class GetUsersAPI(UsersAPI):
    def __init__(self):
        super().__init__()
        self.GET_USERS_API = self.USERS_API
        self.TIMEOUT = 25
        self.SCHEMA = GetUsersResponseSchema

        self.QUERY = None
        self.PAGE = 1
        self.SIZE = 50

    @allure.step("Forming request parameters")
    def create_params(
        self,
        query: str,
        page: int | None = None,
        size: int | None = None,
    ):
        self.QUERY = query
        if page is None:
            page = self.PAGE
        if size is None:
            size = self.SIZE

        params = {
            "query": query,
            "page": page,
            "size": size,
        }

        return params

    @allure.step("Send GET request to get list of users by username")
    def send_request(self, username: str, page=None, size=None):
        self.reset_attributes("REQUEST_PARAMS", "STATUS_CODE", "RESPONSE_DATA")

        params = self.create_params(query=username, page=page, size=size)
        self.REQUEST_PARAMS = params

        response = httpx.get(
            self.GET_USERS_API, params=self.REQUEST_PARAMS, timeout=self.TIMEOUT
        )
        self.STATUS_CODE = response.status_code
        self.get_response_data(response)

    @allure.step("Assert usernames equal to the one requested")
    def assert_usernames(self, username):
        if not isinstance(self.RESPONSE_DATA, GetUsersResponseSchema):
            raise TypeError(
                "Expected RESPONSE_DATA to be GetUsersResponseSchema, "
                f"but got {type(self.RESPONSE_DATA).__name__}"
            )

        for user in self.RESPONSE_DATA.items:
            actual_username = user.username
            assert actual_username == username, (
                f"Users usernames should be '{username}', "
                f"but one user's username is '{actual_username}'"
            )
