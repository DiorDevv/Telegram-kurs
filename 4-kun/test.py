from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import F

import asyncio
import logging
import os

# Tokeningizni shu yerga yozing
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Bot va dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Klaviatura (butonlar)
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Dars haqida")],
        [KeyboardButton(text="📅 Bugungi reja")],
        [KeyboardButton(text="❓ Savollar va Javoblar")],
        [KeyboardButton(text="📞 Admin bilan bog‘lanish")]
    ],
    resize_keyboard=True
)

# Boshlanish komandasi
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Salom! 👋 Bu bot orqali siz kerakli ma'lumotlarga osongina ega bo‘lasiz.", reply_markup=menu)

# Tugmalar uchun javoblar
@dp.message(F.text == "📚 Dars haqida")
async def lesson_info(message: types.Message):
    await message.answer("📚 Bugungi dars mavzusi: Telegram botlar bilan ishlash. Aiogram kutubxonasi asoslari.")

@dp.message(F.text == "📅 Bugungi reja")
async def plan(message: types.Message):
    await message.answer("📅 Reja:\n1. Aiogram o‘rnatish\n2. Tugmalar bilan ishlash\n3. Inline tugmalar\n4. Callback funksiyalar")

@dp.message(F.text == "❓ Savollar va Javoblar")
async def faq(message: types.Message):
    await message.answer("❓Savollar bo‘lsa, shu yerga yozing. O‘qituvchi imkon qadar tez javob beradi.")

@dp.message(F.text == "📞 Admin bilan bog‘lanish")
async def contact_admin(message: types.Message):
    await message.answer("📞 Admin: @your_username")

# Botni ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
