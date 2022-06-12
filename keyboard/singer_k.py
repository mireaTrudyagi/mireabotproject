from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('AJR\U0001F604')
b2 = KeyboardButton('Главное меню\U0001F3E0')

kb_singer = ReplyKeyboardMarkup(resize_keyboard=True)

kb_singer.add(b1).add(b2)
