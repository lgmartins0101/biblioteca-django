from django_filters import rest_framework as filters
from .models import Livro, Categoria
class LivroFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='autor__nome',lookup_expr='icontains')
    categoria = filters.AllValuesFilter(field_name='categoria__nome')

class Meta:
    model = Livro
    fields = ['titulo', 'autor', 'categoria']


class CategoriaFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='startswith')  # Busca por nome que começa com a string

    class Meta:
        model = Categoria
        fields = ['nome']
