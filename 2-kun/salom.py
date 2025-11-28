from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio

API_TOKEN = "8192874862:AAFp8EyJHxEl2TZzETXD2LrS3ffh3ecR_nE"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# /start komandasi
@dp.message(CommandStart())
async def start(message: types.Message):
    username = message.from_user.username
    if username:
        await message.answer(f"Salom, @{username}!")
    else:
        await message.answer("Salom, foydalanuvchi!")



# Ishga tushirish
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
