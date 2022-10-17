from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..domain.language_code import schema, services

router = APIRouter(prefix='/language_codes', tags=['language_codes'])


@router.get('/', response_model=List[schema.LanguageCode])
def get_language_codes(db: Session = Depends(get_db)):
    language_codes = services.get_language_code(db)
    return language_codes


@router.post('/', response_model=schema.LanguageCode)
def create_language_codes(language_code: schema.LanguageCode, db: Session = Depends(get_db)):
    return services.create_language_code(db, language_code)
