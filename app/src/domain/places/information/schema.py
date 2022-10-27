from typing import List
from pydantic import BaseModel
from ..place.schema import Place


class PlaceInformation(BaseModel):
    id: int
    place: Place
    intro: str | None = None
    description: str | None = None
    activities: List[str] | None = None
    facilities: List[str] | None = None
    how_to_travel: str | None = None
    combined_text: str | None = None

    class Config:
        orm_mode = True
