from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from config import owner_id

router = Router()

@router.message(Command("admin"))
async def cmd_admin(message: Message):
    if message.from_user.id != owner_id:
        return
    
    await message.answer("Привет, Администратор!")
    

