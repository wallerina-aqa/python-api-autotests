from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl, Field


class CharacterGender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    UNKNOWN = "UNKNOWN"


class CharacterStatus(str, Enum):
    ALIVE = "ALIVE"
    DEAD = "DEAD"
    UNKNOWN = "UNKNOWN"


class CharactersSpecies(str, Enum):
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
    createdAt: datetime
    image: HttpUrl | None = None


class GetListOfCharactersResponseSchema(BaseModel):
    items: list[GetCharacterResponseSchema]
    total: int = Field(description="Total number of characters")
    page: int = Field(description="Page number")
    size: int = Field(description="Size per page")
    pages: int = Field(description="Number of pages")
