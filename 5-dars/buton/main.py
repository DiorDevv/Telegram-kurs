import asyncio
from aiogram import Bot, Dispatcher
from handlers import register_handlers
from aiogram.enums import ParseMode

# Tokeningizni shu yerga yozing
TOKEN = "7582468943:AAHjgqxeUYBhXmjlEcW-1aXdS0XKuXs04Kw"

async def main():
    # Bot va Dispatcher obyektlarini yaratish
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    # Handlerlarni ro'yxatdan o'tkazish
    register_handlers(dp)

    # Pollingni boshlash
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
