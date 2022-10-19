from typing import List
from pydantic import BaseModel

from ..place.schema import Place
from ...day.schema import Day
from ...time_periods.schema import TimePeriods


class PlaceOpeningPeriodBase(BaseModel):
    day: Day
    open: TimePeriods
    close: TimePeriods


class SinglePlaceOpeningPeriod(PlaceOpeningPeriodBase):
    class Config:
        orm_mode = True


class PlaceOpeningPeriod(PlaceOpeningPeriodBase):
    id: int
    place: Place

    class Config:
        orm_mode = True
