from sqlalchemy.orm import Session
from . import model, schema
from fastapi import HTTPException


def get_days(db: Session):
    return db.query(model.Day).all()
