from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

storage = MemoryStorage()

#Токен бота
bot = Bot(token="5305638021:AAEW69hy3rstaidolehzj7DNPgDcbXqFkqU")
# Диспетчер для бота
dp = Dispatcher(bot, storage=MemoryStorage())