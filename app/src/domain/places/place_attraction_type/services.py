from sqlalchemy.orm import Session
from . import model, schema
from fastapi import HTTPException


def get_place_attraction_types(db: Session):
    return db.query(model.AttractionType).all()
