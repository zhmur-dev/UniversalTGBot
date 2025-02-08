from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.keyboards import feedback_kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        'Hello World!',
        reply_markup=feedback_kb()
    )
