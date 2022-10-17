from sqlalchemy.orm import Session
from . import model, schema


def get_place_translation(db: Session):
    return db.query(model.PlaceTranslation).all()
