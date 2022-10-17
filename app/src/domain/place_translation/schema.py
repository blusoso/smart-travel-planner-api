from pydantic import BaseModel
from ..place.schema import Place
from ..language_code.schema import LanguageCode


class PlaceTranslation(BaseModel):
    id: int
    place: Place
    name: str
    language_code: LanguageCode

    class Config:
        orm_mode = True
