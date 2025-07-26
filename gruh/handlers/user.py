from aiogram import Dispatcher
from aiogram.types import Message

# Oddiy foydalanuvchi xabari
async def echo_user_message(message: Message):
    if message.chat.type == "private":
        await message.answer(f"Siz yozdingiz: {message.text}")

def register_user_handlers(dp: Dispatcher):
    dp.message.register(echo_user_message)
