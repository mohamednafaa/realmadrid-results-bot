import asyncio
from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()
telegram_token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = Bot(token=telegram_token)

async def send_message(text, chat_id):
    async with bot:
        await bot.send_message(text=text, chat_id=chat_id)

async def run_bot(messages, chat_id):
    text = '\n'.join(messages)
    await send_message(text, chat_id)

#Test messages
messages = [
    'Hola Boss'
]

if messages:
     asyncio.run(run_bot(messages, chat_id))