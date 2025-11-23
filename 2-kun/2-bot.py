from aiogram import Bot, Dispatcher, types
import asyncio

# Tokeningizni shu yerga yozing
BOT_TOKEN = "123456789:ABCDEF-your-real-token"

# Bot va dispatcher obyektlari
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



print("nevjen;")

print("Bot ishga tush")








print("Bot ishga tush")


# Har qandaypr
# matnli xabarga ishlovchi funksiya
"""

"""

@dp.message()
async def echo_handler(message: types.Message):
    text = message.text.lower()
    if text == "salom":
        await message.answer("Va alaykum assalom!")
    else:
        await message.answer(f"Siz yozgan matn: {message.text}")
pass




print("Bot ishga tush")
# Botni ishga tushirish funksiyasi
async def main():
    await dp.start_polling(bot)


# Asosiy ishga tushirish
if __name__ == "__main__":
    asyncio.run(main())
# hbwdclj

pass