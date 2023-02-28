TELEGRAM_TOKEN = ''
TELEGRAM_CHAT_ID = ''
TELEGRAM_URL = "https://api.telegram.org/bot"

MAIN_DIRS = []

# Local settings
try:
    from local_settings import *
except Exception:
    pass
