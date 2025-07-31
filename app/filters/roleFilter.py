from aiogram.filters import BaseFilter
from aiogram.types import Message
from app.config import Config

class IsAdminFilter(BaseFilter):
    def __init__(self, config: Config) -> None:
        self.config = config
    async def __call__(self, msg: Message) -> bool:
        return True if msg.from_user.id in self.config.bot.ADMINS_IDS else False