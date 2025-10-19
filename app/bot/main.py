import logging
from aiogram import Bot, Dispatcher

from .handlers.user import router as user_router
from .handlers.admin import router as admin_router
from config import bot_token

async def run_bot():
    bot = Bot(token=bot_token)
    
    dp = Dispatcher()
    
    dp.include_router(user_router)
    dp.include_router(admin_router)
    
    await dp.start_polling(bot)
