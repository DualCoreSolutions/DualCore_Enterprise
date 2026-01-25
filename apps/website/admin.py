from django.contrib import admin
from .models import Orcamento

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'servico', 'data_envio')
    list_filter = ('servico',)
    search_fields = ('nome', 'email')
    