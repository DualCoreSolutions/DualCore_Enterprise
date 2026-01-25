from django import forms
from .models import Orcamento

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['nome', 'email', 'servico', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu@email.com'}),
            'servico': forms.Select(),
            'mensagem': forms.Textarea(attrs={'placeholder': 'Descreva brevemente o que você precisa...', 'rows': 5}),
        }
        