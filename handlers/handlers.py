from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.database import test_db_connection
from database.users import check_user_by_id, register_new_user
from gsheets.gsheets import test_gsheets_connection
from keyboards.keyboards import main_kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user = await check_user_by_id(message.from_user.id)
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
            f'You were registered on {user.registered}'.,
            reply_markup=main_kb(message.from_user.id)
        )

@router.message(F.text == 'Test Database connection')
async def admin_test_db(message: Message):
    result = await test_db_connection()
    await message.answer(
        result,
        reply_markup=main_kb(message.from_user.id)
    )

@router.message(F.text == 'Test Google connection')
async def admin_test_gsheets(message: Message):
    result = test_gsheets_connection()
    await message.answer(
        result,
        reply_markup=main_kb(message.from_user.id)
    )
