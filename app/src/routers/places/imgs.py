from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ...dependencies import get_db
from ...domain.places.img import schema, services

router = APIRouter(prefix='/imgs', tags=['place_imgs'])


@router.get('/', response_model=List[schema.PlaceImg])
def get_place_imgs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    place_imgs = services.get_place_imgs(db, skip, limit)
    return place_imgs
