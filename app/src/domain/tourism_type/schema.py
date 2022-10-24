from pydantic import BaseModel
from ..language_code.schema import LanguageCode


class TourismType(BaseModel):
    id: int
    name: str
    language_code: LanguageCode

    class Config:
        orm_mode = True
