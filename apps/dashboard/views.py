# apps/dashboard/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin # Importado para segurança
from django.db.models import Count
from xhtml2pdf import pisa
from apps.website.models import Orcamento

class DashboardIndexView(UserPassesTestMixin, TemplateView):
    template_name = 'dashboard/index.html'
    
    # Esta função define QUEM pode ver a página
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    # Se o usuário não tiver permissão, ele é mandado de volta para a Home
    def handle_no_permission(self):
        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Dados para a tabela e os cards
        orçamentos = Orcamento.objects.all().order_by('-data_envio')
        context['orçamentos'] = orçamentos
        context['pendentes'] = Orcamento.objects.filter(status='pendente').count()

        # Dados para os Gráficos
        stats = Orcamento.objects.values('servico').annotate(total=Count('servico'))
        servicos_dict = dict(Orcamento.SERVICOS)
        
        labels = []
        dados = []
        for item in stats:
            label_formatado = servicos_dict.get(item['servico'], item['servico'])
            labels.append(label_formatado)
            dados.append(item['total'])

        context['labels_grafico'] = labels
        context['dados_grafico'] = dados
        return context

def gerar_pdf_orcamento(request, pk):
    # Proteção extra para a função de PDF
    if not request.user.is_staff:
        return HttpResponse("Acesso negado", status=403)

    orcamento = get_object_or_404(Orcamento, pk=pk)
    template_path = 'dashboard/pdf_template.html'
    context = {'orcamento': orcamento}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Orcamento_{orcamento.nome}.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
       return HttpResponse('Erro ao gerar o PDF', status=400)
       
    return response