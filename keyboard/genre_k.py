from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Rock\U0001FAA8')
b2 = KeyboardButton('Главное меню\U0001F3E0')

kb_genre = ReplyKeyboardMarkup(resize_keyboard=True)

kb_genre.add(b1).add(b2)
