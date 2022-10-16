from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..domain.country import schema, services

router = APIRouter(prefix='/countries', tags=['countries'])


@router.get('/', response_model=List[schema.Country])
def get_countries(db: Session = Depends(get_db)):
    countries = services.get_countries(db)
    return countries


@router.post('/', response_model=schema.Country)
def create_country(country: schema.CountryCreate, db: Session = Depends(get_db)):
    return services.create_country(db, country)
