from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

genre_markup = InlineKeyboardMarkup()
comedy_button = InlineKeyboardButton('Комедии', callback_data='comedy_button')
fantasy_button = InlineKeyboardButton('Фэнтези', callback_data='fantasy_button')
adventure_button = InlineKeyboardButton('Приключения', callback_data='adventure_button')
everyday_button = InlineKeyboardButton('Повседневность', callback_data='everyday_button')
romance_button = InlineKeyboardButton('Романтические', callback_data='romance_button')
sport_button = InlineKeyboardButton('Спортивные', callback_data='sport_button')
detectives_button = InlineKeyboardButton('Детективы', callback_data='detectives_button')
horrors_button = InlineKeyboardButton('Ужасы', callback_data='horrors_button')

genre_markup.add(horrors_button, detectives_button, sport_button, romance_button,
                 everyday_button, adventure_button, fantasy_button, comedy_button, )
