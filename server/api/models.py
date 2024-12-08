from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    telegram_account_id = Column(Integer, ForeignKey("telegram_accounts.id"))
    telegram_account = relationship("TelegramAccount", back_populates="user")

class TelegramAccount(Base):
    __tablename__ = "telegram_accounts"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String)
    user = relationship("User", back_populates="telegram_account")
