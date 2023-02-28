import requests

from settings import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN, TELEGRAM_URL


def send_message(dir_name):
    text = f'No han llegado nuevos ficheros al directorio {dir_name} en los últimos 10 minutos'
    url = (
        f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={text}'
    )

    print(url)

    req = requests.post(url)

    if req.status_code >= 300:
        raise Exception(req.content)
