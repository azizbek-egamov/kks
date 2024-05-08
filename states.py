from aiogram.fsm.state import State, StatesGroup

class addKino(StatesGroup):
    inf = State()
    name = State()
    desc = State()
    kino = State()
    
class delKino(StatesGroup):
    cod = State()