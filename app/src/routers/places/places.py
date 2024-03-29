from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ...dependencies import get_db
from ...domain.places.place import schema, services
from ...domain.places.fee import schema as feeSchema

router = APIRouter(tags=['places'])


@router.get('/', response_model=List[schema.Place])
def get_places(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = services.get_places(db, skip, limit)
    return places


@router.get('/{lang_code}/listing', response_model=List[schema.PlaceCard])
def get_place_card(
        lang_code: str = 'th',
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):
    place = services.get_places_with_fee(db, lang_code, skip, limit)
    return place


@router.get('/{lang_code}/discover', response_model=List[schema.PlaceCard])
def get_place_card(
        lang_code: str = 'th',
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
):
    place = services.discover(db, lang_code, skip, limit)
    return place


@router.get('/{lang_code}/{place_id}', response_model=schema.PlaceCard)
def get_place_card(
        place_id: str,
        lang_code: str = 'th',
        db: Session = Depends(get_db)
):
    place = services.get_place_with_fee(db, place_id, lang_code)
    return place


@router.get('/{place_id}', response_model=schema.Place)
def get_place(place_id: str, db: Session = Depends(get_db)):
    place = services.get_place(db, place_id)
    return place
