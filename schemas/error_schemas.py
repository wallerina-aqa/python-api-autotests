from pydantic import BaseModel


class ErrorMessageResponseSchema(BaseModel):
    detail: str
