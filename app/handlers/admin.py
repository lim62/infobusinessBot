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

@admin_router.callback_query(F.data == 'contacts')
async def call_contacts(call: CallbackQuery) -> None:
    contacts = db.get_data('users')
    if contacts:
        is_fulled: bool = False
        for contact in contacts:
            if contact[-1]:
                is_fulled = True
                break
        if is_fulled:
            await call.message.edit_text(lexRU.text.contacts, reply_markup=get_cancel_markup())
            for contact in contacts:
                if contact[-1]:
                    await call.message.answer(lexRU.load_contact(contact))
                    db.update_data('users',
                                {'name': None, 'age': None, 'story': None, 'in_developing': None},
                                {'id': contact[0]})
        else: 
            await call.message.edit_text(lexRU.text.no_contacts, reply_markup=get_cancel_markup())
    else: 
        await call.message.edit_text(lexRU.text.no_contacts, reply_markup=get_cancel_markup())

@admin_router.callback_query(F.data == 'database')
async def call_database(call: CallbackQuery) -> None:
    database = db.get_data('users')
    if database:
        await call.message.edit_text(lexRU.text.database + lexRU.load_database(database), reply_markup=get_cancel_markup())
    else:
        await call.message.edit_text(lexRU.text.no_database, reply_markup=get_cancel_markup())

@admin_router.callback_query(F.data == 'cancel')
async def call_cancel(call: CallbackQuery) -> None:
    await call.message.edit_text(lexRU.text.admin_start, reply_markup=get_start_markup())

@admin_router.message()
async def admin_cmd_else(msg: Message) -> None:
    await msg.answer(lexRU.text.admin_else)