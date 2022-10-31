from aiogram import Bot, Dispatcher
# from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
TOKEN = "5652445713:AAGeqGWfB8vrG6MByg90clrJivBFJrEPUAU"
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = [553984727, ]
