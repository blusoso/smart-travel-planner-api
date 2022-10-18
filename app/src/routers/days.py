from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..domain.day import schema, services

router = APIRouter(prefix='/days', tags=['days'])


@router.get('/', response_model=List[schema.Day])
def get_days(db: Session = Depends(get_db)):
    days = services.get_days(db)
    return days
