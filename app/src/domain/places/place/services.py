from sqlalchemy.orm import Session
from . import model
from ..fee.model import PlaceFee
from ..translation.model import PlaceTranslation
from ...country.model import Country
from fastapi import HTTPException

DEFAULT_LIMIT_PLACE = 100


def get_places(db: Session, skip: int = 0, limit: int = DEFAULT_LIMIT_PLACE):
    return db.query(model.Place).offset(skip).limit(limit).all()


def get_place(db: Session, place_id: str):
    db_place = db.query(model.Place).filter(model.Place.id == place_id).first()
    if db_place is None:
        raise HTTPException(status_code=404, detail='place does not exit')
    return db_place


def get_places_with_fee(db: Session, lang_code: str = 'th', skip: int = 0, limit: int = DEFAULT_LIMIT_PLACE):
    db_place = db.query(
        model.Place.id,
        PlaceTranslation.name,
        model.Place.tags,
        Country.name.label('country_name'),
        PlaceFee.child_fee,
        PlaceFee.adult_fee,
        PlaceFee.foreigner_child_fee,
        PlaceFee.foreigner_adult_fee,
        PlaceTranslation.language_code_id,
    )\
        .join(PlaceTranslation)\
        .join(PlaceFee)\
        .join(Country)\
        .filter(model.Place.is_active == True)\
        .filter(PlaceTranslation.language_code_id == lang_code)\
        .filter(Country.language_code_id == lang_code)\
        .offset(skip)\
        .limit(limit)\
        .all()

    return db_place


def get_place_with_fee(db: Session, place_id: str, lang_code: str = 'th'):
    db_place = db.query(
        model.Place.id,
        PlaceTranslation.name,
        model.Place.tags,
        Country.name.label('country_name'),
        PlaceFee.child_fee,
        PlaceFee.adult_fee,
        PlaceFee.foreigner_child_fee,
        PlaceFee.foreigner_adult_fee,
        PlaceTranslation.language_code_id,
    )\
        .join(PlaceTranslation)\
        .join(PlaceFee)\
        .join(Country)\
        .filter(model.Place.is_active == True)\
        .filter(PlaceTranslation.language_code_id == lang_code)\
        .filter(Country.language_code_id == lang_code)\
        .filter(model.Place.id == place_id)\
        .first()

    return db_place
