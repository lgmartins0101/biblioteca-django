from django.core.management.base import BaseCommand
from core.models import Categoria, Autor, Livro

class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        categoria_misterio = Categoria.objects.create(nome="Mistério")
        categoria_ficcao = Categoria.objects.create(nome="Ficção")
        categoria_fantasia = Categoria.objects.create(nome="Fantasia")
        categoria_romance = Categoria.objects.create(nome="Romance")
        
        autor_agatha_christie = Autor.objects.create(nome="Agatha Christie")
        autor_arthur_c_clarke = Autor.objects.create(nome="Arthur C. Clarke")
        autor_arthur_conan_doyle = Autor.objects.create(nome="Arthur Conan Doyle")
        autor_cs_lewis = Autor.objects.create(nome="C.S. Lewis")
        autor_emily_bronte = Autor.objects.create(nome="Emily Brontë")
        
        autor_george_rr_martin = Autor.objects.create(nome="George R.R. Martin")
        autor_isaac_asimov = Autor.objects.create(nome="Isaac Asimov")
        autor_jrr_tolkien = Autor.objects.create(nome="J.R.R. Tolkien")

        Livro.objects.create(
            titulo="O Morro dos Ventos Uivantes",
            autor=autor_emily_bronte,
            categoria=categoria_romance,
            publicado_em="1847-12-01",
        )

        Livro.objects.create(
            titulo="A Guerra dos Tronos",
            autor=autor_george_rr_martin,
            categoria=categoria_fantasia,
            publicado_em="1996-08-06",
        )

        Livro.objects.create(
            titulo="A Fúria dos Reis",
            autor=autor_george_rr_martin,
            categoria=categoria_fantasia,
            publicado_em="1998-11-16",
        )

        Livro.objects.create(
            titulo="Fundação",
            autor=autor_isaac_asimov,
            categoria=categoria_ficcao,
            publicado_em="1951-06-01",
        )

        Livro.objects.create(
            titulo="Eu, Robô",
            autor=autor_isaac_asimov,
            categoria=categoria_ficcao,
            publicado_em="1950-12-02",
        )

        Livro.objects.create(
            titulo="O Senhor dos Anéis",
            autor=autor_jrr_tolkien,
            categoria=categoria_fantasia,
            publicado_em="1954-07-29",
        )

        Livro.objects.create(
            titulo="O Hobbit",
            autor=autor_jrr_tolkien,
            categoria=categoria_fantasia,
            publicado_em="1937-09-21",
        )
