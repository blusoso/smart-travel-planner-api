from pydantic import BaseModel
from ..place.schema import Place
from ...language_code.schema import LanguageCode


class PlaceLocation(BaseModel):
    id: int
    place: Place
    address: str | None = None
    sub_district: str
    district: str
    province: str
    postcode: str | None = None
    geography: str | None = None
    language_code: LanguageCode

    class Config:
        orm_mode = True
