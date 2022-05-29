from aiogram.utils import executor
from create import dp
from data import search

search.firebase_start()

async def on_startup(_):
    print('bot is online')


from handlers import client, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
