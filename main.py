import requests
from dotenv import load_dotenv
import os
import time

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("Токен не найден!")

API_URL = 'https://api.telegram.org/bot'
# CHAT_ID = 932451561 #z
# CHAT_ID = 849291610 #Улитка

offset = -2
updates: dict
timeout = 20.63


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(
        f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Затрачено времени: {end_time - start_time}')
