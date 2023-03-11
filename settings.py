TELEGRAM_TOKEN = ''
TELEGRAM_CHAT_ID = ''
TELEGRAM_URL = "https://api.telegram.org/bot"

MAIN_DIRS = []
WAIT_TIME = 10  # Time in seconds

# Local settings
try:
    from local_settings import *
except Exception:
    pass
