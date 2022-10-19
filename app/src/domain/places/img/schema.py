from typing import List
from pydantic import BaseModel
from ..place.schema import Place


class PlaceImg(BaseModel):
    id: int
    place: Place
    img_desktop: str
    img_mobile: str | None = None
    is_thumbnail: bool
    is_active: bool

    class Config:
        orm_mode = True
