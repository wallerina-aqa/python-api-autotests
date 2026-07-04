import allure
import pytest


@pytest.mark.users
@pytest.mark.regression
class TestCreateUser:
    @allure.feature("Users service")
    @allure.story("Create user")
    @allure.title("Create user success")
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_create_user_positive(self, new_user_data, create_user_api, get_users_api):
        create_user_api.send_request(new_user_data=new_user_data)
        create_user_api.assert_response_status(status_code=201)

        username = new_user_data.get("username")
        get_users_api.send_request(username=username)
        get_users_api.assert_response_status(status_code=200)
        get_users_api.assert_usernames(username=username)

    @allure.feature("Users service")
    @allure.story("Create user")
    @allure.title("Create user with existing username failure")
    @pytest.mark.negative
    @pytest.mark.smoke
    def test_create_user_with_existing_username_negative(
        self, created_user_username_password, new_user_data, create_user_api
    ):
        existing_username = created_user_username_password[0]
        new_user_data["username"] = existing_username
        create_user_api.send_request(new_user_data=new_user_data)
        create_user_api.assert_response_status(status_code=409)
        create_user_api.assert_error_message()
