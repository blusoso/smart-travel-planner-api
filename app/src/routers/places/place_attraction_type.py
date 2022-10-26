from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ...dependencies import get_db
from ...domain.places.place_attraction_type import schema, services

router = APIRouter(prefix='/place_attraction_types',
                   tags=['place_attraction_types'])


@router.get('/', response_model=List[schema.PlaceAttractionType])
def get_place_attraction_types(db: Session = Depends(get_db)):
    place_attraction_types = services.get_place_attraction_types(db)
    return place_attraction_types
