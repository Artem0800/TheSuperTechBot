import time
from confic import bot, dp
from aiogram import executor, types
from keyboard import main_keyboard, select_tech_keyboard, add_korzina, otbor_tovara
from keyboard import delete_korzina, swipe_news
from aiogram.utils.markdown import hbold, hlink
from aiogram.dispatcher.filters import Text
from Scraping.Videocard.videocard import videocard
from Scraping.GameLaptop.game_laptop import game_laptop
import json
from aiogram.dispatcher import FSMContext
from state_machine import State_Otbor
from aiogram.types import ReplyKeyboardRemove
from sqlite import bd_conect, add_korzina_to_db, get_id, delete_korzina_to_db
from ScrapingNews.scraping_news import get_news

async def info_start(_):
    print("Я запустился")

@dp.message_handler(Text(equals=["/start", "Вернуться в главное меню🚶🏼"]))
async def cmd_start(message: types.Message):
    await message.delete()
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://b1.filmpro.ru/c/43526.jpg",
                            caption="<b>Добро пожаловать в бота Валеру!</b>",
                           parse_mode="HTML",
                           reply_markup=main_keyboard())

@dp.message_handler(Text(equals="Обновить данные🔄"))
async def cmd_update_scrap(message: types.Message):
    await message.reply(text="Подождите, обновляем информацию...", reply_markup=ReplyKeyboardRemove())
    videocard()
    game_laptop()

    with open("Scraping//GameLaptop//result.json", encoding="utf-8") as file:
        data1 = json.load(file)

    with open("Scraping//Videocard//result.json", encoding="utf-8") as file:
        data2 = json.load(file)

    union = data1 + data2

    with open("Korzina//ebaty.json", "w", encoding="utf-8") as file:
        json.dump(union, file, indent=4, ensure_ascii=False)

    await message.answer(text="Данные обновлены", reply_markup=main_keyboard())

@dp.message_handler(Text(equals="Найти товар💻"))
async def cmd_select_tech(message: types.Message):
    await message.reply(text="<i>Выберите категорию товара которую хотите найти</i>",
                        reply_markup=select_tech_keyboard(),
                        parse_mode="HTML")

name_search = ""

@dp.message_handler(Text(equals=["Видеокарты", "Игровые ноутбуки"]))
async def cmd_get_videocard(message: types.Message):
    global name_search
    name_search = ""
    name_search += message.text

    await message.reply(text="<i>Выберите пункт по которому вы будете искать товар</i>", reply_markup=otbor_tovara(),
                        parse_mode="HTML")

@dp.message_handler(Text(equals="1️⃣По ценовому диапозону"))
async def cmd_otbor_1(message: types.Message):
    await message.reply(text="Введите ценовой диапозон. Пример: 15000 20000\nДопускаются только цифры и не "
                             "какие больше символы", reply_markup=ReplyKeyboardRemove())
    await State_Otbor.category_price.set()

@dp.message_handler(Text(equals="2️⃣Поиск по тексту"))
async def cmd_otbor_1(message: types.Message):
    await message.reply(text="Введите любой текст и мы по нему будет искать нужные товары\n"
                             "Пример: Asus 16gb", reply_markup=ReplyKeyboardRemove())
    await State_Otbor.search_text.set()

@dp.message_handler(state=State_Otbor.search_text)
async def cmd_state_search_text(message: types.Message, state: FSMContext):
    global name_search
    pizda_bobra = {
        "Видеокарты": "Videocard",
        "Игровые ноутбуки": "GameLaptop"
    }
    try:
        await state.update_data(search_text=message.text)

        data = await state.get_data()

        search_tovar = data["search_text"].split()
        await message.answer("Пожалуйста подождите...")

        with open(f"Scraping//{pizda_bobra[name_search]}//result.json", encoding="utf-8") as file:
            data = json.load(file)

        for index, item in enumerate(data):
            pisa = item.get("Стоимость")
            if all(word.lower() in item["Описание"].lower() for word in search_tovar):
                card = (f"{hlink(item.get('Название'), item.get('Ссылка на товар'))}\n "
                        f"{hbold('Id: ')}{item.get('Id')}\n "
                        f"{hbold('Описание: ')}{item.get('Описание')}\n "
                        f"{hbold('Цена: ')}{item.get('Стоимость')}руб.\n "
                        f"{hbold('Средняя оценка: ')}{item.get('Средняя оценка')}\n "
                        f"{hbold('Количество отзывов: ')}{item.get('Количество отзывов')}\n ")

                if index % 20 == 0:
                    time.sleep(5)

                await message.answer(card, parse_mode="HTML", reply_markup=add_korzina())

        await message.answer("Вот, все что мы нашли для вас", reply_markup=main_keyboard())
        await state.finish()
    except:
        await message.answer("Что-то не так, попробуй еще раз😢")

