from os import getenv
from dotenv import load_dotenv, find_dotenv

from aiogram import Bot, Dispatcher, F

from aiogram.types import Message

load_dotenv(find_dotenv())
BOT_TOKEN = getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(F.text)
async def message(message: Message):
    await message.reply('Ого, это обычное сообщение')


@dp.message(F.photo)
async def message(message: Message):
    await message.reply('Ого, это фотография')


@dp.message(F.sticker)
async def message(message: Message):
    await message.reply('Ого, это стикер')


@dp.message(F.animation)
async def message(message: Message):
    await message.reply('Ого, это гифка')


@dp.message(F.document)
async def message(message: Message):
    await message.reply('Ого, это файл')


@dp.message(F.video)
async def message(message: Message):
    await message.reply('Ого, это видео')


@dp.message(F.voice)
async def message(message: Message):
    await message.reply('Ого, это войс')


@dp.message(F.location)
async def message(message: Message):
    await message.reply('Ого, это местоположение')


@dp.message(F.poll)
async def message(message: Message):
    await message.reply('Ого, это опрос')


if __name__ == '__main__':
    dp.run_polling(bot)
