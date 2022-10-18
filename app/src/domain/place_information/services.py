from sqlalchemy.orm import Session
from . import model, schema
from fastapi import HTTPException

DEFAULT_LIMIT_PLACE_INFO = 100


def get_place_information(db: Session, skip: int = 0, limit: int = DEFAULT_LIMIT_PLACE_INFO):
    return db.query(model.PlaceInformation).offset(skip).limit(limit).all()
