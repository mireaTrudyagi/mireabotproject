from aiogram import types, Dispatcher
from create import dp, bot

@dp.message_handler()
async def echo(message : types.Message):
    if message.text == 'Hello':
        await message.answer('Hey, how r u?')

def reg_other(dp : Dispatcher):
    dp.register_message_handler(echo)