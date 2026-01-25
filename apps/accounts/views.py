from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') # Depois de cadastrar, manda pro login
    template_name = 'registration/register.html' # Vamos criar esse HTML no passo 4