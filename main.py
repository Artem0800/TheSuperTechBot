import time
from confic import bot, dp
from aiogram import executor, types
from keyboard import main_keyboard, add_korzina, otbor_tovara
from keyboard import delete_korzina, swipe_news, kb_add_target_pay, api_pay, detali_pc
from aiogram.utils.markdown import hbold, hlink
from aiogram.dispatcher.filters import Text
from Scraping.Видеокарты.parce import videocard
from Scraping.Процессоры.parce import procces
from Scraping.БлокПитания.parce import block_energy
from Scraping.МатеринскиеПлаты.parce import mother_plata
from Scraping.ОперативнаяПамять.parce import memory_oper
from Scraping.ЖесткиеДискиHDD25.parce import hd25
from Scraping.ЖесткиеДискиHDD35.parce import hd35
from Scraping.ТвердотельныеНакопителиSSD.parce import sdd
from Scraping.Корпуса.parce import korpus
from Scraping.ОхлаждениеЖиткое.parce import wsh
from Scraping.КулерыДляПроцессоров.parce import kprs
from Scraping.ВентиляторДляКорпуса.parce import vk
import json
from aiogram.dispatcher import FSMContext
from state_machine import State_Otbor
from aiogram.types import ReplyKeyboardRemove
from sqlite import bd_conect, add_korzina_to_db, get_id, delete_korzina_to_db, get_pay_target
from sqlite import create_target_pay, delete_target_pay, update_user_sum
from ScrapingNews.scraping_news import get_news
from pay import order
from filter_user import filter_products

async def info_start(_):
    print("Я запустился")

@dp.message_handler(Text(equals=["/start", "Вернуться в главное меню🚶🏼"]))
async def cmd_start(message: types.Message):
    await message.delete()
    await bd_conect(message.from_user.id)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://b1.filmpro.ru/c/43526.jpg",
                            caption="<b>Добро пожаловать в бота Валеру!</b>",
                           parse_mode="HTML",
                           reply_markup=main_keyboard())

@dp.message_handler(Text(equals="Обновить данные🔄"))
async def cmd_update_scrap(message: types.Message):
    await message.reply(text="Подождите, обновляем информацию...", reply_markup=ReplyKeyboardRemove())

    block_energy(),
    vk(),
    kprs(),
    wsh(),
    hd35(),
    time.sleep(3)
    hd25(),
    sdd(),
    videocard(),
    procces(),
    time.sleep(3)
    mother_plata(),
    memory_oper(),
    korpus()

    with open("Scraping//Корпуса//result.json", encoding="utf-8") as file:
        data1 = json.load(file)

    with open("Scraping//ОперативнаяПамять//result.json", encoding="utf-8") as file:
        data2 = json.load(file)

    with open("Scraping//МатеринскиеПлаты//result.json", encoding="utf-8") as file:
        data3 = json.load(file)

    with open("Scraping//Процессоры//result.json", encoding="utf-8") as file:
        data4 = json.load(file)

    with open("Scraping//БлокПитания//result.json", encoding="utf-8") as file:
        data5 = json.load(file)

    with open("Scraping//ТвердотельныеНакопителиSSD//result.json", encoding="utf-8") as file:
        data6 = json.load(file)

    with open("Scraping//ЖесткиеДискиHDD25//result.json", encoding="utf-8") as file:
        data7 = json.load(file)

    with open("Scraping//ЖесткиеДискиHDD35//result.json", encoding="utf-8") as file:
        data8 = json.load(file)

    with open("Scraping//Видеокарты//result.json", encoding="utf-8") as file:
        data9 = json.load(file)

    with open("Scraping//ОхлаждениеЖиткое//result.json", encoding="utf-8") as file:
        data10 = json.load(file)

    with open("Scraping//КулерыДляПроцессоров//result.json", encoding="utf-8") as file:
        data11 = json.load(file)

    with open("Scraping//ВентиляторДляКорпуса//result.json", encoding="utf-8") as file:
        data12 = json.load(file)

    union = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12

    with open("SQL//ebaty.json", "w", encoding="utf-8") as file:
        json.dump(union, file, indent=4, ensure_ascii=False)

    await message.answer(text="Данные обновлены", reply_markup=main_keyboard())

