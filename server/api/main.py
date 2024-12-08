from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers.auth import auth_router
from api.routers.telegram import telegram_router
from api.database import init_db

app = FastAPI()

init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(telegram_router, prefix="/telegram", tags=["Telegram"])
