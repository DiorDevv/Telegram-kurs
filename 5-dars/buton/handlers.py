from aiogram import Dispatcher, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from datetime import datetime
from keyboards import main_menu

import random

def register_handlers(dp: Dispatcher):

    @dp.message(CommandStart())
    async def start_handler(message: Message):
        await message.answer(
            "👋 Assalomu alaykum! Iltimos, quyidagilardan birini tanlang:",
            reply_markup=main_menu()
        )

    @dp.callback_query()
    async def callback_handler(callback: CallbackQuery):
        data = callback.data

        if data == "datetime":
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            await callback.message.answer(f"📅 Sana va vaqt:\n`{now}`", parse_mode="Markdown")

        elif data == "location":
            await callback.message.answer_location(latitude=41.311081, longitude=69.240562)
            await callback.message.answer("📍 Bu — Toshkent markazi.")

        elif data == "about":
            await callback.message.answer("🤖 Bu bot `aiogram` kutubxonasi yordamida tuzilgan.")

        elif data == "random":
            number = random.randint(1, 100)
            await callback.message.answer(f"🎲 Tasodifiy son: {number}")

        elif data == "back":
            await callback.message.answer("🔙 Menyuga qaytdingiz:", reply_markup=main_menu())

        await callback.answer()
