import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from datetime import datetime

TOKEN = "7582468943:AAHjgqxeUYBhXmjlEcW-1aXdS0XKuXs04Kw"  # Tokeningizni shu yerga yozing

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Inline tugmalar
main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🕐 Sana va vaqt", callback_data="datetime")],
    [InlineKeyboardButton(text="📍 Lokatsiya", callback_data="location")],
    [InlineKeyboardButton(text="🤖 Bot haqida", callback_data="about")]
])

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Assalomu alaykum! Quyidagilardan birini tanlang:",
        reply_markup=main_menu
    )

@dp.callback_query()
async def callback_handler(callback: CallbackQuery):
    data = callback.data

    if data == "datetime":
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await callback.message.answer(f"📅 Bugungi sana va vaqt:\n`{now}`", parse_mode=ParseMode.MARKDOWN)

    elif data == "location":
        await callback.message.answer_location(latitude=41.311081, longitude=69.240562)
        await callback.message.answer("📍 Bu Toshkentning markazi!")

    elif data == "about":
        await callback.message.answer(
            "🤖 Bu bot `aiogram` yordamida yaratilgan.\nInline tugmalar orqali interaktiv imkoniyatlar taqdim etiladi.",
            parse_mode=ParseMode.MARKDOWN
        )

    await callback.answer()

# Main loop
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
