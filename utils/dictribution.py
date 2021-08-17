from loader import db_api, dp
from aiogram import types
import asyncio
import time


async def check_new_dictribution():
    dictribtuions = db_api.get_dictributions()
    print(dictribtuions)
    for dictribtuion in dictribtuions:
        await send_dictribution(dictribtuion)
        await asyncio.sleep(100)


async def send_dictribution(dictribtuion):
    message = make_message(dictribtuion)
    for user in db_api.get_users():
        print(user)
        try:
            await dp.bot.send_message(chat_id=user, **message)
            time.sleep(0.5)
        except:
            pass


def make_message(dictribution):
    text = ''
    markup = types.InlineKeyboardMarkup()
    if dictribution["content_url"]:
        url = dictribution['content_url']
        text = f'<a href="{url}"></a>'
    if dictribution["button_url"]:
        button_url = dictribution['button_url']
        button_name = dictribution['button_text']
        button = types.InlineKeyboardButton(button_name, url=button_url)
        markup.add(button)
    text += f'<b>{dictribution["heading_text"]}</b>\n\n'
    text += dictribution['main_text']
    return {'text': text, 'reply_markup': markup}
