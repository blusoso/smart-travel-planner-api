from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ...dependencies import get_db
from ...domain.places.fee import schema, services

router = APIRouter(prefix='/fees', tags=['place_fees'])


@router.get('/', response_model=List[schema.PlaceFee])
def get_place_fees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    place_fees = services.get_place_fees(db, skip, limit)
    return place_fees
