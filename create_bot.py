from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from decouple import config


BOT_TOKEN = config('BOT_TOKEN')
BOT_ADMINS = [int(admin_id) for admin_id in config('BOT_ADMINS').split(',')]


bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()
