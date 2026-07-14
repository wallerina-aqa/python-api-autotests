from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class CreateUserRequestSchema(BaseModel):
    name: str = Field(min_length=1, max_length=64)
    surname: str = Field(min_length=1, max_length=64)
    middleName: str | None = Field(default=None, min_length=1, max_length=64)
    email: EmailStr
    username: str = Field(min_length=5, max_length=64)
    password: str = Field(min_length=8, max_length=128)
    isSubscribed: bool = Field(default=True)


class UserResponseSchema(BaseModel):
    id: int
    createdAt: datetime
    name: str = Field(min_length=1, max_length=64)
    surname: str = Field(min_length=1, max_length=64)
    middleName: str | None = Field(default=None, min_length=1, max_length=64)
    email: EmailStr
    username: str = Field(min_length=5, max_length=64)
    password: str = Field(min_length=8, max_length=128)
    isSubscribed: bool
    isConfirmed: bool


class UserDataSchema(BaseModel):
    id: int
    isConfirmed: bool
    createdAt: datetime
    username: str = Field(min_length=5, max_length=64)
    name: str | None = None
    surname: str | None = None


class GetUsersResponseSchema(BaseModel):
    items: list[UserDataSchema]
    total: int = Field(ge=0)
    page: int = Field(ge=1)
    size: int = Field(ge=1)
    pages: int = Field(ge=0)


class UpdateUserRequestSchema(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=64)
    surname: str | None = Field(default=None)
    middleName: str | None = Field(default=None, min_length=1, max_length=64)
    password: str | None = Field(default=None, min_length=8, max_length=128)
    isSubscribed: bool | None = Field(default=None)
