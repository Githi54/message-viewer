from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from pydantic import BaseModel

from api.models import User
from api.utils import hash_password, verify_password, get_db, error_messages, success_messages

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail=error_messages["already_exist"])

    hashed_password = hash_password(user.password)

    new_user = User(username=user.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": success_messages["user_registered"]}

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    user_data = db.query(User).filter(User.username == user.username).first()
    if not user_data:
        raise HTTPException(status_code=400, detail=error_messages["wrong_user"])

    if not verify_password(user.password, user_data.password):
        raise HTTPException(status_code=400, detail=error_messages["wrong_data"])

    return {"message": success_messages["login"]}
