# apps/website/models.py
from django.db import models

class Orcamento(models.Model):
    SERVICOS = [
        ('infra', 'Infraestrutura de Redes'),
        ('python', 'Automação Python'),
        ('web', 'Sistemas Web'),
    ]
    
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('analise', 'Em Análise'),
        ('enviado', 'Orçamento Enviado'),
        ('finalizado', 'Finalizado'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True) 
    servico = models.CharField(max_length=20, choices=SERVICOS)
    mensagem = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.get_servico_display()}"

class ServicoPrestado(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, help_text="Ex: bi-cpu")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

# NOVO MODELO: Projetos do Portfólio
class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='portfolio/')
    tecnologias = models.CharField(max_length=200, help_text="Ex: Python, Django, Docker")
    data_conclusao = models.DateField()

    def __str__(self):
        return self.titulo