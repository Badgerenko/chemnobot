import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def echo(message: Message):
    await message.answer("✅ Бот працює")

async def main():
    dp.startup.register(lambda _: print("Bot started!"))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
