from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..domain.user import schema, services

router = APIRouter(prefix='/users', tags=["users"])


@router.get('/', response_model=List[schema.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = services.get_users(db, skip, limit)
    return users


@router.get('/{user_id}', response_model=schema.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = services.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return user


@router.post('/', response_model=schema.User)
def create_users(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = services.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return services.create_user(db, user)
