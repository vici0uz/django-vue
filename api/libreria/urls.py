from django.urls import path

from . import views

app_name = 'libreria'

urlpatterns = [
    # path('', views.index, name='index'),
    path('listaLibros', views.ListaLibros.as_view(), name='listaLibros'),
    path('creaLibros', views.CreaLibros.as_view(), name='creaLibros'),
    path('listaAutores', views.ListaAutores.as_view(), name='listaAutores'),
    path('creaAutores', views.CreaAutores.as_view(), name='creaAutores'),
    path('api.libros', views.API_ListaLibros.as_view(), name='libros'),
    path('api.libros/<int:pk>', views.API_LibroDetail.as_view(), name='libro_detail'),
    path('api.autores', views.API_ListaAutores.as_view(), name='autores')
]
