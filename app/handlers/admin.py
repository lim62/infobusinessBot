from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from app.lexicon import lexRU
from app.keyboards import get_start_markup, get_cancel_markup
from app.database import db

admin_router = Router()

@admin_router.message(CommandStart())
async def cmd_start(msg: Message) -> None:
    await msg.answer(lexRU.text.admin_start, reply_markup=get_start_markup())

@admin_router.callback_query(F.data == 'mailing')
async def call_mailing(call: CallbackQuery) -> None:
    await call.answer('mailing')

@admin_router.callback_query(F.data == 'contacts')
async def call_contacts(call: CallbackQuery) -> None:
    await call.message.edit_text(lexRU.text.contacts, reply_markup=get_cancel_markup())
    contacts = db.get_data('users')
    for contact in contacts:
        await call.message.answer(lexRU.load_contact(contact))
        db.delete_data('users', {'id': contact[0]})

@admin_router.callback_query(F.data == 'database')
async def call_database(call: CallbackQuery) -> None:
    await call.answer('database')

@admin_router.callback_query(F.data == 'cancel')
async def call_cancel(call: CallbackQuery) -> None:
    await call.message.edit_text(lexRU.text.admin_start, reply_markup=get_start_markup())