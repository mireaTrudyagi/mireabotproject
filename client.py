from aiogram import types, Dispatcher
from create import dp, bot

@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.message):
    try:
        await bot.send_message(message.from_user.id, 'Команды:\n\n/song (Песня)\n/singer (Исполнитель)\n/style (Жанр)')
        await message.delete()
    except:
        await message.reply('https://t.me/musicboy')

@dp.message_handler(commands=['song'])
async def search_song(message : types.message):
    await bot.send_message(message.from_user.id, 'Suc1')

@dp.message_handler(commands=['singer'])
async def search_singer(message: types.message):
    await bot.send_message(message.from_user.id, 'Suc2')

@dp.message_handler(commands=['style'])
async def search_style(message: types.message):
    await bot.send_message(message.from_user.id, 'Suc3')


def reg_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(search_song, commands=['song'])
    dp.register_message_handler(search_singer, commands=['singer'])
    dp.register_message_handler(search_style, commands=['style'])