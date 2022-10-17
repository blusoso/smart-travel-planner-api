from sqlalchemy.orm import Session
from . import model, schema


def get_language_code(db: Session):
    return db.query(model.LanguageCode).all()


def create_language_code(db: Session, language_code: schema.LanguageCode):
    db_language_code = model.LanguageCode(**language_code.dict())
    db.add(db_language_code)
    db.commit()
    db.refresh(db_language_code)
    return db_language_code
