from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from config import owner_id
from ..keyboards.admin import main_menu_kb

router = Router()

@router.message(Command("admin"))
async def cmd_admin(message: Message):
    if message.from_user.id != owner_id:
        return
    
    await message.answer("Привет, Администратор!")
    

@router.callback_query(F.data.startswith("button"))
async def handle_buttons(callback: CallbackQuery):
    button_number = callback.data.replace("button", "")
    
    if button_number == "1":
        try:
            await callback.message.edit_text(
            "Вы нажали кнопку 1.",
            reply_markup=main_menu_kb
        )
            await callback.answer()
        except Exception:
            await callback.answer()

    elif button_number == "2":
        await callback.answer("Вы нажали кнопку 2", show_alert=False)

    elif button_number == "3":
        await callback.answer("Вы нажали кнопку 3", show_alert=True)