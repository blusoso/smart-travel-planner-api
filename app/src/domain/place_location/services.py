from sqlalchemy.orm import Session
from . import model, schema
from fastapi import HTTPException

DEFAULT_LIMIT_PLACE_LOCATION = 100


def get_place_locations(db: Session, skip: int = 0, limit: int = DEFAULT_LIMIT_PLACE_LOCATION):
    return db.query(model.PlaceLocation).offset(skip).limit(limit).all()
