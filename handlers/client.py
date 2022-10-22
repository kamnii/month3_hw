from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
import random
from database.bot_db import sql_command_backend, sql_command_frontend


lst = ['group', 'supergroup']


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(f'Приветствую тебя, {message.from_user.first_name}!')


async def dice(message: types.Message):
    if message.chat.type in lst:
        user_dice = await bot.send_dice(message.chat.id)
        await bot.send_message(message.chat.id, 'Это Ваша кость', reply_to_message_id=user_dice.message_id)
        bot_dice = await bot.send_dice(message.chat.id)
        await bot.send_message(message.chat.id, 'Это моя кость', reply_to_message_id=bot_dice.message_id)
        if bot_dice.dice.value > user_dice.dice.value:
            await message.answer('Я выйграл')
        elif bot_dice.dice.value < user_dice.dice.value:
            await message.answer('Вы выйграли')
        else:
            await message.answer('Ничья!')
    else:
        user_dice = await bot.send_dice(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Это Ваша кость', reply_to_message_id=user_dice.message_id)
        bot_dice = await bot.send_dice(message.chat.id)
        await bot.send_message(message.from_user.id, 'Это моя кость', reply_to_message_id=bot_dice.message_id)
        if bot_dice.dice.value > user_dice.dice.value:
            await message.answer('Я выйграл')
        elif bot_dice.dice.value < user_dice.dice.value:
            await message.answer('Вы выйграли')
        else:
            await message.answer('Ничья!')


# @dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    img_list = ['media/photo_2022-10-10_10-51-49.jpg', 'media/photo_2022-10-10_10-52-02.jpg',
                'media/photo_2022-10-10_10-52-12.jpg', 'media/photo_2022-10-10_10-52-37.jpg',
                'media/photo_2022-10-10_10-53-06.jpg', 'media/photo_2022-10-10_10-54-15.jpg',
                'media/photo_2022-10-10_10-54-36.jpg', 'media/photo_2022-10-14_23-46-47.jpg', ]
    img_path = random.choice(img_list)

    if message.chat.type in lst:
        await bot.send_photo(message.chat.id, photo=open(img_path, 'rb'))
    else:
        await bot.send_photo(message.from_user.id, photo=open(img_path, 'rb'))


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='1button')
    markup = InlineKeyboardMarkup().add(button_call_1)

    question = "Что из этого не считается планетой?"
    answers = [
        'Сатурн',
        'Меркурий',
        'Марс',
        'Плутон',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        type="quiz",
        question=question,
        options=answers,
        correct_option_id=3,
        reply_markup=markup,
        explanation='Плутон не смог расчистить пространство вокруг своей орбиты от других объектов и это явилось'
                    ' главной причиной вычеркнуть его из списка планет.'
    )


async def get_back_mentors(message: types.Message):
    await sql_command_backend(message)


async def get_front_mentors(message: types.Message):
    await sql_command_frontend(message)


def register_client_handler(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(dice, commands=['dice'])
    dp.register_message_handler(sql_command_backend, commands=['backend'])
    dp.register_message_handler(sql_command_frontend, commands=['frontend'])
