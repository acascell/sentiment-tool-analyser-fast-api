from sqlalchemy import Column, Integer, Sequence, Date, Text, ForeignKey
from sqlalchemy.orm import relationship

from src.app.models.base import Base


class Mood(Base):
    __table__ = "moods"

    id = Column(Integer, Sequence("mood_id_seq"), primary_key=True)
    date = Column(Date, nullable=False)
    mood_value = Column(Integer, nullable=False)
    note = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="moods")
