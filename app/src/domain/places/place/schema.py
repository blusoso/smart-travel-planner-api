from pydantic import BaseModel
from typing import List
from ...country.schema import Country


class Place(BaseModel):
    id: str
    latitude: float
    longitude: float
    tags: List[str] | None = None
    country: Country
    is_active: bool

    class Config:
        orm_mode = True


class PlaceCard(BaseModel):
    id: str
    name: str
    tags: List[str] | None = None
    country_name: str
    child_fee: float | None = 0.0
    adult_fee: float | None = 0.0
    foreigner_child_fee: float | None = 0.0
    foreigner_adult_fee: float | None = 0.0
    language_code_id: str
