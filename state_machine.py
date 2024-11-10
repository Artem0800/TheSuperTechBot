from aiogram.dispatcher.filters.state import StatesGroup, State

class State_Otbor(StatesGroup):
    category_price = State()
    search_text = State()