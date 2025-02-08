import asyncio
import logging

from aiogram.types import BotCommand, BotCommandScopeDefault

from create_bot import bot, dp
from handlers.handlers import router


async def set_commands():
    await bot.set_my_commands([
            BotCommand(command='start', description='Start'),
    ],
        BotCommandScopeDefault()
    )


async def main() -> None:
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await set_commands()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    asyncio.run(main())
