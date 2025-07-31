from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from app.lexicon import lexRU
from app.states import TheUserFSM
from app.keyboards import get_final_markup
from app.database import db

user_router = Router()

# POLL

@user_router.message(CommandStart())
async def cmd_start(msg: Message, state: FSMContext) -> None:
    await msg.answer(lexRU.text.user_start)
    await state.set_state(TheUserFSM.name)
    if not db.get_data('users', {'id': msg.from_user.id}):
        db.insert_data('users', {'id': msg.from_user.id,
                                'username': f'@{msg.from_user.username}'})

@user_router.message(StateFilter(TheUserFSM.name))
async def state_name(msg: Message, state: FSMContext) -> None:
    await msg.answer(lexRU.text.name)
    await state.set_state(TheUserFSM.age)
    db.update_data('users', {'name': msg.text}, {'id': msg.from_user.id})

@user_router.message(StateFilter(TheUserFSM.age))
async def state_age(msg: Message, state: FSMContext) -> None:
    await msg.reply(lexRU.text.age)
    await state.set_state(TheUserFSM.story)
    db.update_data('users', {'age': msg.text}, {'id': msg.from_user.id})

@user_router.message(StateFilter(TheUserFSM.story))
async def state_story(msg: Message, state: FSMContext) -> None:
    to_answer = lexRU.text.small_story if len(msg.text) < 80 else lexRU.text.big_story
    await msg.answer_photo(photo=lexRU.photo.iphone, caption=to_answer + lexRU.text.my_story)
    await msg.answer(lexRU.text.in_developing)
    await state.set_state(TheUserFSM.in_developing)
    db.update_data('users', {'story': msg.text}, {'id': msg.from_user.id})

@user_router.message(StateFilter(TheUserFSM.in_developing))
async def state_in_developing(msg: Message, state: FSMContext) -> None:
    await msg.answer(lexRU.text.meeting, reply_markup=get_final_markup())
    await state.set_state(TheUserFSM.final)
    db.update_data('users', {'in_developing': msg.text}, {'id': msg.from_user.id})