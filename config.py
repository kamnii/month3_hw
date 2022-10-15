from aiogram import Bot, Dispatcher
from decouple import config
from ast import literal_eval


TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot)
ADMIN = literal_eval(config("ADMIN"))
# ADMIN = [553984727, ]
