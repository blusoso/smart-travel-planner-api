from typing import List
from pydantic import BaseModel

from ..place.schema import Place
from ...day.schema import Day
from ...time_periods.schema import TimePeriods


class PlaceOpeningPeriod(BaseModel):
    id: int
    place: Place
    day: Day
    open: TimePeriods
    close: TimePeriods

    class Config:
        orm_mode = True
