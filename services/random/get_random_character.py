import allure
import httpx

from schemas.characters_schemas import GetCharacterResponseSchema
from services.random.random_api import RandomAPI


class GetRandomCharacterAPI(RandomAPI):
    def __init__(self):
        super().__init__()
        self.RANDOM_CHARACTER_API = f"{self.RANDOM_API}/character"
        self.TIMEOUT = 10

    @allure.step("Send GET request to get random character")
    def send_request(self):
        self.reset_attributes("STATUS_CODE", "RESPONSE_DATA")

        response = httpx.get(self.RANDOM_CHARACTER_API, timeout=self.TIMEOUT)
        self.STATUS_CODE = response.status_code

        content_type = response.headers.get("content-type", "")
        if "application/json" not in content_type:
            raise ValueError(
                f"Expected application/json content type, but got {content_type!r}"
            )
        self.RESPONSE_DATA = GetCharacterResponseSchema(**response.json())
