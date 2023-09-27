import ormar
from datetime import date

import sqlalchemy

from src.app.core.base import BaseMeta
from src.app.core.config import settings
from src.app.models.user import User


class Mood(ormar.Model):
    class Meta(BaseMeta):
        tablename = "moods"

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    date: date = ormar.Date(nullable=False)
    mood_value: int = ormar.Integer(nullable=False)
    note: str = ormar.Text()
    user_id: int = ormar.ForeignKey(User, related_name="moods")


engine = sqlalchemy.create_engine(settings.db_url)
Mood.Meta.table.create(engine)
