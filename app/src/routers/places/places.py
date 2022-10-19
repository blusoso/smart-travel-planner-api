from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ...dependencies import get_db
from ...domain.place import schema, services

router = APIRouter(tags=['places'])


@router.get('/', response_model=List[schema.Place])
def get_places(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = services.get_places(db, skip, limit)
    return places


@router.get('/{place_id}', response_model=schema.Place)
def get_place(place_id: str, db: Session = Depends(get_db)):
    place = services.get_place(db, place_id)
    return place
