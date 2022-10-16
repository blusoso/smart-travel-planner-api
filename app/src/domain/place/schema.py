from pydantic import BaseModel
from typing import List


class Place(BaseModel):
    id: str
    name: str
    latitude: float
    longitude: float
    tags: List[str] | None = None

    class Config:
        orm_mode = True
