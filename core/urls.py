from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. Interface Administrativa (Onde estava o erro: trocado status por urls)
    path('admin/', admin.site.urls),

    # 2. Gestão de Contas (Login, Logout, Registo)
    path('accounts/', include('apps.accounts.urls')),

    # 3. Dashboard e PDF (Nível Staff/Equipa)
    path('dashboard/', include('apps.dashboard.urls')),

    # 4. Website Principal e Portfólio (Público)
    path('', include('apps.website.urls')),
]

# 5. Configuração para servir ficheiros de IMAGEM e MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)