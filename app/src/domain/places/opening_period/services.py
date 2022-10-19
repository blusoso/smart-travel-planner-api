from sqlalchemy.orm import Session
from . import model

DEFAULT_LIMIT_PLACE_OPENING_PERIOD = 100


def get_place_opening_periods(db: Session, skip: int = 0, limit: int = DEFAULT_LIMIT_PLACE_OPENING_PERIOD):
    return db.query(model.PlaceOpeningPeriod).offset(skip).limit(limit).all()


def get_place_opening_period(db: Session, place_id: str):
    data = model.PlaceOpeningPeriod

    return db.query(data)\
        .filter(model.PlaceOpeningPeriod.place_id == place_id)\
        .all()
