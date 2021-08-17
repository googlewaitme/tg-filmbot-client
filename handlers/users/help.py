from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp, db_api


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message, *args, **kwargs):
    text = db_api.get_message('сообщение_помощь')
    await message.answer(text)
