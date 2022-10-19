from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
import random


class FSMAdmin(StatesGroup):

    name = State()
    direction = State()
    age = State()
    group = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in ADMIN:
        await FSMAdmin.name.set()
        await message.answer("Как звать?")
    else:
        await message.answer("Недостаточно прав!")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.message_id
        # lst = []
        # k = random.randint(100000, 999999)
        # while k in lst:
        #     k = random.randint(100000, 999999)
        # lst.append(k)
        # data['id'] = k
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Направление")


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Возраст")


async def load_age(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("Группа")
    except ValueError:
        await message.answer("Вводить только цифрами!")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await state.finish()
    await message.answer("Ментор добавлен в базу")
    print(data)


def register_fsm_admin_handler(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['add_mentor'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
