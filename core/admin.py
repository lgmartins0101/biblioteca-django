from django.contrib import admin
from .models import Categoria, Autor, Livro

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome') 
    search_fields = ('nome',) 

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome') 
    search_fields = ('nome',) 

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'categoria', 'publicado_em')
    search_fields = ('titulo', 'autor__nome', 'categoria__nome') 
    list_filter = ('autor', 'categoria', 'publicado_em')
    ordering = ('titulo',) 

