import allure
import pytest


@pytest.mark.characters
@pytest.mark.regression
class TestGetCharacters:
    @allure.feature("Characters service")
    @allure.story("Get list of characters")
    @allure.title("Get list of characters success")
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_get_characters_positive(self, get_characters_api):
        get_characters_api.send_request()
        get_characters_api.assert_response_status(status_code=200)
        get_characters_api.assert_items_quantity()
