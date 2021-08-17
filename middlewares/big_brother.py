from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from loader import db_api


class BigBrotherMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        db_api.send_activity('user', message.from_user.id)
