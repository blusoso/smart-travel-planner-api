from sqlalchemy.orm import Session
from . import model, schema
from fastapi import HTTPException


def get_place_locations(db: Session):
    return db.query(model.PlaceLocation).all()
