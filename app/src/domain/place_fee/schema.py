from typing import List
from pydantic import BaseModel
from ..place.schema import Place


class PlaceFee(BaseModel):
    id: int
    place: Place
    child_fee: float
    adult_fee: float
    foreigner_child_fee: float
    foreigner_adult_fee: float

    class Config:
        orm_mode = True
