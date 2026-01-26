# apps/dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # O nome 'dashboard' aqui resolve o erro de redirecionamento
    path('', views.DashboardIndexView.as_view(), name='dashboard'),
]