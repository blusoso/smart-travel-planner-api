from pydantic import BaseModel
from ..language_code.schema import LanguageCode
from ..tourism_type.schema import TourismType


class AttractionType(BaseModel):
    id: int
    name: str
    tourism_type: TourismType | None = None
    language_code: LanguageCode

    class Config:
        orm_mode = True
