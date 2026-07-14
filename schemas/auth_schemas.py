from pydantic import BaseModel


class GetUserAuthTokenResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
