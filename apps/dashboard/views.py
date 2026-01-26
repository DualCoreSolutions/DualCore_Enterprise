# apps/dashboard/views.py
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from apps.website.models import Orcamento
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orçamentos'] = Orcamento.objects.all().order_by('-data_envio')
        context['pendentes'] = Orcamento.objects.filter(status='pendente').count()
        return context

def gerar_pdf_orcamento(request, pk):
    # 1. Busca os dados do orçamento no banco de dados
    orcamento = get_object_or_404(Orcamento, pk=pk)
    
    # 2. Define o template que será usado para o PDF
    template_path = 'dashboard/pdf_template.html'
    context = {'orcamento': orcamento}
    
    # 3. Prepara a resposta do navegador
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Orcamento_{orcamento.nome}.pdf"'
    
    # 4. Renderiza o HTML e converte para PDF
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
       return HttpResponse('Erro ao gerar PDF', status=400)
    return response