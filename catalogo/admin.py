from django.contrib import admin
from .models import Categoria, Libro

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion",)
    list_filter = ("nombre",)
    search_fields = ("nombre",)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "disponible", "categoria",)
    list_filter = ("titulo", "autor", "disponible", "categoria",)
    search_fields = ("titulo", "autor", "categoria",)