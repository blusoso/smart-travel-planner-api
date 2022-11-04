from typing import List
from pydantic import BaseModel
from ..place.schema import Place
from ...language_code.schema import LanguageCode


class PlaceInformationBase(BaseModel):
    intro: str | None = None
    description: str | None = None
    activities: List[str] | None = None
    facilities: List[str] | None = None
    how_to_travel: str | None = None


class PlaceInformationCreate(PlaceInformationBase):
    place_id: str
    language_code_id: str

    class Config:
        orm_mode = True


class PlaceInformation(PlaceInformationBase):
    id: int
    place: Place
    bag_of_words: List[str] | None = None
    language_code: LanguageCode

    class Config:
        orm_mode = True
