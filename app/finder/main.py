from aiogram import Router
from aiogram.types import Message

import sqlite3

rt = Router()

con = sqlite3.connect("db.db")
cur = con.cursor()

# find samokat
@rt.message()
async def echo_message(message: Message, User: tuple):
    if User[2] == "client" or not User:
        select = cur.execute('SELECT * FROM samokats WHERE "number" = ? AND id_telegram_client = ?', (message.text, message.from_user.id)).fetchall()
        select = cur.execute('SELECT * FROM samokats WHERE id_telegram_client = ?', (message.from_user.id,)) if message.text == "всі" else select

        ms_text = ""
        for x in select:
            ms_text += f"\n\n----------\nсамокат - {x[2]}\nстатус самоката - {x[3]}\nім'я клієнта - {x[8][0].upper() + x[8][1:]}\nномер телефона -  {x[1]}\n\nполомка - {x[5]}"
        await message.answer(ms_text)
    else:
        select = cur.execute('SELECT * FROM samokats WHERE "number" = ?', (message.text,)).fetchall()
        select = select if select else cur.execute('SELECT * FROM samokats WHERE "client_phone" = ?', (message.text,)).fetchall()
        select = select if select else cur.execute('SELECT * FROM samokats WHERE "client_name" = ?', ((message.text).lower(),)).fetchall()
        select = select if select else cur.execute('SELECT * FROM samokats WHERE "status" = ?', (message.text,)).fetchall()

        select = cur.execute('SELECT * FROM samokats') if message.text == "всі" else select

        if select :
            ms_text = ""
            for x in select:
                ms_text += f"\n\n----------\nсамокат - {x[2]}\nстатус самоката - {x[3]}\nім'я клієнта - {x[8][0].upper() + x[8][1:]}\nномер телефона -  {x[1]}\n\nполомка - {x[5]}"
            await message.answer(ms_text)
        else :
            await message.answer("не знайдено самоката по вашому запросу")