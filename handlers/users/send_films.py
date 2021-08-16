from aiogram import types
from loader import dp, db_api
from keyboards.inline import send_films_key


@dp.message_handler(state='*')
async def send_films(message: types.Message):
    films = db_api.get_films(message.text)
    text = db_api.get_message(unique_name='найденные_фильмы')
    markup = send_films_key.make(films)
    await message.answer(text=text, reply_markup=markup)
