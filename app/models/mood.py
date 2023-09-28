import ormar
from datetime import date

import sqlalchemy

from app.core.base import BaseMeta
from app.core.config import settings
from app.models.user import User


class Mood(ormar.Model):
    class Meta(BaseMeta):
        tablename = "moods"

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    date: date = ormar.Date(nullable=False)
    mood_value: int = ormar.Integer(nullable=False)
    note: str = ormar.Text()
    user_id: int = ormar.ForeignKey(User, related_name="moods")


engine = sqlalchemy.create_engine(settings.db_url)
if not engine.dialect.has_table(engine.connect(), "moods"):
    Mood.Meta.table.create(engine)
