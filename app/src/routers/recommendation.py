from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..domain.recommendation import services

router = APIRouter(prefix='/recommendation', tags=["recommendation"])


@router.get('/content-based')
def get_content_based_data(db: Session = Depends(get_db)):
    data = services.get_content_based_data(db)
    return data
