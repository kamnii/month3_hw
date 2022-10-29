from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.bot_db import sql_command_delete_mentor
from aiogram import types, Dispatcher
from config import bot
from pars.comedy_anime import parser_comedy, parser_romance, parser_sport, parser_adventure, parser_detectives, \
    parser_everyday, parser_fantasy, parser_horrors

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


async def delete_mentor(call: types.CallbackQuery):
    await sql_command_delete_mentor(call.data.replace('Delete ', ''))
    await call.answer(text='Ментор удален', show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


async def comedy_anime(call: types.CallbackQuery):
    items = parser_comedy()
    for item in items:
        await bot.send_message(call.from_user.id, f"{item['link']}\n\n"
                                                  f"{item['title']}\n"
                                                  f"{item['length']}\n"
                                                  f"#{item['country']}\n"
                                                  f"#year_{item['year']}")


async def fantasy_anime(call: types.CallbackQuery):
    items = parser_fantasy()
    for item in items:
        await bot.send_message(call.from_user.id, f"{item['link']}\n\n"
                                                  f"{item['title']}\n"
                                                  f"{item['length']}\n"
                                                  f"#{item['country']}\n"
                                                  f"#year_{item['year']}")


async def adventure_anime(call: types.CallbackQuery):
    items = parser_adventure()
    for item in items:
        await bot.send_message(call.from_user.id, f"{item['link']}\n\n"
                                                  f"{item['title']}\n"
                                                  f"{item['length']}\n"
                                                  f"#{item['country']}\n"
                                                  f"#year_{item['year']}")


async def everyday_anime(call: types.CallbackQuery):
    items = parser_everyday()
    for item in items:
        await bot.send_message(call.from_user.id, f"{item['link']}\n\n"
                                                  f"{item['title']}\n"
                                                  f"{item['length']}\n"
                                                  f"#{item['country']}\n"
                                                  f"#year_{item['year']}")


async def romance_anime(call: types.CallbackQuery):
    items = parser_romance()
    for item in items:
        await bot.send_message(call.from_user.id, f"{item['link']}\n\n"
                                                  f"{item['title']}\n"
                                                  f"{item['length']}\n"
                                                  f"#{item['country']}\n"
                                                  f"#year_{item['year']}")


async def sport_anime(call: types.CallbackQuery):
    items = parser_sport()
    for item in items:
        await bot.send_message(call.from_user.id, f"{item['link']}\n\n"
                                                  f"{item['title']}\n"
                                                  f"{item['length']}\n"
                                                  f"#{item['country']}\n"
                                                  f"#year_{item['year']}")


async def detective_anime(call: types.CallbackQuery):
    items = parser_detectives()
    for item in items:
        await bot.send_message(call.from_user.id, f"{item['link']}\n\n"
                                                  f"{item['title']}\n"
                                                  f"{item['length']}\n"
                                                  f"#{item['country']}\n"
                                                  f"#year_{item['year']}")


async def horror_anime(call: types.CallbackQuery):
    items = parser_horrors()
    for item in items:
        await bot.send_message(call.from_user.id, f"{item['link']}\n\n"
                                                  f"{item['title']}\n"
                                                  f"{item['length']}\n"
                                                  f"#{item['country']}\n"
                                                  f"#year_{item['year']}")


def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == '1button')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == '2button')
    dp.register_callback_query_handler(delete_mentor, lambda call: call.data.startswith('Delete '))
    dp.register_callback_query_handler(comedy_anime, lambda call: call.data == 'comedy_button')
    dp.register_callback_query_handler(fantasy_anime, lambda call: call.data == 'fantasy_button')
    dp.register_callback_query_handler(adventure_anime, lambda call: call.data == 'adventure_button')
    dp.register_callback_query_handler(everyday_anime, lambda call: call.data == 'everyday_button')
    dp.register_callback_query_handler(romance_anime, lambda call: call.data == 'romance_button')
    dp.register_callback_query_handler(sport_anime, lambda call: call.data == 'sport_button')
    dp.register_callback_query_handler(detective_anime, lambda call: call.data == 'detectives_button')
    dp.register_callback_query_handler(horror_anime, lambda call: call.data == 'horrors_button')

