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
