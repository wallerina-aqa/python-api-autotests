import allure
import pytest


@pytest.mark.tokens
@pytest.mark.regression
class TestGetUserAuthToken:
    @allure.feature("Authentication")
    @allure.story("Get user auth tokens")
    @allure.title("Get user auth tokens success")
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_get_user_auth_token_positive(
        self, get_user_auth_token_api, created_user_username_password
    ):
        username, password = created_user_username_password
        get_user_auth_token_api.send_request(username=username, password=password)
        get_user_auth_token_api.assert_response_status(status_code=200)

    @allure.feature("Authentication")
    @allure.story("Get user auth tokens")
    @allure.title("Get unexisting user auth tokens failure")
    @pytest.mark.negative
    @pytest.mark.smoke
    def test_get_unexisting_user_auth_token_negative(
        self, get_user_auth_token_api, unexisting_user_username_password
    ):
        username, password = unexisting_user_username_password
        get_user_auth_token_api.send_request(username=username, password=password)
        get_user_auth_token_api.assert_response_status(status_code=401)
        get_user_auth_token_api.assert_error_message()
