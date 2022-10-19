from pydantic import BaseModel


class TimePeriods(BaseModel):
    id: int
    time: str

    class Config:
        orm_mode = True
