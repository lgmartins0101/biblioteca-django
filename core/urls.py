from django.urls import path
from . import views

urlpatterns = [
    path("livros/", views.livro_list_create, name="livros-list-create"),
    path("livros/<int:pk>/", views.livro_detail, name="livro-detail"),
    path("autores/", views.autor_list_create, name="autores-list-create"),
    path("autores/<int:pk>/", views.autor_detail, name="autor-detail"),
]
