import sqlite3

#Подключение к базе данных
connection = sqlite3.connect('data.db', check_same_thread=False)

#Связь между Python и SQL
sql = connection.cursor()

#Создание таблицы пользователей
sql.execute('CREATE TABLE IF NOT EXISTS users'
            '(id INTEGER,'
            'username TEXT,'
            'name TEXT);')

#Регистрация
def register(id, name):
    sql.execute('INSERT INTO users VALUES (?, ?);',
                (id, name))
    #Фиксируем изменения
    connection.commit()
    connection.close()

#Проверка на регистрацию
def checker(id):
    check = sql.execute('SELECT id FROM users WHERE id=?;', (id,))

    if check.fetchone():
        return True
    else:
        return False


