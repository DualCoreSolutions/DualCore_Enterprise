"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rotas de Autenticação Padrão (Login/Logout)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Nossas Rotas Customizadas (Registro) - AQUI ESTÁ A SOLUÇÃO
    path('accounts/', include('apps.accounts.urls')),
    
    # Rota da Home (para não dar erro 404 quando logar)
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # Rota do Dashboard
    path('painel/', include('apps.dashboard.urls')),
]
