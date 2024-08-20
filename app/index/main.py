from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import sqlite3

con = sqlite3.connect("db.db")
cur = con.cursor()

rt = Router()

class Add_Samokat_Form(StatesGroup):
    name = State()
    phone = State()
    notes = State()

# add samokat
@rt.message(Command("addsamokat"))
async def add_samokat_name_client(message: Message, state: FSMContext, User: tuple):
    if User:
        await message.answer("Опишіть поломку самоката")
        await state.set_state(Add_Samokat_Form.notes)
    else:
        await message.answer("Як вас звати?")
        await state.set_state(Add_Samokat_Form.name)

@rt.message(Add_Samokat_Form.name)
async def add_samokat_phone_client(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("За яким номером ми зможемо з вами зв'язатись?")
    await state.set_state(Add_Samokat_Form.phone)

@rt.message(Add_Samokat_Form.phone)
async def add_samokat_notes(message: Message, state: FSMContext):
    await state.update_data(phone=message.text.replace(" ", ""))
    await message.answer("Опишіть поломку самоката")
    await state.set_state(Add_Samokat_Form.notes)

@rt.message(Add_Samokat_Form.notes)
async def add_samokat_notes(message: Message, state: FSMContext, User: tuple):
    await state.update_data(notes=message.text)
    data = await state.get_data()

    for count_number in range(-3, -7, -1):
        if User:
            select = cur.execute('SELECT id FROM samokats WHERE "number" = ?', (User[4][count_number:],)).fetchone()
            if not bool(select):
                number = User[4][count_number:]
                break
        else:
            select = cur.execute('SELECT id FROM samokats WHERE "number" = ?', (data["phone"][count_number:],)).fetchone()
            if not bool(select):
                number = data["phone"][count_number:]
                break

    if User:
        cur.execute('INSERT INTO samokats (client_name, client_phone, notes, "number", client_id) VALUES (?, ?, ?, ?, ?)',
                    (User[3], User[4], data["notes"], number, User[0]))
        con.commit()
    else:
        cur.execute('INSERT INTO samokats (client_name, client_phone, notes, "number") VALUES (?, ?, ?, ?)',
                    (data["name"].lower(), data["phone"], data["notes"], number))
        con.commit()

    await message.answer("Замовлення успішно додано")
    await state.clear()