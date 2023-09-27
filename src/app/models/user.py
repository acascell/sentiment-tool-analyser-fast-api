from sqlalchemy import Column, Integer, String, Sequence
from src.app.models.base import Base


class User(Base):
    __table__ = "users"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
