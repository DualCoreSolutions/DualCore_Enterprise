from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # Campos que aparecem no registo inicial
        fields = ('username', 'email', 'telefone')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # Campos que aparecem na edição do perfil no dashboard
        fields = ('email', 'telefone', 'bio')