from django.urls import path
from .views import menu, index, agregar_reseña
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path("menu/", menu, name="menu"),
    path('agregar_reseña/', agregar_reseña, name='agregar_reseña'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
