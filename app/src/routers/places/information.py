from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ...dependencies import get_db
from ...domain.places.information import schema, services

router = APIRouter(prefix='/information', tags=['place_information'])


@router.get('/', response_model=List[schema.PlaceInformation])
def get_place_information(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    place_information = services.get_place_information(db, skip, limit)
    return place_information
