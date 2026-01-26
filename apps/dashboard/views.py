# apps/dashboard/views.py
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.website.models import Orcamento # Certifique-se desta importação

class DashboardIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Busca todos os orçamentos para listar no dashboard
        context['orçamentos'] = Orcamento.objects.all().order_by('-data_envio')
        # Conta quantos estão pendentes para o card de resumo
        context['pendentes'] = Orcamento.objects.filter(status='pendente').count()
        return context