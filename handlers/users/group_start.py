from aiogram import types
from loader import dp
from filters.is_group import IsGroup

@dp.message_handler(IsGroup(),commands=['start','help'])
async def start_in_group(message: types.Message):
    await message.reply(f'{message.from_user.first_name} siz guruhdasiz!')