from pydantic import BaseModel
from ..language_code.schema import LanguageCode


class CountryBase(BaseModel):
    name: str
    language_code: LanguageCode
    flag_img: str | None = None


class CountryCreate(CountryBase):
    pass


class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True
