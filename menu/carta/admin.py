from django.contrib import admin
from .models import Seccion, Plato, Galeria

@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "seccion", "precio")
    list_filter = ("seccion",)
    search_fields = ("nombre", "descripcion")




@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'foto')


# Register your models here.
