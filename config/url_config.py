import os

from dotenv import load_dotenv

load_dotenv()

GOOGLE_MAIL_REGISTER_URL = os.getenv('GOOGLE_MAIL_REGISTER_URL') # Адрес регистрации гугл почты
OZON_URL = os.getenv('OZON_URL')
