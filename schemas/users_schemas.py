from datetime import datetime

from pydantic import BaseModel, Field, EmailStr, ConfigDict


class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    name: str = Field(min_length=1, max_length=64)
    surname: str = Field(min_length=1, max_length=64)
    middle_name: str | None = Field(
        alias="middleName", default=None, min_length=1, max_length=64
    )
    email: EmailStr
    username: str = Field(min_length=5, max_length=64)
    password: str = Field(min_length=8, max_length=128)
    is_subscribed: bool = Field(alias="isSubscribed", default=True)


class UserResponseSchema(BaseModel):
    id: int
    created_at: datetime = Field(alias="createdAt")
    name: str = Field(min_length=1, max_length=64)
    surname: str = Field(min_length=1, max_length=64)
    middle_name: str | None = Field(
        alias="middleName", default=None, min_length=1, max_length=64
    )
    email: EmailStr
    username: str = Field(min_length=5, max_length=64)
    password: str = Field(min_length=8, max_length=128)
    is_subscribed: bool = Field(alias="isSubscribed")
    is_confirmed: bool = Field(alias="isConfirmed")


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
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    name: str | None = Field(default=None, min_length=1, max_length=64)
    surname: str | None = Field(default=None)
    middle_name: str | None = Field(
        alias="middleName", default=None, min_length=1, max_length=64
    )
    password: str | None = Field(default=None, min_length=8, max_length=128)
    is_subscribed: bool | None = Field(alias="isSubscribed", default=None)
