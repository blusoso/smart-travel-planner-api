from sqlalchemy.orm import Session
from . import model, schema
from fastapi import HTTPException

DEFAULT_LIMIT_PLACE_CONTACT = 100


def get_place_contacts(db: Session, skip: int = 0, limit: int = DEFAULT_LIMIT_PLACE_CONTACT):
    return db.query(model.PlaceContact).offset(skip).limit(limit).all()
