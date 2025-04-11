import requests
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
# CHAT_ID = 1434161192 #Данек
CHAT_ID = 932451561 #z

TEXT = 'Суууууубооооооо'

if not BOT_TOKEN:
    raise ValueError("Токен не найден! Проверь файл .env")


response = requests.get(
    f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={TEXT}')

if response.status_code == 200:
    print(response.json())
else:
    print(f'Ошибка: {response.status_code}')
