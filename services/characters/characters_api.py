import allure
from pydantic import HttpUrl

from services.base_api import BaseAPI


class CharactersAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.CHARACTERS_API = f"{self.BASE_API}/characters"
        self.NOT_FOUND_ERROR_MESSAGE = "Character not found"

    @allure.step("Assert character name")
    def assert_character_name(self, character_name):
        expected_name = character_name
        actual_name = self.RESPONSE_DATA.name
        assert actual_name == expected_name, (
            f"Character's name should be '{expected_name}', "
            f"but actual name is '{actual_name}'"
        )

    @allure.step("Assert character image")
    def assert_character_image(self, character_image):
        expected_image = character_image
        actual_image = self.RESPONSE_DATA.image
        assert actual_image == HttpUrl(expected_image), (
            f"Character's image should be '{expected_image}', "
            f"but actual image is '{actual_image}'"
        )
