import sqlite3
import random
from aiogram import types


def sql_creat():
    global db, cursor
    db = sqlite3.connect('Bot.sqlite3')
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(id INTEGER PRIMARY KEY, name TEXT, "
               "direction TEXT, age INTEGER, "
               "groupe TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_backend(message):
    result = cursor.execute('SELECT * FROM mentors WHERE direction="Backend"').fetchall()
    random_mentor = random.choice(result)
    await message.answer(f"Имя => {random_mentor[1]}\n"
                         f"Направление => {random_mentor[2]}\n"
                         f"Возраст => {random_mentor[3]}\n"
                         f"Группа => {random_mentor[4]}")
    db.commit()


async def sql_command_frontend(message):
    result = cursor.execute('SELECT * FROM mentors WHERE direction="Frontend"').fetchall()
    random_mentor = random.choice(result)
    await message.answer(f"Имя => {random_mentor[1]}\n"
                         f"Направление => {random_mentor[2]}\n"
                         f"Возраст => {random_mentor[3]}\n"
                         f"Группа => {random_mentor[4]}")
    db.commit()


async def sql_command_android(message):
    result = cursor.execute('SELECT * FROM mentors WHERE direction="Android"').fetchall()
    random_mentor = random.choice(result)
    await message.answer(f"Имя => {random_mentor[1]}\n"
                         f"Направление => {random_mentor[2]}\n"
                         f"Возраст => {random_mentor[3]}\n"
                         f"Группа => {random_mentor[4]}")
    db.commit()


async def sql_command_ios(message):
    result = cursor.execute('SELECT * FROM mentors WHERE direction="Ios"').fetchall()
    random_mentor = random.choice(result)
    await message.answer(f"Имя => {random_mentor[1]}\n"
                         f"Направление => {random_mentor[2]}\n"
                         f"Возраст => {random_mentor[3]}\n"
                         f"Группа => {random_mentor[4]}")
    db.commit()


async def sql_command_all_mentors():
    return cursor.execute("SELECT * FROM mentors")


async def sql_command_delete_mentor(id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (id,))
    db.commit()
