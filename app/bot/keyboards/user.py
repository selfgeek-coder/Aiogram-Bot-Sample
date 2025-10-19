# Клавиатуры пользователя

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Кнопка 1", callback_data="button1")
        ],
        [
            InlineKeyboardButton(text="Кнопка 2", callback_data="button2")
        ],
        [
            InlineKeyboardButton(text="Кнопка 3", callback_data="button3")
        ]
    ]
)