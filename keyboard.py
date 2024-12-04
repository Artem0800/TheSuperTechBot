from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import WebAppInfo

def main_keyboard():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Собрать ПК🖥"),
                                                         KeyboardButton(text="Новости об мире технике📰")).add(
        KeyboardButton(text="Накопительные цели💳"),KeyboardButton(text="Моя корзина🗑")
    ).add(KeyboardButton(text="Обновить данные🔄"))

def detali_pc():
    return ReplyKeyboardMarkup(resize_keyboard=True, row_width=20).add(KeyboardButton("1️⃣"), KeyboardButton("2️⃣"), KeyboardButton("3️⃣"),
                                                         KeyboardButton("4️⃣")).add(
        KeyboardButton("5️⃣"), KeyboardButton("6️⃣"), KeyboardButton("7️⃣"), KeyboardButton("8️⃣")
    ).add(KeyboardButton("9️⃣"), KeyboardButton("1️⃣0️⃣"), KeyboardButton("1️⃣1️⃣"), KeyboardButton("1️⃣2️⃣")).add(KeyboardButton("Вернуться в главное меню🚶🏼"))

def add_korzina():
    return InlineKeyboardMarkup(row_width=5).add(InlineKeyboardButton(
        text="Добавить в корзину🗑", callback_data="add_korzina_push"
    ))

def delete_korzina():
    return InlineKeyboardMarkup(row_width=3).add(InlineKeyboardButton(
        text="Удалить из корзины❌", callback_data="delete_korzina_push"
    ))

def otbor_tovara():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Начать отбор товара", web_app=WebAppInfo(url="https://artem0800.github.io/WebAppTG/"))
                                                         ).add(KeyboardButton("Вернуться в главное меню🚶🏼"))


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