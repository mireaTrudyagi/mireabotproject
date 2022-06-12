from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Scaled And Icy\U0001F432')
b2 = KeyboardButton('Главное меню\U0001F3E0')

kb_album = ReplyKeyboardMarkup(resize_keyboard=True)

kb_album.add(b1).add(b2)
