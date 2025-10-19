import logging
import asyncio

from app.db.database import init_database
from app.bot.main import run_bot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    init_database()
    asyncio.run(run_bot())

if __name__ == "__main__":
    main()
