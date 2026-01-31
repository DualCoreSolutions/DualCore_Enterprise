from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Modelos e Forms
from .models import Orcamento, ServicoPrestado, Projeto
from .forms import OrcamentoForm

class IndexView(TemplateView):
    """
    View principal da DualCore Solutions.
    Busca dados dinâmicos do banco para preencher a Home.
    """
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 1. Busca serviços ativos para a seção de serviços
        context['servicos'] = ServicoPrestado.objects.filter(ativo=True)
        
        # 2. Busca os últimos 6 projetos para a galeria do Portfólio
        # .order_by('-id') garante que os mais novos apareçam primeiro
        context['projetos'] = Projeto.objects.all().order_by('-id')[:6]
        
        return context

class OrcamentoCreateView(CreateView):
    """
    View para solicitação de orçamentos.
    Salva no banco e dispara notificações por e-mail.
    """
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'website/orcamento.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # 1. Salva o orçamento na base de dados (PostgreSQL no Render)
        self.object = form.save()
        
        # 2. Coleta dados para os e-mails
        nome = form.cleaned_data['nome']
        email_cliente = form.cleaned_data['email']
        servico = self.object.get_servico_display()
        mensagem = form.cleaned_data['mensagem']

        # 3. Prepara o conteúdo do e-mail (HTML e Texto simples)
        context_email = {
            'nome': nome, 
            'servico': servico,
            'mensagem': mensagem
        }
        
        # Certifique-se de que este arquivo existe em templates/emails/
        try:
            html_content = render_to_string('emails/confirmacao_orcamento.html', context_email)
            text_content = strip_tags(html_content)
        except:
            html_content = None
            text_content = f"Olá {nome}, recebemos seu pedido de orçamento para {servico}."

        # 4. Envio de Notificações com tratamento de erro
        try:
            # Notificação para a empresa (dualcoresolutions.tech@gmail.com)
            send_mail(
                subject=f"🚀 Novo Orçamento: {servico}", 
                message=f"Olá Equipa DualCore,\n\nO cliente {nome} ({email_cliente}) solicitou um orçamento.\nServiço: {servico}\n\nMensagem: {mensagem}", 
                from_email=settings.DEFAULT_FROM_EMAIL, 
                recipient_list=[settings.DEFAULT_FROM_EMAIL]
            )

            # Resposta Automática para o Cliente
            send_mail(
                subject="Recebemos o seu pedido - DualCore Solutions",
                message=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email_cliente],
                html_message=html_content
            )
        except Exception as e:
            # Registra o erro no console do Render para debug
            print(f"Erro ao enviar e-mails: {e}")

        # 5. Renderiza a página de sucesso com o resumo dos dados
        context_sucesso = {
            'nome': nome,
            'servico': servico,
        }
        return render(self.request, 'website/sucesso.html', context_sucesso)