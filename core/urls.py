from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rotas de Autenticação
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('apps.accounts.urls')),
    
    # Rota do Dashboard
    path('painel/', include('apps.dashboard.urls')),

    # Rotas do Website (Início e Orçamentos)
    path('', include('apps.website.urls')), # <--- ESSA LINHA É ESSENCIAL
]