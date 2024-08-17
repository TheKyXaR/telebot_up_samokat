import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN = '7272830857:AAF_bZ7caaSpBTIXcapgPsqZjGuULV7TZOg'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(f"Привіт, {message.from_user.first_name}, {message.from_user.id}, {message.contact.phone_number}!")

# @dp.message(Command(""))
# async def start_command(message: Message):
#     await message.answer(f"Привіт, {message.from_user.first_name}!")

"""




"""

@dp.message()
async def echo_message(message: Message):
    await message.answer(message.text)

async def main():
    # Запускаємо бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    print("bot start\nhttps://t.me/Up_Samokat_Bot")
    asyncio.run(main())