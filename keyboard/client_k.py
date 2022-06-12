from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bs = KeyboardButton('Поиск клипов\U0001F50E')
b1 = KeyboardButton('Жанр\U0001F3AD')
b2 = KeyboardButton('Исполнитель\U0001F60E')
b3 = KeyboardButton('Песня\U0001F3B5')
b4 = KeyboardButton('Альбом\U0001F4C1')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(bs).add(b1).insert(b2).add(b3).insert(b4)
