import logging
import asyncio

from app.db.database import init_database
from app.bot.main import run_bot
from app.db.repository import DatabaseRepository
from app.pay.repository import PayRepository

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    init_database()
    asyncio.run(run_bot())
