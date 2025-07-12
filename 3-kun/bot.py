# pip install aiogram aiohttp python-dotenv
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from weather import get_weather

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Logging
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Salom! 🌤\nShahar nomini yuboring va men sizga ob-havoni aytaman.")

@dp.message()
async def weather_handler(message: Message):
    city = message.text.strip()
    weather_info = await get_weather(city)
    await message.answer(weather_info)

if __name__ == "__main__":
    import asyncio
    async def main():
        await dp.start_polling(bot)

    asyncio.run(main())