@dp.message_handler(Text(equals="Собрать ПК🖥"))
async def cmd_detal_PC(message: types.Message):
    await message.reply("<i>Вот список деталей</i>\n1)Процессоры\n2)Материнские платы\n3)Видеокарты\n"
                        "4)Оперативная память\n5)Корпуса\n6)Блок питания\n7)Житкостное охлаждение\n8)Кулеры для процессоров\n"
                        "9)Вентилятор для корпуса\n10)Твердотельные Накопители SSD\n11)Жесткие Диски HDD 3.5\n12)Жесткие Диски HDD 2.5\n"
                        
                        "Выбери нужную тебе деталь из данного списка",
                        reply_markup=detali_pc(),
                        parse_mode="HTML")

name_search = ""

@dp.message_handler(Text(equals=["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","1️⃣0️⃣","1️⃣1️⃣","1️⃣2️⃣" "Игровые ноутбуки"]))
async def cmd_get_videocard(message: types.Message):
    global name_search
    name_search = ""
    if message.text == "1️⃣":
        message.text = "Процессоры"
    elif message.text == "2️⃣":
        message.text = "МатеринскиеПлаты"
    elif message.text == "3️⃣":
        message.text = "Видеокарты"
    elif message.text == "4️⃣":
        message.text = "ОперативнаяПамять"
    elif message.text == "5️⃣":
        message.text = "Корпуса"
    elif message.text == "6️⃣":
        message.text = "БлокПитания"
    elif message.text == "7️⃣":
        message.text = "Житкостное охлаждение"
    elif message.text == "8️⃣":
        message.text = "Кулеры для процессоров"
    elif message.text == "9️⃣":
        message.text = "Вентилятор для корпуса"
    elif message.text == "1️⃣0️⃣":
        message.text = "ТвердотельныеНакопителиSSD"
    elif message.text == "1️⃣1️⃣":
        message.text = "ЖесткиеДискиHDD3.5"
    elif message.text == "1️⃣2️⃣":
        message.text = "ЖесткиеДискиHDD2.5"

    name_search += message.text

    await message.reply(text="<i>Нажмите на кнопку чтобы отфильтровать товары</i>", reply_markup=otbor_tovara(),
                        parse_mode="HTML")

@dp.message_handler(content_types=["web_app_data"])
async def cmd_get_tovar(message: types.Message):
    global name_search
    filter_user = json.loads(message.web_app_data.data)

    pizda_bobra = {
        "Видеокарты": "Видеокарты",
        "Корпуса": "Корпуса",
        "Процессоры": "Процессоры",
        "ОперативнаяПамять": "ОперативнаяПамять",
        "БлокПитания": "БлокПитания",
        "МатеринскиеПлаты": "МатеринскиеПлаты",
        "ТвердотельныеНакопителиSSD": "ТвердотельныеНакопителиSSD",
        "ЖесткиеДискиHDD3.5": "ЖесткиеДискиHDD3.5",
        "ЖесткиеДискиHDD2.5": "ЖесткиеДискиHDD2.5",
        "Житкостное охлаждение": "ОхлаждениеЖиткое",
        "Кулеры для процессоров": "КулерыДляПроцессоров",
        "Вентилятор для корпуса": "ВентиляторДляКорпуса"
    }

    try:
        with open(f"Scraping//{pizda_bobra[name_search]}//result.json", encoding="utf-8") as file:
            data = json.load(file)

        get_result = await filter_products(data, filter_user)

        result_otbor = []

        for i in get_result:
            result_otbor.append(i)

        for index, item in enumerate(result_otbor):
            card = (f"{hlink(item.get('Название'), item.get('Ссылка на товар'))}\n"
                    f"{hbold('Id: ')}{item.get('Id')}\n"
                    f"{hbold('Описание: ')}{item.get('Описание')}\n"
                    f"{hbold('Цена: ')}{item.get('Стоимость')}руб.\n"
                    f"{hbold('Средняя оценка: ')}{item.get('Средняя оценка')}\n"
                    f"{hbold('Количество отзывов: ')}{item.get('Количество отзывов')}\n")

            if index % 20 == 0:
                time.sleep(5)

            await message.answer(card, parse_mode="HTML", reply_markup=add_korzina())

        await message.answer("Вот, все что мы нашли для вас", reply_markup=main_keyboard())
    except Exception as ex:
        print(ex)
        await message.answer("Что-то не так, попробуй еще раз😢")

