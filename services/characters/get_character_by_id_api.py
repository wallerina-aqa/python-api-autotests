import allure
import httpx
from pydantic import HttpUrl

from schemas.characters_schemas import GetCharacterResponseSchema
from schemas.error_schemas import ErrorMessageResponseSchema
from services.characters.characters_api import CharactersAPI


class GetCharacterByIdAPI(CharactersAPI):
    def __init__(self):
        super().__init__()
        self.TIMEOUT = 20

    @allure.step("Send GET request to get character by id")
    def send_request(self, character_id=1):
        self.reset_attributes("STATUS_CODE", "ERROR_MESSAGE", "RESPONSE_DATA")

        response = httpx.get(
            f"{self.CHARACTERS_API}/{character_id}", timeout=self.TIMEOUT
        )
        self.STATUS_CODE = response.status_code

        if response.status_code == 404:
            self.ERROR_MESSAGE = self.NOT_FOUND_ERROR_MESSAGE
            self.SCHEMA = ErrorMessageResponseSchema
        else:
            self.SCHEMA = GetCharacterResponseSchema

        self.get_response_data(response)

    @allure.step("Assert character name")
    def assert_character_name(self, character_name):
        if not isinstance(self.RESPONSE_DATA, GetCharacterResponseSchema):
            raise TypeError(
                "Expected RESPONSE_DATA to be GetCharacterResponseSchema, "
                f"but got {type(self.RESPONSE_DATA).__name__}"
            )

        expected_name = character_name
        actual_name = self.RESPONSE_DATA.name
        assert actual_name == expected_name, (
            f"Character's name should be '{expected_name}', "
            f"but actual name is '{actual_name}'"
        )

    @allure.step("Assert character image")
    def assert_character_image(self, character_image):
        if not isinstance(self.RESPONSE_DATA, GetCharacterResponseSchema):
            raise TypeError(
                "Expected RESPONSE_DATA to be GetCharacterResponseSchema, "
                f"but got {type(self.RESPONSE_DATA).__name__}"
            )

        expected_image = character_image
        actual_image = self.RESPONSE_DATA.image
        assert actual_image == HttpUrl(expected_image), (
            f"Character's image should be '{expected_image}', "
            f"but actual image is '{actual_image}'"
        )
