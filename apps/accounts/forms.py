from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # Campos que aparecem no cadastro
        fields = ('username', 'email', 'telefone')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # Campos que aparecem na edição do admin
        fields = ('username', 'email', 'telefone', 'bio', 'is_client')