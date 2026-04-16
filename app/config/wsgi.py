import os
from django.core.wsgi import get_wsgi_application

# Importante: Que apunte a tus nuevos settings de desarrollo
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

application = get_wsgi_application()