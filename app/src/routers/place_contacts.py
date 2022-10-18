from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..domain.place_contact import schema, services

router = APIRouter(prefix='/place_contacts', tags=['place_contacts'])


@router.get('/', response_model=List[schema.PlaceContact])
def get_place_contacts(db: Session = Depends(get_db)):
    place_contacts = services.get_place_contacts(db)
    return place_contacts
