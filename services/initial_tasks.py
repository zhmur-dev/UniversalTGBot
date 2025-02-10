from sqlalchemy import text

from database.config import engine, Base, AsyncSessionLocal
from database.models import *


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
