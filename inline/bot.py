import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from datetime import datetime

TOKEN = "7582468943:AAHjgqxeUYBhXmjlEcW-1aXdS0XKuXs04Kw"
bot = Bot(token=TOKEN)
dp = Dispatcher()
# Inline keyboard
main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Sana va Vaqt", callback_data="get_time")],
    [InlineKeyboardButton(text="Lokations", callback_data="get_info")],
    [InlineKeyboardButton(text="Help", callback_data="help")]
])





@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Salom! Quyidagilardan birini tanlang ", reply_markup=main_menu)

"""Inline tugmalar yordamida foydalanuvchi tanlovini amalga oshirish uchun"""
@dp.callback_query()
async def callback_query(callback: CallbackQuery):
    data = callback.data
    if data == "get_time":
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await callback.message.answer("Bugungi sana va vaqt: " + now,
                                      parse_mode=ParseMode.MARKDOWN)

    elif data == "get_info":
        await callback.message.answer_location(latitude=41.311081, longitude=69.240562)
        await callback.message.answer("Bu Toshkent shahrining joylashuvi")

    elif data == "help":
        await callback.message.answer("Bu bot yordamida sana va vaqtni, joylashuvni "
                                      "ko'rishingiz mumkin.",
                                      parse_mode=ParseMode.MARKDOWN)

    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
