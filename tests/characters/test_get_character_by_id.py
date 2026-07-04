import allure
import pytest

from tests.characters.test_data import characters_ids_names_images


@pytest.mark.characters
@pytest.mark.regression
class TestGetCharacterById:
    @allure.feature("Characters service")
    @allure.story("Get character by id")
    @allure.title("Get character by id success")
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "params",
        characters_ids_names_images,
        ids=[
            "id_1_Philip_J_Fry",
            "id_16_Bender_Bending_Rodriguez",
            "id_425_Turanga_Leela",
        ],
    )
    def test_get_character_by_id_positive(self, get_character_by_id_api, params):
        character_id, character_name, character_image = params
        get_character_by_id_api.send_request(character_id=character_id)
        get_character_by_id_api.assert_response_status(status_code=200)
        get_character_by_id_api.assert_character_name(character_name=character_name)
        get_character_by_id_api.assert_character_image(character_image=character_image)

    @allure.feature("Characters service")
    @allure.story("Get character by id")
    @allure.title("Get character by unexisting id failure")
    @pytest.mark.negative
    @pytest.mark.smoke
    def test_get_character_by_unexisting_id_negative(self, get_character_by_id_api):
        get_character_by_id_api.send_request(character_id=0)
        get_character_by_id_api.assert_response_status(status_code=404)
        get_character_by_id_api.assert_error_message()
