from pydantic import BaseModel


class GetUserAuthTokenResponse(BaseModel):
    access_token: str
    refresh_token: str
