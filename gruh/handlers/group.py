from aiogram import Dispatcher, F
from aiogram.types import Message, ChatMemberUpdated
from aiogram.filters import ChatMemberUpdatedFilter, Command
from aiogram.enums.chat_member_status import ChatMemberStatus

# Guruhga kirganda salomlashadi
async def on_user_join(message: Message):
    for user in message.new_chat_members:
        await message.reply(f"👋 Xush kelibsiz, {user.full_name}!")

# Faqat adminlar ishlatishi mumkin bo‘lgan buyruq
async def admin_only_command(message: Message):
    member = await message.chat.get_member(message.from_user.id)
    if member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        await message.reply("✅ Siz adminsiz, bu buyruq bajarildi.")
    else:
        await message.reply("❌ Bu buyruq faqat adminlar uchun!")

def register_group_handlers(dp: Dispatcher):
    dp.message.register(on_user_join, F.new_chat_members)
    dp.message.register(admin_only_command, Command("admin"))
