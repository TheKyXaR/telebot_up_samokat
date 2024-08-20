from aiogram import BaseMiddleware
from aiogram.types import Update, Message
from typing import Callable, Dict, Any, Awaitable

import sqlite3

con = sqlite3.connect("db.db")
cur = con.cursor()

class Check_user(BaseMiddleware):
    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Update, data: Dict[str, Any]) -> Any:
        if event.message:
            data['User'] = cur.execute("SELECT * FROM users WHERE id_telegram=?", (event.message.from_user.id,)).fetchone()
            return await handler(event, data)