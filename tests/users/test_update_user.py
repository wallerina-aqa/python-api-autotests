import allure
import pytest


@pytest.mark.users
@pytest.mark.regression
class TestUpdateUser:
    @allure.feature("Users service")
    @allure.story("Update user details")
    @allure.title("Update user details success")
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_update_user_positive(
        self, update_user_api, user_data_to_update, access_token, get_me_api
    ):
        update_user_api.send_request(
            user_data_to_update=user_data_to_update,
            access_token=access_token,
        )
        update_user_api.assert_response_status(status_code=200)

        get_me_api.send_request(access_token=access_token)
        get_me_api.assert_response_status(status_code=200)
        get_me_api.assert_response_data(
            expected_data=user_data_to_update, ignore_missing_fields=True
        )

    @allure.feature("Users service")
    @allure.story("Update user details")
    @allure.title("Update user details without access token failure")
    @pytest.mark.negative
    @pytest.mark.smoke
    def test_update_user_without_access_token_negative(
        self, update_user_api, user_data_to_update
    ):
        update_user_api.send_request(user_data_to_update=user_data_to_update)
        update_user_api.assert_response_status(status_code=401)
        update_user_api.assert_error_message()