@dp.callback_query_handler(text="add_korzina_push")
async def cmd_add_korzina(callback: types.CallbackQuery):
    index_id = callback.message.text.split().index("Id:") + 1
    id_tovar = callback.message.text.split()[index_id]
    result = await add_korzina_to_db(callback.message.chat.id, id_tovar)
    await callback.answer(result)

@dp.callback_query_handler(text="delete_korzina_push")
async def cmd_delete_korzina(callback: types.CallbackQuery):
    index_id = callback.message.text.split().index("Id:") + 1
    id_tovar = callback.message.text.split()[index_id]
    await delete_korzina_to_db(callback.message.chat.id, id_tovar)
    await callback.answer("Товар удален из корзины!")
    await callback.message.delete()

@dp.message_handler(Text(equals="Моя корзина🗑"))
async def cmd_korzina(message: types.Message):
    id_tovar = await get_id(message.from_user.id)

    with open("SQL//ebaty.json", encoding="utf-8") as file:
        fuck = json.load(file)

    count_tovar = 0
    count_price = 0

    for item in fuck:
        for i in id_tovar:
            if item["Id"] == i:
                card = (f"{hlink(item.get('Название'), item.get('Ссылка на товар'))}\n"
                        f"{hbold('Id: ')}{item.get('Id')}\n"
                        f"{hbold('Описание: ')}{item.get('Описание')}\n"
                        f"{hbold('Цена: ')}{item.get('Стоимость')}руб.\n"
                        f"{hbold('Средняя оценка: ')}{item.get('Средняя оценка')}\n"
                        f"{hbold('Количество отзывов: ')}{item.get('Количество отзывов')}\n")

                await message.answer(card, parse_mode="HTML", reply_markup=delete_korzina())
                count_tovar += 1
                count_price += item["Стоимость"]

    await message.answer(f"В вашей корзине {count_tovar} товара\nНа сумму {count_price}руб")

count_news = 0

