import datetime

from sqlalchemy.orm import mapped_column, Mapped

from database.config import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    telegram_id: Mapped[int]
    # Спросить, нужна ли уникальность?
    username: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    authorized: Mapped[bool]
    registered_at: Mapped[datetime.datetime]