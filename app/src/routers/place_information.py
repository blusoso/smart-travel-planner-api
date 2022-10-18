from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..domain.place_information import schema, services

router = APIRouter(prefix='/place_information', tags=['place_information'])


@router.get('/', response_model=List[schema.PlaceInformation])
def get_place_information(db: Session = Depends(get_db)):
    place_information = services.get_place_information(db)
    return place_information
