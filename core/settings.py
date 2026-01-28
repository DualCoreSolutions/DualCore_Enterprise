import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url  # Importante para o banco de dados de produção

# Carrega as variáveis do arquivo .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# --- SEGURANÇA ---
# Em produção, a SECRET_KEY deve estar obrigatoriamente no .env
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-mude-isso-em-producao')

# O DEBUG deve ser False em produção. No seu .env, coloque DEBUG=True para testar localmente.
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Domínios permitidos (Render, Railway e locais)
ALLOWED_HOSTS = [
    '127.0.0.1', 
    'localhost', 
    '.render.com', 
    '.railway.app', 
    'dualcoresolutions.tech' # Substitua pelo seu domínio futuro
]

# --- APPS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # App para gerir estáticos em produção
    'whitenoise.runserver_nostatic', 
    
    # Apps da DualCore Solutions
    'apps.website',
    'apps.accounts',
    'apps.dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # DEVE vir logo após o SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'

# --- BANCO DE DADOS ---
# Se houver uma variável DATABASE_URL (comum em servidores de produção), ele usa ela (PostgreSQL)
# Caso contrário, usa o SQLite local para desenvolvimento.

# No core/settings.py, por volta da linha 80

db_url = os.getenv('DATABASE_URL')

if db_url and db_url.startswith('postgres'):
    DATABASES = {
        'default': dj_database_url.config(
            default=db_url, 
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# --- VALIDAÇÃO DE SENHA ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- LOCALIZAÇÃO E IDIOMA ---
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# --- ARQUIVOS ESTÁTICOS E MÍDIA ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Pasta onde o Django reunirá todos os arquivos estáticos para o servidor
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Otimização do WhiteNoise para comprimir arquivos CSS/JS
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- AUTENTICAÇÃO E REDIRECIONAMENTO ---
AUTH_USER_MODEL = 'accounts.CustomUser'
LOGIN_REDIRECT_URL = 'dashboard' 
LOGOUT_REDIRECT_URL = 'login'

# --- CONFIGURAÇÃO DE E-MAIL REAL (GMAIL SMTP) ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')

DEFAULT_FROM_EMAIL = f"DualCore Solutions <{os.getenv('EMAIL_USER')}>"