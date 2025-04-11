import requests
from dotenv import load_dotenv
import os
import time

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("Токен не найден!")

API_URL = 'https://api.telegram.org/bot'
# cat = response.json()[0]['url']
API_URL_CAT = 'https://api.thecatapi.com/v1/images/search'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('
API_URL_DOG = 'https://random.dog/woof.json'  # url
API_URL_FOX = 'https://randomfox.ca/floof/'  # image or link

# CHAT_ID = 811061359 #Дарина
# CHAT_ID = 849291610 #Улитка
# CHAT_ID = 932451561 #z

offset = -2
counter = 0
cat_response: requests.Response
cat_link: str

while True:
    print('attempt = ', counter)
    updates = requests.get(
        f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_URL_CAT)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(
                    f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(
                    f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&text={ERROR_TEXT}')
    counter += 1
    time.sleep(1)
'''
cat_response = requests.get(API_URL_CAT)
if cat_response.status_code == 200:
    cat_link = cat_response.json()[0]['url']
    requests.get(
        f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={CHAT_ID}&photo={cat_link}')
else:
    requests.get(
        f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={CHAT_ID}&text={ERROR_TEXT}')
'''
