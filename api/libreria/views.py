# from django.shortcuts import render
from django.views.generic import ListView, CreateView

from rest_framework import generics
from . import models
from . import serializers
# Create your views here.


class ListaLibros(ListView):

    model = models.Libro
    template_name = 'templates/lista.html'
    # queryset = model.objects.all()


class CreaLibros(CreateView):
    success_url = 'listaLibros'
    model = models.Libro
    template_name = 'templates/forms.html'
    fields = ['nombre', 'autor']


class ListaAutores(ListView):

    model = models.Autor
    template_name = 'templates/lista.html'


class CreaAutores(CreateView):
    success_url = 'listaAutores'

    model = models.Autor
    template_name = 'templates/forms.html'
    fields = ['nombre']


class API_ListaLibros(generics.ListCreateAPIView):

    queryset = models.Libro.objects.all()

    serializer_class = serializers.LibroSerializer


class API_LibroDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Libro.objects.all()

    serializer_class = serializers.LibroSerializer

class API_ListaAutores(generics.ListCreateAPIView):

    queryset = models.Autor.objects.all()

    serializer_class = serializers.AutorSerializer