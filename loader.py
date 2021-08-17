import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.database_api import DBApi

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
db_api = DBApi(config.IP)
loop = asyncio.get_event_loop()
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
