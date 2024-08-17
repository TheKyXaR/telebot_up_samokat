import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

import config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(f"Привіт, {message.from_user.first_name}, {message.from_user.id}!")  # change start message

# @dp.message(Command(""))
# async def start_command(message: Message):
#     await message.answer(f"Привіт, {message.from_user.first_name}!")

"""

create work (add samokat)
check samokat


"""

@dp.message()
async def echo_message(message: Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    print("bot start\nhttps://t.me/Up_Samokat_Bot")
    asyncio.run(main())