from aiogram import executor
import asyncio
from loader import dp, loop
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.dictribution import check_new_dictribution


def repeat_check(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    time_for_wait = 300
    loop.call_later(time_for_wait, repeat_check, coro, loop)


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    loop.call_later(5, repeat_check, check_new_dictribution, loop)
    executor.start_polling(dp, on_startup=on_startup, loop=loop)
