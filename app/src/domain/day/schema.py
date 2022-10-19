from pydantic import BaseModel


class Day(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
