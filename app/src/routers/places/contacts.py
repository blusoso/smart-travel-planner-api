from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ...dependencies import get_db
from ...domain.places.contact import schema, services

router = APIRouter(prefix='/contacts', tags=['place_contacts'])


@router.get('/', response_model=List[schema.PlaceContact])
def get_place_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    place_contacts = services.get_place_contacts(db, skip, limit)
    return place_contacts
