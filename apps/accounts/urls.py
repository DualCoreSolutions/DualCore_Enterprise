from django.urls import path
from .views import SignUpView

urlpatterns = [
    # O nome='register' aqui é o que o login.html está procurando!
    path('register/', SignUpView.as_view(), name='register'),
]