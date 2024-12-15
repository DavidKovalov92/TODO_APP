from aiogram import Bot, Dispatcher
import asyncio
from handlers.handler import handlers_router
import logging


from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_BOT = os.getenv('TOKEN_BOT')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



bot = Bot(TOKEN_BOT)
dp = Dispatcher()

dp.include_router(handlers_router)

async def main():
    logger.info("Бот запускається...")
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())