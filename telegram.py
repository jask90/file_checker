import logging

import requests

from settings import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN, TELEGRAM_URL, WAIT_TIME


def send_message(dir_name):
    text = (
        "No han llegado nuevos ficheros al directorio"
        f" {dir_name} en los últimos {round((WAIT_TIME / 60), 2)} minutos"
    )
    url = (
        f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage"
        f"?chat_id={TELEGRAM_CHAT_ID}&text={text}"
    )

    req = requests.post(url)

    if req.status_code >= 300:
        logging.error(req.content)
        raise Exception(req.content)
    logging.warning(f"Message sended: {text}")
