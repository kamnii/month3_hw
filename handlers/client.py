from database.bot_db import sql_command_backend, sql_command_frontend, sql_command_android, sql_command_ios
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot
from buttons.inline_buttons import genre_markup
import random

lst = ['group', 'supergroup']


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(f'Приветствую тебя, {message.from_user.first_name}! '
                         f'Для того чтобы увидеть список команд нажми на /help')


async def help_handler(message: types.Message):
    await message.answer(f'/dice - игра с ботом\n'
                         f'/mem - случайный мем\n'
                         f'/quiz - викторина\n'
                         f'/anime - ссылки на аниме\n'
                         f'/pin - закрепить сообщение(ответом на сообщение)\n'
                         f'/backend_men - случайный ментор с Backend\n'
                         f'/frontend_men - случайный ментор с Frontend\n'
                         f'/android_men - случайный ментор с Android\n'
                         f'/ios_men - случайный ментор с Ios\n\n'
                         f'Для админов:\n'
                         f'/add_men - добавить ментора в БД\n'
                         f'/del_men - удаление менторов с БД\n'
                         f'')


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


async def get_backend_mentors(message: types.Message):
    await sql_command_backend(message)


async def get_frontend_mentors(message: types.Message):
    await sql_command_frontend(message)


async def get_android_mentors(message: types.Message):
    await sql_command_android(message)


async def get_ios_mentors(message: types.Message):
    await sql_command_ios(message)


async def get_anime(message: types.Message):
    await message.answer('Какой жанр хотите?', reply_markup=genre_markup)


def register_client_handler(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(dice, commands=['dice'])
    dp.register_message_handler(get_backend_mentors, commands=['backend_men'])
    dp.register_message_handler(get_frontend_mentors, commands=['frontend_men'])
    dp.register_message_handler(get_android_mentors, commands=['android_men'])
    dp.register_message_handler(get_ios_mentors, commands=['ios_men'])
    dp.register_message_handler(get_anime, commands=['anime'])
    dp.register_message_handler(help_handler, commands=['help'])
