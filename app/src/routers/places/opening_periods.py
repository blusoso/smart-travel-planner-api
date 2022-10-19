from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ...dependencies import get_db
from ...domain.places.opening_period import schema, services

router = APIRouter(prefix='/opening_periods',
                   tags=['place_opening_periods'])


@router.get('/', response_model=List[schema.PlaceOpeningPeriod])
def get_place_opening_periods(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    place_opening_periods = services.get_place_opening_periods(db, skip, limit)
    return place_opening_periods


@router.get('/{place_id}', response_model=List[schema.SinglePlaceOpeningPeriod])
def get_place_opening_periods(place_id: str, db: Session = Depends(get_db)):
    place_opening_period = services.get_place_opening_period(db, place_id)
    return place_opening_period
