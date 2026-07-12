import allure
import httpx

from services.users.users_api import UsersAPI


class GetMeAPI(UsersAPI):
    def __init__(self):
        super().__init__()
        self.GET_ME_API = f"{self.USERS_API}/me"
        self.TIMEOUT = 10

    @allure.step("Send GET request to get information about current user")
    def send_request(self, access_token=None):
        headers = {"Authorization": f"Bearer {access_token}"}
        response = httpx.get(self.GET_ME_API, headers=headers, timeout=self.TIMEOUT)
        self.STATUS_CODE = response.status_code
        self.get_user_response_data(response)
