from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required # <--- Isso é o segurança na porta. Só entra com crachá.
def dashboard_home(request):
    return render(request, 'dashboard/home.html')