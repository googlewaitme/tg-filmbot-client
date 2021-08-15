from aiogram import types
from loader import dp, db_api


@dp.message_handler(state='*')
async def send_films(message: types.Message):
    films = db_api.get_films(message.text)
    # print(data)
    # films = [{'film_name': 'GG1', 'url': 'http://google.com/'}]  # api.get_films(message)
    text = 'Подобранные фильмы'  # api.get_message(unique_name='найденные_фильмы')
    markup = types.InlineKeyboardMarkup()
    for film in films:
        button = types.InlineKeyboardButton(film['film_name'], url=film['url'])
        markup.add(button)
    await message.answer(text=text, reply_markup=markup)
