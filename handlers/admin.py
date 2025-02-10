from aiogram import F, Router
from aiogram.types import Message

from create_bot import BOT_ADMINS
from keyboards.keyboards import main_kb
from services.gsheets import test_gsheets_connection
from services.initial_tasks import test_db_connection

admin_router = Router()


@admin_router.message(F.text == 'Test Database connection')
async def admin_test_db(message: Message):
    if message.from_user.id not in BOT_ADMINS:
        await message.answer(
            '403 Unauthorized',
            reply_markup=main_kb(message.from_user.id)
        )
    else:
        result = await test_db_connection()
        await message.answer(
            result,
            reply_markup=main_kb(message.from_user.id)
        )


@admin_router.message(F.text == 'Test Google connection')
async def admin_test_gsheets(message: Message):
    if message.from_user.id not in BOT_ADMINS:
        await message.answer(
            '403 Unauthorized',
            reply_markup=main_kb(message.from_user.id)
        )
    else:
        result = test_gsheets_connection()
        await message.answer(
            result,
            reply_markup=main_kb(message.from_user.id)
        )
