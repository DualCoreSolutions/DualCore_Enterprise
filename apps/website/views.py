# apps/website/views.py
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Orcamento
from .forms import OrcamentoForm

# Esta é a classe que estava em falta!
class IndexView(TemplateView):
    template_name = 'website/index.html'

class OrcamentoCreateView(CreateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'website/orcamento.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Primeiro, guardamos o orçamento no banco de dados
        self.object = form.save()
        
        # Coletamos os dados para as notificações
        nome = form.cleaned_data['nome']
        email_cliente = form.cleaned_data['email']
        servico = self.object.get_servico_display()
        mensagem = form.cleaned_data['mensagem']

        # 1. Notificação para a Equipa DualCore
        assunto_equipa = f"Novo Orçamento Recebido: {servico}"
        corpo_equipa = f"Olá Equipa,\n\nO cliente {nome} solicitou um orçamento para {servico}.\nMensagem: {mensagem}"
        
        # 2. Resposta Automática para o Cliente
        assunto_cliente = "Recebemos o seu pedido - DualCore Solutions"
        corpo_cliente = f"Olá {nome},\n\nObrigado por nos contactar. Recebemos o seu pedido para {servico} e analisaremos os detalhes em breve."

        try:
            # Envia e-mail para a equipa
            send_mail(assunto_equipa, corpo_equipa, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
            # Envia e-mail de agradecimento para o cliente
            send_mail(assunto_cliente, corpo_cliente, settings.DEFAULT_FROM_EMAIL, [email_cliente])
        except Exception as e:
            print(f"Erro ao enviar e-mails: {e}")

        messages.success(self.request, "Solicitação enviada com sucesso! Verifique o seu e-mail.")
        return redirect(self.get_success_url())