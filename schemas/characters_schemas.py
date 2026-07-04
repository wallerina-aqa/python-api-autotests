from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl, Field


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    UNKNOWN = "UNKNOWN"


class Status(str, Enum):
    ALIVE = "ALIVE"
    DEAD = "DEAD"
    UNKNOWN = "UNKNOWN"


class Species(str, Enum):
    HUMAN = "HUMAN"
    ROBOT = "ROBOT"
    HEAD = "HEAD"
    ALIEN = "ALIEN"
    MUTANT = "MUTANT"
    MONSTER = "MONSTER"
    UNKNOWN = "UNKNOWN"


class GetCharacterResponse(BaseModel):
    id: int
    name: str
    gender: Gender
    status: Status
    createdAt: datetime
    image: HttpUrl | None = None


class GetListOfCharactersResponse(BaseModel):
    items: list[GetCharacterResponse]
    total: int = Field(description="Total number of characters")
    page: int = Field(description="Page number")
    size: int = Field(description="Size per page")
    pages: int = Field(description="Number of pages")
