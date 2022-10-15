from aiogram import types, Dispatcher
from config import bot, ADMIN
from random import choice


async def pin(message: types.Message):
    await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


def register_admin_handler(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
