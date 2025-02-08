from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from database.database import test_db_connection
from keyboards.keyboards import feedback_kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        'Hello World!',
        reply_markup=feedback_kb()
    )

@router.message(Command('test_db'))
async def cmd_test_db(message: Message):
    result = await test_db_connection()
    await message.answer(
        result,
        reply_markup=feedback_kb()
    )
