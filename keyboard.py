from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_keyboard():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Подобрать технику💻"),
                                                         KeyboardButton(text="Новости об мире технике📰")).add(
        KeyboardButton(text="Создать финансовую цель💳"),KeyboardButton(text="Моя корзина🗑")
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
    return InlineKeyboardMarkup(row_width=5).add(InlineKeyboardButton(
        text="Удалить из корзины❌", callback_data="delete_korzina_push"
    ))

def otbor_tovara():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="1️⃣По ценовому диапозону")).add(KeyboardButton(
        text="Вернуться в главное меню🚶🏼"
    ))