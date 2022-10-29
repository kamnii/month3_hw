from aiogram import types, Dispatcher
from config import bot, ADMIN
from database.bot_db import sql_command_all_mentors
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def pin(message: types.Message):
    await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


lst = ['group', 'supergroup']


async def get_delete_mentor(message: types.Message):
    a = message.from_user.id if not message.chat.type in lst else message.chat.id
    if not message.from_user.id in ADMIN:
        await message.answer("Недостаточно прав!")
    else:
        mentors = await sql_command_all_mentors()
        for mentor in mentors:
            await bot.send_message(a, f"Имя => {mentor[1]}\n"
                                      f"Направление => {mentor[2]}\n"
                                      f"Возраст => {mentor[3]}\n"
                                      f"Группа => {mentor[4]}",
                                   InlineKeyboardMarkup().add(
                                       InlineKeyboardButton(f'Delete {mentor[1]}',
                                                            callback_data=f'delete {mentor[0]}')))


def register_admin_handler(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(get_delete_mentor, commands=['del_men'])
