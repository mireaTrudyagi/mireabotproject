from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Жанр')
b2 = KeyboardButton('Исполнитель')
b3 = KeyboardButton('Песня')
b4 = KeyboardButton('Альбом')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).insert(b2).add(b3).insert(b4)
