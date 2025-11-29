import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

# Tokeningizni shu yerga yozing
TOKEN = "YOUR_BOT_TOKEN"

# Bot va dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()


# Tugmalar (butonlar)
buttons = [
    [KeyboardButton(text="🔘 1-Button - Oddiy Matn")],
    [KeyboardButton(text="📌 2-Button - Havola berish")],
    [KeyboardButton(text="📷 3-Button - Rasm yuborish")],
    [KeyboardButton(text="❓ 4-Button - Savol-javob")]
]


menu = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "👋 Salom! Bu bot 4 ta tugma orqali qanday funksiyalarni bajarish mumkinligini ko'rsatadi.",
        reply_markup=menu
    )


@dp.message()
async def message_handler(message: Message):
    text = message.text

    if text == "🔘 1-Button - Oddiy Matn":
        await message.answer("Bu tugma oddiy matn yuboradi. Masalan, salom, qanday yuribsiz?")

    elif text == "📌 2-Button - Havola berish":
        await message.answer(
            "Bu tugma foydalanuvchiga havola yuboradi: [OpenAI sayti](https://openai.com)",
            parse_mode=ParseMode.MARKDOWN
        )

    elif text == "📷 3-Button - Rasm yuborish":
        await message.answer_photo(
            photo="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Aiogram_logo.svg/640px-Aiogram_logo.svg.png",
            caption="Bu tugma rasm yuboradi."
        )

    elif text == "❓ 4-Button - Savol-javob":
        await message.answer("Savol: Python dasturlash tilining yaratuvchisi kim?\n\nJavob: Guido van Rossum.")

    else:
        await message.answer("Iltimos, menyudan biror tugmani tanlang.")


# Main
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
