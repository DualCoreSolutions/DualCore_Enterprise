# apps/accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Adicione esta linha para resolver o erro "NoReverseMatch"
    # Se você ainda não criou a view 'register', aponte para a IndexView temporariamente
    path('register/', auth_views.LoginView.as_view(), name='register'), 
]