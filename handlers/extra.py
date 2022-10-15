from aiogram import types, Dispatcher
from config import bot, ADMIN
from random import choice


lst = ['group', 'supergroup']


# @dp.message_handler()
async def echo(message: types.Message):

    list_dice = ['🏀', '🎲', '⚽', '🎯', '🎳', '🎰']
    random_dice = choice(list_dice)

    if message.from_user.id in ADMIN:
        if message.text.startswith('game'):
            await bot.send_dice(message.chat.id, emoji=random_dice)
        else:
            if message.text.isdigit():
                if not message.chat.type in lst:
                    await bot.send_message(message.from_user.id, int(message.text) ** 2)
                else:
                    await bot.send_message(message.chat.id, int(message.text) ** 2)
            else:
                if not message.chat.type in lst:
                    await bot.send_message(message.from_user.id, message.text)
                else:
                    await bot.send_message(message.chat.id, message.text)
    else:
        if message.text.isdigit():
            if not message.chat.type in lst:
                await bot.send_message(message.from_user.id, int(message.text) ** 2)
            else:
                await bot.send_message(message.chat.id, int(message.text) ** 2)
        else:
            if not message.chat.type in lst:
                await bot.send_message(message.from_user.id, message.text)
            else:
                await bot.send_message(message.chat.id, message.text)


def register_extra_handler(dp: Dispatcher):
    dp.register_message_handler(echo)
