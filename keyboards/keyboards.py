from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup
)


def feedback_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Report a bug', url='tg://resolve?domain=agent_zhmur')]
        ]
    )
