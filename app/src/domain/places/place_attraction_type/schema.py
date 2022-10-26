from pydantic import BaseModel
from ..place.schema import Place
from ...attraction_type.schema import AttractionType


class PlaceAttractionType(BaseModel):
    id: int
    place: Place
    attraction_typ: AttractionType

    class Config:
        orm_mode = True
