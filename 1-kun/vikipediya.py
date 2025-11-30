import logging
import wikipedia
import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

# Tokenni kiriting
API_TOKEN = "8192874862:AAFp8EyJHxEl2TZzETXD2LrS3ffh3ecR_nE"

wikipedia.set_lang("uz")
logging.basicConfig(level=logging.INFO)

# Aiogram v3.7.0+ uchun to'g'ri Bot yaratish
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)


dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: Message):
    await message.answer("👋 Assalomu alaykum!\nWikipedia botiga xush kelibsiz!\nShunchaki mavzu yozing.")

@dp.message(F.text)
async def send_wiki(message: Message):
    try:
        result = wikipedia.summary(message.text, sentences=3)
        if len(result) > 4096:
            for x in range(0, len(result), 4096):
                await message.answer(result[x:x+4096])
        else:
            await message.answer(result)
    except wikipedia.exceptions.DisambiguationError as e:
        await message.answer(f"🔍 Juda ko'p natija topildi. Aniqlashtiring.\nMisol: {e.options[0]}")
    except wikipedia.exceptions.PageError:
        await message.answer("❌ Maqola topilmadi.")
    except Exception as e:
        logging.exception("Xatolik yuz berdi:")
        await message.answer("⚠️ Noma'lum xatolik. Keyinroq urinib ko‘ring.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
