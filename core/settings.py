"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
# No core/settings.py

# Adicione o domínio do seu site (copiado do painel do Render)
ALLOWED_HOSTS = ['dualcore-enterprise.onrender.com', 'localhost', '127.0.0.1']

# Verifique se o WhiteNoise está no lugar certo nos MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # DEVE ser a segunda linha
    # ... outros middlewares ...
]