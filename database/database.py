from decouple import config
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.sql import text


POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_DB = config('POSTGRES_DB')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')

DATABASE_URL = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}'

engine = create_async_engine(DATABASE_URL, pool_pre_ping=True)

#noinspection PyTypeChecker
AsyncSessionLocal = sessionmaker (
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase): pass


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    authorized = Column(Boolean)
    registered = Column(DateTime)


async def set_up_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def test_db_connection():
    async with AsyncSessionLocal() as session:
        try:
            result = await session.execute(text('SELECT 1'))
            return f'DB Test Passed! Result: {result.scalar()}'
        except Exception as e:
            return f'DB Test Failed: {e}'
