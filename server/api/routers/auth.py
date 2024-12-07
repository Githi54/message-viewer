from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.auth import register_user, login_user
from api.utils import UserCreate, get_db

auth_router = APIRouter()

@auth_router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)

@auth_router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    return login_user(user, db)
