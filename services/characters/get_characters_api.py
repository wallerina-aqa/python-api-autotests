import allure
import httpx

from schemas.characters_schemas import GetListOfCharactersResponseSchema
from services.characters.characters_api import CharactersAPI


class GetCharactersAPI(CharactersAPI):
    def __init__(self):
        super().__init__()
        self.GET_CHARACTERS_API = self.CHARACTERS_API
        self.TIMEOUT = 10

        self.GENDER = None
        self.STATUS = None
        self.SPECIES = None
        self.ORDER_BY = "id"
        self.ORDER_BY_DIRECTION = "asc"
        self.QUERY = None
        self.PAGE = 1
        self.SIZE = 50

    @allure.step("Forming request parameters")
    def create_params(
        self,
        gender: str | None = None,
        status: str | None = None,
        species: str | None = None,
        order_by: str | None = None,
        order_by_direction: str | None = None,
        query: str | None = None,
        page: int | None = None,
        size: int | None = None,
    ):
        if gender is None:
            gender = self.GENDER
        if status is None:
            status = self.STATUS
        if species is None:
            species = self.SPECIES
        if order_by is None:
            order_by = self.ORDER_BY
        if order_by_direction is None:
            order_by_direction = self.ORDER_BY_DIRECTION
        if query is None:
            query = self.QUERY
        if page is None:
            page = self.PAGE
        if size is None:
            size = self.SIZE

        params = {
            "gender": gender,
            "status": status,
            "species": species,
            "orderBy": order_by,
            "orderByDirection": order_by_direction,
            "query": query,
            "page": page,
            "size": size,
        }

        return {key: value for key, value in params.items() if value is not None}

    @allure.step("Send GET request to get characters")
    def send_request(
        self,
        gender=None,
        status=None,
        species=None,
        order_by=None,
        order_by_direction=None,
        query=None,
        page=None,
        size=None,
    ):
        params = self.create_params(
            gender=gender,
            status=status,
            species=species,
            order_by=order_by,
            order_by_direction=order_by_direction,
            query=query,
            page=page,
            size=size,
        )
        self.REQUEST_PARAMS = params

        response = httpx.get(
            self.GET_CHARACTERS_API, params=self.REQUEST_PARAMS, timeout=self.TIMEOUT
        )
        self.STATUS_CODE = response.status_code

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            self.RESPONSE_DATA = GetListOfCharactersResponseSchema(**response.json())
