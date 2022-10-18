from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..domain.place_opening_periods import schema, services

router = APIRouter(prefix='/place_opening_periods',
                   tags=['place_opening_periods'])


@router.get('/', response_model=List[schema.PlaceOpeningPeriod])
def get_place_opening_periods(db: Session = Depends(get_db)):
    place_opening_periods = services.get_place_opening_periods(db)
    return place_opening_periods
