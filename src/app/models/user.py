import ormar
import sqlalchemy

from src.app.core.base import BaseMeta
from src.app.core.config import settings


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    username: str = ormar.String(max_length=50, unique=True, nullable=False)
    email: str = ormar.String(max_length=100, unique=True, nullable=False)
    hashed_password: str = ormar.String(nullable=False, max_length=200)


engine = sqlalchemy.create_engine(settings.db_url)
User.Meta.table.create(engine)
