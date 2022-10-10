from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import logging
import random


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Добро пожаловать, {message.from_user.first_name}!')


@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    img_list = ['media/photo_2022-10-10_10-51-49.jpg', 'media/photo_2022-10-10_10-52-02.jpg',
                'media/photo_2022-10-10_10-52-12.jpg', 'media/photo_2022-10-10_10-52-37.jpg',
                'media/photo_2022-10-10_10-53-06.jpg', 'media/photo_2022-10-10_10-54-15.jpg',
                'media/photo_2022-10-10_10-54-36.jpg']
    img_path = random.choice(img_list)

    await bot.send_photo(message.from_user.id, photo=open(img_path, 'rb'))


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1)

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


@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    question = ' Кто основал Microsoft?'
    answers = [
        'Билл Хайдер',
        "Стив Джобс",
        "Эсенбек Саматович",
        "Билл Гейтс"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        type="quiz",
        correct_option_id=3,
        explanation='Одна из крупнейших транснациональных компаний по производству проприетарного программного'
                    ' обеспечения для различного рода вычислительной техники была основана Биллом Гейтсом'
    )


@dp.message_handler()
async def echo(message: types.Message):
    a = message.text
    if a.isdigit():
        await bot.send_message(message.from_user.id, int(a) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
