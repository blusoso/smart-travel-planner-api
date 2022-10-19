from sqlalchemy.orm import Session
from . import model, schema
from fastapi import HTTPException

DEFAULT_LIMIT_PLACE_TRANSLATION = 100


def get_place_translations(db: Session, skip: int = 0, limit: int = DEFAULT_LIMIT_PLACE_TRANSLATION):
    return db.query(model.PlaceTranslation).offset(skip).limit(limit).all()


def get_place_translation(db: Session, id: int):
    db_place_translation = db.query(model.PlaceTranslation).filter(
        model.PlaceTranslation.id == id).first()
    if db_place_translation is None:
        raise HTTPException(status_code=404, detail='place does not exit')
    return db_place_translation
