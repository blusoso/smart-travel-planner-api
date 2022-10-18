from sqlalchemy.orm import Session
from . import model, schema
from fastapi import HTTPException

DEFAULT_LIMIT_PLACE_FEE = 100


def get_place_fees(db: Session, skip: int = 0, limit: int = DEFAULT_LIMIT_PLACE_FEE):
    return db.query(model.PlaceFee).offset(skip).limit(limit).all()
