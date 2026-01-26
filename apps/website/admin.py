from django.contrib import admin
from .models import Orcamento, ServicoPrestado

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    # Itens que aparecem na lista
    list_display = ('nome', 'servico', 'status', 'data_envio')
    # Filtros laterais para facilitar a busca
    list_filter = ('status', 'servico', 'data_envio')
    # Permite editar o status sem abrir o orçamento
    list_editable = ('status',)
    search_fields = ('nome', 'email')

@admin.register(ServicoPrestado)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo')