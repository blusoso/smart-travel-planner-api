from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..domain.tourism_type import schema, services

router = APIRouter(prefix='/tourism_types', tags=['tourism_types'])


@router.get('/', response_model=List[schema.AttractionType])
def get_tourism_types(db: Session = Depends(get_db)):
    tourism_types = services.get_tourism_types(db)
    return tourism_types
