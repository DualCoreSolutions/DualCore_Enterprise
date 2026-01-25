from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='E-mail')
    bio = models.TextField(blank=True, verbose_name='Biografia')
    
    # Validador: Aceita de 10 a 15 dígitos numéricos
    telefone_validator = RegexValidator(
        regex=r'^\d{10,15}$',
        message="O número de telefone deve conter apenas dígitos (10 a 15 caracteres)."
    )
    
    telefone = models.CharField(
        max_length=15, 
        validators=[telefone_validator], 
        blank=True, 
        null=True
    )
    is_client = models.BooleanField(default=False, verbose_name='É Cliente?')

    def __str__(self):
        return self.username