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
    # Adicionando o telefone que validamos anteriormente
    telefone = models.CharField(max_length=20, blank=True, null=True) 
    servico = models.CharField(max_length=20, choices=SERVICOS)
    mensagem = models.TextField()
    # Novo campo para gestão interna
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.get_servico_display()}"

# Novo modelo para tornar seus serviços editáveis pelo Admin
class ServicoPrestado(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, help_text="Nome do ícone (ex: bi-code-slash)")
    ativo = models.BooleanField(default=True)

    def __clstr__(self):
        return self.titulo