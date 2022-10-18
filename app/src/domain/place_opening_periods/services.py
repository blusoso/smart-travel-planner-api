from sqlalchemy.orm import Session
from . import model, schema
from fastapi import HTTPException


def get_place_information(db: Session):
    return db.query(model.PlaceInformation).all()
