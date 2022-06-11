from aiogram.utils import executor
from create import dp
from handlers import client
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

client.firebase_start()

async def on_startup(_):
    print('bot is online')

client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
