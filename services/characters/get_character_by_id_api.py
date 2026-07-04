import allure
import httpx

from schemas.characters_schemas import GetCharacterResponse
from schemas.error_schemas import ErrorMessageResponse
from services.characters.characters_api import CharactersAPI


class GetCharacterByIdAPI(CharactersAPI):
    def __init__(self):
        super().__init__()
        self.TIMEOUT = 20

    @allure.step("Send GET request to get character by id")
    def send_request(self, character_id=1):
        response = httpx.get(
            f"{self.CHARACTERS_API}/{character_id}", timeout=self.TIMEOUT
        )
        self.STATUS_CODE = response.status_code

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            if response.status_code == 404:
                self.ERROR_MESSAGE = self.NOT_FOUND_ERROR_MESSAGE
                self.RESPONSE_DATA = ErrorMessageResponse(**response.json())
            else:
                self.RESPONSE_DATA = GetCharacterResponse(**response.json())
