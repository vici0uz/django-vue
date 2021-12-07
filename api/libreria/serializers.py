from rest_framework import serializers
from . import models


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Libro
        fields = ['id', 'nombre', 'autor']


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Autor
        fields = ['id', 'nombre']