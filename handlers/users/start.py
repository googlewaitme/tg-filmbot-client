from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db_api


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = db_api.get_message('стартовое_сообщение')
    await message.answer(text)
