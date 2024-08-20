from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import sqlite3

con = sqlite3.connect("db.db")
cur = con.cursor()

class Reg_Form(StatesGroup):
	name = State()
	phone = State()

rt = Router()

@rt.message(Command("reg"))
async def registration(message: Message, state: FSMContext, User: tuple):
	if not User:
	    await message.answer("Як вас звати?")
	    await state.set_state(Reg_Form.name)
	else:
		await message.answer("Ви вже зареєстровані")

@rt.message(Reg_Form.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("За яким номером ми зможемо з вами зв'язатись?")
    await state.set_state(Reg_Form.phone)

@rt.message(Reg_Form.phone)
async def add_phone(message: Message, state: FSMContext):
	await state.update_data(phone=message.text.replace(" ", ""))
	data = await state.get_data()

	cur.execute('INSERT INTO users (name, phone, id_telegram) VALUES (?, ?, ?)',
                (data["name"].lower(), data["phone"], message.from_user.id))
	con.commit()

	await message.answer("Вітаємо ви зареєструвались )")
	await state.clear()


@rt.message(Command("delacc"))
async def delete_account(message: Message, User: tuple):
	if User:
		cur.execute("DELETE FROM users WHERE id_telegram = ?", (User[1],))
		con.commit()
		await message.answer("Ваш аккаунт видалено")
	else:
		await message.answer("Ви ще не зареєстровані")