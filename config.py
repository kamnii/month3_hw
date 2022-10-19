from aiogram import Bot, Dispatcher
from decouple import config
from ast import literal_eval
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = literal_eval(config("ADMIN"))
# ADMIN = [553984727, ]
