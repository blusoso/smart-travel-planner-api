from sqlalchemy.orm import Session
from . import model, schema
from fastapi import HTTPException


def get_time_periods(db: Session):
    return db.query(model.TimePeriods).all()
