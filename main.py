from telethon import TelegramClient
from utils.config import API_ID, API_HASH
from utils.messages import send_message
import asyncio

client = TelegramClient('session_name', API_ID, API_HASH)

async def main():
    # Подключение
    await client.start()

    # Отправка тестового сообщения
    await send_message(client, 'me', 'test')

    
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())