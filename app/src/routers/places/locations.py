from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ...dependencies import get_db
from ...domain.places.location import schema, services

router = APIRouter(prefix='/locations', tags=['place_locations'])


@router.get('/', response_model=List[schema.PlaceLocation])
def get_place_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    place_locations = services.get_place_locations(db, skip, limit)
    return place_locations
