from sqlalchemy.orm import Session
from . import model, schema

DEFAULT_LIMIT_PLACE = 100


def get_places(db: Session, skip: int = 0, limit: int = DEFAULT_LIMIT_PLACE):
    return db.query(model.Place).offset(skip).limit(limit).all()
