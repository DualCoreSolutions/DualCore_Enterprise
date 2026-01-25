from django.db import models

class Orcamento(models.Model):
    SERVICOS = [
        ('infra', 'Infraestrutura de Redes'),
        ('python', 'Automação Python'),
        ('web', 'Sistemas Web'),
    ]
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    servico = models.CharField(max_length=20, choices=SERVICOS)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.get_servico_display()}"