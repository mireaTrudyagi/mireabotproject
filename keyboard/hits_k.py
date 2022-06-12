from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Главное меню\U0001F3E0')

kb_hits = ReplyKeyboardMarkup(resize_keyboard=True)

kb_hits.add(b1)
