from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ...dependencies import get_db
from ...domain.places.translation import schema, services

router = APIRouter(prefix='/translations', tags=['place_translations'])


@router.get('/', response_model=List[schema.PlaceTranslation])
def get_place_translations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    place_translations = services.get_place_translations(db, skip, limit)
    return place_translations


@router.get('/{id}', response_model=schema.PlaceTranslation)
def get_place_translation(id: int, db: Session = Depends(get_db)):
    return services.get_place_translation(db, id)
