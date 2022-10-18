from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..domain.place_fee import schema, services

router = APIRouter(prefix='/place_fees', tags=['place_fees'])


@router.get('/', response_model=List[schema.PlaceFee])
def get_place_fees(db: Session = Depends(get_db)):
    place_fees = services.get_place_fees(db)
    return place_fees
