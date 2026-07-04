import allure
import httpx

from schemas.users_schemas import GetUsersResponse
from services.users.users_api import UsersAPI


class GetUsersAPI(UsersAPI):
    def __init__(self):
        super().__init__()
        self.GET_USERS_API = self.USERS_API
        self.TIMEOUT = 25

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
        params = self.create_params(query=username, page=page, size=size)
        self.REQUEST_PARAMS = params

        response = httpx.get(self.GET_USERS_API, params=params, timeout=self.TIMEOUT)
        self.STATUS_CODE = response.status_code

        content_type = response.headers.get("content-type")
        if content_type == "application/json":
            self.RESPONSE_DATA = GetUsersResponse(**response.json())
