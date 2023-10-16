from telebot import types

def app_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    app_button = types.KeyboardButton('Выбрать персонажа')

    kb.add(app_button)

    return kb