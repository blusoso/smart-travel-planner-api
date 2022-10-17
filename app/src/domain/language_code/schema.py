from pydantic import BaseModel


class LanguageCode(BaseModel):
    id: str
    language_en: str
    language_native: str

    class Config:
        orm_mode = True
