from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = True # 추후에 False로 변경 예정

ALLOWED_HOSTS = [
    '.compute.amazonaws.com',
    'a0c208cd3ea0.ngrok.io'
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')