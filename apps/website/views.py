from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Modelos e Forms
from .models import Orcamento, ServicoPrestado, Projeto # Adicionado Projeto aqui
from .forms import OrcamentoForm

class IndexView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        """Passa serviços ativos e projetos do portfólio para a Home"""
        context = super().get_context_data(**kwargs)
        
        # 1. Busca serviços ativos
        context['servicos'] = ServicoPrestado.objects.filter(ativo=True)
        
        # 2. Busca os últimos 6 projetos cadastrados para o Portfólio
        context['projetos'] = Projeto.objects.all()[:6]
        
        return context

class OrcamentoCreateView(CreateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'website/orcamento.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # 1. Salva o orçamento na base de dados
        self.object = form.save()
        
        # 2. Coleta dados para e-mails e página de sucesso
        nome = form.cleaned_data['nome']
        email_cliente = form.cleaned_data['email']
        servico = self.object.get_servico_display()
        mensagem = form.cleaned_data['mensagem']

        # 3. Conteúdo do e-mail HTML
        context_email = {'nome': nome, 'servico': servico}
        html_content = render_to_string('emails/confirmacao_orcamento.html', context_email)
        text_content = strip_tags(html_content)

        # 4. Envio de Notificações
        try:
            # Notificação para a DualCore
            send_mail(
                f"Novo Orçamento: {servico}", 
                f"Olá Equipa,\n\nO cliente {nome} solicitou orçamento para {servico}.\nMensagem: {mensagem}", 
                settings.DEFAULT_FROM_EMAIL, 
                [settings.DEFAULT_FROM_EMAIL]
            )

            # Resposta Automática para o Cliente
            send_mail(
                "Recebemos o seu pedido - DualCore Solutions",
                text_content,
                settings.DEFAULT_FROM_EMAIL,
                [email_cliente],
                html_message=html_content
            )
        except Exception as e:
            print(f"Erro ao enviar e-mails: {e}")

        # 5. Redireciona para página de sucesso personalizada
        context_sucesso = {
            'nome': nome,
            'servico': servico,
        }
        return render(self.request, 'website/sucesso.html', context_sucesso)