@dp.message_handler(state=State_Otbor.category_price)
async def cmd_state_category(message: types.Message, state: FSMContext):
    global name_search
    pizda_bobra = {
        "Видеокарты": "Videocard",
        "Игровые ноутбуки": "GameLaptop"
    }
    try:
        await state.update_data(category_price=message.text)

        data = await state.get_data()

        put_user1, put_user2 = data["category_price"].split()
        await message.answer("Пожалуйста подождите...")

        with open(f"Scraping//{pizda_bobra[name_search]}//result.json", encoding="utf-8") as file:
            data = json.load(file)

        for index, item in enumerate(data):
            pisa = item.get("Стоимость")
            if pisa >= int(put_user1) and pisa <= int(put_user2):
                card = (f"{hlink(item.get('Название'), item.get('Ссылка на товар'))}\n "
                        f"{hbold('Id: ')}{item.get('Id')}\n "
                        f"{hbold('Описание: ')}{item.get('Описание')}\n "
                        f"{hbold('Цена: ')}{item.get('Стоимость')}руб.\n "
                        f"{hbold('Средняя оценка: ')}{item.get('Средняя оценка')}\n "
                        f"{hbold('Количество отзывов: ')}{item.get('Количество отзывов')}\n ")

                if index % 20 == 0:
                    time.sleep(5)

                await message.answer(card, parse_mode="HTML", reply_markup=add_korzina())

        await message.answer("Вот, все что мы нашли для вас", reply_markup=main_keyboard())
        await state.finish()
    except:
        await message.answer("Что-то не так, попробуй еще раз😢")

@dp.callback_query_handler(text="add_korzina_push")
async def cmd_add_korzina(callback: types.CallbackQuery):
    index_id = callback.message.text.split().index("Id:") + 1
    id_tovar = callback.message.text.split()[index_id]
    await bd_conect(callback.message.chat.id)
    result = await add_korzina_to_db(callback.message.chat.id, id_tovar)
    await callback.answer(result)

@dp.callback_query_handler(text="delete_korzina_push")
async def cmd_delete_korzina(callback: types.CallbackQuery):
    index_id = callback.message.text.split().index("Id:") + 1
    id_tovar = callback.message.text.split()[index_id]
    await bd_conect(callback.message.chat.id)
    await delete_korzina_to_db(callback.message.chat.id, id_tovar)
    await callback.answer("Товар удален из корзины!")
    await callback.message.delete()

@dp.message_handler(Text(equals="Моя корзина🗑"))
async def cmd_korzina(message: types.Message):
    try:
        id_tovar = await get_id(message.from_user.id)

        with open("Korzina//ebaty.json", encoding="utf-8") as file:
            fuck = json.load(file)

        count_tovar = 0
        count_price = 0

        for item in fuck:
            for i in id_tovar:
                if item["Id"] == i:
                    card = (f"{hlink(item.get('Название'), item.get('Ссылка на товар'))}\n "
                            f"{hbold('Id: ')}{item.get('Id')}\n "
                            f"{hbold('Описание: ')}{item.get('Описание')}\n "
                            f"{hbold('Цена: ')}{item.get('Стоимость')}руб.\n "
                            f"{hbold('Средняя оценка: ')}{item.get('Средняя оценка')}\n "
                            f"{hbold('Количество отзывов: ')}{item.get('Количество отзывов')}\n ")

                    await message.answer(card, parse_mode="HTML", reply_markup=delete_korzina())
                    count_tovar += 1
                    count_price += item["Стоимость"]

        await message.answer(f"В вашей корзине {count_tovar} товара\nНа сумму {count_price}руб")
    except:
        await message.answer("Ваша корзина пустая")

count_news = 0

