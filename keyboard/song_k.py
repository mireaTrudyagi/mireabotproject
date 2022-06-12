from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Enemy\U0001F480')
b2 = KeyboardButton('Shape of You\U0001F498')
b3 = KeyboardButton('The Nights\U0001F319')
b4 = KeyboardButton('Youre Gonna Go Far, Kid\U0001F92C')
b5 = KeyboardButton('Dynamite\U0001F4A5')
b6 = KeyboardButton('Главное меню\U0001F3E0')

kb_song = ReplyKeyboardMarkup(resize_keyboard=True)

kb_song.add(b1).insert(b2).add(b3).insert(b4).insert(b5).add(b6)
