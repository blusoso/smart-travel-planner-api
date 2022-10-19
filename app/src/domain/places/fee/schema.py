from typing import List
from pydantic import BaseModel
from ..place.schema import Place


class PlaceFee(BaseModel):
    id: int
    place: Place
    child_fee: float | None = None
    adult_fee: float | None = None
    foreigner_child_fee: float | None = None
    foreigner_adult_fee: float | None = None

    class Config:
        orm_mode = True