@dp.callback_query_handler(text="swipe_one")
async def cmd_news_forward(callback: types.CallbackQuery):
    global count_news
    try:
        with open("ScrapingNews//news.json", encoding="utf-8") as file:
            news_js = json.load(file)

        count_news = 0

        card = (f"{hlink(news_js[count_news].get('Название'), news_js[count_news].get('Ссылка'))}\n"
                f"{hbold('Дата публикации: ')}{news_js[count_news].get('Дата')}\n"
                f"{news_js[count_news].get('Текст')}\n"
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

        card = (f"{hlink(news_js[count_news].get('Название'), news_js[count_news].get('Ссылка'))}\n"
                f"{hbold('Дата публикации: ')}{news_js[count_news].get('Дата')}\n"
                f"{news_js[count_news].get('Текст')}\n"
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

            card = (f"{hlink(news_js[count_news].get('Название'), news_js[count_news].get('Ссылка'))}\n"
                    f"{hbold('Дата публикации: ')}{news_js[count_news].get('Дата')}\n"
                    f"{news_js[count_news].get('Текст')}\n"
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

            card = (f"{hlink(news_js[count_news].get('Название'), news_js[count_news].get('Ссылка'))}\n"
                    f"{hbold('Дата публикации: ')}{news_js[count_news].get('Дата')}\n"
                    f"{news_js[count_news].get('Текст')}\n"
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

    card = (f"{hlink(news_js[count_news].get('Название'), news_js[count_news].get('Ссылка'))}\n"
            f"{hbold('Дата публикации: ')}{news_js[count_news].get('Дата')}\n"
            f"{news_js[count_news].get('Текст')}\n"
            f"{hbold(f'{count_news + 1}/{len(news_js)}')}")

    await callback.message.edit_text(card, parse_mode="HTML", reply_markup=swipe_news())

@dp.callback_query_handler(text="close_news")
async def cmd_close_news(callback: types.CallbackQuery):
    await callback.message.delete()

@dp.message_handler(Text(equals="Новости об мире технике📰"))
async def cmd_get_news(message: types.Message):
    global count_news

    with open("ScrapingNews//news.json", encoding="utf-8") as file:
        news_js = json.load(file)

    card = (f"{hlink(news_js[count_news].get('Название'), news_js[count_news].get('Ссылка'))}\n"
            f"{hbold('Дата публикации: ')}{news_js[count_news].get('Дата')}\n"
            f"{news_js[count_news].get('Текст')}\n"
            f"{hbold(f'{count_news + 1}/{len(news_js)}')}")

    await message.answer(card, parse_mode="HTML", reply_markup=swipe_news())

@dp.callback_query_handler(text="create_target_pay")
async def cmd_create_target_pay(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="Какое название у вашей цели?", reply_markup=ReplyKeyboardRemove())
    await State_Otbor.name_target.set()

@dp.message_handler(state=State_Otbor.name_target)
async def state_name_target(message: types.Message, state: FSMContext):
    await state.update_data(name_target=message.text)
    await message.reply(text="Сколько нужно накопить?")
    await State_Otbor.sum_target.set()

@dp.message_handler(state=State_Otbor.sum_target)
async def cmd_sum_target(message: types.Message, state: FSMContext):
    fun = lambda num: str(num).isdigit()
    if fun(message.text) is True and message.text[0] != "0":
        await state.update_data(sum_target=message.text)
        result_data = await state.get_data()
        await create_target_pay(message.from_user.id, result_data['name_target'], result_data['sum_target'])
        await state.finish()
        await message.reply("Ваша цель была создана!\nНажмите снова на накопительные цели",
                                reply_markup=main_keyboard())
    else:
        await message.reply(text="Используй только цифры!")

@dp.callback_query_handler(text="delete_target")
async def cmd_delete_target_pay(callback: types.CallbackQuery):
    target = " ".join(callback.message.text.split()[1:callback.message.text.split().index("Сумма:")])
    ind = callback.message.text.split()[callback.message.text.split().index("Сумма:") + 1].split("/")[1]
    sum = callback.message.text.split()[callback.message.text.split().index("Сумма:") + 1].split("/")[1][0:ind.index("р")]
    await delete_target_pay(callback.message.chat.id, target, sum)
    await callback.answer("Цель удалена!")
    await callback.message.delete()

user_target = ""
user_sum = ""

@dp.callback_query_handler(text="Popolnity")
async def cmd_popolnity_pay(callback: types.CallbackQuery):
    global user_target, user_sum
    user_target = ""
    user_sum = ""

    target = " ".join(callback.message.text.split()[1:callback.message.text.split().index("Сумма:")])
    ind = callback.message.text.split()[callback.message.text.split().index("Сумма:") + 1].split("/")[1]
    sum = callback.message.text.split()[callback.message.text.split().index("Сумма:") + 1].split("/")[1][0:ind.index("р")]

    user_target += target
    user_sum += sum

    await callback.message.delete()
    await callback.message.answer("Введите сумму которую хотите положить", reply_markup=ReplyKeyboardRemove())
    await State_Otbor.price_pay.set()

@dp.message_handler(state=State_Otbor.price_pay)
async def state_price_pay(message: types.Message, state: FSMContext):
    fun = lambda num: str(num).isdigit()
    if fun(message.text) is True and message.text[0] != "0":
        await state.update_data(price_pay=message.text)
        result = await state.get_data()
        await order(message.chat.id, bot, int(result['price_pay']))
        await state.finish()
    else:
        await message.reply("Используй только цифры!")

@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(checkout: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(checkout.id, ok=True)

# Handler когда оплата будет успешной
@dp.message_handler(content_types=[types.ContentType.SUCCESSFUL_PAYMENT])
async def successful_payment(message: types.Message):
    msg = f"Вы успешно пополнили свой счёт!\nНа сумму: {message.successful_payment.total_amount // 100}руб"
    await update_user_sum(message.from_user.id, user_target, int(message.successful_payment.total_amount // 100))

    await message.answer(msg, reply_markup=main_keyboard())

@dp.message_handler(Text(equals="Накопительные цели💳"))
async def cmd_pay(message: types.Message):
    count_sum = 0
    result = await get_pay_target(message.from_user.id)
    if result is False:
        await message.reply("У вас нет созданых целей", reply_markup=kb_add_target_pay())
    else:
        for i in result:
            name, summ, price_user = i
            count_sum += summ
            await message.answer(f"Цель: {name}\nСумма: {price_user}/{summ}руб\nОсталось: {summ - price_user}руб",
                                 reply_markup=api_pay())
        await message.answer(f"Общая сумма: {count_sum}руб")
        await message.reply("Вот ваши цели, вы можете создать еще", reply_markup=kb_add_target_pay())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=info_start)