from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from database.bot_db import sql_command_insert
from buttons.keyboard_buttons import submit_markup


class FSMAdmin(StatesGroup):
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in ADMIN:
        await FSMAdmin.name.set()
        await message.answer("Как звать?")
    else:
        await message.answer("Недостаточно прав!")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.message_id
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
    await message.answer(f"Имя => {data['name']}\n"
                         f"Направление => {data['direction']}\n"
                         f"Возраст => {data['age']}\n"
                         f"Группа => {data['group']}")
    await FSMAdmin.next()
    await message.answer('Всё верно?', reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Ментор добавлен в базу")
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer("Отменено")
    else:
        await message.answer("Не понял")


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено')


def register_fsm_admin_handler(dp: Dispatcher):
    dp.register_message_handler(cancel, state='*', commands=['cancel'])
    dp.register_message_handler(fsm_start, commands=['add_men'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
