from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.database import test_db_connection
from gsheets.gsheets import test_gsheets_connection
from keyboards.keyboards import main_kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        'Hello World!',
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
