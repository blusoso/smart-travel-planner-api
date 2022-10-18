from typing import List
from pydantic import BaseModel
from ..place.schema import Place


class TimePeriods(BaseModel):
    id: int
    time: str

    class Config:
        orm_mode = True
