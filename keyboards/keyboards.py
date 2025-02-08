from create_bot import BOT_ADMINS


from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
    KeyboardButton, ReplyKeyboardMarkup
)


def main_kb(user_telegram_id: int):
    if user_telegram_id in BOT_ADMINS:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='Test Database connection'), KeyboardButton(text='Test Google connection')],
            ]
        )
    else:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Report a bug', url='tg://resolve?domain=agent_zhmur')]
            ]
        )
