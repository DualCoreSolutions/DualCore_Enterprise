# apps/website/views.py
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Importações dos modelos e do formulário (Onde o erro estava ocorrendo)
from .models import Orcamento, ServicoPrestado 
from .forms import OrcamentoForm # <-- ESTA LINHA É ESSENCIAL

class IndexView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        """Passa a lista de serviços ativos para a página inicial"""
        context = super().get_context_data(**kwargs)
        # Busca serviços que você marcou como 'ativo' no Admin
        context['servicos'] = ServicoPrestado.objects.filter(ativo=True)
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

        # 3. Prepara o conteúdo do e-mail HTML para o cliente
        context_email = {'nome': nome, 'servico': servico}
        html_content = render_to_string('emails/confirmacao_orcamento.html', context_email)
        text_content = strip_tags(html_content)

        # 4. Envio de Notificações
        try:
            # Notificação Interna para a DualCore
            assunto_equipa = f"Novo Orçamento Recebido: {servico}"
            corpo_equipa = f"Olá Equipa,\n\nO cliente {nome} solicitou um orçamento para {servico}.\nMensagem: {mensagem}"
            
            send_mail(
                assunto_equipa, 
                corpo_equipa, 
                settings.DEFAULT_FROM_EMAIL, 
                [settings.DEFAULT_FROM_EMAIL]
            )

            # Resposta Automática Profissional para o Cliente
            send_mail(
                "Recebemos o seu pedido - DualCore Solutions",
                text_content,
                settings.DEFAULT_FROM_EMAIL,
                [email_cliente],
                html_message=html_content
            )
        except Exception as e:
            print(f"Erro ao enviar e-mails: {e}")

        # 5. Contexto para a página de sucesso com botão WhatsApp
        context_sucesso = {
            'nome': nome,
            'servico': servico,
        }
        return render(self.request, 'website/sucesso.html', context_sucesso)