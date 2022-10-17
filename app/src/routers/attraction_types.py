from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..domain.attraction_type import schema, services

router = APIRouter(prefix='/attraction_types', tags=['attraction_types'])


@router.get('/', response_model=List[schema.AttractionType])
def get_attraction_types(db: Session = Depends(get_db)):
    attraction_types = services.get_attraction_types(db)
    return attraction_types
