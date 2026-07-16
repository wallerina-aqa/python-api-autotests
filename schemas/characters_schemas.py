from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, HttpUrl, Field


class CharacterGender(StrEnum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    UNKNOWN = "UNKNOWN"


class CharacterStatus(StrEnum):
    ALIVE = "ALIVE"
    DEAD = "DEAD"
    UNKNOWN = "UNKNOWN"


class CharactersSpecies(StrEnum):
    HUMAN = "HUMAN"
    ROBOT = "ROBOT"
    HEAD = "HEAD"
    ALIEN = "ALIEN"
    MUTANT = "MUTANT"
    MONSTER = "MONSTER"
    UNKNOWN = "UNKNOWN"


class GetCharacterResponseSchema(BaseModel):
    id: int
    name: str
    gender: CharacterGender
    status: CharacterStatus
    created_at: datetime = Field(alias="createdAt")
    image: HttpUrl | None = None


class GetListOfCharactersResponseSchema(BaseModel):
    items: list[GetCharacterResponseSchema]
    total: int = Field(description="Total number of characters")
    page: int = Field(description="Page number")
    size: int = Field(description="Size per page")
    pages: int = Field(description="Number of pages")
