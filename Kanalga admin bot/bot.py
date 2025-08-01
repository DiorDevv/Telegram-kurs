import asyncio
from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN
from handlers import register_handlers

bot = Bot(token=BOT_TOKEN)
db = Dispatcher()


register_handlers(db)




async def main():
    print("Bot started")
    await db.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
