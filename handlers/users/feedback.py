from aiogram import types
from loader import dp, db_api
from aiogram.dispatcher import FSMContext


# TODO
@dp.message_handler(commands=['feedback'])
async def send_feedback(message: types.Message, state: FSMContext):
    text = db_api.get_message('обратная_связь')
    await message.answer(text)
