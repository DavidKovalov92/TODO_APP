import sqlite3



def init_db():
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'в процесі',
        reminder_time TEXT
    )
    ''')

    connection.commit()
    connection.close()



def add_task(title, description):
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO tasks (title, description)
    VALUES (?, ?)
    ''', (title, description))

    connection.commit()
    connection.close()



def get_tasks():
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()

    connection.close()
    return tasks



def update_task_status(title, status):
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()

    cursor.execute('''
    UPDATE tasks
    SET status = ?
    WHERE title = ?
    ''', (status, title))

    connection.commit()
    connection.close()


def delete_task(title):
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()

    cursor.execute('''
    DELETE FROM tasks WHERE title = ?
    ''', (title,))

    connection.commit()
    connection.close()



def update_task_reminder(title, reminder_time):
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()

    cursor.execute('''
    UPDATE tasks
    SET reminder_time = ?
    WHERE title = ?
    ''', (reminder_time, title))

    connection.commit()
    connection.close()
