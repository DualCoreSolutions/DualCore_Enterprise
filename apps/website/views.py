from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Orcamento
from .forms import OrcamentoForm

class IndexView(TemplateView):
    template_name = 'website/index.html'

class OrcamentoCreateView(CreateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'website/orcamento.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Solicitação enviada com sucesso! Entraremos em contato em breve.")
        return super().form_valid(form)