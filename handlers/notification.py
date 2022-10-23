from aiogram import types, Dispatcher
from config import bot
import aioschedule
import asyncio


async def basketball():
    await bot.send_message(chat_id=553984727, text='Через 45 минут баскетбол🏀')


async def courses():
    await bot.send_message(chat_id=553984727, text='Через 1 час и 30 минут курсы💻')


async def schedule():
    aioschedule.every().monday.at('17:45').do(basketball)
    aioschedule.every().wednesday.at('15:15').do(basketball)
    aioschedule.every().saturday.at('11:15').do(basketball)
    aioschedule.every().wednesday.at('18:30').do(courses)
    aioschedule.every().saturday.at('18:30').do(courses)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(5)


def register_notification_handler(dp: Dispatcher):
    dp.register_message_handler(schedule,
                                lambda word: 'напомни' in word.text)
