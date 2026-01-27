from django.db import models

class Orcamento(models.Model):
    """Modelo para capturar solicitações de orçamento via site"""
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

    class Meta:
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"
        ordering = ['-data_envio']

    def __str__(self):
        return f"{self.nome} - {self.get_servico_display()}"


class ServicoPrestado(models.Model):
    """Modelo para os serviços exibidos dinamicamente na Home"""
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, help_text="Ex: bi-cpu, bi-code-slash, bi-diagram-3")
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Serviço Prestado"
        verbose_name_plural = "Serviços Prestados"

    def __str__(self):
        return self.titulo


class Projeto(models.Model):
    """Modelo para o portfólio de projetos concluídos"""
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='portfolio/')
    tecnologias = models.CharField(max_length=200, help_text="Ex: Python, Django, Docker")
    data_conclusao = models.DateField()

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-data_conclusao']

    def __str__(self):
        return self.titulo