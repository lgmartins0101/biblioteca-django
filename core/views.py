from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .models import Livro, Autor
from .serializers import LivroSerializer, AutorSerializer
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET', 'POST'])
def livro_list_create(request):
    if request.method == "GET":
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def livro_detail(request, pk):
    livro = Livro.objects.get(pk=pk)
    if request.method == "GET":
        serializer = LivroSerializer(livro)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        livro.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def autor_list_create(request):
    if request.method == "GET":
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def autor_detail(request, pk):
    autor = Autor.objects.get(pk=pk)
    if request.method == "GET":
        serializer = AutorSerializer(autor)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        autor.delete()
        return Response({"message":"Instancia apagada com sucesso"}, status=200)

    return Response(status=status.HTTP_204_NO_CONTENT)
