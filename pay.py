from confic import bot
from aiogram.types import LabeledPrice

# Функция выставление счета пользователю
async def order(id, Bot: bot, price_user):
    await bot.send_invoice(
        chat_id=id,
        title="Пополнение накопительного счета",
        description="Пополните свой накопительный счет",
        payload="pay_data",
        provider_token="1744374395:TEST:f6217ca16ce632e10a64",
        currency="rub",
        prices=[LabeledPrice(label="Сумма пополнения", amount=price_user * 100)]
    )