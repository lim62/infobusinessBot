from random import choice
from aiogram import Router
from aiogram.types import Message
from app.lexicon import lexRU

other_router = Router()

@other_router.message()
async def cmd_else(msg: Message) -> None:
    await msg.answer(choice(lexRU.text.text_else))