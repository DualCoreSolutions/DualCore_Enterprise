from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='E-mail')
    bio = models.TextField(blank=True, verbose_name='Biografia')
    telefone = models.CharField(max_length=15, blank=True, null=True)
    is_client = models.BooleanField(default=False, verbose_name='É Cliente?')

    def __str__(self):
        return self.username