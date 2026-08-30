from services.base_api import BaseAPI


class TokensAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.TOKENS_API = f"{self.BASE_API}/tokens/users"
