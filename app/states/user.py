from aiogram.fsm.state import State, StatesGroup

class TheUserFSM(StatesGroup):
    name = State()
    age = State()
    story = State()
    in_developing = State()
    final = State()