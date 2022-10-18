from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..domain.place_img import schema, services

router = APIRouter(prefix='/place_imgs', tags=['place_imgs'])


@router.get('/', response_model=List[schema.PlaceImg])
def get_place_imgs(db: Session = Depends(get_db)):
    place_imgs = services.get_place_imgs(db)
    return place_imgs
