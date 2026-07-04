import allure
import pytest


@pytest.mark.random
@pytest.mark.regression
class TestGetRandomCharacter:
    @allure.feature("Random service")
    @allure.story("Get random character")
    @allure.title("Get random character success")
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_get_random_character_positive(self, get_random_character_api):
        get_random_character_api.send_request()
        get_random_character_api.assert_response_status(status_code=200)
