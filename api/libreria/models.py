from django.db import models
from django.contrib import admin

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    autor = models.ForeignKey(Autor, related_name='autor', verbose_name='Autor', on_delete=models.PROTECT)


    def __str__(self):
        return self.nombre
