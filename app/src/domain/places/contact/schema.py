from typing import List
from pydantic import BaseModel
from ..place.schema import Place


class PlaceContact(BaseModel):
    id: int
    place: Place
    phones: List[str] | None = None
    emails: List[str] | None = None
    urls: List[str] | None = None

    class Config:
        orm_mode = True
