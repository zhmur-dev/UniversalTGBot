from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.crud import get_user_by_id, register_new_user
from keyboards.keyboards import main_kb

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    user = await get_user_by_id(message.from_user.id)
    if not user:
        await message.answer(
            'Hello! You are a new user and will now be registered.',
            reply_markup=main_kb(message.from_user.id)
        )
        await register_new_user(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name
        )
    else:
        await message.answer(
            'Hello! You are a registered user.\n'
            f'Your authorization status is {user.authorized}.\n'
            f'You were registered on {user.registered}',
            reply_markup=main_kb(message.from_user.id)
        )
