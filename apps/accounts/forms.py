from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'telefone')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # Campos que o usuário pode editar no dashboard
        fields = ('email', 'telefone', 'bio')
        