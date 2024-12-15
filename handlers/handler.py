from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from database.requests import init_db, add_task, get_tasks, update_task_status, delete_task

handlers_router = Router()


init_db()


@handlers_router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        f"Привіт! Це TODO APP бот 🔥, який допоможе тобі спланувати свій день 💼 та впорядкувати твої задачі🚀!")


@handlers_router.message(Command("create"))
async def create(message: Message):
    task_data = message.text[8:].strip()

    if ':' not in task_data:
        await message.answer("Формат задачі повинен бути: Назва задачі: Опис задачі.")
        return

    task_title, task_description = task_data.split(':', 1)
    task_title = task_title.strip()
    task_description = task_description.strip()


    add_task(task_title, task_description)

    await message.answer(f"Задача додана: {task_title} - {task_description}")


@handlers_router.message(Command("show"))
async def show(message: Message):
    tasks = get_tasks()

    if not tasks:
        await message.answer('У вас немає задач☔️! Додайте задачі за допомогою /create.')
        return

    response = "Ваші задачі:\n"
    for task in tasks:
        response += f"{task[0]} - {task[1]} (Статус: {task[2]})\n"

    await message.answer(response)


@handlers_router.message(Command("edit"))
async def edit(message: Message):
    task_data = message.text[6:].strip()

    if ':' not in task_data:
        await message.answer("Формат задачі повинен бути: Назва задачі: Опис задачі.")
        return

    task_title, new_task_description = task_data.split(':', 1)
    task_title = task_title.strip()
    new_task_description = new_task_description.strip()


    update_task_status(task_title, new_task_description)

    await message.answer(f"Задача '{task_title}' була успішно оновлена на: {new_task_description}")


@handlers_router.message(Command("delete"))
async def delete(message: Message):
    task_data = message.text[8:].strip()

    if ':' not in task_data:
        await message.answer("Формат задачі повинен бути: Назва задачі: Опис задачі.")
        return

    task_title = task_data.split(':', 1)[0].strip()


    delete_task(task_title)

    await message.answer(f"Задача '{task_title}' була успішно видалена!")


@handlers_router.message(Command("mark"))
async def mark_task(message: Message):
    command_data = message.text[6:].strip()

    if ' ' not in command_data:
        await message.answer("Формат повинен бути: /mark <статус> <назва_задачі>")
        return

    status, task_title = command_data.split(' ', 1)
    task_title = task_title.strip()

    if status not in ["виконано", "в процесі", "пізніше"]:
        await message.answer("Невірний статус! Доступні статуси: 'виконано', 'в процесі', 'пізніше'.")
        return


    update_task_status(task_title, status)

    await message.answer(f"Статус задачі '{task_title}' було оновлено на '{status}'!")









