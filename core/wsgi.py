"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Importação necessária para servir arquivos estáticos em produção
try:
    from whitenoise import WhiteNoise
except ImportError:
    WhiteNoise = None

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Inicializa a aplicação Django padrão
application = get_wsgi_application()

# Aplica o WhiteNoise para gerir CSS, JS e Imagens no servidor de produção
if WhiteNoise:
    application = WhiteNoise(application)
    # Define onde os arquivos estáticos coletados estão (configurado no seu settings.py)
    # Isso evita erros de 'failed while running' no Render
    static_root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles')
    if os.path.exists(static_root):
        application.add_files(static_root, prefix='static/')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
