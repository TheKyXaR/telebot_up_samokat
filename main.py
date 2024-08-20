import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

import middleware

import app.registration.main as reg
import app.index.main as index
import app.finder.main as finder

import keyboard
import config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# start (add registration)
@dp.message(Command("start"))
async def start_command(message: Message, User: tuple):
    if User:
        await message.answer(f"Привіт {message.from_user.first_name}! Для створення замовлення виконай команду /addsamokat")
    else:
        await message.answer(f"Ви не зареєстровані для реєстрації виконайте /reg")

# price list
@dp.message(Command("pricelist"))
async def add_samokat_name_client(message: Message):
    await message.answer("тут вивести всі ціни")

async def main():
    dp.update.middleware(middleware.Check_user())

    dp.include_router(reg.rt)
    dp.include_router(index.rt)
    dp.include_router(finder.rt)
    await dp.start_polling(bot)

if __name__ == '__main__':
    print("bot start\nhttps://t.me/Up_Samokat_Bot")
    asyncio.run(main())



# @dp.message(Command("start"))
# async def start_command(message: Message):
#     is_user = cur.execute(f'SELECT * FROM users WHERE id_telegram = "{message.from_user.id}"').fetchone()

#     if is_user :
#         await message.answer(f"Привіт, {message.from_user.first_name}!")
#     else :
#         cur.execute("""INSERT INTO users (id_telegram, status, name) 
#                         VALUES (?, ?, ?)""", 
#                         (message.from_user.id, "client", message.from_user.first_name))
#         con.commit()

#         await message.answer(f"Привіт, {message.from_user.first_name}, тебе вітає бот ... !")  # change start message