from pydantic import BaseModel
from ..language_code.schema import LanguageCode


class AttractionType(BaseModel):
    id: int
    name: str
    tourism_type_id: int | None = None
    language_code: LanguageCode

    class Config:
        orm_mode = True
