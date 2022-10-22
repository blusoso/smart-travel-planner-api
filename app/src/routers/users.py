from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from sqlalchemy.orm import Session
from datetime import timedelta

from ..dependencies import get_db
from ..domain.user import schema, services
from ..config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(prefix='/users', tags=["users"])


@router.get('/', response_model=List[schema.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = services.get_users(db, skip, limit)
    return users


@router.post('/signup', response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    user_created = services.create_user(user, db)
    return user_created


@router.post('/token', response_model=schema.Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = services.authenticate_user(
        form_data.username,
        form_data.password,
        db
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = services.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/me', response_model=schema.User)
async def read_users_me(current_user: schema.User = Depends(services.get_current_active_user)):
    return current_user


@router.get('/{user_id}', response_model=schema.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = services.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return user
