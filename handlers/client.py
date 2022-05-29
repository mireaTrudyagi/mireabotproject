from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import kb_client
from date_base import search

async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Команды:\n\nПесня\nИсполнитель (в работе)\nЖанр (в работе)', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('https://t.me/musicprojectmirea_bot')

async def search_song(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите песню: S1, S2, S3')

async def search_singer(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите исполнителя: (Пока не работает)')

async def search_style(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите стиль: (Пока не работает)')

async def search_album(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите альбом: (Пока не работает)')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(search_song, text=['Песня'])
    dp.register_message_handler(search_singer, text=['Исполнитель'])
    dp.register_message_handler(search_style, text=['Жанр'])
    dp.register_message_handler(search_album, text=['Альбом'])
