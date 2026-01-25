from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.accounts.forms import CustomUserChangeForm
from apps.website.models import Orcamento # Importação necessária

@login_required # Garante que só usuários logados entrem
def dashboard_home(request):
    # Coletamos os 5 orçamentos mais recentes para exibir ao staff
    orcamentos = None
    if request.user.is_staff:
        orcamentos = Orcamento.objects.all().order_by('-data_envio')[:5]
    
    context = {
        'orcamentos': orcamentos,
    }
    return render(request, 'dashboard/home.html', context)

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('dashboard')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'dashboard/editar_perfil.html', {'form': form})