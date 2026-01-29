import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# Troque pelos dados que você deseja
username = 'bborges'
email = 'dualcoresolutions.tech@gmail.com'
password = 'Dc17012000'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superusuario {username} criado com sucesso!")
else:
    print("Usuario ja existe.")