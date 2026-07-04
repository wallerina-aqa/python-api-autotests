import allure
import pytest


@pytest.mark.users
@pytest.mark.regression
class TestGetUsers:
    @allure.feature("Users service")
    @allure.story("Get list of users by username")
    @allure.title("Get list of users by username success")
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_get_users_positive(self, get_users_api, created_user_username_password):
        get_users_api.send_request(username=created_user_username_password[0])
        get_users_api.assert_response_status(status_code=200)
        get_users_api.assert_usernames(username=created_user_username_password[0])
