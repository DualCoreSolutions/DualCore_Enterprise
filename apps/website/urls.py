from django.urls import path
from .views import IndexView, OrcamentoCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('orcamento/', OrcamentoCreateView.as_view(), name='pedir_orcamento'),
]