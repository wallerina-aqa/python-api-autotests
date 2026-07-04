import allure

from services.base_api import BaseAPI


class UsersAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.USERS_API = f"{self.BASE_API}/users"
        self.ALREADY_EXISTS_ERROR_MESSAGE = "User already exists."

    @allure.step("Assert usernames equal to the one requested")
    def assert_usernames(self, username):
        for user in self.RESPONSE_DATA.items:
            actual_username = user.username
            assert actual_username == username, (
                f"Users usernames should be '{username}', "
                f"but one user's username is '{actual_username}'"
            )
