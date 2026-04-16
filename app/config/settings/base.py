import os
from pathlib import Path
import environ

# 1. Rutas
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
# Busca el .env en la raíz (un nivel arriba de /app)
environ.Env.read_env(os.path.join(BASE_DIR.parent, '.env'))

# 2. Seguridad Básica
SECRET_KEY = env('SECRET_KEY', default='django-insecure-key-charleston-2026')
DEBUG = env.bool('DEBUG', default=False)

# 3. Definición de Apps (Arquitectura Modular)
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_prometheus',
    'drf_spectacular',
]

LOCAL_APPS = []  # Aquí irán tus módulos como 'modules.patients'

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# 4. Middlewares (Orden Crítico)
MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Requerido por Admin
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Requerido por Admin
    'django.contrib.messages.middleware.MessageMiddleware',  # Requerido por Admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ROOT_URLCONF = 'config.urls'

# 5. Templates (Lo que causó el error admin.E403)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# 6. Archivos Estáticos
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR.parent, 'static')
