from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_keyboard():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Найти товар💻"),
                                                         KeyboardButton(text="Новости об мире технике📰")).add(
        KeyboardButton(text="Накопительные цели💳"),KeyboardButton(text="Моя корзина🗑")
    ).add(KeyboardButton(text="Обновить данные🔄"))

def select_tech_keyboard():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Видеокарты"), KeyboardButton(
        text="Игровые ноутбуки"
    )).add(
        KeyboardButton(text="Вернуться в главное меню🚶🏼")
    )

def add_korzina():
    return InlineKeyboardMarkup(row_width=5).add(InlineKeyboardButton(
        text="Добавить в корзину🗑", callback_data="add_korzina_push"
    ))

def delete_korzina():
    return InlineKeyboardMarkup(row_width=3).add(InlineKeyboardButton(
        text="Удалить из корзины❌", callback_data="delete_korzina_push"
    ))

def otbor_tovara():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="1️⃣По ценовому диапозону"),
                                                         KeyboardButton(text="2️⃣Поиск по тексту")).add(KeyboardButton(
        text="Вернуться в главное меню🚶🏼"
    ))

def swipe_news():
    return InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text="⬅️", callback_data="back"),
                                                 InlineKeyboardButton(text="➡️", callback_data="forward"),
    InlineKeyboardButton(text="Первая", callback_data="swipe_one"),
    InlineKeyboardButton(text="Последняя", callback_data="swipe_last"),
                                                 ).add(InlineKeyboardButton(text="Обновить новости🔄", callback_data="reset")
                                                ).add(InlineKeyboardButton("Закрыть❌", callback_data="close_news"))

def kb_add_target_pay():
    return InlineKeyboardMarkup(row_width=4).add(InlineKeyboardButton(text="Создать💵", callback_data="create_target_pay"))

def api_pay():
    return InlineKeyboardMarkup(row_width=4).add(InlineKeyboardButton("Пополнить💰", callback_data="Popolnity")).add(
        InlineKeyboardButton("Вывести💸", callback_data="get_money")
    ).add(
        InlineKeyboardButton("Удалить❌", callback_data="delete_target")
    )