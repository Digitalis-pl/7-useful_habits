import requests
from config.settings import TELEGRAM_BOT_TOKEN


def send_message_in_tg(chat_id, message):
    params = {
        'text': message,
        'chaat_id': chat_id,
    }
    requests.get(f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage', params=params)
