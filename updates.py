import requests
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = 849291610
TEXT = 'text'

if not BOT_TOKEN:
    raise ValueError("Токен не найден! Проверь файл .env")

API_URL = 'https://api.telegram.org/bot'

response = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates')

if response.status_code == 200:
    print(response.json())
else:
    print(f'Ошибка: {response.status_code}')
