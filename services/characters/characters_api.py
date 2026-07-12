from services.base_api import BaseAPI


class CharactersAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.CHARACTERS_API = f"{self.BASE_API}/characters"
        self.NOT_FOUND_ERROR_MESSAGE = "Character not found"
