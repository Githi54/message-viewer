from bcrypt import hashpw, gensalt, checkpw

from pydantic import BaseModel

def hash_password(password: str) -> str:
    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

error_messages = {
    "already_exist": "A user with this username already exists.",
    "wrong_user": "User with this username was not found.",
    "wrong_data": "Incorrect username or password."
}

success_messages = {
    "user_registered": "User registration was successful.",
    "login": "Login successful."
}

class UserCreate(BaseModel):
    username: str
    password: str
