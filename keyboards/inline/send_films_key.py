from aiogram import types


def make(films):
    markup = types.InlineKeyboardMarkup()
    for film in films:
        button = types.InlineKeyboardButton(film['film_name'], url=film['url'])
        markup.add(button)
    return markup
