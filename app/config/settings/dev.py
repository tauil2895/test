from .base import *
from datetime import timedelta

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres://app_user:password123@db:5432/app_db')
}

# Configuraciones de JWT para desarrollo
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
