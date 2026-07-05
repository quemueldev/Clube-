
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .api import nucleo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', nucleo.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

"""
faz o Django servir arquivos de mídia localmente durante o desenvolvimento.

Quando você salva uma imagem em ImageField
Ela vai para a pasta media/club_photos/
O banco salva só o caminho, tipo:
"""