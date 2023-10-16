import telebot, buttons,db

#Подключение к боту
bot = telebot.TeleBot('6434309590:AAGcWdFu54HxRHkIdOu0XBnqqzAb2pqpVYM')

@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    check_user = db.checker(user_id)
    #Проверка на наличие пользователя в базе данных
    if check_user:
        bot.send_message(user_id, 'Добро пожаловать!', reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, 'Здравствуйте запишите ваше имя!', reply_markup=telebot.types.ReplyKeyboardRemove())
        #Перевести на этап получения имени
        bot.register_next_step_handler(message, get_name)

#Этап получения имени
def get_name(message):
    user_name = message.text
    bot.send_message(user_id, 'Отлично, наш бот предназначен для общения с воображаемым персонажем', reply_markup=buttons.app_button())
    #Перевести на этап получения номера
    bot.register_next_step_handler(message, user_name)

#Запуск бота
bot.polling(non_stop=True)