from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Жанр\U0001F3AD')
b2 = KeyboardButton('Исполнитель\U0001F60E')
b3 = KeyboardButton('Песня\U0001F3B5')
b4 = KeyboardButton('Альбом\U0001F4C1')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b2).add(b3).insert(b4)
