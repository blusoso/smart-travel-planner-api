from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..domain.place_translation import schema, services

router = APIRouter(prefix='/place_translations', tags=['place_translations'])


@router.get('/', response_model=List[schema.PlaceTranslation])
def get_place_translations(db: Session = Depends(get_db)):
    place_translations = services.get_place_translation(db)
    return place_translations
