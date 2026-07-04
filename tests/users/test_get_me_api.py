import allure
import pytest


@pytest.mark.users
@pytest.mark.regression
class TestGetMe:
    @allure.feature("Users service")
    @allure.story("Get information about current user")
    @allure.title("Get current user details success")
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_get_me_positive(self, get_me_api, access_token):
        get_me_api.send_request(access_token=access_token)
        get_me_api.assert_response_status(status_code=200)

    @allure.feature("Users service")
    @allure.story("Get information about current user")
    @allure.title("Get current user details without access token failure")
    @pytest.mark.negative
    @pytest.mark.smoke
    def test_get_me_without_token_negative(self, get_me_api):
        get_me_api.send_request()
        get_me_api.assert_response_status(status_code=401)
        get_me_api.assert_error_message()
