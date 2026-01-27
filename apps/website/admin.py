from django.contrib import admin
from .models import Orcamento, ServicoPrestado, Projeto

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    # Itens que aparecem na lista principal
    list_display = ('nome', 'servico', 'status', 'data_envio')
    # Filtros laterais para facilitar a gestão de leads
    list_filter = ('status', 'servico', 'data_envio')
    # Permite editar o status diretamente na lista (ganho de produtividade)
    list_editable = ('status',)
    # Campo de busca para localizar clientes rapidamente
    search_fields = ('nome', 'email')
    # Organiza os campos dentro da edição do orçamento
    readonly_fields = ('data_envio',)

@admin.register(ServicoPrestado)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo')
    list_editable = ('ativo',)
    search_fields = ('titulo',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    # Vitrine técnica: exibe título, tecnologias e data de conclusão
    list_display = ('titulo', 'tecnologias', 'data_conclusao')
    # Filtro por data para acompanhar a evolução da empresa
    list_filter = ('data_conclusao', 'tecnologias')
    # Busca por título ou stack tecnológica
    search_fields = ('titulo', 'tecnologias', 'descricao')
    # Ordenação padrão por projetos mais recentes
    ordering = ('-data_conclusao',)