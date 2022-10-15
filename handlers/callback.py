from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


lst = ['group', 'supergroup']


# @dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='2button')
    markup = InlineKeyboardMarkup().add(button_call_1)

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
                    ' обеспечения для различного рода вычислительной техники была основана Биллом Гейтсом',
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = 'Из чего в основном состоит Солнце?'
    answers = [
        'Жидкая лава',
        'Расплавленный металл',
        'Газ',
        'Камень',
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        correct_option_id=2,
        explanation='Солнце в основном состоит из двух газов: водорода и гелия.',
        type='quiz',
    )


def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == '1button')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == '2button')
