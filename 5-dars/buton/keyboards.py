from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🕐 Sana va vaqt", callback_data="datetime")],
        [InlineKeyboardButton(text="📍 Lokatsiya", callback_data="location")],
        [InlineKeyboardButton(text="🤖 Bot haqida", callback_data="about")],
        [InlineKeyboardButton(text="🎲 Random son", callback_data="random")],
        [InlineKeyboardButton(text="🔁 Menyuga qaytish", callback_data="back")]
    ])
