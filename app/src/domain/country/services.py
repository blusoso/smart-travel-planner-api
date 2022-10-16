from sqlalchemy.orm import Session
from . import model, schema


def get_countries(db: Session):
    return db.query(model.Country).all()


def create_country(db: Session, country: schema.CountryCreate):
    db_country = model.Country(**country.dict())
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country
