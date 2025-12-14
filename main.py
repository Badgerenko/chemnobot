import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import F

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def echo(message: Message):
    await message.answer("✅ Бот працює")

async def on_startup():
    print("Bot started!")

dp.startup.register(on_startup)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
