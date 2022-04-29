from aiogram.utils import executor
from create import dp


async def on_startup(_):
    print('bot is online')

from things import client, admin, other

client.reg_client(dp)
other.reg_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)