import enum
from pydantic import BaseModel
from typing import List
from ...country.schema import Country


class CategoryType(str, enum.Enum):
    ATTRACTION = 'attraction'
    RESTAURANT = 'restaurant'
    SHOP = 'shop'


class Place(BaseModel):
    id: str
    latitude: float
    longitude: float
    tags: List[str] | None = None
    country: Country
    category_type: CategoryType = CategoryType.ATTRACTION
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
