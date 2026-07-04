from services.base_api import BaseAPI


class RandomAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.RANDOM_API = f"{self.BASE_API}/random"
