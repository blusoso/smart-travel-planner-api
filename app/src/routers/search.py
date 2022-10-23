from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..domain.search import services

router = APIRouter(prefix='/search', tags=["search"])


@router.get('/{keyword}')
def search_places_by_keyword(keyword: str, skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    search_places = services.search_places_by_keyword(db, keyword, skip, limit)
    return search_places
