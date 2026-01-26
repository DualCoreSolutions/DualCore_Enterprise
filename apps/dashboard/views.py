# apps/dashboard/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from xhtml2pdf import pisa
from apps.website.models import Orcamento

class DashboardIndexView(LoginRequiredMixin, TemplateView):
    """View principal do Dashboard com contagem para os Gráficos"""
    template_name = 'dashboard/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 1. Dados para a tabela e os cards de resumo
        orçamentos = Orcamento.objects.all().order_by('-data_envio')
        context['orçamentos'] = orçamentos
        context['pendentes'] = Orcamento.objects.filter(status='pendente').count()

        # 2. Lógica para os Gráficos (Agrupamento por tipo de serviço)
        stats = Orcamento.objects.values('servico').annotate(total=Count('servico'))
        
        # Mapeamento para transformar siglas (infra) em nomes bonitos (Infraestrutura de Redes)
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
    """Função que gera o arquivo PDF (O trabalho que havia sumido)"""
    # 1. Busca o orçamento específico pelo ID (pk)
    orcamento = get_object_or_404(Orcamento, pk=pk)
    
    # 2. Prepara o template do PDF
    template_path = 'dashboard/pdf_template.html'
    context = {'orcamento': orcamento}
    
    # 3. Cria a resposta do navegador como um arquivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Orcamento_{orcamento.nome}.pdf"'
    
    # 4. Converte o HTML em PDF usando a biblioteca pisa
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    # 5. Se der erro na conversão, avisa o usuário
    if pisa_status.err:
       return HttpResponse('Erro ao gerar o PDF do orçamento.', status=400)
       
    return response