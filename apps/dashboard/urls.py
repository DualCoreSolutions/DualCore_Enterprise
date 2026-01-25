from django.urls import path
from .views import dashboard_home, editar_perfil

urlpatterns = [
    path('', dashboard_home, name='dashboard'),
    path('editar/', editar_perfil, name='editar_perfil'),
]