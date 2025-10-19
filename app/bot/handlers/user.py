from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from app.db.repository import DatabaseRepository
from app.pay.repository import PayRepository
from ..keyboards.user import main_menu_kb

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Это шаблон для aiogram 3x ботов. Здесь используется платежная система *aiocryptopay* и база данных _sqlite3_",
                         reply_markup=main_menu_kb,
                         parse_mode="Markdown")

@router.callback_query(F.data.startswith("button"))
async def handle_buttons(callback: CallbackQuery):
    button_number = callback.data.replace("button", "")
    
    if button_number == "1":
        await callback.message.edit_text(
            "Вы нажали кнопку 1.",
            reply_markup=main_menu_kb
        )
        
        await callback.answer()

    elif button_number == "2":
        await callback.answer("Вы нажали кнопку 2", show_alert=False)

    elif button_number == "3":
        await callback.answer("Вы нажали кнопку 3", show_alert=True)