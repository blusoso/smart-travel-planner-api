from pydantic import BaseModel


class CountryBase(BaseModel):
    name_th: str
    name_en: str
    language_code: str
    flag_img: str | None = None


class CountryCreate(CountryBase):
    pass


class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True
