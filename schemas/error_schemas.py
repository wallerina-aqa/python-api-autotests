from pydantic import BaseModel


class ErrorMessageResponse(BaseModel):
    detail: str
