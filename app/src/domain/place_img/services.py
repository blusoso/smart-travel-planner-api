from sqlalchemy.orm import Session
from . import model, schema
from fastapi import HTTPException

DEFAULT_LIMIT_PLACE_IMG = 100


def get_place_imgs(db: Session, skip: int = 0, limit: int = DEFAULT_LIMIT_PLACE_IMG):
    return db.query(model.PlaceImg).offset(skip).limit(limit).all()
