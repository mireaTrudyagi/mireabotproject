#Тестовые модули:
# Песня: Film
# Исполнитель: Daft Punk
# Жанр: Поп
# Альбом: The works
import logging
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor
from aiogram.types import BotCommand
from Messages import register_handlers_song
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

logger = logging.getLogger(__name__)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/song", description="Найти песню"),
        BotCommand(command="/artist", description="Найти исполнителя"),
        BotCommand(command="/genre", description="Поиск по жанру"),
        BotCommand(command="/album", description="Найти альбом")
    ]
    await bot.set_my_commands(commands)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")
    storage = MemoryStorage()
    # Токен бота
    bot = Bot(token="5305638021:AAEW69hy3rstaidolehzj7DNPgDcbXqFkqU")
    # Диспетчер для бота
    dp = Dispatcher(bot, storage=MemoryStorage())

    await set_commands(bot)

    @dp.message_handler(commands=['help', 'start'])
    async def cmd_start(message: types.Message):
        await message.answer("Привет! Я музыкальный бот. В данный момент доступны такие команды: /song, /artist, /genre, /album")
    register_handlers_song(dp)

    await dp.start_polling()
if __name__ == "__main__":
    # Запуск бота
    asyncio.run(main())
