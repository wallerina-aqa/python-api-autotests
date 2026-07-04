import allure
import httpx

from schemas.characters_schemas import GetCharacterResponse
from services.random.random_api import RandomAPI


class GetRandomCharacterAPI(RandomAPI):
    def __init__(self):
        super().__init__()
        self.RANDOM_CHARACTER_API = f"{self.RANDOM_API}/character"
        self.TIME_OUT = 10

    @allure.step("Send GET request to get random character")
    def send_request(self):
        response = httpx.get(self.RANDOM_CHARACTER_API)
        self.STATUS_CODE = response.status_code

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            self.RESPONSE_DATA = GetCharacterResponse(**response.json())
