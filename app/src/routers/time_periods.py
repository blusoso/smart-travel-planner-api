from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..domain.time_periods import schema, services

router = APIRouter(prefix='/time_periods', tags=['time_periods'])


@router.get('/', response_model=List[schema.TimePeriods])
def get_time_periods(db: Session = Depends(get_db)):
    time_periods = services.get_time_periods(db)
    return time_periods
