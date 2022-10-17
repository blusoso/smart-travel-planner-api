from pydantic import BaseModel


class PlaceTranslation(BaseModel):
    place_id: str
    name: str
    language_code_id: str

    class Config:
        orm_mode = True
