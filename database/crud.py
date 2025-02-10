from datetime import datetime

from sqlalchemy import select

from database.config import AsyncSessionLocal
from database.models import User


async def register_new_user(
        telegram_id: int, username: str, first_name: str, last_name: str
):
    async with AsyncSessionLocal() as session:
        session.add(
            User(
                telegram_id=telegram_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                authorized=False,
                registered=datetime.now(),
            )
        )
        await session.commit()


async def get_user_by_id(telegram_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar()
