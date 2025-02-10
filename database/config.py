from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from config_data.config import settings

# Создание движка для связи с БД
engine = create_async_engine(url=settings.db_url, future=True, echo=False, pool_pre_ping=True)

# Создание асинхронной сессии
AsyncSessionLocal = async_sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


class Base(DeclarativeBase): pass



