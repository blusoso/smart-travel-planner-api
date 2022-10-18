from typing import List
from pydantic import BaseModel
from ..place.schema import Place


class Day(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
