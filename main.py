import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from app.config import Config, load_config
from app.handlers import admin_router, user_router, other_router
from app.filters import IsAdminFilter
from app.database import get_storage, db

async def main() -> None:
    config: Config = load_config()
    logging.basicConfig(
        level=config.log.LEVEL,
        format=config.log.FORMAT,
        style='{'
    )
    bot = Bot(
        token=config.bot.TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    db.create_table('users', {
                            'id': 'INT PRIMARY KEY', 'username': 'VARCHAR(255)',
                            'name': 'VARCHAR(255)', 'age': 'VARCHAR(255)',
                            'story': 'TEXT', 'in_developing': 'VARCHAR(255)'
                            }
                    )
    dp = Dispatcher(storage=get_storage(config))
    dp.include_routers(admin_router, user_router, other_router)
    admin_router.message.filter(IsAdminFilter(config))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())