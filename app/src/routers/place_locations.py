from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..domain.place_location import schema, services

router = APIRouter(prefix='/place_locations', tags=['place_locations'])


@router.get('/', response_model=List[schema.PlaceLocation])
def get_place_locations(db: Session = Depends(get_db)):
    place_locations = services.get_place_locations(db)
    return place_locations
