from sqlalchemy.orm import Session
from . import model


def get_tourism_types(db: Session):
    return db.query(model.TourismType).all()