@dp.callback_query_handler(text="swipe_one")
async def cmd_news_forward(callback: types.CallbackQuery):
    global count_news
    try:
        with open("ScrapingNews//news.json", encoding="utf-8") as file:
            news_js = json.load(file)

        count_news = 0

        card = (f"{hlink(news_js[count_news].get('Название'), news_js[count_news].get('Ссылка'))}\n "
                f"{hbold('Дата публикации: ')}{news_js[count_news].get('Дата')}\n "
                f"{news_js[count_news].get('Текст')}\n "
                f"{hbold(f'{count_news + 1}/{len(news_js)}')}")

        await callback.message.edit_text(card, parse_mode="HTML", reply_markup=swipe_news())
    except:
        await callback.answer("Ты тупой?")

@dp.callback_query_handler(text="swipe_last")
async def cmd_news_forward(callback: types.CallbackQuery):
    global count_news
    try:
        with open("ScrapingNews//news.json", encoding="utf-8") as file:
            news_js = json.load(file)

        count_news = 29

        card = (f"{hlink(news_js[count_news].get('Название'), news_js[count_news].get('Ссылка'))}\n "
                f"{hbold('Дата публикации: ')}{news_js[count_news].get('Дата')}\n "
                f"{news_js[count_news].get('Текст')}\n "
                f"{hbold(f'{count_news + 1}/{len(news_js)}')}")

        await callback.message.edit_text(card, parse_mode="HTML", reply_markup=swipe_news())
    except:
        await callback.answer("Ты тупой?")

@dp.callback_query_handler(text="forward")
async def cmd_news_forward(callback: types.CallbackQuery):
    try:
        global count_news
        if count_news >= 29:
            await callback.answer("Ты тупой?")
        else:
            count_news += 1

            with open("ScrapingNews//news.json", encoding="utf-8") as file:
                news_js = json.load(file)

            card = (f"{hlink(news_js[count_news].get('Название'), news_js[count_news].get('Ссылка'))}\n "
                    f"{hbold('Дата публикации: ')}{news_js[count_news].get('Дата')}\n "
                    f"{news_js[count_news].get('Текст')}\n "
                    f"{hbold(f'{count_news + 1}/{len(news_js)}')}")

            await callback.message.edit_text(card, parse_mode="HTML", reply_markup=swipe_news())
    except:
        pass

@dp.callback_query_handler(text="back")
async def cmd_news_forward(callback: types.CallbackQuery):
    try:
        global count_news
        if count_news <= 0:
            await callback.answer("Ты тупой?")
        else:
            count_news -= 1

            with open("ScrapingNews//news.json", encoding="utf-8") as file:
                news_js = json.load(file)

            card = (f"{hlink(news_js[count_news].get('Название'), news_js[count_news].get('Ссылка'))}\n "
                    f"{hbold('Дата публикации: ')}{news_js[count_news].get('Дата')}\n "
                    f"{news_js[count_news].get('Текст')}\n "
                    f"{hbold(f'{count_news + 1}/{len(news_js)}')}")

            await callback.message.edit_text(card, parse_mode="HTML", reply_markup=swipe_news())
    except:
        pass

@dp.callback_query_handler(text="reset")
async def cmd_news_forward(callback: types.CallbackQuery):
    global count_news
    await callback.message.edit_text("Мы собираем свежие данные подождите...")
    await get_news()
    count_news = 0

    with open("ScrapingNews//news.json", encoding="utf-8") as file:
        news_js = json.load(file)

    card = (f"{hlink(news_js[count_news].get('Название'), news_js[count_news].get('Ссылка'))}\n "
            f"{hbold('Дата публикации: ')}{news_js[count_news].get('Дата')}\n "
            f"{news_js[count_news].get('Текст')}\n "
            f"{hbold(f'{count_news + 1}/{len(news_js)}')}")

    await callback.message.edit_text(card, parse_mode="HTML", reply_markup=swipe_news())

@dp.message_handler(Text(equals="Новости об мире технике📰"))
async def cmd_get_news(message: types.Message):
    global count_news

    with open("ScrapingNews//news.json", encoding="utf-8") as file:
        news_js = json.load(file)

    card = (f"{hlink(news_js[count_news].get('Название'), news_js[count_news].get('Ссылка'))}\n "
            f"{hbold('Дата публикации: ')}{news_js[count_news].get('Дата')}\n "
            f"{news_js[count_news].get('Текст')}\n "
            f"{hbold(f'{count_news + 1}/{len(news_js)}')}")

    await message.answer(card, parse_mode="HTML", reply_markup=swipe_news())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=info_start)