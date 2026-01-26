from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardIndexView.as_view(), name='dashboard'),
    # Esta linha abaixo é a que ativa a função PDF
    path('pdf/<int:pk>/', views.gerar_pdf_orcamento, name='gerar_pdf'),
]