from sqlalchemy.orm import Session
from . import model, schema
from fastapi import HTTPException

DEFAULT_LIMIT_PLACE = 100


def get_places(db: Session, skip: int = 0, limit: int = DEFAULT_LIMIT_PLACE):
    return db.query(model.Place).offset(skip).limit(limit).all()


def get_place(db: Session, place_id: str):
    db_place = db.query(model.Place).filter(model.Place.id == place_id).first()
    if db_place is None:
        raise HTTPException(status_code=404, detail='place does not exit')
    return db_place
